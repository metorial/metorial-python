import json
from typing import Any, Dict, Iterable, List


def build_mistral_tools(tool_mgr):
  """Build Mistral-compatible tool definitions from Metorial tools."""
  tools = []
  if tool_mgr is None:
    return tools
  for t in tool_mgr.get_tools():
    tools.append(
      {
        "type": "function",
        "function": {
          "name": t.name,
          "description": t.description or "",
          "parameters": t.get_parameters_as("json-schema"),
          "strict": True,
        },
      }
    )
  return tools


def _attr_or_key(obj, attr, key, default=None):
  """Helper to get attribute or key from object."""
  if hasattr(obj, attr):
    return getattr(obj, attr)
  if isinstance(obj, dict):
    return obj.get(key, default)
  return default


async def call_mistral_tools(tool_mgr, tool_calls: List[Any]) -> List[Dict[str, Any]]:
  """
  Call Metorial tools from Mistral tool calls.
  Returns a list of tool messages.
  """
  messages = []

  if tool_mgr is None:
    # Return error message for each tool call if no tool manager available
    for tc in tool_calls:
      tool_call_id = _attr_or_key(tc, "id", "id")
      messages.append(
        {
          "tool_call_id": tool_call_id,
          "role": "tool",
          "content": "[ERROR] Tool manager not available",
        }
      )
    return messages

  for tc in tool_calls:
    tool_call_id = _attr_or_key(tc, "id", "id")
    function_obj = _attr_or_key(tc, "function", "function", {})
    function_name = _attr_or_key(function_obj, "name", "name")
    function_args = _attr_or_key(function_obj, "arguments", "arguments", "{}")

    try:
      if isinstance(function_args, str):
        args = json.loads(function_args) if function_args.strip() else {}
      else:
        args = function_args
    except Exception as e:
      messages.append(
        {
          "tool_call_id": tool_call_id,
          "role": "tool",
          "content": f"[ERROR] Invalid JSON arguments: {e}",
        }
      )
      continue

    try:
      result = await tool_mgr.execute_tool(function_name, args)
      if hasattr(result, "model_dump"):
        result = result.model_dump()
      content = json.dumps(result, ensure_ascii=False, default=str)
    except Exception as e:
      content = f"[ERROR] Tool call failed: {e!r}"

    messages.append(
      {
        "tool_call_id": tool_call_id,
        "role": "tool",
        "content": content,
      }
    )

  return messages


class MetorialMistralSession:
  """Mistral-specific session wrapper for Metorial tools."""

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
      self.tools = build_mistral_tools(tool_mgr)
      self._initialized = True

  async def _init_from_session(self):
    """Initialize from a session by getting the tool manager."""
    if self._session is not None and not self._initialized:
      self._tool_mgr = await self._session.get_tool_manager()
      self.tools = build_mistral_tools(self._tool_mgr)
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

  async def call_tools(self, tool_calls: Iterable[Any]) -> List[Dict[str, Any]]:
    """Execute tool calls and return Mistral-compatible messages."""
    return await call_mistral_tools(self._tool_mgr, list(tool_calls))

  @staticmethod
  async def chat_completions(session) -> Dict[str, Any]:
    """Convenience provider for with_provider_session.

    Example:
      await metorial.with_provider_session(
        MetorialMistralSession.chat_completions,
        ["your-deployment-id"],
        action
      )
    """
    tool_mgr = await session.get_tool_manager()
    provider_session = MetorialMistralSession(tool_mgr)
    return {"tools": provider_session.tools}


async def chat_completions(session) -> Dict[str, Any]:
  """Module-level convenience provider to pass into with_provider_session.

  Usage:
    import metorial_mistral as mmistral
    await metorial.with_provider_session(
      mmistral.chat_completions,
      ["your-deployment-id"],
      action
    )
  """
  tool_mgr = await session.get_tool_manager()
  provider_session = MetorialMistralSession(tool_mgr)
  return {"tools": provider_session.tools}
