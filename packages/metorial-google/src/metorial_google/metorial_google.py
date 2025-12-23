import json
from typing import Any, Dict, Iterable, List


def build_google_tools(tool_mgr):
  """Build Google Gemini-compatible tool definitions from Metorial tools."""
  function_declarations = []
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


def _attr_or_key(obj, attr, key, default=None):
  """Helper to get attribute or key from object."""
  if hasattr(obj, attr):
    return getattr(obj, attr)
  if isinstance(obj, dict):
    return obj.get(key, default)
  return default


async def call_google_tools(tool_mgr, function_calls: List[Any]) -> Dict[str, Any]:
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
      if isinstance(call_args, str):
        args = json.loads(call_args)
      else:
        args = call_args
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
      result = await tool_mgr.execute_tool(call_name, args)
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

  def __init__(self, tool_mgr):
    # Check if we received a session instead of a tool manager
    # Sessions have get_tool_manager method, tool managers have get_tools method
    if hasattr(tool_mgr, 'get_tool_manager') and not hasattr(tool_mgr, 'get_tools'):
      # This is a session, defer initialization until __await__
      self._session = tool_mgr
      self._tool_mgr = None
      self.tools = []
      self._initialized = False
    else:
      # This is a tool manager, initialize normally
      self._session = None
      self._tool_mgr = tool_mgr
      self.tools = build_google_tools(tool_mgr)
      self._initialized = True

  async def _init_from_session(self):
    """Initialize from a session by getting the tool manager."""
    if self._session is not None and not self._initialized:
      self._tool_mgr = await self._session.get_tool_manager()
      self.tools = build_google_tools(self._tool_mgr)
      self._initialized = True

  def __await__(self):
    """Make the session awaitable for use with with_provider_session."""
    return self._get_provider_data().__await__()

  async def _get_provider_data(self) -> Dict[str, Any]:
    """Get provider data dict for with_provider_session."""
    await self._init_from_session()
    return {
      "tools": self.tools,
      "callTools": self.call_tools,
    }

  async def call_tools(self, function_calls: Iterable[Any]) -> Dict[str, Any]:
    """Execute function calls and return Google-compatible content."""
    return await call_google_tools(self._tool_mgr, list(function_calls))

  @staticmethod
  async def chat_completions(session) -> Dict[str, Any]:
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


async def chat_completions(session) -> Dict[str, Any]:
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
