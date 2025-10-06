"""
Anthropic provider adapter.
"""

from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse

if TYPE_CHECKING:
  from metorial_anthropic import call_anthropic_tools, build_anthropic_tools
else:
  try:
    from metorial_anthropic import call_anthropic_tools, build_anthropic_tools
  except ImportError:
    call_anthropic_tools: Optional[Callable[[Any, List[Any]], Any]] = None
    build_anthropic_tools: Optional[Callable[[Any], Any]] = None


class AnthropicAdapter(ProviderAdapter):
  """Adapter for Anthropic providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "claude-3 - 5-sonnet-20241022",
    **kwargs,
  ) -> ChatResponse:
    # Convert standardized messages to Anthropic format
    anthropic_messages: List[Dict[str, Any]] = []
    for msg in messages:
      if msg.role == "tool":
        # Anthropic uses "user" role for tool results
        anthropic_messages.append({"role": "user", "content": msg.content})
      else:
        anthropic_msg: Dict[str, Any] = {"role": msg.role}
        if msg.content:
          anthropic_msg["content"] = msg.content
        anthropic_messages.append(anthropic_msg)

    response = await self.client.messages.create(
      model=model, messages=anthropic_messages, tools=tools, **kwargs
    )

    # Convert Anthropic response to standardized format
    tool_calls = []
    if response.content:
      for content_block in response.content:
        if hasattr(content_block, "type") and content_block.type == "tool_use":
          tool_calls.append(
            {
              "id": content_block.id,
              "type": "function",
              "function": {
                "name": content_block.name,
                "arguments": str(content_block.input),
              },
            }
          )

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

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "claude-3 - 5-sonnet-20241022",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # Convert standardized messages to Anthropic format
    anthropic_messages: List[Dict[str, Any]] = []
    for msg in messages:
      if msg.role == "tool":
        anthropic_messages.append({"role": "user", "content": msg.content})
      else:
        anthropic_msg: Dict[str, Any] = {"role": msg.role}
        if msg.content:
          anthropic_msg["content"] = msg.content
        anthropic_messages.append(anthropic_msg)

    stream = await self.client.messages.create(
      model=model, messages=anthropic_messages, tools=tools, stream=True, **kwargs
    )

    async for chunk in stream:
      if chunk.type == "content_block_delta":
        if chunk.delta.type == "text_delta":
          yield {"type": "content", "content": chunk.delta.text}
      elif chunk.type == "message_stop":
        break

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using Anthropic format"""
    if call_anthropic_tools is None:
      raise ImportError("metorial-anthropic package is required for Anthropic adapter")

    tool_result = await call_anthropic_tools(self.tool_manager, tool_calls)

    # Convert to standardized format
    return [ChatMessage(role="tool", content=str(tool_result.get("content", "")))]

  def get_tools_for_provider(self) -> List[Dict[str, Any]]:
    """Get tools in Anthropic format"""
    if build_anthropic_tools is None:
      raise ImportError("metorial-anthropic package is required for Anthropic adapter")

    tools = build_anthropic_tools(self.tool_manager)
    # Remove duplicate tools by name
    unique_tools = list({t["name"]: t for t in tools}.values())
    return unique_tools
