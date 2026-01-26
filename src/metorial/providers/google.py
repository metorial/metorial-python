from __future__ import annotations

import json
from collections.abc import Generator, Iterable
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
  from metorial._protocols import (
    SessionWithToolManagerProtocol,
    ToolManagerProtocol,
  )


def build_google_tools(tool_mgr: ToolManagerProtocol | None) -> list[dict[str, Any]]:
  """Build Google Gemini-compatible tool definitions from Metorial tools."""
  function_declarations: list[dict[str, Any]] = []
  if tool_mgr is None:
    return [{"function_declarations": function_declarations}]
  for t in tool_mgr.get_tools():
    function_declarations.append(
      {
        "name": t.name,
        "description": t.description or "",
        "parameters": t.get_parameters_as(
          "openapi-3.0.0"
        ),  # Google uses OpenAPI format
      }
    )

  return [{"function_declarations": function_declarations}]


def _attr_or_key(obj: object, attr: str, key: str, default: object = None) -> object:
  """Helper to get attribute or key from object."""
  if hasattr(obj, attr):
    return getattr(obj, attr)
  if isinstance(obj, dict):
    return obj.get(key, default)
  return default


async def call_google_tools(
  tool_mgr: ToolManagerProtocol | None, function_calls: list[object]
) -> dict[str, Any]:
  """
  Call Metorial tools from Google function calls.
  Returns a user content with function responses.
  """
  parts = []

  if tool_mgr is None:
    # Return error message for each function call if no tool manager available
    for fc in function_calls:
      call_id = _attr_or_key(fc, "id", "id")
      call_name = _attr_or_key(fc, "name", "name")
      parts.append(
        {
          "function_response": {
            "id": call_id,
            "name": call_name,
            "response": {"error": "[ERROR] Tool manager not available"},
          }
        }
      )
    return {"role": "user", "parts": parts}

  for fc in function_calls:
    call_id = _attr_or_key(fc, "id", "id")
    call_name = _attr_or_key(fc, "name", "name")
    call_args = _attr_or_key(fc, "args", "args", {})

    try:
      # Handle args parsing
      args = json.loads(call_args) if isinstance(call_args, str) else call_args
    except Exception as e:
      parts.append(
        {
          "function_response": {
            "id": call_id,
            "name": call_name,
            "response": {"error": f"[ERROR] Invalid JSON arguments: {e}"},
          }
        }
      )
      continue

    try:
      result = await tool_mgr.execute_tool(str(call_name), cast(dict[str, Any], args))
      if hasattr(result, "model_dump"):
        result = result.model_dump()
    except Exception as e:
      result = {"error": f"[ERROR] Tool call failed: {e!r}"}

    parts.append(
      {
        "function_response": {
          "id": call_id,
          "name": call_name,
          "response": result,
        }
      }
    )

  return {
    "role": "user",
    "parts": parts,
  }


class MetorialGoogleSession:
  """Google Gemini-specific session wrapper for Metorial tools."""

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
      self.tools = build_google_tools(self._tool_mgr)
      self._initialized = True

  async def _init_from_session(self) -> None:
    """Initialize from a session by getting the tool manager."""
    if self._session is not None and not self._initialized:
      self._tool_mgr = await self._session.get_tool_manager()
      self.tools = build_google_tools(self._tool_mgr)
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

  async def call_tools(self, function_calls: Iterable[Any]) -> dict[str, Any]:
    """Execute function calls and return Google-compatible content."""
    return await call_google_tools(self._tool_mgr, list(function_calls))

  @staticmethod
  async def chat_completions(session: SessionWithToolManagerProtocol) -> dict[str, Any]:
    """Convenience provider for with_provider_session.

    Example:
      await metorial.with_provider_session(
        MetorialGoogleSession.chat_completions,
        ["your-deployment-id"],
        action
      )
    """
    tool_mgr = await session.get_tool_manager()
    provider_session = MetorialGoogleSession(tool_mgr)
    return {"tools": provider_session.tools}


async def chat_completions(session: SessionWithToolManagerProtocol) -> dict[str, Any]:
  """Module-level convenience provider to pass into with_provider_session.

  Usage:
    import metorial_google as mgoogle
    await metorial.with_provider_session(
      mgoogle.chat_completions,
      ["your-deployment-id"],
      action
    )
  """
  tool_mgr = await session.get_tool_manager()
  provider_session = MetorialGoogleSession(tool_mgr)
  return {"tools": provider_session.tools}
