"""
Base classes for provider adapters.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, AsyncGenerator
from dataclasses import dataclass


@dataclass
class ChatMessage:
  """Standardized chat message format"""

  role: str
  content: Optional[str] = None
  tool_calls: Optional[List[Dict[str, Any]]] = None
  tool_call_id: Optional[str] = None


@dataclass
class ChatResponse:
  """Standardized chat response format"""

  content: Optional[str] = None
  tool_calls: Optional[List[Dict[str, Any]]] = None
  usage: Optional[Dict[str, Any]] = None


class ProviderAdapter(ABC):
  """Abstract base class for provider adapters"""

  def __init__(self, client: Any, tool_manager: Any):
    self.client = client
    self.tool_manager = tool_manager

  @abstractmethod
  async def create_chat_completion(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs,
  ) -> ChatResponse:
    """Create a chat completion using the provider's API"""
    pass

  @abstractmethod
  async def create_chat_completion_stream(
    self,
    messages: List[ChatMessage],
    tools: List[Dict[str, Any]],
    model: str = "gpt-4o",
    **kwargs,
  ) -> AsyncGenerator[Dict[str, Any], None]:
    """Create a streaming chat completion using the provider's API"""
    pass

  @abstractmethod
  async def call_tools(self, tool_calls: List[Dict[str, Any]]) -> List[ChatMessage]:
    """Execute tool calls and return standardized tool response messages"""
    pass

  @abstractmethod
  def get_tools_for_provider(self) -> List[Dict[str, Any]]:
    """Get tools formatted for this provider"""
    pass
