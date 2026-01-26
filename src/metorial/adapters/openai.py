"""
OpenAI provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from metorial._executor import get_executor

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .message_utils import convert_messages_to_openai, extract_openai_tool_calls

if TYPE_CHECKING:
  from metorial_openai import build_openai_tools, call_openai_tools
else:
  try:
    from metorial_openai import build_openai_tools, call_openai_tools
  except ImportError:
    call_openai_tools: Callable[[Any, list[Any]], list[dict[str, Any]]] | None = None
    build_openai_tools: Callable[[Any], list[dict[str, Any]]] | None = None


class OpenAIAdapter(ProviderAdapter):
  """Adapter for OpenAI-compatible providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs: Any,
  ) -> ChatResponse:
    # Convert standardized messages to OpenAI format
    openai_messages = convert_messages_to_openai(messages)

    # Handle both sync and async clients
    # Check if this is an async client by looking at the client type
    if hasattr(self.client, "__class__") and "Async" in self.client.__class__.__name__:
      # Async client
      response = await self.client.chat.completions.create(
        model=model, messages=openai_messages, tools=tools, **kwargs
      )
    else:
      # Sync client - run in shared thread pool
      executor = get_executor()
      future = executor.submit(
        self.client.chat.completions.create,
        model=model,
        messages=openai_messages,
        tools=tools,
        **kwargs,
      )
      response = future.result()

    # Convert OpenAI response to standardized format using shared utility
    tool_calls = extract_openai_tool_calls(response)

    return ChatResponse(
      content=response.choices[0].message.content if response.choices else None,
      tool_calls=tool_calls if tool_calls else None,
      usage=response.usage.dict() if response.usage else None,
    )

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # Convert standardized messages to OpenAI format
    openai_messages = convert_messages_to_openai(messages)

    # Handle both sync and async clients
    if hasattr(self.client, "__class__") and "Async" in self.client.__class__.__name__:
      # Async client
      stream = await self.client.chat.completions.create(
        model=model,
        messages=openai_messages,
        tools=tools,
        stream=True,
        **kwargs,
      )
    else:
      # Sync client - run in shared thread pool
      executor = get_executor()
      future = executor.submit(
        self.client.chat.completions.create,
        model=model,
        messages=openai_messages,
        tools=tools,
        stream=True,
        **kwargs,
      )
      stream = future.result()

    async for chunk in stream:
      if chunk.choices:
        choice = chunk.choices[0]
        delta = choice.delta

        if delta.content:
          yield {"type": "content", "content": delta.content}
        elif delta.tool_calls:
          for tool_call in delta.tool_calls:
            yield {"type": "tool_call", "tool_call": tool_call}

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using OpenAI format"""
    if call_openai_tools is None:
      raise ImportError("metorial-openai package is required for OpenAI adapter")

    tool_messages = await call_openai_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in OpenAI format"""
    if build_openai_tools is None:
      raise ImportError("metorial-openai package is required for OpenAI adapter")

    return cast(list[dict[str, Any]], build_openai_tools(self.tool_manager))
