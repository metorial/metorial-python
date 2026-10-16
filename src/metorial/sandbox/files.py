from __future__ import annotations

import asyncio
import hashlib
import json
import weakref
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from types import TracebackType
from typing import Any, TypeVar

from ._access import SandboxAccessCache
from ._errors import SandboxAccessError, server_error
from ._mux import (
  MuxSocket,
  NoticeHandler,
  create_request_id,
  decode_frame,
  encode_frame,
)

T = TypeVar("T")
_EntriesHandler = Callable[[list[Any]], None]

_CHUNK_SIZE = 64 * 1024
_DEFAULT_LIST_LIMIT = 10000
_MAX_ATTEMPTS = 3
_RESEND_DELAY = 0.2

_unsent_errors: weakref.WeakSet[SandboxAccessError] = weakref.WeakSet()


@dataclass
class SandboxFileEntry:
  name: str
  path: str
  type: str
  size: int
  mode: int
  modified_at: datetime
  target: str | None = None


@dataclass
class SandboxFileList:
  entries: list[SandboxFileEntry]
  truncated: bool


@dataclass
class _PendingOperation:
  future: asyncio.Future[dict[str, Any]]
  on_entries: _EntriesHandler | None = None
  on_data: Callable[[bytes], None] | None = None
  chunks: list[bytes] = field(default_factory=list)


def _join_path(parent: str, child: str) -> str:
  return f"{parent.rstrip('/')}/{child.lstrip('/')}"


def _base_name(path: str) -> str:
  return path.rstrip("/").split("/")[-1] or "/"


def _to_entry(raw: dict[str, Any], parent: str | None = None) -> SandboxFileEntry:
  name = raw.get("name")
  if parent is None:
    path = str(raw.get("path"))
  else:
    path = _join_path(parent, str(name if isinstance(name, str) else raw.get("path")))

  target = raw.get("target")
  return SandboxFileEntry(
    name=name if isinstance(name, str) else _base_name(path),
    path=path,
    type=str(raw.get("type")),
    size=int(raw.get("size") or 0),
    mode=int(raw.get("mode") or 0),
    modified_at=datetime.fromtimestamp(
      int(raw.get("mtime") or 0) / 1000, tz=timezone.utc
    ),
    target=target if isinstance(target, str) else None,
  )


