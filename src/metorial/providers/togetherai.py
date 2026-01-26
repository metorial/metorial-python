from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

from metorial.providers.openai_compatible import MetorialOpenAICompatibleSession

if TYPE_CHECKING:
  from metorial._protocols import (
    SessionWithToolManagerProtocol,
    ToolManagerProtocol,
  )


class MetorialTogetherAISession(MetorialOpenAICompatibleSession):
  """TogetherAI provider session using OpenAI-compatible interface without strict mode."""

  def __init__(
    self, tool_mgr: ToolManagerProtocol | SessionWithToolManagerProtocol
  ) -> None:
    # TogetherAI doesn't support strict mode
    super().__init__(tool_mgr, with_strict=False)

  @staticmethod
  async def chat_completions(session: SessionWithToolManagerProtocol) -> dict[str, Any]:
    """Convenience provider for with_provider_session.

    Example:
      await metorial.with_provider_session(
        MetorialTogetherAISession.chat_completions,
        ["your-deployment-id"],
        action
      )
    """
    tool_mgr = await session.get_tool_manager()
    provider_session = MetorialTogetherAISession(tool_mgr)
    return {"tools": provider_session.tools}


# Convenience functions
def build_togetherai_tools(
  tool_mgr: ToolManagerProtocol | None,
) -> list[dict[str, Any]]:
  """Build TogetherAI-compatible tool definitions from Metorial tools."""
  if tool_mgr is None:
    return []
  session = MetorialTogetherAISession(tool_mgr)
  return session.tools


async def call_togetherai_tools(
  tool_mgr: ToolManagerProtocol | None, tool_calls: Iterable[object]
) -> list[dict[str, Any]]:
  """Call Metorial tools from TogetherAI tool calls."""
  if tool_mgr is None:
    return []
  session = MetorialTogetherAISession(tool_mgr)
  return await session.call_tools(tool_calls)


async def chat_completions(session: SessionWithToolManagerProtocol) -> dict[str, Any]:
  """Module-level convenience provider to pass into with_provider_session.

  Usage:
    import metorial_togetherai as mtogetherai
    await metorial.with_provider_session(
      mtogetherai.chat_completions,
      ["your-deployment-id"],
      action
    )
  """
  tool_mgr = await session.get_tool_manager()
  provider_session = MetorialTogetherAISession(tool_mgr)
  return {"tools": provider_session.tools}
