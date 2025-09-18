"""
OpenAI-compatible provider adapter.
"""

from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_openai_compatible import (
    call_openai_compatible_tools,
    build_openai_compatible_tools,
  )
else:
  try:
    from metorial_openai_compatible import (
      call_openai_compatible_tools,
      build_openai_compatible_tools,
    )
  except ImportError:
    call_openai_compatible_tools: Optional[Callable[[Any, List[Any]], Any]] = None
    build_openai_compatible_tools: Optional[Callable[[Any, bool], Any]] = None


class OpenAICompatibleAdapter(ProviderAdapter):
  """Generic adapter for OpenAI-compatible providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs,
  ) -> ChatResponse:
    # OpenAI-compatible providers use OpenAI format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # OpenAI-compatible providers use OpenAI format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using OpenAI-compatible format"""
    if call_openai_compatible_tools is None:
      raise ImportError(
        "metorial-openai-compatible package is required for OpenAI-compatible adapter"
      )

    tool_messages = await call_openai_compatible_tools(self.tool_manager, tool_calls)

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
    """Get tools in OpenAI-compatible format"""
    if build_openai_compatible_tools is None:
      raise ImportError(
        "metorial-openai-compatible package is required for OpenAI-compatible adapter"
      )

    result = build_openai_compatible_tools(self.tool_manager)
    return result  # type: ignore[no-any-return]
