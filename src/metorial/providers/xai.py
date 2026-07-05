from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

from metorial.providers.openai_compatible import MetorialOpenAICompatibleSession

if TYPE_CHECKING:
  from metorial._protocols import (
    SessionWithToolManagerProtocol,
    ToolManagerProtocol,
  )


class MetorialXAISession(MetorialOpenAICompatibleSession):
  """XAI (Grok) provider session using OpenAI-compatible interface with strict mode."""

  def __init__(
    self, tool_mgr: ToolManagerProtocol | SessionWithToolManagerProtocol
  ) -> None:
    # XAI supports strict mode
    super().__init__(tool_mgr, with_strict=True)


def build_xai_tools(tool_mgr: ToolManagerProtocol | None) -> list[dict[str, Any]]:
  """Build XAI-compatible tool definitions from Metorial tools."""
  if tool_mgr is None:
    return []
  session = MetorialXAISession(tool_mgr)
  return session.tools


async def call_xai_tools(
  tool_mgr: ToolManagerProtocol | None, tool_calls: Iterable[object]
) -> list[dict[str, Any]]:
  """Call Metorial tools from XAI tool calls."""
  if tool_mgr is None:
    return []
  session = MetorialXAISession(tool_mgr)
  return await session.call_tools(tool_calls)
