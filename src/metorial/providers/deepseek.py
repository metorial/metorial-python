from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

from metorial.providers.openai_compatible import MetorialOpenAICompatibleSession

if TYPE_CHECKING:
  from metorial._protocols import (
    SessionWithToolManagerProtocol,
    ToolManagerProtocol,
  )


class MetorialDeepSeekSession(MetorialOpenAICompatibleSession):
  """DeepSeek provider session using OpenAI-compatible interface without strict mode."""

  def __init__(
    self, tool_mgr: ToolManagerProtocol | SessionWithToolManagerProtocol
  ) -> None:
    # DeepSeek doesn't support strict mode
    super().__init__(tool_mgr, with_strict=False)


def build_deepseek_tools(tool_mgr: ToolManagerProtocol | None) -> list[dict[str, Any]]:
  """Build DeepSeek-compatible tool definitions from Metorial tools."""
  if tool_mgr is None:
    return []
  session = MetorialDeepSeekSession(tool_mgr)
  return session.tools


async def call_deepseek_tools(
  tool_mgr: ToolManagerProtocol | None, tool_calls: Iterable[object]
) -> list[dict[str, Any]]:
  """Call Metorial tools from DeepSeek tool calls."""
  if tool_mgr is None:
    return []
  session = MetorialDeepSeekSession(tool_mgr)
  return await session.call_tools(tool_calls)
