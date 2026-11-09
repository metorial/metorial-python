from __future__ import annotations

import json
from collections.abc import AsyncIterator, Callable
from types import SimpleNamespace
from typing import Any

import httpx
import pytest
from mcp.shared.message import SessionMessage
from mcp.types import JSONRPCError, JSONRPCResponse

from metorial.mcp._compat import parse_jsonrpc_message, unwrap_jsonrpc_message
from metorial.mcp.transport import POST_FAILED_ERROR_CODE, MetorialMcpTransport

URL = "http://mcp.test/mcp"

Handler = Callable[[httpx.Request], httpx.Response]


def _request(id_: int, method: str, params: dict[str, Any] | None = None) -> Any:
  payload: dict[str, Any] = {"jsonrpc": "2.0", "id": id_, "method": method}
  if params is not None:
    payload["params"] = params
  return parse_jsonrpc_message(payload)


def _notification(method: str) -> Any:
  return parse_jsonrpc_message({"jsonrpc": "2.0", "method": method})


def _json(body: Any, **headers: str) -> httpx.Response:
  return httpx.Response(
    200,
    content=json.dumps(body).encode(),
    headers={"content-type": "application/json", **headers},
  )


class _Recorder:
  def __init__(self, handler: Handler) -> None:
    self.requests: list[httpx.Request] = []
    self._handler = handler

  def __call__(self, request: httpx.Request) -> httpx.Response:
    self.requests.append(request)
    return self._handler(request)


@pytest.fixture
async def make_transport() -> AsyncIterator[
  Callable[[Handler], tuple[MetorialMcpTransport, _Recorder]]
]:
  transports: list[MetorialMcpTransport] = []

  def factory(handler: Handler) -> tuple[MetorialMcpTransport, _Recorder]:
    recorder = _Recorder(handler)
    client = httpx.AsyncClient(transport=httpx.MockTransport(recorder))
    transport = MetorialMcpTransport(URL, client=client, headers={"x-api": "k"})
    transports.append(transport)
    return transport, recorder

  yield factory

  for transport in transports:
    await transport.close()


async def _roundtrip(transport: MetorialMcpTransport, message: Any) -> Any:
  read, write = await transport.open()
  await write.send(SessionMessage(message))
  received = await read.receive()
  assert isinstance(received, SessionMessage)
  return unwrap_jsonrpc_message(received.message)


async def test_session_and_protocol_headers_follow_initialize(make_transport) -> None:
  def handler(request: httpx.Request) -> httpx.Response:
    body = json.loads(request.content)
    if body["method"] == "initialize":
      return _json(
        {
          "jsonrpc": "2.0",
          "id": body["id"],
          "result": {
            "protocolVersion": "2025-06-18",
            "capabilities": {},
            "serverInfo": {"name": "s", "version": "1"},
          },
        },
        **{"mcp-session-id": "sess-123"},
      )
    return _json({"jsonrpc": "2.0", "id": body["id"], "result": {"tools": []}})

  transport, recorder = make_transport(handler)

  init = await _roundtrip(transport, _request(1, "initialize", {}))
  assert isinstance(init, JSONRPCResponse)
  listed = await _roundtrip(transport, _request(2, "tools/list"))
  assert isinstance(listed, JSONRPCResponse)

  first, second = recorder.requests
  assert first.headers["x-api"] == "k"
  assert "mcp-session-id" not in first.headers
  assert second.headers["mcp-session-id"] == "sess-123"
  assert second.headers["mcp-protocol-version"] == "2025-06-18"
  assert json.loads(second.content) == {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
  }


async def test_per_message_headers_are_forwarded(make_transport) -> None:
  transport, recorder = make_transport(
    lambda request: _json(
      {"jsonrpc": "2.0", "id": json.loads(request.content)["id"], "result": {}}
    )
  )
  read, write = await transport.open()

  metadata = SimpleNamespace(headers={"mcp-method": "tools/list"})
  await write.send(SessionMessage(_request(1, "tools/list"), metadata=metadata))  # type: ignore[arg-type]
  await read.receive()

  assert recorder.requests[0].headers["mcp-method"] == "tools/list"


