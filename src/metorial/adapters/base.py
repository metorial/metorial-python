"""
Base classes for provider adapters.
"""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any


@dataclass
class ChatMessage:
  """Standardized chat message format"""

  role: str
  content: str | None = None
  tool_calls: list[dict[str, Any]] | None = None
  tool_call_id: str | None = None


@dataclass
class ChatResponse:
  """Standardized chat response format"""

  content: str | None = None
  tool_calls: list[dict[str, Any]] | None = None
  usage: dict[str, Any] | None = None


class ProviderAdapter(ABC):
  """Abstract base class for provider adapters"""

  def __init__(self, client: Any, tool_manager: Any):
    self.client = client
    self.tool_manager = tool_manager

  def _convert_tool_responses(
    self, tool_messages: list[dict[str, Any]]
  ) -> list[ChatMessage]:
    """Convert provider tool response messages to standardized format.

    Args:
        tool_messages: List of tool response dicts from provider

    Returns:
        List of standardized ChatMessage objects
    """
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

  @abstractmethod
  async def create_chat_completion(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs: Any,
  ) -> ChatResponse:
    """Create a chat completion using the provider's API"""

  @abstractmethod
  def create_chat_completion_stream(
    self,
    messages: list[ChatMessage],
    tools: list[dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs: Any,
  ) -> AsyncIterator[dict[str, Any]]:
    """Create a streaming chat completion using the provider's API"""

  @abstractmethod
  async def call_tools(self, tool_calls: list[dict[str, Any]]) -> list[ChatMessage]:
    """Execute tool calls and return standardized tool response messages"""

  @abstractmethod
  def get_tools_for_provider(self) -> list[dict[str, Any]]:
    """Get tools formatted for this provider"""
