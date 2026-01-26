from __future__ import annotations

import json
from collections.abc import Generator, Iterable
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
  from metorial._protocols import (
    SessionWithToolManagerProtocol,
    ToolManagerProtocol,
  )


def build_anthropic_tools(tool_mgr: ToolManagerProtocol | None) -> list[dict[str, Any]]:
  """Build Anthropic-compatible tool definitions from Metorial tools."""
  tools: list[dict[str, Any]] = []
  if tool_mgr is None:
    return tools
  for t in tool_mgr.get_tools():
    # Get the raw schema and ensure it has proper structure
    raw_schema = t.get_parameters_as("json-schema")

    if not raw_schema or not raw_schema.get("properties"):
      # Try to access original parameters from various possible attributes
      for attr_name in [
        "_parameters",
        "parameters",
        "_schema",
        "schema",
        "_input_schema",
        "input_schema",
      ]:
        if hasattr(t, attr_name):
          potential_schema = getattr(t, attr_name)
          if (
            potential_schema
            and isinstance(potential_schema, dict)
            and potential_schema.get("properties")
          ):
            raw_schema = potential_schema
            break

      # If still empty, check if it's an MCP tool and access MCP-specific attributes
      if (not raw_schema or not raw_schema.get("properties")) and hasattr(t, "_action"):
        # This might be a MetorialMcpTool - try to get original MCP schema
        if hasattr(t, "_parameters") and t._parameters:
          raw_schema = t._parameters
        elif str(type(t)).find("MetorialMcpTool") != -1:
          # Debug info: MCP tool attributes (removed for clean output)
          pass

        # Try common MCP tool schema attributes
        for mcp_attr in ["_parameters", "_schema", "input_schema"]:
          if hasattr(t, mcp_attr):
            mcp_schema = getattr(t, mcp_attr)
            if mcp_schema and isinstance(mcp_schema, dict):
              raw_schema = mcp_schema
              # Found schema in {mcp_attr}: {mcp_schema} (debug info removed)
              break

    # If still no good schema, create tool-specific defaults based on tool name
    if not raw_schema or not raw_schema.get("properties"):
      if "search" in t.name.lower():
        raw_schema = {
          "type": "object",
          "properties": {
            "query": {"type": "string", "description": "The search query"},
            "numResults": {
              "type": "number",
              "description": "Number of results to return",
              "minimum": 1,
              "maximum": 100,
              "default": 10,
            },
          },
          "required": ["query"],
          "additionalProperties": False,
        }
      elif "content" in t.name.lower():
        raw_schema = {
          "type": "object",
          "properties": {
            "url": {
              "type": "string",
              "description": "URL to get content for",
              "format": "uri",
            }
          },
          "required": ["url"],
          "additionalProperties": False,
        }
      elif "similar" in t.name.lower():
        raw_schema = {
          "type": "object",
          "properties": {
            "url": {
              "type": "string",
              "description": "URL to find similar content for",
              "format": "uri",
            }
          },
          "required": ["url"],
          "additionalProperties": False,
        }
      else:
        # Generic fallback
        raw_schema = {
          "type": "object",
          "properties": {
            "input": {"type": "string", "description": f"Input for {t.name}"}
          },
          "required": [],
          "additionalProperties": False,
        }

    # Ensure the schema has the minimum required structure
    if "type" not in raw_schema:
      raw_schema["type"] = "object"
    if "properties" not in raw_schema:
      raw_schema["properties"] = {}
    if "additionalProperties" not in raw_schema:
      raw_schema["additionalProperties"] = False

    tools.append(
      {
        "name": t.name,
        "description": t.description or f"Tool: {t.name}",
        "input_schema": raw_schema,
      }
    )
  return tools


def _attr_or_key(obj: object, attr: str, key: str, default: object = None) -> object:
  """Helper to get attribute or key from object."""
  if hasattr(obj, attr):
    return getattr(obj, attr)
  if isinstance(obj, dict):
    return obj.get(key, default)
  return default


