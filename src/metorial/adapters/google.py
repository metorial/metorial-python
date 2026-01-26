"""
Google provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .message_utils import convert_messages_to_google

if TYPE_CHECKING:
  from metorial_google import build_google_tools
else:
  try:
    from metorial_google import build_google_tools
  except ImportError:
    build_google_tools: Callable[[Any], list[dict[str, Any]]] | None = None


class GoogleAdapter(ProviderAdapter):
  """Adapter for Google Gemini providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gemini-pro",
    **kwargs: Any,
  ) -> ChatResponse:
    # Convert standardized messages to Google format
    google_messages = convert_messages_to_google(messages)

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

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gemini-pro",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # Convert standardized messages to Google format
    google_messages = convert_messages_to_google(messages)

    # Google streaming
    stream = await self.client.generate_content(
      contents=google_messages, tools=tools, stream=True, **kwargs
    )

    async for chunk in stream:
      if chunk.candidates and chunk.candidates[0].content:
        for part in chunk.candidates[0].content.parts:
          if hasattr(part, "text") and part.text:
            yield {"type": "content", "content": part.text}

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using Google format"""
    # Google uses function calls, similar to OpenAI
    from metorial_openai import call_openai_tools

    tool_messages = await call_openai_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in Google format"""
    if build_google_tools is None:
      raise ImportError("metorial-google package is required for Google adapter")

    return cast(list[dict[str, Any]], build_google_tools(self.tool_manager))
