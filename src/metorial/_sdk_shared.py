"""
Shared SDK utilities used by the Magnetar SDK wiring.

These helpers are API-version agnostic and were previously defined in the
now-removed Pulsar ``_sdk.py`` module.
"""

from typing import Any, TypedDict

from ._api_host import DEFAULT_API_HOST, api_host_from_token


class SDKConfig(TypedDict):
  apiKey: str
  apiVersion: str
  apiHost: str


def get_headers(config: dict[str, Any]) -> dict[str, str]:
  """Get authorization headers for API requests."""
  return {"Authorization": f"Bearer {config['apiKey']}"}


def get_api_host(config: dict[str, Any]) -> str:
  """Get API host URL with default fallback."""
  api_host = config.get("apiHost")
  if isinstance(api_host, str):
    return api_host

  return api_host_from_token(config.get("apiKey")) or DEFAULT_API_HOST


__all__ = ["SDKConfig", "get_headers", "get_api_host"]
