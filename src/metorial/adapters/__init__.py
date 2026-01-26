"""
Provider adapters for making Metorial chat methods provider-agnostic.
"""

from .anthropic import AnthropicAdapter
from .base import ChatMessage, ChatResponse, ProviderAdapter
from .deepseek import DeepSeekAdapter
from .factory import create_provider_adapter, infer_provider_type
from .google import GoogleAdapter
from .message_utils import (
  convert_messages_to_anthropic,
  convert_messages_to_google,
  convert_messages_to_openai,
  deduplicate_tools,
  extract_anthropic_tool_calls,
  extract_openai_tool_calls,
)
from .mistral import MistralAdapter
from .openai import OpenAIAdapter
from .openai_compatible import OpenAICompatibleAdapter
from .togetherai import TogetherAIAdapter
from .xai import XAIAdapter

__all__ = [
  # Base classes
  "ProviderAdapter",
  "ChatMessage",
  "ChatResponse",
  # Provider adapters
  "OpenAIAdapter",
  "AnthropicAdapter",
  "GoogleAdapter",
  "MistralAdapter",
  "DeepSeekAdapter",
  "TogetherAIAdapter",
  "XAIAdapter",
  "OpenAICompatibleAdapter",
  # Factory functions
  "infer_provider_type",
  "create_provider_adapter",
  # Message utilities
  "convert_messages_to_openai",
  "convert_messages_to_anthropic",
  "convert_messages_to_google",
  "extract_openai_tool_calls",
  "extract_anthropic_tool_calls",
  "deduplicate_tools",
]