class SandboxFiles:
  def __init__(
    self, access: SandboxAccessCache, *, on_notice: NoticeHandler | None = None
  ) -> None:
    self._pending: dict[str, _PendingOperation] = {}
    self._socket = MuxSocket(
      access,
      on_text=self._handle_text,
      on_binary=self._handle_binary,
      on_disconnect=self._handle_disconnect,
      on_notice=on_notice,
    )

  @classmethod
  async def connect(
    cls, access: SandboxAccessCache, *, on_notice: NoticeHandler | None = None
  ) -> SandboxFiles:
    files = cls(access, on_notice=on_notice)
    await files._socket.ensure_open()
    return files

  @property
  def is_closed(self) -> bool:
    return self._socket.is_closed

  async def __aenter__(self) -> SandboxFiles:
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc: BaseException | None,
    tb: TracebackType | None,
  ) -> None:
    await self.close()

  async def list(
    self,
    path: str,
    *,
    recursive: bool = False,
    max_depth: int | None = None,
    limit: int | None = None,
  ) -> SandboxFileList:
    async def run() -> SandboxFileList:
      entries: list[SandboxFileEntry] = []
      fields: dict[str, Any] = {
        "path": path,
        "limit": limit if limit is not None else _DEFAULT_LIST_LIMIT,
      }
      if recursive:
        fields["recursive"] = True
      if max_depth is not None:
        fields["maxDepth"] = max_depth

      result = await self._run(
        "list",
        fields,
        on_entries=lambda batch: entries.extend(_to_entry(raw, path) for raw in batch),
      )
      return SandboxFileList(entries=entries, truncated=result.get("truncated") is True)

    return await self._with_retry(run)

  async def stat(self, path: str, *, follow_symlinks: bool = False) -> SandboxFileEntry:
    async def run() -> SandboxFileEntry:
      result = await self._run(
        "stat", {"path": path, "followSymlinks": follow_symlinks}
      )
      return _to_entry(result.get("entry") or {})

    return await self._with_retry(run)

  async def exists(self, path: str) -> bool:
    try:
      await self.stat(path)
      return True
    except SandboxAccessError as error:
      if error.code == "not_found":
        return False
      raise

  async def read(
    self, path: str, *, offset: int | None = None, length: int | None = None
  ) -> bytes:
    async def run() -> bytes:
      chunks: list[bytes] = []
      fields: dict[str, Any] = {"path": path}
      if offset is not None:
        fields["offset"] = offset
      if length is not None:
        fields["length"] = length

      await self._run("read", fields, on_data=chunks.append)
      return b"".join(chunks)

    return await self._with_retry(run)

  async def read_text(
    self,
    path: str,
    *,
    encoding: str = "utf-8",
    offset: int | None = None,
    length: int | None = None,
  ) -> str:
    return (await self.read(path, offset=offset, length=length)).decode(encoding)

  async def write(
    self,
    path: str,
    data: str | bytes,
    *,
    overwrite: bool = True,
    parents: bool = False,
    mode: int | str | None = None,
  ) -> int:
    content = data.encode() if isinstance(data, str) else bytes(data)
    checksum = hashlib.sha256(content).hexdigest()

    fields: dict[str, Any] = {
      "path": path,
      "size": len(content),
      "overwrite": overwrite,
    }
    if parents:
      fields["parents"] = True
    if mode is not None:
      fields["mode"] = mode

    async def upload(request_id: str, is_active: Callable[[], bool]) -> None:
      for start in range(0, len(content), _CHUNK_SIZE):
        if not is_active():
          return
        await self._socket.send(
          encode_frame(request_id, content[start : start + _CHUNK_SIZE])
        )

      if is_active():
        await self._socket.send(
          json.dumps({"id": request_id, "type": "end", "sha256": checksum})
        )

    async def run() -> int:
      result = await self._run("write", fields, upload=upload)
      return int(result.get("size") or len(content))

    return await self._with_retry(run, can_resend=overwrite)

  async def mkdir(
    self, path: str, *, parents: bool = False, mode: int | str | None = None
  ) -> None:
    fields: dict[str, Any] = {"path": path, "parents": parents}
    if mode is not None:
      fields["mode"] = mode

    await self._with_retry(lambda: self._run("mkdir", fields), can_resend=parents)

  async def move(
    self, source: str, destination: str, *, overwrite: bool = False
  ) -> None:
    await self._with_retry(
      lambda: self._run(
        "move", {"from": source, "to": destination, "overwrite": overwrite}
      ),
      can_resend=False,
    )

  async def delete(
    self, path: str, *, recursive: bool = False, missing_ok: bool = False
  ) -> None:
    fields: dict[str, Any] = {"path": path, "recursive": recursive}
    if missing_ok:
      fields["missingOk"] = True

    await self._with_retry(lambda: self._run("delete", fields), can_resend=missing_ok)

  async def close(self) -> None:
    await self._socket.close()

  def _handle_text(self, message: dict[str, Any]) -> None:
    request_id = message.get("id")
    if not isinstance(request_id, str):
      return

    operation = self._pending.get(request_id)
    if operation is None:
      return

    kind = message.get("type")
    if kind == "entries" and operation.on_entries is not None:
      entries = message.get("entries")
      operation.on_entries(entries if isinstance(entries, list) else [])
    elif kind == "result":
      fields = {k: v for k, v in message.items() if k not in ("id", "type")}
      self._settle(request_id, result=fields)
    elif kind == "error":
      self._settle(request_id, error=server_error(message.get("error")))

  def _handle_binary(self, data: bytes) -> None:
    frame = decode_frame(data)
    if frame is None:
      return

    operation = self._pending.get(frame[0])
    if operation is not None and operation.on_data is not None:
      operation.on_data(frame[2])

  def _handle_disconnect(self, error: SandboxAccessError) -> None:
    for request_id in list(self._pending):
      self._settle(request_id, error=error)

  def _settle(
    self,
    request_id: str,
    *,
    result: dict[str, Any] | None = None,
    error: SandboxAccessError | None = None,
  ) -> None:
    operation = self._pending.pop(request_id, None)
    if operation is None or operation.future.done():
      return

    if error is not None:
      operation.future.set_exception(error)
    else:
      operation.future.set_result(result or {})

  async def _with_retry(
    self, run: Callable[[], Awaitable[T]], *, can_resend: bool = True
  ) -> T:
    attempt = 1
    while True:
      try:
        return await run()
      except SandboxAccessError as error:
        should_resend = (
          (can_resend or error in _unsent_errors)
          and attempt < _MAX_ATTEMPTS
          and not self.is_closed
          and error.retryable
        )
        if not should_resend:
          raise

      await asyncio.sleep(_RESEND_DELAY * attempt)
      attempt += 1

  async def _run(
    self,
    op: str,
    fields: dict[str, Any],
    *,
    on_entries: _EntriesHandler | None = None,
    on_data: Callable[[bytes], None] | None = None,
    upload: Callable[[str, Callable[[], bool]], Awaitable[None]] | None = None,
  ) -> dict[str, Any]:
    try:
      await self._socket.ensure_open()
    except SandboxAccessError as error:
      _unsent_errors.add(error)
      raise

    request_id = create_request_id()
    future: asyncio.Future[dict[str, Any]] = asyncio.get_running_loop().create_future()
    self._pending[request_id] = _PendingOperation(
      future=future, on_entries=on_entries, on_data=on_data
    )

    if not await self._socket.send(json.dumps({"id": request_id, "op": op, **fields})):
      lost = SandboxAccessError(
        "disconnected", "The file connection was lost.", retryable=True
      )
      _unsent_errors.add(lost)
      self._settle(request_id, error=lost)
      return await future

    upload_task: asyncio.Task[None] | None = None
    if upload is not None:
      upload_task = asyncio.ensure_future(upload(request_id, lambda: not future.done()))

    try:
      return await future
    except asyncio.CancelledError:
      self._pending.pop(request_id, None)
      await self._socket.send(
        json.dumps({"id": create_request_id(), "op": "cancel", "target": request_id})
      )
      raise
    finally:
      if upload_task is not None and not upload_task.done():
        upload_task.cancel()
