from __future__ import annotations

import asyncio
import hashlib
import json
from collections.abc import AsyncIterator
from datetime import datetime, timedelta, timezone
from typing import Any

import pytest
from aiohttp import WSMsgType, web

from metorial.sandbox import (
  SandboxAccessCache,
  SandboxAccessError,
  SandboxAccessGrant,
  SandboxCommandError,
  SandboxFiles,
  SandboxPort,
  SandboxShell,
)
from metorial.sandbox._mux import decode_frame, encode_frame


class FakeSandbox:
  def __init__(self) -> None:
    self.files: dict[str, bytes] = {}
    self.valid_tokens = {"good"}
    self.connections = 0
    self.flaky_drops = 0
    self.move_requests = 0
    self.token_requests = 0
    self.base_url = ""

  def _token(self, request: web.Request) -> str | None:
    protocols = request.headers.get("Sec-WebSocket-Protocol", "").split(",")
    for protocol in (p.strip() for p in protocols):
      if protocol.startswith("metorial-sandbox-token."):
        return protocol[len("metorial-sandbox-token.") :]
    return None

  async def socket(self, request: web.Request) -> web.StreamResponse:
    if self._token(request) not in self.valid_tokens:
      return web.Response(status=401, text="token_invalid")

    ws = web.WebSocketResponse(protocols=["metorial-sandbox-v1"])
    await ws.prepare(request)
    self.connections += 1

    if request.path == "/files":
      await self._files(ws)
    else:
      await self._exec(ws)
    return ws

  async def _files(self, ws: web.WebSocketResponse) -> None:
    uploads: dict[str, tuple[str, list[bytes]]] = {}

    async for message in ws:
      if message.type == WSMsgType.BINARY:
        frame = decode_frame(message.data)
        assert frame is not None
        if frame[0] in uploads:
          uploads[frame[0]][1].append(frame[2])
        continue

      if message.type != WSMsgType.TEXT:
        continue

      data = json.loads(message.data)
      request_id = data["id"]

      async def reply(fields: dict[str, Any], request_id: str = request_id) -> None:
        await ws.send_str(json.dumps({"id": request_id, **fields}))

      if data.get("type") == "end":
        upload = uploads.pop(request_id, None)
        if upload is None:
          continue
        content = b"".join(upload[1])
        if data.get("sha256") != hashlib.sha256(content).hexdigest():
          await reply({"type": "error", "error": {"code": "checksum_mismatch"}})
          continue
        self.files[upload[0]] = content
        await reply({"type": "result", "size": len(content)})
        continue

      op, path = data.get("op"), data.get("path")

      if op == "write":
        if not data["overwrite"] and path in self.files:
          error = {"code": "already_exists", "path": path}
          await reply({"type": "error", "error": error})
        else:
          uploads[request_id] = (path, [])
      elif op == "read":
        if path not in self.files:
          error = {"code": "not_found", "message": "missing", "path": path}
          await reply({"type": "error", "error": error})
          continue
        content = self.files[path]
        await reply({"type": "start", "size": len(content), "mtime": 0, "offset": 0})
        for start in range(0, len(content), 5):
          await ws.send_bytes(encode_frame(request_id, content[start : start + 5]))
        await reply({"type": "result"})
      elif op == "stat":
        if path not in self.files:
          await reply({"type": "error", "error": {"code": "not_found"}})
          continue
        entry = {
          "path": path,
          "type": "file",
          "size": len(self.files[path]),
          "mode": 420,
          "mtime": 1000,
        }
        await reply({"type": "result", "entry": entry})
      elif op == "list":
        if path == "/flaky" and self.flaky_drops > 0:
          self.flaky_drops -= 1
          await reply({"type": "entries", "entries": [{"name": "partial"}]})
          await ws.close(code=1011)
          return
        entries = [
          {"name": name[len(path) + 1 :], "type": "file", "size": len(c), "mtime": 0}
          for name, c in self.files.items()
          if name.startswith(f"{path}/")
        ]
        await reply({"type": "entries", "entries": entries[:1]})
        await reply({"type": "entries", "entries": entries[1:]})
        await reply({"type": "result", "count": len(entries), "truncated": False})
      elif op == "move":
        self.move_requests += 1
        await ws.close(code=1011)
        return
      elif op == "delete":
        self.files.pop(path, None)
        await reply({"type": "result"})

  async def _exec(self, ws: web.WebSocketResponse) -> None:
    stdin: dict[str, list[bytes]] = {}

    async def output(request_id: str, stream: int, text: str) -> None:
      await ws.send_bytes(encode_frame(request_id, text.encode(), stream))

    async for message in ws:
      if message.type == WSMsgType.BINARY:
        frame = decode_frame(message.data)
        assert frame is not None
        stdin.setdefault(frame[0], []).append(frame[2])
        continue

      if message.type != WSMsgType.TEXT:
        continue

      data = json.loads(message.data)
      request_id = data["id"]

      async def send(fields: dict[str, Any], request_id: str = request_id) -> None:
        await ws.send_str(json.dumps({"id": request_id, **fields}))

      if data.get("type") == "stdin_eof":
        text = b"".join(stdin.pop(request_id, [])).decode().upper()
        await output(request_id, 1, text)
        await send({"type": "exit", "code": 0, "signal": None, "timedOut": False})
        continue

      if data.get("type") == "signal":
        exit = {"code": None, "signal": data["signal"], "timedOut": False}
        await send({"type": "exit", **exit})
        continue

      program, *args = data["command"]
      await send({"type": "started", "pid": 42})

      if program == "missing":
        error = {"code": "spawn_failed", "message": "not found"}
        await send({"type": "error", "error": error})
      elif program == "drop":
        await ws.close(code=1011)
        return
      elif data.get("stdin") or program == "sleep":
        stdin.setdefault(request_id, [])
      else:
        await output(request_id, 1, f"ran {' '.join(args)}")
        await output(request_id, 2, f"cwd={data.get('cwd', '')}")
        await send({"type": "exit", "code": 3, "signal": None, "timedOut": False})

  async def http(self, request: web.Request) -> web.Response:
    token = request.headers.get("Metorial-Sandbox-Token")
    if token not in self.valid_tokens:
      return web.Response(status=401, text="token_invalid")

    body = await request.text()
    return web.json_response(
      {
        "method": request.method,
        "url": str(request.rel_url),
        "body": body,
        "test": request.headers.get("x-test"),
      }
    )

  def access(self, path: str, tokens: list[str] | None = None) -> SandboxAccessCache:
    queue = list(tokens or ["good"])

    async def provider() -> SandboxAccessGrant:
      self.token_requests += 1
      token = queue.pop(0) if len(queue) > 1 else queue[0]
      base = self.base_url
      url = f"{base}/app" if path == "/port" else base.replace("http", "ws") + path
      expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
      return SandboxAccessGrant(url=url, token=token, expires_at=expires_at)

    return SandboxAccessCache(provider)


