"""
OpenAI-compatible provider adapter.
"""

from collections.abc import AsyncGenerator, Callable
from typing import TYPE_CHECKING, Any, cast

from .base import ChatMessage, ChatResponse, ProviderAdapter
from .openai import OpenAIAdapter

if TYPE_CHECKING:
  from metorial_openai_compatible import (
    build_openai_compatible_tools,
    call_openai_compatible_tools,
  )
else:
  try:
    from metorial_openai_compatible import (
      build_openai_compatible_tools,
      call_openai_compatible_tools,
    )
  except ImportError:
    call_openai_compatible_tools: (
      Callable[[Any, list[Any]], list[dict[str, Any]]] | None
    ) = None
    build_openai_compatible_tools: (
      Callable[[Any, bool], list[dict[str, Any]]] | None
    ) = None


class OpenAICompatibleAdapter(ProviderAdapter):
  """Generic adapter for OpenAI-compatible providers"""

  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs: Any,
  ) -> ChatResponse:
    # OpenAI-compatible providers use OpenAI format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    return await openai_adapter.create_chat_completion(messages, tools, model, **kwargs)

  async def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs: Any,
  ) -> AsyncGenerator[dict[str, Any], None]:
    # OpenAI-compatible providers use OpenAI format - delegate to OpenAI adapter
    openai_adapter = OpenAIAdapter(self.client, self.tool_manager)
    async for chunk in openai_adapter.create_chat_completion_stream(
      messages, tools, model, **kwargs
    ):
      yield chunk

  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls using OpenAI-compatible format"""
    if call_openai_compatible_tools is None:
      raise ImportError(
        "metorial-openai-compatible package is required for OpenAI-compatible adapter"
      )

    tool_messages = await call_openai_compatible_tools(self.tool_manager, tool_calls)
    return self._convert_tool_responses(tool_messages)

  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools in OpenAI-compatible format"""
    if build_openai_compatible_tools is None:
      raise ImportError(
        "metorial-openai-compatible package is required for OpenAI-compatible adapter"
      )

    return cast(list[dict[str, Any]], build_openai_compatible_tools(self.tool_manager))
