"""
Google provider adapter.
"""

from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse

if TYPE_CHECKING:
  from metorial_google import build_google_tools
else:
  try:
    from metorial_google import build_google_tools
  except ImportError:
    build_google_tools: Optional[Callable[[Any], Any]] = None


class GoogleAdapter(ProviderAdapter):
  """Adapter for Google Gemini providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gemini-pro",
    **kwargs,
  ) -> ChatResponse:
    # Convert standardized messages to Google format
    google_messages = []
    for msg in messages:
      google_msg: dict[str, Any] = {"role": msg.role}
      if msg.content:
        google_msg["parts"] = [{"text": msg.content}]
      google_messages.append(google_msg)

    # Google uses different API structure
    response = await self.client.generate_content(
      contents=google_messages, tools=tools, **kwargs
    )

    # Convert Google response to standardized format
    tool_calls = []
    if response.candidates and response.candidates[0].content:
      for part in response.candidates[0].content.parts:
        if hasattr(part, "function_call"):
          tool_calls.append(
            {
              "id": part.function_call.name,
              "type": "function",
              "function": {
                "name": part.function_call.name,
                "arguments": str(part.function_call.args),
              },
            }
          )

    return ChatResponse(
      content=(
        response.candidates[0].content.parts[0].text
        if response.candidates and response.candidates[0].content.parts
        else None
      ),
      tool_calls=tool_calls if tool_calls else None,
      usage=(
        response.usage_metadata.dict()
        if hasattr(response, "usage_metadata") and response.usage_metadata
        else None
      ),
    )

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gemini-pro",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # Convert standardized messages to Google format
    google_messages = []
    for msg in messages:
      google_msg: dict[str, Any] = {"role": msg.role}
      if msg.content:
        google_msg["parts"] = [{"text": msg.content}]
      google_messages.append(google_msg)

    # Google streaming
    stream = await self.client.generate_content(
      contents=google_messages, tools=tools, stream=True, **kwargs
    )

    async for chunk in stream:
      if chunk.candidates and chunk.candidates[0].content:
        for part in chunk.candidates[0].content.parts:
          if hasattr(part, "text") and part.text:
            yield {"type": "content", "content": part.text}

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using Google format"""
    # Google uses function calls, similar to OpenAI
    from metorial_openai import call_openai_tools

    tool_messages = await call_openai_tools(self.tool_manager, tool_calls)

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
    """Get tools in Google format"""
    if build_google_tools is None:
      raise ImportError("metorial-google package is required for Google adapter")

    result = build_google_tools(self.tool_manager)
    return result  # type: ignore[no-any-return]