@pytest.fixture
async def sandbox() -> AsyncIterator[FakeSandbox]:
  fake = FakeSandbox()
  app = web.Application()
  app.router.add_get("/files", fake.socket)
  app.router.add_get("/exec", fake.socket)
  app.router.add_route("*", "/app/{tail:.*}", fake.http)

  runner = web.AppRunner(app)
  await runner.setup()
  site = web.TCPSite(runner, "127.0.0.1", 0)
  await site.start()

  port = runner.addresses[0][1]
  fake.base_url = f"http://127.0.0.1:{port}"

  yield fake
  await runner.cleanup()


async def test_files_roundtrip(sandbox: FakeSandbox) -> None:
  async with await SandboxFiles.connect(sandbox.access("/files")) as files:
    big = b"x" * (200 * 1024)
    await files.write("/work/a.txt", "hello world")
    await files.write("/work/b.bin", big)

    assert await files.read_text("/work/a.txt") == "hello world"
    assert await files.read("/work/b.bin") == big

    entry = await files.stat("/work/a.txt")
    assert (entry.name, entry.path, entry.type, entry.size) == (
      "a.txt",
      "/work/a.txt",
      "file",
      11,
    )

    listing = await files.list("/work")
    assert not listing.truncated
    assert sorted(e.path for e in listing.entries) == ["/work/a.txt", "/work/b.bin"]

    await files.delete("/work/a.txt")
    assert not await files.exists("/work/a.txt")