async def test_sse_response_is_parsed(make_transport) -> None:
  def handler(request: httpx.Request) -> httpx.Response:
    request_id = json.loads(request.content)["id"]
    progress = {"jsonrpc": "2.0", "method": "notifications/message", "params": {}}
    result = {"jsonrpc": "2.0", "id": request_id, "result": {"ok": True}}
    body = (
      f"event: message\ndata: {json.dumps(progress)}\n\n"
      f"event: message\ndata: {json.dumps(result)}\n\n"
    )
    return httpx.Response(
      200, content=body.encode(), headers={"content-type": "text/event-stream"}
    )

  transport, _ = make_transport(handler)
  read, write = await transport.open()
  await write.send(SessionMessage(_request(7, "tools/call", {"name": "x"})))

  first = unwrap_jsonrpc_message((await read.receive()).message)  # type: ignore[union-attr]
  second = unwrap_jsonrpc_message((await read.receive()).message)  # type: ignore[union-attr]
  assert first.method == "notifications/message"
  assert isinstance(second, JSONRPCResponse)
  assert second.result == {"ok": True}


async def test_batched_json_response(make_transport) -> None:
  transport, _ = make_transport(
    lambda request: _json(
      [
        {"jsonrpc": "2.0", "method": "notifications/message", "params": {}},
        {"jsonrpc": "2.0", "id": 3, "result": {}},
      ]
    )
  )
  read, write = await transport.open()
  await write.send(SessionMessage(_request(3, "ping")))

  first = unwrap_jsonrpc_message((await read.receive()).message)  # type: ignore[union-attr]
  second = unwrap_jsonrpc_message((await read.receive()).message)  # type: ignore[union-attr]
  assert first.method == "notifications/message"
  assert isinstance(second, JSONRPCResponse)


async def test_failed_request_becomes_error_and_transport_survives(
  make_transport,
) -> None:
  def handler(request: httpx.Request) -> httpx.Response:
    body = json.loads(request.content)
    if body["method"] == "tools/call":
      return httpx.Response(500, content=b"boom")
    return _json({"jsonrpc": "2.0", "id": body["id"], "result": {}})

  transport, _ = make_transport(handler)

  failed = await _roundtrip(transport, _request(1, "tools/call", {"name": "x"}))
  assert isinstance(failed, JSONRPCError)
  assert failed.id == 1
  assert failed.error.code == POST_FAILED_ERROR_CODE
  assert "500" in failed.error.message

  recovered = await _roundtrip(transport, _request(2, "ping"))
  assert isinstance(recovered, JSONRPCResponse)


async def test_failed_notification_surfaces_exception(make_transport) -> None:
  def handler(request: httpx.Request) -> httpx.Response:
    body = json.loads(request.content)
    if "id" not in body:
      raise httpx.ConnectError("down")
    return _json({"jsonrpc": "2.0", "id": body["id"], "result": {}})

  transport, _ = make_transport(handler)
  read, write = await transport.open()

  await write.send(SessionMessage(_notification("notifications/initialized")))
  assert isinstance(await read.receive(), httpx.ConnectError)

  await write.send(SessionMessage(_request(2, "ping")))
  received = await read.receive()
  assert isinstance(received, SessionMessage)
  assert isinstance(unwrap_jsonrpc_message(received.message), JSONRPCResponse)


async def test_accepted_notification_produces_no_message(make_transport) -> None:
  def handler(request: httpx.Request) -> httpx.Response:
    body = json.loads(request.content)
    if "id" not in body:
      return httpx.Response(202)
    return _json({"jsonrpc": "2.0", "id": body["id"], "result": {}})

  transport, recorder = make_transport(handler)
  read, write = await transport.open()

  await write.send(SessionMessage(_notification("notifications/initialized")))
  await write.send(SessionMessage(_request(4, "ping")))
  received = await read.receive()

  assert isinstance(received, SessionMessage)
  assert unwrap_jsonrpc_message(received.message).id == 4
  assert len(recorder.requests) == 2


async def test_close_terminates_session(make_transport) -> None:
  def handler(request: httpx.Request) -> httpx.Response:
    if request.method == "DELETE":
      return httpx.Response(204)
    body = json.loads(request.content)
    return _json(
      {"jsonrpc": "2.0", "id": body["id"], "result": {}},
      **{"mcp-session-id": "sess-9"},
    )

  transport, recorder = make_transport(handler)
  await _roundtrip(transport, _request(1, "ping"))
  await transport.close()

  delete = recorder.requests[-1]
  assert delete.method == "DELETE"
  assert delete.headers["mcp-session-id"] == "sess-9"
