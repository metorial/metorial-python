"""
Provider adapters for making Metorial chat methods provider-agnostic.
"""

from .base import ProviderAdapter, ChatMessage, ChatResponse
from .openai import OpenAIAdapter
from .anthropic import AnthropicAdapter
from .google import GoogleAdapter
from .mistral import MistralAdapter
from .deepseek import DeepSeekAdapter
from .togetherai import TogetherAIAdapter
from .xai import XAIAdapter
from .openai_compatible import OpenAICompatibleAdapter
from .factory import infer_provider_type, create_provider_adapter

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
]