async def test_files_errors(sandbox: FakeSandbox) -> None:
  async with await SandboxFiles.connect(sandbox.access("/files")) as files:
    with pytest.raises(SandboxAccessError) as missing:
      await files.read("/nope")
    assert (missing.value.code, missing.value.path) == ("not_found", "/nope")

    await files.write("/exists", "a")
    with pytest.raises(SandboxAccessError) as exists:
      await files.write("/exists", "b", overwrite=False)
    assert exists.value.code == "already_exists"


async def test_files_refreshes_rejected_token(sandbox: FakeSandbox) -> None:
  files = await SandboxFiles.connect(sandbox.access("/files", ["stale", "good"]))
  assert sandbox.token_requests == 2
  await files.write("/refresh", "ok")
  assert await files.read_text("/refresh") == "ok"
  await files.close()


async def test_files_resends_pending_list(sandbox: FakeSandbox) -> None:
  async with await SandboxFiles.connect(sandbox.access("/files")) as files:
    await files.write("/flaky/one", "1")
    sandbox.flaky_drops = 2

    listing = await files.list("/flaky")
    assert sandbox.flaky_drops == 0
    assert [e.path for e in listing.entries] == ["/flaky/one"]


async def test_files_does_not_resend_move(sandbox: FakeSandbox) -> None:
  async with await SandboxFiles.connect(sandbox.access("/files")) as files:
    with pytest.raises(SandboxAccessError) as error:
      await files.move("/a", "/b")
    assert error.value.code == "disconnected"
    assert sandbox.move_requests == 1


async def test_files_closed(sandbox: FakeSandbox) -> None:
  files = await SandboxFiles.connect(sandbox.access("/files"))
  await files.close()
  with pytest.raises(SandboxAccessError) as error:
    await files.stat("/x")
  assert error.value.code == "closed"


async def test_shell_commands(sandbox: FakeSandbox) -> None:
  async with await SandboxShell.connect(sandbox.access("/exec")) as shell:
    result = await shell.command(["echo", "hi", "there"], cwd="/tmp")
    assert (result.exit_code, result.signal, result.timed_out) == (3, None, False)
    assert (result.stdout, result.stderr) == ("ran hi there", "cwd=/tmp")

    via_shell = await shell.command("ls -la")
    assert via_shell.stdout == "ran -c ls -la"

    piped = await shell.command(["cat"], stdin="shout")
    assert piped.stdout == "SHOUT"


async def test_shell_spawn_signal(sandbox: FakeSandbox) -> None:
  async with await SandboxShell.connect(sandbox.access("/exec")) as shell:
    process = await shell.spawn(["sleep", "100"])
    assert await process.started() == 42

    await process.signal("SIGTERM")
    exit = await process.wait()
    assert (exit.exit_code, exit.signal) == (None, "TERM")


async def test_shell_errors_and_reconnect(sandbox: FakeSandbox) -> None:
  async with await SandboxShell.connect(sandbox.access("/exec")) as shell:
    with pytest.raises(SandboxCommandError) as spawn_error:
      await shell.command(["missing"])
    assert spawn_error.value.code == "spawn_failed"

    before = sandbox.connections
    with pytest.raises(SandboxCommandError) as dropped:
      await shell.command(["drop"])
    assert dropped.value.code == "connection_interrupted"

    await asyncio.sleep(0.6)
    assert sandbox.connections - before == 1

    result = await shell.command(["echo", "again"])
    assert result.stdout == "ran again"


async def test_port_requests(sandbox: FakeSandbox) -> None:
  async with await SandboxPort.connect(3000, sandbox.access("/port")) as port:
    response = await port.get("/testing?x=1", headers={"x-test": "yes"})
    assert response.json() == {
      "method": "GET",
      "url": "/app/testing?x=1",
      "body": "",
      "test": "yes",
    }

    posted = await port.post("/items", json={"name": "a"})
    assert posted.json()["body"] == '{"name":"a"}'
    assert port.url == f"{sandbox.base_url}/app"

    with pytest.raises(ValueError):
      await port.get("https://example.com/")


async def test_port_retries_401(sandbox: FakeSandbox) -> None:
  port = await SandboxPort.connect(3000, sandbox.access("/port", ["stale", "good"]))
  response = await port.get("/")
  assert response.status_code == 200

  await port.close()
  with pytest.raises(SandboxAccessError):
    await port.get("/")
