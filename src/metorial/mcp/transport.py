from __future__ import annotations

import asyncio
import contextlib
import json
import logging
from datetime import timedelta
from typing import Any

import anyio
import httpx
from anyio.streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream
from httpx_sse import EventSource

from mcp.shared.message import SessionMessage
from mcp.types import InitializeResult, JSONRPCError, JSONRPCMessage, JSONRPCRequest, JSONRPCResponse

logger = logging.getLogger("metorial.mcp.transport")

MCP_SESSION_ID = "mcp-session-id"
MCP_PROTOCOL_VERSION = "mcp-protocol-version"
ACCEPT = "accept"
CONTENT_TYPE = "content-type"
JSON = "application/json"
SSE = "text/event-stream"


class MetorialMcpTransportError(RuntimeError):
  pass


class MetorialMcpTransport:
  def __init__(
    self,
    url: str,
    *,
    headers: dict[str, str] | None = None,
    client: httpx.AsyncClient | None = None,
    connect_timeout: float = 30.0,
    read_timeout: float = 60.0,
    terminate_on_close: bool = True,
  ) -> None:
    self._url = url
    self._headers = headers or {}
    self._owns_client = client is None
    self._client = client or httpx.AsyncClient(
      timeout=httpx.Timeout(connect_timeout, read=read_timeout)
    )
    self._terminate_on_close = terminate_on_close
    self._session_id: str | None = None
    self._protocol_version: str | None = None
    self._closed = False
    self._writer_task: asyncio.Task[None] | None = None
    self._read_stream_writer, self.read_stream = anyio.create_memory_object_stream[
      SessionMessage | Exception
    ](0)
    self.write_stream, self._write_stream_reader = anyio.create_memory_object_stream[
      SessionMessage
    ](0)

  async def open(
    self,
  ) -> tuple[
    MemoryObjectReceiveStream[SessionMessage | Exception],
    MemoryObjectSendStream[SessionMessage],
  ]:
    if self._writer_task is None:
      self._writer_task = asyncio.create_task(
        self._post_writer(),
        name="metorial-mcp-transport",
      )
    return self.read_stream, self.write_stream

  def _prepare_headers(self) -> dict[str, str]:
    headers = {
      ACCEPT: f"{JSON}, {SSE}",
      CONTENT_TYPE: JSON,
      **self._headers,
    }
    if self._session_id:
      headers[MCP_SESSION_ID] = self._session_id
    if self._protocol_version:
      headers[MCP_PROTOCOL_VERSION] = self._protocol_version
    return headers

  def _is_initialize_request(self, message: JSONRPCMessage) -> bool:
    return isinstance(message.root, JSONRPCRequest) and message.root.method == "initialize"

  def _update_session_id(self, response: httpx.Response) -> None:
    session_id = response.headers.get(MCP_SESSION_ID)
    if session_id:
      self._session_id = session_id

  def _update_protocol_version(self, message: JSONRPCMessage) -> None:
    if isinstance(message.root, JSONRPCResponse) and message.root.result:
      try:
        init_result = InitializeResult.model_validate(message.root.result)
        self._protocol_version = str(init_result.protocolVersion)
      except Exception:
        logger.debug("Failed to extract negotiated protocol version", exc_info=True)

  async def _send_message(
    self,
    message: JSONRPCMessage,
    *,
    is_initialize: bool = False,
  ) -> None:
    if is_initialize:
      self._update_protocol_version(message)
    await self._read_stream_writer.send(SessionMessage(message))

  async def _handle_json_response(
    self,
    response: httpx.Response,
    *,
    is_initialize: bool = False,
  ) -> None:
    content = await response.aread()
    if not content:
      return

    payload = json.loads(content)
    messages = payload if isinstance(payload, list) else [payload]
    for item in messages:
      message = JSONRPCMessage.model_validate(item)
      await self._send_message(message, is_initialize=is_initialize)

  async def _handle_sse_response(
    self,
    response: httpx.Response,
    *,
    is_initialize: bool = False,
  ) -> None:
    event_source = EventSource(response)
    async for sse in event_source.aiter_sse():
      if sse.event not in ("message", ""):
        continue
      if not sse.data:
        continue
      message = JSONRPCMessage.model_validate_json(sse.data)
      await self._send_message(message, is_initialize=is_initialize)
      if isinstance(message.root, (JSONRPCResponse, JSONRPCError)):
        await response.aclose()
        return
    await response.aclose()

  async def _handle_post(self, session_message: SessionMessage) -> None:
    message = session_message.message
    is_initialize = self._is_initialize_request(message)
    payload = message.model_dump(by_alias=True, mode="json", exclude_none=True)

    async with self._client.stream(
      "POST",
      self._url,
      json=payload,
      headers=self._prepare_headers(),
    ) as response:
      if response.status_code == 202:
        return

      response.raise_for_status()
      self._update_session_id(response)

      if not isinstance(message.root, JSONRPCRequest):
        await response.aclose()
        return

      content_type = response.headers.get(CONTENT_TYPE, "").lower()
      if content_type.startswith(JSON):
        await self._handle_json_response(response, is_initialize=is_initialize)
      elif content_type.startswith(SSE):
        await self._handle_sse_response(response, is_initialize=is_initialize)
      else:
        raise MetorialMcpTransportError(
          f"Unexpected content type from MCP endpoint: {content_type}"
        )

  async def _post_writer(self) -> None:
    try:
      async with self._write_stream_reader:
        async for session_message in self._write_stream_reader:
          await self._handle_post(session_message)
    except asyncio.CancelledError:
      raise
    except Exception as exc:
      logger.debug("Transport writer failed", exc_info=True)
      with contextlib.suppress(Exception):
        await self._read_stream_writer.send(exc)
    finally:
      with contextlib.suppress(Exception):
        await self._read_stream_writer.aclose()
      with contextlib.suppress(Exception):
        await self.write_stream.aclose()

  async def terminate_session(self) -> None:
    if not self._session_id:
      return

    try:
      response = await self._client.delete(self._url, headers=self._prepare_headers())
      await response.aclose()
      if response.status_code not in (200, 204, 405):
        logger.debug("Session termination returned status %s", response.status_code)
    except Exception:
      logger.debug("Session termination failed", exc_info=True)

  async def close(self) -> None:
    if self._closed:
      return
    self._closed = True

    if self._terminate_on_close:
      await self.terminate_session()

    if self._writer_task is not None:
      self._writer_task.cancel()
      with contextlib.suppress(asyncio.CancelledError, Exception):
        await self._writer_task

    with contextlib.suppress(Exception):
      await self._write_stream_reader.aclose()
    with contextlib.suppress(Exception):
      await self.write_stream.aclose()
    with contextlib.suppress(Exception):
      await self._read_stream_writer.aclose()
    with contextlib.suppress(Exception):
      await self.read_stream.aclose()

    if self._owns_client:
      with contextlib.suppress(Exception):
        await self._client.aclose()
