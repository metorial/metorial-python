"""Bridges the differences between the 1.x and 2.x MCP Python SDKs.

Every place in Metorial that depends on an API that changed between the two
majors goes through this module, so the rest of the SDK can stay
version-agnostic. The differences handled here:

- ``ClientSession(read_timeout_seconds=...)`` takes a ``timedelta`` in 1.x and
  a ``float`` of seconds in 2.x.
- ``mcp.types.JSONRPCMessage`` is a pydantic ``RootModel`` in 1.x (the concrete
  message lives on ``.root``) and a plain ``Union`` of message models in 2.x.
- MCP models expose camelCase attributes in 1.x (``tool.inputSchema``) and
  snake_case attributes in 2.x (``tool.input_schema``). The wire format is
  camelCase in both.
- ``ClientSession.get_server_capabilities()`` became the
  ``ClientSession.server_capabilities`` property in 2.x.
- ``ClientSession.read_resource`` takes a pydantic ``AnyUrl`` in 1.x and a
  ``str`` in 2.x.
"""

from __future__ import annotations

import re
from datetime import timedelta
from typing import TYPE_CHECKING, Any

from mcp.types import JSONRPCMessage, ServerCapabilities, Tool
from pydantic import AnyUrl, TypeAdapter

if TYPE_CHECKING:
  from mcp import ClientSession

MCP_V2: bool = "input_schema" in Tool.model_fields

_JSONRPC_MESSAGE_ADAPTER: TypeAdapter[JSONRPCMessage] = TypeAdapter(JSONRPCMessage)

_CAMEL_BOUNDARY = re.compile(r"(?<!^)(?=[A-Z])")

_MISSING = object()


def session_read_timeout(seconds: float | None) -> Any:
  if seconds is None:
    return None
  return float(seconds) if MCP_V2 else timedelta(seconds=seconds)


def parse_jsonrpc_message(data: Any) -> JSONRPCMessage:
  return _JSONRPC_MESSAGE_ADAPTER.validate_python(data)


def parse_jsonrpc_json(data: str | bytes) -> JSONRPCMessage:
  return _JSONRPC_MESSAGE_ADAPTER.validate_json(data)


def unwrap_jsonrpc_message(message: JSONRPCMessage) -> Any:
  """Return the concrete request/notification/response/error model."""
  return message if MCP_V2 else message.root  # type: ignore[union-attr,attr-defined,unused-ignore]


def to_snake_case(name: str) -> str:
  return _CAMEL_BOUNDARY.sub("_", name).lower()


def get_field(obj: Any, name: str, default: Any = None) -> Any:
  """Read an MCP field by its camelCase wire name from a dict or a model.

  Accepts raw JSON dicts, 1.x models (camelCase attributes) and 2.x models
  (snake_case attributes) alike.
  """
  if obj is None:
    return default

  snake = to_snake_case(name)

  if isinstance(obj, dict):
    if name in obj:
      return obj[name]
    return obj.get(snake, default)

  value = getattr(obj, name, _MISSING)
  if value is _MISSING:
    value = getattr(obj, snake, default)
  return value


def get_server_capabilities(session: ClientSession) -> ServerCapabilities | None:
  if MCP_V2:
    return session.server_capabilities  # type: ignore[attr-defined,no-any-return,unused-ignore]
  return session.get_server_capabilities()  # type: ignore[attr-defined,no-any-return,unused-ignore]


def resource_uri(uri: str) -> Any:
  return uri if MCP_V2 else AnyUrl(uri)
