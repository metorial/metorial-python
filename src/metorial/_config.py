"""
Configuration management for Metorial client.

This module provides unified configuration management with a frozen dataclass
as the single source of truth.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ProviderConfig:
  """Configuration for a specific provider."""

  api_key: str | None = None
  base_url: str | None = None
  model: str | None = None


@dataclass(frozen=True)
class MetorialConfig:
  """Immutable configuration for Metorial SDK.

  This is the single source of truth for all SDK configuration.

  Attributes:
      api_key: API key for Metorial authentication
      api_host: Base URL for the API server
      mcp_host: Base URL for the MCP server
      timeout: Default request timeout in seconds
      max_retries: Maximum number of retry attempts for failed requests
      enable_debug_logging: Whether to enable debug-level logging
  """

  api_key: str
  api_host: str = "https://api.metorial.com"
  mcp_host: str = "https://mcp.metorial.com"
  timeout: float = 30.0
  max_retries: int = 3
  enable_debug_logging: bool = False

  # Provider configurations
  openai: ProviderConfig | None = None
  anthropic: ProviderConfig | None = None
  google: ProviderConfig | None = None
  mistral: ProviderConfig | None = None
  deepseek: ProviderConfig | None = None
  togetherai: ProviderConfig | None = None
  xai: ProviderConfig | None = None

  # Extra fields for forward compatibility
  extra: dict[str, Any] = field(default_factory=dict)

  # Legacy alias for backward compatibility
  @property
  def host(self) -> str:
    """Legacy alias for api_host."""
    return self.api_host

  @classmethod
  def from_dict(cls, config: dict[str, Any]) -> MetorialConfig:
    """Create a MetorialConfig from a dictionary.

    Args:
        config: Dictionary with configuration values. Supports both
                camelCase (apiKey) and snake_case (api_key) keys.

    Returns:
        MetorialConfig instance
    """
    # Extract known fields, supporting both camelCase and snake_case
    api_key = config.get("apiKey") or config.get("api_key") or ""
    api_host = (
      config.get("apiHost")
      or config.get("api_host")
      or config.get("host")
      or "https://api.metorial.com"
    )
    mcp_host = (
      config.get("mcpHost") or config.get("mcp_host") or "https://mcp.metorial.com"
    )
    timeout = config.get("timeout", 30.0)
    max_retries = config.get("maxRetries") or config.get("max_retries") or 3
    enable_debug_logging = config.get("enable_debug_logging", False)

    # Derive hosts if needed
    api_host, mcp_host = derive_hosts(str(api_host), str(mcp_host))

    # Collect extra fields
    known_keys = {
      "apiKey",
      "api_key",
      "apiHost",
      "api_host",
      "host",
      "mcpHost",
      "mcp_host",
      "timeout",
      "maxRetries",
      "max_retries",
      "enable_debug_logging",
      "openai",
      "anthropic",
      "google",
      "mistral",
      "deepseek",
      "togetherai",
      "xai",
    }
    extra = {k: v for k, v in config.items() if k not in known_keys}

    return cls(
      api_key=str(api_key),
      api_host=str(api_host),
      mcp_host=str(mcp_host),
      timeout=float(timeout),
      max_retries=int(max_retries),
      enable_debug_logging=bool(enable_debug_logging),
      extra=extra,
    )

  def to_dict(self) -> dict[str, Any]:
    """Convert to a dictionary with camelCase keys for API compatibility.

    Returns:
        Dictionary representation with camelCase keys
    """
    result: dict[str, Any] = {
      "apiKey": self.api_key,
      "apiHost": self.api_host,
      "mcpHost": self.mcp_host,
      "timeout": self.timeout,
      "maxRetries": self.max_retries,
    }
    result.update(self.extra)
    return result

  def with_updates(self, **kwargs: Any) -> MetorialConfig:
    """Create a new config with updated values.

    Since the config is frozen, this creates a new instance.

    Args:
        **kwargs: Fields to update

    Returns:
        New MetorialConfig with updated values
    """
    current: dict[str, Any] = {
      "api_key": self.api_key,
      "api_host": self.api_host,
      "mcp_host": self.mcp_host,
      "timeout": self.timeout,
      "max_retries": self.max_retries,
      "enable_debug_logging": self.enable_debug_logging,
      "openai": self.openai,
      "anthropic": self.anthropic,
      "google": self.google,
      "mistral": self.mistral,
      "deepseek": self.deepseek,
      "togetherai": self.togetherai,
      "xai": self.xai,
      "extra": dict(self.extra),
    }
    current.update(kwargs)
    return MetorialConfig(**current)


def derive_hosts(api_host: str, mcp_host: str) -> tuple[str, str]:
  """Derive one host from the other if only one is customized.

  Args:
      api_host: The API host URL
      mcp_host: The MCP host URL

  Returns:
      Tuple of (api_host, mcp_host) with derived values if applicable
  """
  default_api = "https://api.metorial.com"
  default_mcp = "https://mcp.metorial.com"

  if api_host != default_api and mcp_host == default_mcp:
    # Derive MCP host from API host
    mcp_host = api_host.replace("api.", "mcp.")
  elif mcp_host != default_mcp and api_host == default_api:
    # Derive API host from MCP host
    api_host = mcp_host.replace("mcp.", "api.")

  return api_host, mcp_host


def load_config_from_env() -> MetorialConfig:
  """Load configuration from environment variables.

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
  api_host = os.getenv("METORIAL_HOST", "https://api.metorial.com")
  mcp_host = os.getenv("METORIAL_MCP_HOST", "https://mcp.metorial.com")
  timeout = float(os.getenv("METORIAL_TIMEOUT", "30.0"))
  max_retries = int(os.getenv("METORIAL_MAX_RETRIES", "3"))

  # Derive hosts if needed
  api_host, mcp_host = derive_hosts(api_host, mcp_host)

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
    api_host=api_host,
    mcp_host=mcp_host,
    timeout=timeout,
    max_retries=max_retries,
    openai=openai_config,
    anthropic=anthropic_config,
    google=google_config,
    mistral=mistral_config,
    deepseek=deepseek_config,
    togetherai=togetherai_config,
    xai=xai_config,
  )


def get_provider_config(config: MetorialConfig, provider: str) -> ProviderConfig | None:
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


def validate_config(config: MetorialConfig) -> dict[str, Any]:
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
  print("Metorial Configuration Status:")
  print(f"  API Host: {config.api_host}")
  print(f"  MCP Host: {config.mcp_host}")
  print(f"  API Key: {'*' * 8}{config.api_key[-4:] if config.api_key else 'Not set'}")
  print(f"  Timeout: {config.timeout}s")
  print(f"  Max Retries: {config.max_retries}")

  print("\nProvider Status:")
  validation = validate_config(config)

  for provider, status in validation.items():
    if status["configured"]:
      print(f"  {provider.title()}: Configured")
    else:
      print(f"  {provider.title()}: Not configured")

  print("\nTo configure providers, set the appropriate environment variables:")
  print("   OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, etc.")


__all__ = [
  "MetorialConfig",
  "ProviderConfig",
  "derive_hosts",
  "load_config_from_env",
  "get_provider_config",
  "validate_config",
  "print_config_status",
]
