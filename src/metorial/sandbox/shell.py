from __future__ import annotations

import asyncio
import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from types import TracebackType
from typing import Any

from ._access import SandboxAccessCache
from ._errors import SandboxAccessError, SandboxCommandError, server_error
from ._mux import (
  MuxSocket,
  NoticeHandler,
  create_request_id,
  decode_frame,
  encode_frame,
)

_STDERR = 2

OutputHandler = Callable[[bytes], None]
SandboxCommand = str | Sequence[str]


@dataclass
class SandboxProcessExit:
  exit_code: int | None
  signal: str | None
  timed_out: bool


@dataclass
class SandboxCommandResult(SandboxProcessExit):
  stdout_bytes: bytes
  stderr_bytes: bytes

  @property
  def stdout(self) -> str:
    return self.stdout_bytes.decode(errors="replace")

  @property
  def stderr(self) -> str:
    return self.stderr_bytes.decode(errors="replace")


def _to_argv(command: SandboxCommand) -> list[str]:
  if isinstance(command, str):
    return ["/bin/sh", "-c", command]
  return list(command)


def _lost_error() -> SandboxCommandError:
  return SandboxCommandError("connection_interrupted", "The shell connection was lost.")


class SandboxProcess:
  def __init__(self, request_id: str, socket: MuxSocket) -> None:
    loop = asyncio.get_running_loop()

    self.id = request_id
    self.pid: int | None = None
    self._socket = socket
    self._started: asyncio.Future[int] = loop.create_future()
    self._exit: asyncio.Future[SandboxProcessExit] = loop.create_future()
    self._stdout_handlers: list[OutputHandler] = []
    self._stderr_handlers: list[OutputHandler] = []

  @property
  def is_done(self) -> bool:
    return self._exit.done()

  async def started(self) -> int:
    return await asyncio.shield(self._started)

  async def wait(self) -> SandboxProcessExit:
    return await asyncio.shield(self._exit)

  def on_stdout(self, handler: OutputHandler) -> None:
    self._stdout_handlers.append(handler)

  def on_stderr(self, handler: OutputHandler) -> None:
    self._stderr_handlers.append(handler)

  async def write(self, data: str | bytes) -> None:
    self._ensure_running()
    payload = data.encode() if isinstance(data, str) else data
    if not await self._socket.send(encode_frame(self.id, payload)):
      raise _lost_error()

  async def close_stdin(self) -> None:
    await self._send_control({"type": "stdin_eof"})

  async def signal(self, signal: str) -> None:
    name = signal.upper()
    if name.startswith("SIG"):
      name = name[3:]
    await self._send_control({"type": "signal", "signal": name})

  async def kill(self) -> None:
    await self.signal("KILL")

  def _handle_output(self, stream: int | None, data: bytes) -> None:
    handlers = self._stderr_handlers if stream == _STDERR else self._stdout_handlers
    for handler in handlers:
      handler(data)

  def _handle_started(self, pid: int) -> None:
    self.pid = pid
    if not self._started.done():
      self._started.set_result(pid)

  def _handle_exit(self, exit: SandboxProcessExit) -> None:
    if not self._started.done():
      self._started.set_result(self.pid if self.pid is not None else -1)
    if not self._exit.done():
      self._exit.set_result(exit)

  def _handle_error(self, error: SandboxAccessError) -> None:
    for future in (self._started, self._exit):
      if not future.done():
        future.set_exception(error)
        future.exception()

  async def _send_control(self, fields: dict[str, Any]) -> None:
    self._ensure_running()
    if not await self._socket.send(json.dumps({"id": self.id, **fields})):
      raise _lost_error()

  def _ensure_running(self) -> None:
    if self.is_done:
      raise SandboxCommandError("unknown_command", "The command has already finished.")


