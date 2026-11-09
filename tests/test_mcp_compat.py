from __future__ import annotations

from datetime import timedelta
from importlib.metadata import version
from typing import Any

import mcp.types as mcp_types
import pytest
from pydantic import AnyUrl

from metorial._tool_results import normalize_tool_result, serialize_tool_result
from metorial.mcp._compat import (
  MCP_V2,
  get_field,
  parse_jsonrpc_json,
  parse_jsonrpc_message,
  resource_uri,
  session_read_timeout,
  to_snake_case,
  unwrap_jsonrpc_message,
)
from metorial.mcp.mcp_client import MetorialClientSession
from metorial.mcp.mcp_tool import MetorialMcpTool

TOOL_WIRE = {
  "name": "search",
  "description": "Search things",
  "inputSchema": {
    "type": "object",
    "properties": {"q": {"type": "string"}},
    "required": ["q"],
  },
}

CALL_RESULT_WIRE = {
  "content": [{"type": "text", "text": "hi"}],
  "structuredContent": {"answer": 42},
  "isError": False,
}


def test_detected_major_matches_installed_mcp() -> None:
  installed_major = int(version("mcp").split(".")[0])
  assert MCP_V2 is (installed_major >= 2)


def test_session_read_timeout_matches_client_session_contract() -> None:
  assert session_read_timeout(None) is None
  converted = session_read_timeout(2.5)
  if MCP_V2:
    assert converted == 2.5
    assert isinstance(converted, float)
  else:
    assert converted == timedelta(seconds=2.5)


@pytest.mark.parametrize(
  ("camel", "snake"),
  [
    ("inputSchema", "input_schema"),
    ("uriTemplate", "uri_template"),
    ("resourceTemplates", "resource_templates"),
    ("isError", "is_error"),
    ("name", "name"),
  ],
)
def test_to_snake_case(camel: str, snake: str) -> None:
  assert to_snake_case(camel) == snake


def test_get_field_reads_models_of_installed_major() -> None:
  tool = mcp_types.Tool.model_validate(TOOL_WIRE)
  assert get_field(tool, "inputSchema") == TOOL_WIRE["inputSchema"]
  assert get_field(tool, "description") == "Search things"
  assert get_field(tool, "outputSchema") is None
  assert get_field(tool, "doesNotExist", "fallback") == "fallback"


@pytest.mark.parametrize(
  "obj",
  [
    {"inputSchema": {"type": "object"}},
    {"input_schema": {"type": "object"}},
    type("V1Like", (), {"inputSchema": {"type": "object"}})(),
    type("V2Like", (), {"input_schema": {"type": "object"}})(),
  ],
  ids=["camel-dict", "snake-dict", "camel-attr", "snake-attr"],
)
def test_get_field_accepts_either_naming(obj: Any) -> None:
  assert get_field(obj, "inputSchema") == {"type": "object"}


def test_get_field_handles_none() -> None:
  assert get_field(None, "inputSchema", "x") == "x"


def test_jsonrpc_parse_and_unwrap_round_trip() -> None:
  request = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
  for message in (
    parse_jsonrpc_message(request),
    parse_jsonrpc_json('{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}'),
  ):
    inner = unwrap_jsonrpc_message(message)
    assert isinstance(inner, mcp_types.JSONRPCRequest)
    assert inner.method == "tools/list"
    assert (
      message.model_dump(by_alias=True, mode="json", exclude_none=True) == request  # type: ignore[union-attr]
    )

  error = unwrap_jsonrpc_message(
    parse_jsonrpc_message(
      {"jsonrpc": "2.0", "id": 2, "error": {"code": -1, "message": "no"}}
    )
  )
  assert isinstance(error, mcp_types.JSONRPCError)


def test_resource_uri_matches_read_resource_contract() -> None:
  uri = resource_uri("note://alpha")
  if MCP_V2:
    assert uri == "note://alpha"
  else:
    assert isinstance(uri, AnyUrl)
    assert str(uri) == "note://alpha"


def test_client_session_overrides_both_validation_hooks() -> None:
  assert "_validate_tool_result" in MetorialClientSession.__dict__
  assert "validate_tool_result" in MetorialClientSession.__dict__


def test_normalize_tool_result_uses_wire_names() -> None:
  result = mcp_types.CallToolResult.model_validate(CALL_RESULT_WIRE)
  normalized = normalize_tool_result(result)

  assert normalized["content"] == CALL_RESULT_WIRE["content"]
  assert normalized["structuredContent"] == {"answer": 42}
  assert normalized["isError"] is False
  assert not any("_" in key.lstrip("_") for key in normalized)


def test_normalize_tool_result_passes_plain_data_through() -> None:
  assert normalize_tool_result({"a": 1}) == {"a": 1}
  assert normalize_tool_result("text") == "text"
  assert serialize_tool_result({"a": "é"}) == '{"a": "é"}'


def test_normalize_tool_result_supports_duck_typed_models() -> None:
  class Legacy:
    def model_dump(self) -> dict[str, Any]:
      return {"legacy": True}

  assert normalize_tool_result(Legacy()) == {"legacy": True}


class _NoSession:
  async def get_client(self, opts: dict[str, str]) -> Any:
    raise AssertionError("not called")


def test_metorial_tool_reads_schema_from_installed_major_model() -> None:
  capability = {
    "type": "tool",
    "tool": mcp_types.Tool.model_validate(TOOL_WIRE),
    "serverDeployment": {"id": "dep"},
  }
  tool = MetorialMcpTool.from_capability(_NoSession(), capability)  # type: ignore[arg-type]

  assert tool.name == "search"
  assert tool.description == "Search things"
  assert tool.parameters == TOOL_WIRE["inputSchema"]


def test_metorial_tool_reads_uri_template_from_installed_major_model() -> None:
  capability = {
    "type": "resource-template",
    "resourceTemplate": mcp_types.ResourceTemplate.model_validate(
      {"name": "note", "uriTemplate": "note://{name}"}
    ),
    "serverDeployment": {"id": "dep"},
  }
  tool = MetorialMcpTool.from_capability(_NoSession(), capability)  # type: ignore[arg-type]

  assert tool.parameters["required"] == ["name"]
