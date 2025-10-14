from typing import Any, Dict
from metorial_openai_compatible import MetorialOpenAICompatibleSession


class MetorialXAISession(MetorialOpenAICompatibleSession):
  """XAI (Grok) provider session using OpenAI-compatible interface with strict mode."""

  def __init__(self, tool_mgr):
    # XAI supports strict mode
    super().__init__(tool_mgr, with_strict=True)

  @staticmethod
  async def chat_completions(session) -> Dict[str, Any]:
    """Convenience provider for with_provider_session.

    Example:
      await metorial.with_provider_session(
        MetorialXAISession.chat_completions,
        ["your-deployment-id"],
        action
      )
    """
    tool_mgr = await session.get_tool_manager()
    provider_session = MetorialXAISession(tool_mgr)
    return {"tools": provider_session.tools}


def build_xai_tools(tool_mgr):
  """Build XAI-compatible tool definitions from Metorial tools."""
  if tool_mgr is None:
    return []
  session = MetorialXAISession(tool_mgr)
  return session.tools


async def call_xai_tools(tool_mgr, tool_calls):
  """Call Metorial tools from XAI tool calls."""
  if tool_mgr is None:
    return []
  session = MetorialXAISession(tool_mgr)
  return await session.call_tools(tool_calls)


async def chat_completions(session) -> Dict[str, Any]:
  """Module-level convenience provider to pass into with_provider_session.

  Usage:
    import metorial_xai as mxai
    await metorial.with_provider_session(
      mxai.chat_completions,
      ["your-deployment-id"],
      action
    )
  """
  tool_mgr = await session.get_tool_manager()
  provider_session = MetorialXAISession(tool_mgr)
  return {"tools": provider_session.tools}
