"""
XAI (Grok) provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_xai import build_xai_tools, call_xai_tools
else:
  try:
    from metorial_xai import build_xai_tools, call_xai_tools
  except ImportError:
    call_xai_tools: Callable[[Any, Any], list[dict[str, Any]]] | None = None
    build_xai_tools: Callable[[Any], list[dict[str, Any]]] | None = None


class XAIAdapter(ProviderAdapter):
  """Adapter for XAI (Grok) providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "grok-beta",
    **kwargs: Any,
  ) -> ChatResponse:
    # XAI uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "grok-beta",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # XAI uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using XAI format"""
    if call_xai_tools is None:
      raise ImportError("metorial-xai package is required for XAI adapter")

    tool_messages = await call_xai_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in XAI format"""
    if build_xai_tools is None:
      raise ImportError("metorial-xai package is required for XAI adapter")

    return cast(list[dict[str, Any]], build_xai_tools(self.tool_manager))
