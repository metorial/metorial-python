"""
Configuration management for Metorial client.
"""

import os
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class ProviderConfig:
  """Configuration for a specific provider."""

  api_key: Optional[str] = None
  base_url: Optional[str] = None
  model: Optional[str] = None


@dataclass
class MetorialConfig:
  """Main configuration for Metorial client."""

  api_key: str
  host: str = "https://api.metorial.com"

  # Provider configurations
  openai: Optional[ProviderConfig] = None
  anthropic: Optional[ProviderConfig] = None
  google: Optional[ProviderConfig] = None
  mistral: Optional[ProviderConfig] = None
  deepseek: Optional[ProviderConfig] = None
  togetherai: Optional[ProviderConfig] = None
  xai: Optional[ProviderConfig] = None


def load_config_from_env() -> MetorialConfig:
  """
  Load configuration from environment variables.

  Returns:
    MetorialConfig: Configuration object with all settings

  Raises:
    ValueError: If required METORIAL_API_KEY is not found
  """
  # Required configuration
  api_key = os.getenv("METORIAL_API_KEY")
  if not api_key:
    raise ValueError(
      "METORIAL_API_KEY environment variable is required. "
      "Please set it or create a .env file with your API key."
    )

  # Optional Metorial configuration
  host = os.getenv("METORIAL_HOST", "https://api.metorial.com")

  # Provider configurations
  openai_config = None
  if openai_key := os.getenv("OPENAI_API_KEY"):
    openai_config = ProviderConfig(
      api_key=openai_key,
      base_url=os.getenv("OPENAI_BASE_URL"),
      model=os.getenv("OPENAI_MODEL"),
    )

  anthropic_config = None
  if anthropic_key := os.getenv("ANTHROPIC_API_KEY"):
    anthropic_config = ProviderConfig(
      api_key=anthropic_key,
      base_url=os.getenv("ANTHROPIC_BASE_URL"),
      model=os.getenv("ANTHROPIC_MODEL"),
    )

  google_config = None
  if google_key := os.getenv("GOOGLE_API_KEY"):
    google_config = ProviderConfig(
      api_key=google_key,
      base_url=os.getenv("GOOGLE_BASE_URL"),
      model=os.getenv("GOOGLE_MODEL"),
    )

  mistral_config = None
  if mistral_key := os.getenv("MISTRAL_API_KEY"):
    mistral_config = ProviderConfig(
      api_key=mistral_key,
      base_url=os.getenv("MISTRAL_BASE_URL"),
      model=os.getenv("MISTRAL_MODEL"),
    )

  deepseek_config = None
  if deepseek_key := os.getenv("DEEPSEEK_API_KEY"):
    deepseek_config = ProviderConfig(
      api_key=deepseek_key,
      base_url=os.getenv("DEEPSEEK_BASE_URL"),
      model=os.getenv("DEEPSEEK_MODEL"),
    )

  togetherai_config = None
  if togetherai_key := os.getenv("TOGETHERAI_API_KEY"):
    togetherai_config = ProviderConfig(
      api_key=togetherai_key,
      base_url=os.getenv("TOGETHERAI_BASE_URL"),
      model=os.getenv("TOGETHERAI_MODEL"),
    )

  xai_config = None
  if xai_key := os.getenv("XAI_API_KEY"):
    xai_config = ProviderConfig(
      api_key=xai_key,
      base_url=os.getenv("XAI_BASE_URL"),
      model=os.getenv("XAI_MODEL"),
    )

  return MetorialConfig(
    api_key=api_key,
    host=host,
    openai=openai_config,
    anthropic=anthropic_config,
    google=google_config,
    mistral=mistral_config,
    deepseek=deepseek_config,
    togetherai=togetherai_config,
    xai=xai_config,
  )


def get_provider_config(
  config: MetorialConfig, provider: str
) -> Optional[ProviderConfig]:
  """Get configuration for a specific provider."""

  provider_map = {
    "openai": config.openai,
    "anthropic": config.anthropic,
    "google": config.google,
    "mistral": config.mistral,
    "deepseek": config.deepseek,
    "togetherai": config.togetherai,
    "xai": config.xai,
  }
  return provider_map.get(provider.lower())


def validate_config(config: MetorialConfig) -> Dict[str, Any]:
  """Validate configuration and return status of each provider."""

  providers = [
    "openai",
    "anthropic",
    "google",
    "mistral",
    "deepseek",
    "togetherai",
    "xai",
  ]
  results = {}

  for provider in providers:
    provider_config = get_provider_config(config, provider)
    results[provider] = {
      "configured": provider_config is not None,
      "has_api_key": (
        provider_config.api_key is not None if provider_config else False
      ),
      "has_base_url": (
        provider_config.base_url is not None if provider_config else False
      ),
    }

  return results


def print_config_status(config: MetorialConfig) -> None:
  """Print a summary of configuration status."""
  print("🔧 Metorial Configuration Status:")
  print(f"  ✅ Metorial API: {config.host}")
  print(f"  ✅ API Key: {'*' * 8}{config.api_key[-4:] if config.api_key else 'Not set'}")

  print("\n📡 Provider Status:")
  validation = validate_config(config)

  for provider, status in validation.items():
    if status["configured"]:
      print(f"  ✅ {provider.title()}: Configured")
    else:
      print(f"  ❌ {provider.title()}: Not configured")

  print("\n💡 To configure providers, set the appropriate environment variables:")
  print("   OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, etc.")
