"""End-to-end tests of the Metorial MCP client against a real MCP server.

The server is the official Streamable HTTP server shipped by whichever MCP
Python SDK is installed (``FastMCP`` in 1.x, ``MCPServer`` in 2.x), so running
this suite under both majors checks that the client interoperates with each.
"""

from __future__ import annotations

import asyncio
import json
import socket
import threading
import time
from collections.abc import Iterator
from typing import Any

import pytest
import uvicorn

from metorial._tool_results import normalize_tool_result, serialize_tool_result
from metorial.mcp import MetorialMagnetarMcpSession, MetorialMcpClient
from metorial.mcp._compat import MCP_V2, get_field
from metorial.mcp.mcp_client import RequestOptions

ADD_SCHEMA_PROPERTIES = {"a", "b"}


def _build_app(json_response: bool) -> Any:
  if MCP_V2:
    from mcp.server.mcpserver import MCPServer

    server: Any = MCPServer("metorial-test")
  else:
    from mcp.server.fastmcp import FastMCP

    server = FastMCP("metorial-test", json_response=json_response)

  @server.tool(description="Add two integers")
  def add(a: int, b: int) -> int:
    return a + b

  @server.tool(description="Always fails")
  def explode() -> str:
    raise ValueError("kaboom")

  @server.tool(description="Sleeps before answering")
  async def slow(seconds: float) -> str:
    await asyncio.sleep(seconds)
    return "done"

  @server.resource("config://app", description="Static config")
  def config() -> str:
    return "config-body"

  @server.resource("note://{name}", description="A note by name")
  def note(name: str) -> str:
    return f"note:{name}"

  @server.prompt(description="Greets someone")
  def greet(name: str) -> str:
    return f"Hello {name}"

  if MCP_V2:
    return server.streamable_http_app(json_response=json_response)
  return server.streamable_http_app()


def _free_port() -> int:
  with socket.socket() as sock:
    sock.bind(("127.0.0.1", 0))
    return int(sock.getsockname()[1])


@pytest.fixture(scope="module", params=["sse", "json"])
def server_url(request: pytest.FixtureRequest) -> Iterator[str]:
  port = _free_port()
  config = uvicorn.Config(
    _build_app(json_response=request.param == "json"),
    host="127.0.0.1",
    port=port,
    log_level="error",
  )
  server = uvicorn.Server(config)
  thread = threading.Thread(target=server.run, daemon=True)
  thread.start()

  deadline = time.monotonic() + 10
  while not server.started:
    if time.monotonic() > deadline:
      raise RuntimeError("MCP test server did not start")
    time.sleep(0.02)

  yield f"http://127.0.0.1:{port}/mcp"

  server.should_exit = True
  thread.join(timeout=10)


async def _connect(url: str, **kwargs: Any) -> MetorialMcpClient:
  return await MetorialMcpClient.from_url(url, use_http_stream=True, **kwargs)


async def test_handshake_and_capabilities(server_url: str) -> None:
  async with await _connect(server_url) as client:
    caps = client.get_server_capabilities()
    assert get_field(caps, "tools") is not None
    assert get_field(caps, "resources") is not None
    assert get_field(caps, "prompts") is not None


async def test_list_tools_exposes_input_schema(server_url: str) -> None:
  async with await _connect(server_url) as client:
    result = await client.list_tools()

  tools = {tool.name: tool for tool in get_field(result, "tools")}
  assert set(tools) == {"add", "explode", "slow"}

  schema = get_field(tools["add"], "inputSchema")
  assert schema["type"] == "object"
  assert set(schema["properties"]) == ADD_SCHEMA_PROPERTIES


async def test_call_tool_result_serializes_to_wire_format(server_url: str) -> None:
  async with await _connect(server_url) as client:
    result = await client.call_tool({"name": "add", "arguments": {"a": 2, "b": 3}})

  payload = normalize_tool_result(result)
  assert payload["isError"] is False
  assert payload["content"][0] == {"type": "text", "text": "5"}
  assert "is_error" not in payload
  assert "structured_content" not in payload
  assert json.loads(serialize_tool_result(result)) == payload


