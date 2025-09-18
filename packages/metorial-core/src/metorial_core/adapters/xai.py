"""
XAI (Grok) provider adapter.
"""

from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_xai import call_xai_tools, build_xai_tools
else:
  try:
    from metorial_xai import call_xai_tools, build_xai_tools
  except ImportError:
    call_xai_tools: Optional[Callable[[Any, Any], Any]] = None
    build_xai_tools: Optional[Callable[[Any], Any]] = None


class XAIAdapter(ProviderAdapter):
  """Adapter for XAI (Grok) providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "grok-beta",
    **kwargs,
  ) -> ChatResponse:
    # XAI uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "grok-beta",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # XAI uses OpenAI-compatible format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using XAI format"""
    if call_xai_tools is None:
      raise ImportError("metorial-xai package is required for XAI adapter")

    tool_messages = await call_xai_tools(self.tool_manager, tool_calls)

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
    """Get tools in XAI format"""
    if build_xai_tools is None:
      raise ImportError("metorial-xai package is required for XAI adapter")

    result = build_xai_tools(self.tool_manager)
    return result  # type: ignore[no-any-return]
