"""
DeepSeek provider adapter.
"""

from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_deepseek import call_deepseek_tools, build_deepseek_tools
else:
  try:
    from metorial_deepseek import call_deepseek_tools, build_deepseek_tools
  except ImportError:
    call_deepseek_tools: Optional[Callable[[Any, Any], Any]] = None
    build_deepseek_tools: Optional[Callable[[Any], Any]] = None


class DeepSeekAdapter(ProviderAdapter):
  """Adapter for DeepSeek providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "deepseek-chat",
    **kwargs,
  ) -> ChatResponse:
    # DeepSeek uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "deepseek-chat",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # DeepSeek uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using DeepSeek format"""
    if call_deepseek_tools is None:
      raise ImportError("metorial-deepseek package is required for DeepSeek adapter")

    tool_messages = await call_deepseek_tools(self.tool_manager, tool_calls)

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
    """Get tools in DeepSeek format"""
    if build_deepseek_tools is None:
      raise ImportError("metorial-deepseek package is required for DeepSeek adapter")

    result = build_deepseek_tools(self.tool_manager)
    return result  # type: ignore[no-any-return]