async def test_failing_tool_reports_error_result(server_url: str) -> None:
  async with await _connect(server_url) as client:
    result = await client.call_tool({"name": "explode", "arguments": {}})

  payload = normalize_tool_result(result)
  text = payload["content"][0]["text"]
  assert payload["isError"] is True
  assert "explode" in text or "kaboom" in text


async def test_read_timeout_is_enforced(server_url: str) -> None:
  async with await _connect(server_url, read_timeout=0.5) as client:
    started = time.monotonic()
    with pytest.raises(Exception, match="(?i)tim"):
      await client.call_tool({"name": "slow", "arguments": {"seconds": 5}})
    assert time.monotonic() - started < 4

    result = await client.call_tool({"name": "add", "arguments": {"a": 1, "b": 1}})
    assert normalize_tool_result(result)["content"][0]["text"] == "2"


async def test_per_request_timeout_option(server_url: str) -> None:
  async with await _connect(server_url) as client:
    with pytest.raises(asyncio.TimeoutError):
      await client.list_tools(options=RequestOptions(timeout=0.000001))


async def test_resources(server_url: str) -> None:
  async with await _connect(server_url) as client:
    resources = await client.list_resources()
    templates = await client.list_resource_templates()
    static = await client.read_resource({"uri": "config://app"})
    templated = await client.read_resource({"uri": "note://alpha"})

  assert [str(get_field(r, "uri")) for r in get_field(resources, "resources")] == [
    "config://app"
  ]
  assert [
    get_field(t, "uriTemplate") for t in get_field(templates, "resourceTemplates")
  ] == ["note://{name}"]
  assert normalize_tool_result(static)["contents"][0]["text"] == "config-body"
  assert normalize_tool_result(templated)["contents"][0]["text"] == "note:alpha"


async def test_prompts(server_url: str) -> None:
  async with await _connect(server_url) as client:
    prompts = await client.list_prompts()
    prompt = await client.get_prompt({"name": "greet", "arguments": {"name": "Ada"}})

  assert [p.name for p in get_field(prompts, "prompts")] == ["greet"]
  message = normalize_tool_result(prompt)["messages"][0]
  assert message["content"]["text"] == "Hello Ada"


async def test_close_is_idempotent_and_blocks_further_use(server_url: str) -> None:
  client = await _connect(server_url)
  await client.close()
  await client.close()

  with pytest.raises(RuntimeError, match="closed"):
    await client.list_tools()


class _FakeMagnetarSessions:
  def __init__(self, connection_url: str) -> None:
    self._connection_url = connection_url

  def create(self, **kwargs: Any) -> dict[str, Any]:
    return {
      "id": "ses_test",
      "connection_url": self._connection_url,
      "provider_deployments": [{"id": "dep_test"}],
    }


class _FakeMagnetarSDK:
  def __init__(self, connection_url: str) -> None:
    self._config = {"apiKey": "test-key", "apiHost": "http://127.0.0.1"}
    self.magnetar_sessions = _FakeMagnetarSessions(connection_url)


async def test_magnetar_session_tool_discovery_and_execution(server_url: str) -> None:
  session = MetorialMagnetarMcpSession(
    _FakeMagnetarSDK(server_url),  # type: ignore[arg-type]
    {"providers": ["dep_test"]},
  )
  try:
    manager = await session.get_tool_manager()

    add = manager.get_tool("add")
    assert add is not None
    assert set(add.parameters["properties"]) == ADD_SCHEMA_PROPERTIES

    note = manager.get_tool("note")
    assert note is not None
    assert note.parameters["required"] == ["name"]

    result = await manager.call_tool("add", {"a": 20, "b": 22})
    assert normalize_tool_result(result)["content"][0]["text"] == "42"

    resource = await manager.call_tool("note", {"name": "beta"})
    assert normalize_tool_result(resource)["contents"][0]["text"] == "note:beta"
  finally:
    await session.close()
