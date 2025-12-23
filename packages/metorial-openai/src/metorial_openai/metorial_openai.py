import json
from typing import Any, Dict, Iterable, List


def build_openai_tools(tool_mgr):
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
        },
      }
    )
  return tools


def _attr_or_key(obj, attr, key, default=None):
  if hasattr(obj, attr):
    return getattr(obj, attr)
  if isinstance(obj, dict):
    return obj.get(key, default)
  return default


async def call_openai_tools(tool_mgr, tool_calls: List[Any]) -> List[Dict[str, Any]]:
  msgs: List[Dict[str, Any]] = []

  if tool_mgr is None:
    # Return error message for each tool call if no tool manager available
    for tc in tool_calls:
      tc_id = _attr_or_key(tc, "id", "id")
      msgs.append(
        {
          "role": "tool",
          "tool_call_id": tc_id,
          "content": "[ERROR] Tool manager not available",
        }
      )
    return msgs

  for tc in tool_calls:
    tc_id = _attr_or_key(tc, "id", "id")
    fn_obj = _attr_or_key(tc, "function", "function", {})
    fn_name = _attr_or_key(fn_obj, "name", "name")
    raw_args = _attr_or_key(fn_obj, "arguments", "arguments", "{}")

    try:
      args = (
        json.loads(raw_args) if isinstance(raw_args, str) and raw_args.strip() else {}
      )
    except Exception as e:
      msgs.append(
        {
          "role": "tool",
          "tool_call_id": tc_id,
          "content": f"[ERROR] Invalid JSON arguments: {e}",
        }
      )
      continue

    try:
      result = await tool_mgr.execute_tool(fn_name, args)
      if hasattr(result, "model_dump"):
        result = result.model_dump()
      content = json.dumps(result, ensure_ascii=False, default=str)
    except Exception as e:
      content = f"[ERROR] Tool call failed: {e!r}"

    msgs.append(
      {
        "role": "tool",
        "tool_call_id": tc_id,
        "content": content,
      }
    )

  return msgs


class MetorialOpenAISession:
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
      self.tools = build_openai_tools(tool_mgr)
      self._initialized = True

  async def _init_from_session(self):
    """Initialize from a session by getting the tool manager."""
    if self._session is not None and not self._initialized:
      self._tool_mgr = await self._session.get_tool_manager()
      self.tools = build_openai_tools(self._tool_mgr)
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
    return await call_openai_tools(self._tool_mgr, list(tool_calls))

  @staticmethod
  async def chat_completions(session) -> Dict[str, Any]:
    """Convenience provider for with_provider_session.

    Example:
      await metorial.with_provider_session(
        MetorialOpenAISession.chat_completions,
        ["your-deployment-id"],
        action
      )
    """
    tool_mgr = await session.get_tool_manager()
    provider_session = MetorialOpenAISession(tool_mgr)
    return {"tools": provider_session.tools, "callTools": provider_session.call_tools}


async def chat_completions(session) -> Dict[str, Any]:
  """Module-level convenience provider to pass into with_provider_session.

  Usage:
    import metorial_openai as mopenai
    await metorial.with_provider_session(
      mopenai.chat_completions,
      ["your-deployment-id"],
      action
    )
  """
  tool_mgr = await session.get_tool_manager()
  provider_session = MetorialOpenAISession(tool_mgr)
  return {"tools": provider_session.tools}
