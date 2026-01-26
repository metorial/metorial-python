"""
Factory functions for creating provider adapters.
"""

import logging
from typing import Any

from .anthropic import AnthropicAdapter
from .base import ProviderAdapter
from .deepseek import DeepSeekAdapter
from .google import GoogleAdapter
from .mistral import MistralAdapter
from .openai import OpenAIAdapter
from .openai_compatible import OpenAICompatibleAdapter
from .togetherai import TogetherAIAdapter
from .xai import XAIAdapter


def infer_provider_type(client: Any) -> str:
  """Automatically infer provider type from client instance"""

  client_type = type(client).__name__
  client_module = type(client).__module__

  # Check for OpenAI clients
  if (
    "openai" in client_module.lower()
    or "AsyncOpenAI" in client_type
    or "OpenAI" in client_type
  ):
    return "openai"

  # Check for Anthropic clients
  if "anthropic" in client_module.lower() or "Anthropic" in client_type:
    return "anthropic"

  # Check for Google clients
  if "google" in client_module.lower() or "generativeai" in client_module.lower():
    return "google"

  # Check for Mistral clients
  if "mistral" in client_module.lower() or "Mistral" in client_type:
    return "mistral"

  # Check for DeepSeek clients
  if "deepseek" in client_module.lower() or "DeepSeek" in client_type:
    return "deepseek"

  # Check for Together AI clients
  if "together" in client_module.lower() or "Together" in client_type:
    return "togetherai"

  # Check for XAI clients
  if (
    "xai" in client_module.lower()
    or "XAI" in client_type
    or "grok" in client_module.lower()
  ):
    return "xai"

  # Default to OpenAI-compatible for unknown clients (most are OpenAI-compatible)
  logger = logging.getLogger(__name__)
  logger.warning(
    f"Unknown client type '{client_type}' from module '{client_module}'. "
    f"Defaulting to 'openai-compatible' provider type. If this is incorrect, please specify "
    f"provider_type explicitly in your run() call."
  )
  return "openai-compatible"


def create_provider_adapter(
  provider_type: str | None, client: Any, tool_manager: Any
) -> ProviderAdapter:
  """Factory function to create provider adapters with automatic type inference"""

  # If no provider type specified, infer it from the client
  if provider_type is None:
    provider_type = infer_provider_type(client)
    logger = logging.getLogger(__name__)
    logger.info(
      f"Auto-inferred provider type: '{provider_type}' for client {type(client).__name__}"
    )

  if provider_type == "openai":
    return OpenAIAdapter(client, tool_manager)
  elif provider_type == "anthropic":
    return AnthropicAdapter(client, tool_manager)
  elif provider_type == "google":
    return GoogleAdapter(client, tool_manager)
  elif provider_type == "mistral":
    return MistralAdapter(client, tool_manager)
  elif provider_type == "deepseek":
    return DeepSeekAdapter(client, tool_manager)
  elif provider_type == "togetherai":
    return TogetherAIAdapter(client, tool_manager)
  elif provider_type == "xai":
    return XAIAdapter(client, tool_manager)
  elif provider_type == "openai-compatible":
    return OpenAICompatibleAdapter(client, tool_manager)
  else:
    raise ValueError(
      f"Unsupported provider type: {provider_type}. Supported types: "
      f"['openai', 'anthropic', 'google', 'mistral', 'deepseek', 'togetherai', 'xai', 'openai-compatible']"
    )
