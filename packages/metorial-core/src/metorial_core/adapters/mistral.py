"""
Mistral provider adapter.
"""

from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_mistral import call_mistral_tools, build_mistral_tools
else:
  try:
    from metorial_mistral import call_mistral_tools, build_mistral_tools
  except ImportError:
    call_mistral_tools: Optional[Callable[[Any, List[Any]], Any]] = None
    build_mistral_tools: Optional[Callable[[Any], Any]] = None


class MistralAdapter(ProviderAdapter):
  """Adapter for Mistral AI providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "mistral-large-latest",
    **kwargs,
  ) -> ChatResponse:
    # Mistral uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "mistral-large-latest",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # Mistral uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using Mistral format"""
    if call_mistral_tools is None:
      raise ImportError("metorial-mistral package is required for Mistral adapter")

    tool_messages = await call_mistral_tools(self.tool_manager, tool_calls)

    # Convert to standardized format
    messages = []
    for msg in tool_messages:
      messages.append(
        ChatMessage(
          role=msg.get("role", "tool"),
          content=msg.get("content"),
          tool_call_id=msg.get("tool_call_id"),
        )
      )
    return messages

  def get_tools_for_provider(self) -> List[Dict[str, Any]]:
    """Get tools in Mistral format"""
    if build_mistral_tools is None:
      raise ImportError("metorial-mistral package is required for Mistral adapter")

    result = build_mistral_tools(self.tool_manager)
    return result  # type: ignore[no-any-return]
