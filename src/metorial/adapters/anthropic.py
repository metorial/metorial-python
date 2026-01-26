"""
Anthropic provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .message_utils import (
  convert_messages_to_anthropic,
  deduplicate_tools,
  extract_anthropic_tool_calls,
)

if TYPE_CHECKING:
  from metorial_anthropic import build_anthropic_tools, call_anthropic_tools
else:
  try:
    from metorial_anthropic import build_anthropic_tools, call_anthropic_tools
  except ImportError:
    call_anthropic_tools: Callable[[Any, list[Any]], Any] | None = None
    build_anthropic_tools: Callable[[Any], Any] | None = None


class AnthropicAdapter(ProviderAdapter):
  """Adapter for Anthropic providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "claude-3 - 5-sonnet-20241022",
    **kwargs: Any,
  ) -> ChatResponse:
    # Convert standardized messages to Anthropic format
    anthropic_messages = convert_messages_to_anthropic(messages)

    response = await self.client.messages.create(
      model=model, messages=anthropic_messages, tools=tools, **kwargs
    )

    # Convert Anthropic response to standardized format using shared utility
    tool_calls = extract_anthropic_tool_calls(response)

    text_content = None
    if response.content:
      for content_block in response.content:
        if hasattr(content_block, "text"):
          text_content = content_block.text
          break

    if tool_calls and not text_content:
      text_content = f"Called {len(tool_calls)} tool(s)"

    return ChatResponse(
      content=text_content,
      tool_calls=tool_calls if tool_calls else None,
      usage=response.usage.dict() if response.usage else None,
    )

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "claude-3 - 5-sonnet-20241022",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # Convert standardized messages to Anthropic format
    anthropic_messages = convert_messages_to_anthropic(messages)

    stream = await self.client.messages.create(
      model=model, messages=anthropic_messages, tools=tools, stream=True, **kwargs
    )

    async for chunk in stream:
      if chunk.type == "content_block_delta":
        if chunk.delta.type == "text_delta":
          yield {"type": "content", "content": chunk.delta.text}
      elif chunk.type == "message_stop":
        break

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using Anthropic format"""
    if call_anthropic_tools is None:
      raise ImportError("metorial-anthropic package is required for Anthropic adapter")

    tool_result = await call_anthropic_tools(self.tool_manager, tool_calls)

    # Convert to standardized format
    return [ChatMessage(role="tool", content=str(tool_result.get("content", "")))]

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in Anthropic format"""
    if build_anthropic_tools is None:
      raise ImportError("metorial-anthropic package is required for Anthropic adapter")

    tools = build_anthropic_tools(self.tool_manager)
    # Remove duplicate tools by name using shared utility
    return deduplicate_tools(tools, key="name")
