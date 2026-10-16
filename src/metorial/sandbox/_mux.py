from __future__ import annotations

import asyncio
import contextlib
import itertools
import json
import secrets
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

import aiohttp

from ._access import SandboxAccessCache
from ._errors import SandboxAccessError, closed_error, describe_socket_close

_MAX_CONNECT_ATTEMPTS = 3
_CONNECT_BASE_DELAY = 0.3
_MAX_RECONNECT_DELAY = 10.0
_MAX_MESSAGE_SIZE = 16 * 1024 * 1024

_RECONNECT_CODES = frozenset(
  {
    "disconnected",
    "unauthorized",
    "rate_limited",
    "machine_restarting",
    "machine_unavailable",
  }
)

_id_counter = itertools.count(1)
_id_prefix = secrets.token_hex(3)


def create_request_id() -> str:
  return f"{_id_prefix}_{next(_id_counter):x}"


def socket_protocols(token: str) -> list[str]:
  return ["metorial-sandbox-v1", f"metorial-sandbox-token.{token}"]


def encode_frame(request_id: str, payload: bytes, tag: int | None = None) -> bytes:
  id_bytes = request_id.encode()
  header = bytes([len(id_bytes)]) + id_bytes
  if tag is not None:
    header += bytes([tag])
  return header + payload


def decode_frame(
  data: bytes, has_tag: bool = False
) -> tuple[str, int | None, bytes] | None:
  if not data:
    return None

  id_length = data[0]
  offset = 1 + id_length
  if len(data) < offset + (1 if has_tag else 0):
    return None

  request_id = data[1:offset].decode(errors="replace")
  tag: int | None = None
  if has_tag:
    tag = data[offset]
    offset += 1

  return request_id, tag, data[offset:]


@dataclass
class SandboxConnectionNotice:
  notice: str
  reason: str | None = None
  idle_in_seconds: float | None = None


NoticeHandler = Callable[[SandboxConnectionNotice], None]


def _handshake_error(error: aiohttp.WSServerHandshakeError) -> SandboxAccessError:
  if error.status in (401, 403):
    return SandboxAccessError(
      "unauthorized", "Access to the machine was rejected.", retryable=True
    )
  if error.status == 404:
    return SandboxAccessError("not_found", "This machine could not be found.")
  if error.status == 429:
    return SandboxAccessError(
      "rate_limited", "Too many connections to the machine.", retryable=True
    )
  return SandboxAccessError(
    "disconnected", f"The connection failed ({error.status}).", retryable=True
  )


