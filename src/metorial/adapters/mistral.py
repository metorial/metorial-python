"""
Mistral provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_mistral import build_mistral_tools, call_mistral_tools
else:
  try:
    from metorial_mistral import build_mistral_tools, call_mistral_tools
  except ImportError:
    call_mistral_tools: Callable[[Any, list[Any]], list[dict[str, Any]]] | None = None
    build_mistral_tools: Callable[[Any], list[dict[str, Any]]] | None = None


class MistralAdapter(ProviderAdapter):
  """Adapter for Mistral AI providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "mistral-large-latest",
    **kwargs: Any,
  ) -> ChatResponse:
    # Mistral uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "mistral-large-latest",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # Mistral uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using Mistral format"""
    if call_mistral_tools is None:
      raise ImportError("metorial-mistral package is required for Mistral adapter")

    tool_messages = await call_mistral_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in Mistral format"""
    if build_mistral_tools is None:
      raise ImportError("metorial-mistral package is required for Mistral adapter")

    return cast(list[dict[str, Any]], build_mistral_tools(self.tool_manager))
