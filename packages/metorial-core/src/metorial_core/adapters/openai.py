"""
OpenAI provider adapter.
"""

import concurrent.futures
from typing import Any, Dict, List, AsyncGenerator, Optional, Callable, TYPE_CHECKING

from .base import ProviderAdapter, ChatMessage, ChatResponse

if TYPE_CHECKING:
  from metorial_openai import call_openai_tools, build_openai_tools
else:
  try:
    from metorial_openai import call_openai_tools, build_openai_tools
  except ImportError:
    call_openai_tools: Optional[Callable[[Any, List[Any]], Any]] = None
    build_openai_tools: Optional[Callable[[Any], Any]] = None


class OpenAIAdapter(ProviderAdapter):
  """Adapter for OpenAI-compatible providers"""

  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs,
  ) -> ChatResponse:
    # Convert standardized messages to OpenAI format
    openai_messages = []
    for msg in messages:
      openai_msg: Dict[str, Any] = {"role": msg.role}
      if msg.content:
        openai_msg["content"] = msg.content
      if msg.tool_calls:
        openai_msg["tool_calls"] = msg.tool_calls
      if msg.tool_call_id:
        openai_msg["tool_call_id"] = msg.tool_call_id
      openai_messages.append(openai_msg)

    # Handle both sync and async clients
    # Check if this is an async client by looking at the client type
    if hasattr(self.client, "__class__") and "Async" in self.client.__class__.__name__:
      # Async client
      response = await self.client.chat.completions.create(
        model=model, messages=openai_messages, tools=tools, **kwargs
      )
    else:
      # Sync client - run in thread pool
      with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
          self.client.chat.completions.create,
          model=model,
          messages=openai_messages,
          tools=tools,
          **kwargs,
        )
        response = future.result()

    # Convert OpenAI response to standardized format
    tool_calls = []
    if response.choices and response.choices[0].message.tool_calls:
      for tool_call in response.choices[0].message.tool_calls:
        tool_calls.append(
          {
            "id": tool_call.id,
            "type": tool_call.type,
            "function": {
              "name": tool_call.function.name,
              "arguments": tool_call.function.arguments,
            },
          }
        )

    return ChatResponse(
      content=response.choices[0].message.content if response.choices else None,
      tool_calls=tool_calls if tool_calls else None,
      usage=response.usage.dict() if response.usage else None,
    )

  async def create_chat_completion_stream(  # type: ignore[override]
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    # Convert standardized messages to OpenAI format
    openai_messages = []
    for msg in messages:
      openai_msg: Dict[str, Any] = {"role": msg.role}
      if msg.content:
        openai_msg["content"] = msg.content
      if msg.tool_calls:
        openai_msg["tool_calls"] = msg.tool_calls
      if msg.tool_call_id:
        openai_msg["tool_call_id"] = msg.tool_call_id
      openai_messages.append(openai_msg)

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
      # Sync client - run in thread pool
      with concurrent.futures.ThreadPoolExecutor() as executor:
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

  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls using OpenAI format"""
    if call_openai_tools is None:
      raise ImportError("metorial-openai package is required for OpenAI adapter")

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
    """Get tools in OpenAI format"""
    if build_openai_tools is None:
      raise ImportError("metorial-openai package is required for OpenAI adapter")

    result = build_openai_tools(self.tool_manager)
    return result  # type: ignore[no-any-return]