class MuxSocket:
  def __init__(
    self,
    access: SandboxAccessCache,
    *,
    on_text: Callable[[dict[str, Any]], None],
    on_binary: Callable[[bytes], None],
    on_disconnect: Callable[[SandboxAccessError], None],
    on_notice: NoticeHandler | None = None,
  ) -> None:
    self._access = access
    self._on_text = on_text
    self._on_binary = on_binary
    self._on_disconnect = on_disconnect
    self._on_notice = on_notice

    self._session: aiohttp.ClientSession | None = None
    self._ws: aiohttp.ClientWebSocketResponse[bool] | None = None
    self._opening: asyncio.Task[aiohttp.ClientWebSocketResponse[bool]] | None = None
    self._reader: asyncio.Task[None] | None = None
    self._reconnect: asyncio.Task[None] | None = None
    self._reconnect_attempt = 0
    self._closed = False

  @property
  def is_closed(self) -> bool:
    return self._closed

  @property
  def is_open(self) -> bool:
    return self._ws is not None and not self._ws.closed

  async def ensure_open(self) -> aiohttp.ClientWebSocketResponse[bool]:
    if self._closed:
      raise closed_error()
    if self._ws is not None and not self._ws.closed:
      return self._ws

    if self._opening is None or self._opening.done():
      self._opening = asyncio.ensure_future(self._connect())

    return await asyncio.shield(self._opening)

  async def send(self, data: str | bytes) -> bool:
    ws = self._ws
    if ws is None or ws.closed:
      return False

    try:
      if isinstance(data, str):
        await ws.send_str(data)
      else:
        await ws.send_bytes(data)
      return True
    except (ConnectionError, RuntimeError, aiohttp.ClientError):
      return False

  async def close(self) -> None:
    if self._closed:
      return
    self._closed = True

    for task in (self._reconnect, self._opening):
      if task is not None and not task.done():
        task.cancel()

    ws, self._ws = self._ws, None
    if ws is not None:
      with contextlib.suppress(Exception):
        await ws.close(code=1000, message=b"closed")

    if self._reader is not None and not self._reader.done():
      self._reader.cancel()

    if self._session is not None:
      await self._session.close()
      self._session = None

    self._on_disconnect(closed_error())

  async def _connect(self) -> aiohttp.ClientWebSocketResponse[bool]:
    last_error: SandboxAccessError | None = None

    for attempt in range(1, _MAX_CONNECT_ATTEMPTS + 1):
      if attempt > 1:
        await asyncio.sleep(_CONNECT_BASE_DELAY * 2 ** (attempt - 2))
      if self._closed:
        raise closed_error()

      grant = await self._access.get()
      if self._session is None or self._session.closed:
        self._session = aiohttp.ClientSession()

      try:
        ws = await self._session.ws_connect(
          grant.url,
          protocols=socket_protocols(grant.token),
          max_msg_size=_MAX_MESSAGE_SIZE,
        )
      except aiohttp.WSServerHandshakeError as error:
        last_error = _handshake_error(error)
      except (aiohttp.ClientError, OSError, asyncio.TimeoutError) as error:
        last_error = SandboxAccessError(
          "disconnected", str(error) or None, retryable=True
        )
      else:
        if self.is_closed:
          await ws.close(code=1000, message=b"closed")
          raise closed_error()

        self._ws = ws
        self._reader = asyncio.ensure_future(self._read(ws))
        return ws

      if not last_error.retryable:
        raise last_error
      self._access.invalidate()

    assert last_error is not None
    raise last_error

  async def _read(self, ws: aiohttp.ClientWebSocketResponse[bool]) -> None:
    close_code: int | None = None
    close_reason = ""

    try:
      while True:
        message = await ws.receive()

        if message.type == aiohttp.WSMsgType.TEXT:
          self._handle_text(message.data)
        elif message.type == aiohttp.WSMsgType.BINARY:
          self._on_binary(message.data)
        elif message.type == aiohttp.WSMsgType.CLOSE:
          close_code = message.data
          close_reason = message.extra or ""
          break
        elif message.type in (
          aiohttp.WSMsgType.CLOSING,
          aiohttp.WSMsgType.CLOSED,
          aiohttp.WSMsgType.ERROR,
        ):
          break
    except asyncio.CancelledError:
      return
    except Exception:
      pass

    if close_code is None:
      close_code = ws.close_code

    if self._closed or self._ws is not ws:
      return

    error = describe_socket_close(close_code, close_reason)
    if error.code == "unauthorized":
      self._access.invalidate()

    self._ws = None
    self._on_disconnect(error)

    if error.code in _RECONNECT_CODES:
      self._schedule_reconnect()

  def _schedule_reconnect(self) -> None:
    if self._closed or (self._reconnect is not None and not self._reconnect.done()):
      return

    delay = min(_CONNECT_BASE_DELAY * 2**self._reconnect_attempt, _MAX_RECONNECT_DELAY)
    self._reconnect_attempt += 1
    self._reconnect = asyncio.ensure_future(self._reconnect_after(delay))

  async def _reconnect_after(self, delay: float) -> None:
    await asyncio.sleep(delay)

    try:
      await self.ensure_open()
      self._reconnect_attempt = 0
    except SandboxAccessError as error:
      if error.code in _RECONNECT_CODES:
        self._reconnect = None
        self._schedule_reconnect()
    except Exception:
      pass

  def _handle_text(self, data: str) -> None:
    try:
      message = json.loads(data)
    except ValueError:
      return

    if not isinstance(message, dict):
      return

    if message.get("type") == "connection_notice":
      if self._on_notice is not None:
        reason = message.get("reason")
        idle = message.get("idleInSeconds")
        self._on_notice(
          SandboxConnectionNotice(
            notice=str(message.get("notice") or ""),
            reason=reason if isinstance(reason, str) else None,
            idle_in_seconds=idle if isinstance(idle, (int, float)) else None,
          )
        )
      return

    self._on_text(message)
