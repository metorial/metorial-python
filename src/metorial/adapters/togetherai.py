"""
Together AI provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_togetherai import build_togetherai_tools, call_togetherai_tools
else:
  try:
    from metorial_togetherai import build_togetherai_tools, call_togetherai_tools
  except ImportError:
    call_togetherai_tools: Callable[[Any, Any], list[dict[str, Any]]] | None = None
    build_togetherai_tools: Callable[[Any], list[dict[str, Any]]] | None = None


class TogetherAIAdapter(ProviderAdapter):
  """Adapter for Together AI providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "meta-llama/Llama-2 - 70b-chat-hf",
    **kwargs: Any,
  ) -> ChatResponse:
    # Together AI uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "meta-llama/Llama-2 - 70b-chat-hf",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # Together AI uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using Together AI format"""
    if call_togetherai_tools is None:
      raise ImportError(
        "metorial-togetherai package is required for Together AI adapter"
      )

    tool_messages = await call_togetherai_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in Together AI format"""
    if build_togetherai_tools is None:
      raise ImportError(
        "metorial-togetherai package is required for Together AI adapter"
      )

    return cast(list[dict[str, Any]], build_togetherai_tools(self.tool_manager))
