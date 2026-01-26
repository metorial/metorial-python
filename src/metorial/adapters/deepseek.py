"""
DeepSeek provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_deepseek import build_deepseek_tools, call_deepseek_tools
else:
  try:
    from metorial_deepseek import build_deepseek_tools, call_deepseek_tools
  except ImportError:
    call_deepseek_tools: Callable[[Any, Any], list[dict[str, Any]]] | None = None
    build_deepseek_tools: Callable[[Any], list[dict[str, Any]]] | None = None


class DeepSeekAdapter(ProviderAdapter):
  """Adapter for DeepSeek providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "deepseek-chat",
    **kwargs: Any,
  ) -> ChatResponse:
    # DeepSeek uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "deepseek-chat",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # DeepSeek uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using DeepSeek format"""
    if call_deepseek_tools is None:
      raise ImportError("metorial-deepseek package is required for DeepSeek adapter")

    tool_messages = await call_deepseek_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in DeepSeek format"""
    if build_deepseek_tools is None:
      raise ImportError("metorial-deepseek package is required for DeepSeek adapter")

    return cast(list[dict[str, Any]], build_deepseek_tools(self.tool_manager))