async def call_anthropic_tools(
  tool_mgr: ToolManagerProtocol | None, tool_calls: list[object]
) -> dict[str, Any]:
  """
  Call Metorial tools from Anthropic tool use blocks.
  Returns a user message with tool results.
  """
  tool_results = []

  if tool_mgr is None:
    # Return error message for each tool call if no tool manager available
    for tc in tool_calls:
      tool_use_id = _attr_or_key(tc, "id", "id")
      tool_results.append(
        {
          "type": "tool_result",
          "tool_use_id": tool_use_id,
          "content": "[ERROR] Tool manager not available",
        }
      )
    return {"role": "user", "content": tool_results}

  for tc in tool_calls:
    # Handle both direct tool call objects and standardized format
    if isinstance(tc, dict) and "function" in tc:
      # Standardized format from ChatResponse
      tool_use_id = tc.get("id")
      function_obj = tc.get("function", {})
      tool_name = function_obj.get("name")
      raw_args = function_obj.get("arguments", "{}")

      # Parse arguments if they're a string
      try:
        tool_input = (
          eval(raw_args) if isinstance(raw_args, str) and raw_args.strip() else {}
        )
      except Exception:
        try:
          tool_input = (
            json.loads(raw_args)
            if isinstance(raw_args, str) and raw_args.strip()
            else {}
          )
        except Exception:
          tool_input = {}
    else:
      # Direct tool call object format
      tool_use_id = _attr_or_key(tc, "id", "id")
      tool_name = _attr_or_key(tc, "name", "name")
      tool_input = _attr_or_key(tc, "input", "input", {})

    try:
      # Handle input parsing
      args = json.loads(tool_input) if isinstance(tool_input, str) else tool_input
    except Exception as e:
      tool_results.append(
        {
          "type": "tool_result",
          "tool_use_id": tool_use_id,
          "content": f"[ERROR] Invalid JSON arguments: {e}",
        }
      )
      continue

    try:
      result = await tool_mgr.execute_tool(str(tool_name), args)
      if hasattr(result, "model_dump"):
        result = result.model_dump()
      content = json.dumps(result, ensure_ascii=False, default=str)
    except Exception as e:
      content = f"[ERROR] Tool call failed: {e!r}"

    tool_results.append(
      {
        "type": "tool_result",
        "tool_use_id": tool_use_id,
        "content": content,
      }
    )

  return {
    "role": "user",
    "content": tool_results,
  }


class MetorialAnthropicSession:
  """Anthropic-specific session wrapper for Metorial tools."""

  def __init__(
    self, tool_mgr: ToolManagerProtocol | SessionWithToolManagerProtocol
  ) -> None:
    # Check if we received a session instead of a tool manager
    # Sessions have get_tool_manager method, tool managers have get_tools method
    if hasattr(tool_mgr, "get_tool_manager") and not hasattr(tool_mgr, "get_tools"):
      # This is a session, defer initialization until __await__
      self._session: SessionWithToolManagerProtocol | None = tool_mgr
      self._tool_mgr: ToolManagerProtocol | None = None
      self.tools: list[dict[str, Any]] = []
      self._initialized = False
    else:
      # This is a tool manager, initialize normally
      self._session = None
      self._tool_mgr = cast("ToolManagerProtocol", tool_mgr)
      self.tools = build_anthropic_tools(self._tool_mgr)
      self._initialized = True

  async def _init_from_session(self) -> None:
    """Initialize from a session by getting the tool manager."""
    if self._session is not None and not self._initialized:
      self._tool_mgr = await self._session.get_tool_manager()
      self.tools = build_anthropic_tools(self._tool_mgr)
      self._initialized = True

  def __await__(self) -> Generator[Any, None, dict[str, Any]]:
    """Make the session awaitable for use with with_provider_session."""
    return self._get_provider_data().__await__()

  async def _get_provider_data(self) -> dict[str, Any]:
    """Get provider data dict for with_provider_session."""
    await self._init_from_session()
    return {
      "tools": self.tools,
      "callTools": self.call_tools,
    }

  async def call_tools(self, tool_calls: Iterable[Any]) -> dict[str, Any]:
    """Execute tool calls and return Anthropic-compatible message."""
    return await call_anthropic_tools(self._tool_mgr, list(tool_calls))

  @staticmethod
  async def chat_completions(session: SessionWithToolManagerProtocol) -> dict[str, Any]:
    """Convenience provider for with_provider_session.

    Example:
      await metorial.with_provider_session(
        MetorialAnthropicSession.chat_completions,
        ["your-deployment-id"],
        action
      )
    """
    tool_mgr = await session.get_tool_manager()
    provider_session = MetorialAnthropicSession(tool_mgr)
    return {"tools": provider_session.tools}


async def chat_completions(session: SessionWithToolManagerProtocol) -> dict[str, Any]:
  """Module-level convenience provider to pass into with_provider_session.

  Usage:
    import metorial_anthropic as manthro
    await metorial.with_provider_session(
      manthro.chat_completions,
      ["your-deployment-id"],
      action
    )
  """
  tool_mgr = await session.get_tool_manager()
  provider_session = MetorialAnthropicSession(tool_mgr)
  return {"tools": provider_session.tools}