class SandboxShell:
  def __init__(
    self, access: SandboxAccessCache, *, on_notice: NoticeHandler | None = None
  ) -> None:
    self._processes: dict[str, SandboxProcess] = {}
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
  ) -> SandboxShell:
    shell = cls(access, on_notice=on_notice)
    await shell._socket.ensure_open()
    return shell

  @property
  def is_closed(self) -> bool:
    return self._socket.is_closed

  async def __aenter__(self) -> SandboxShell:
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc: BaseException | None,
    tb: TracebackType | None,
  ) -> None:
    await self.close()

  async def spawn(
    self,
    command: SandboxCommand,
    *,
    cwd: str | None = None,
    env: dict[str, str] | None = None,
    timeout_ms: int | None = None,
    stdin: bool = False,
    on_stdout: OutputHandler | None = None,
    on_stderr: OutputHandler | None = None,
  ) -> SandboxProcess:
    await self._socket.ensure_open()

    request_id = create_request_id()
    process = SandboxProcess(request_id, self._socket)
    if on_stdout is not None:
      process.on_stdout(on_stdout)
    if on_stderr is not None:
      process.on_stderr(on_stderr)

    self._processes[request_id] = process

    request: dict[str, Any] = {
      "id": request_id,
      "op": "run",
      "v": 1,
      "command": _to_argv(command),
    }
    if cwd is not None:
      request["cwd"] = cwd
    if env is not None:
      request["env"] = env
    if stdin:
      request["stdin"] = True
    if timeout_ms is not None:
      request["timeoutMs"] = timeout_ms

    if not await self._socket.send(json.dumps(request)):
      self._processes.pop(request_id, None)
      process._handle_error(_lost_error())

    return process

  async def command(
    self,
    command: SandboxCommand,
    *,
    cwd: str | None = None,
    env: dict[str, str] | None = None,
    timeout_ms: int | None = None,
    stdin: str | bytes | None = None,
    on_stdout: OutputHandler | None = None,
    on_stderr: OutputHandler | None = None,
  ) -> SandboxCommandResult:
    stdout: list[bytes] = []
    stderr: list[bytes] = []

    process = await self.spawn(
      command,
      cwd=cwd,
      env=env,
      timeout_ms=timeout_ms,
      stdin=stdin is not None,
      on_stdout=stdout.append,
      on_stderr=stderr.append,
    )
    if on_stdout is not None:
      process.on_stdout(on_stdout)
    if on_stderr is not None:
      process.on_stderr(on_stderr)

    if stdin is not None and not process.is_done:
      if stdin:
        await process.write(stdin)
      await process.close_stdin()

    exit = await process.wait()
    return SandboxCommandResult(
      exit_code=exit.exit_code,
      signal=exit.signal,
      timed_out=exit.timed_out,
      stdout_bytes=b"".join(stdout),
      stderr_bytes=b"".join(stderr),
    )

  async def close(self) -> None:
    await self._socket.close()

  def _handle_text(self, message: dict[str, Any]) -> None:
    request_id = message.get("id")
    if not isinstance(request_id, str):
      return

    process = self._processes.get(request_id)
    if process is None:
      return

    kind = message.get("type")
    if kind == "started":
      process._handle_started(int(message.get("pid") or 0))
    elif kind == "exit":
      self._processes.pop(request_id, None)
      code = message.get("code")
      signal = message.get("signal")
      process._handle_exit(
        SandboxProcessExit(
          exit_code=code if isinstance(code, int) else None,
          signal=signal if isinstance(signal, str) else None,
          timed_out=message.get("timedOut") is True,
        )
      )
    elif kind == "error":
      self._processes.pop(request_id, None)
      process._handle_error(server_error(message.get("error"), SandboxCommandError))

  def _handle_binary(self, data: bytes) -> None:
    frame = decode_frame(data, has_tag=True)
    if frame is None:
      return

    process = self._processes.get(frame[0])
    if process is not None:
      process._handle_output(frame[1], frame[2])

  def _handle_disconnect(self, error: SandboxAccessError) -> None:
    interrupted = (
      error
      if error.code == "closed"
      else SandboxCommandError("connection_interrupted", str(error))
    )

    processes = list(self._processes.values())
    self._processes.clear()
    for process in processes:
      process._handle_error(interrupted)
