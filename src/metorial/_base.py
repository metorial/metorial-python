"""
Metorial Base Client
"""

from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Any, cast

import httpx

from metorial._magnetar_sdk import (
  MagnetarCustomProvidersGroup,
  MagnetarProviderDeploymentsGroup,
  MagnetarProvidersGroup,
  MagnetarSessionsGroup,
  MagnetarSessionTemplatesGroup,
  create_magnetar_sdk,
)
from metorial._session import MetorialSession, SessionFactory
from metorial.mcp import MagnetarMcpSessionInit, MetorialMagnetarMcpSession
from metorial.mcp.magnetar_mcp_session import MagnetarCoreSDK

if TYPE_CHECKING:
  from metorial._generated.magnetar.endpoints.instance import (
    MetorialInstanceEndpoint as MagnetarInstanceEndpoint,
  )
  from metorial._generated.magnetar.endpoints.provider_runs import (
    MetorialProviderRunsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.tool_calls import (
    MetorialToolCallsEndpoint,
  )


class MetorialBase:
  """Base class with shared Magnetar-only initialization and configuration logic."""

  _magnetar_instance: MagnetarInstanceEndpoint | None
  _magnetar_publishers: Any | None
  _magnetar_providers: MagnetarProvidersGroup | None
  _magnetar_provider_categories: Any | None
  _magnetar_provider_collections: Any | None
  _magnetar_provider_groups: Any | None
  _magnetar_provider_listings: Any | None
  _magnetar_provider_deployments: MagnetarProviderDeploymentsGroup | None
  _magnetar_provider_setup_sessions: Any | None
  _magnetar_sessions: MagnetarSessionsGroup | None
  _magnetar_session_templates: MagnetarSessionTemplatesGroup | None
  _magnetar_custom_providers: MagnetarCustomProvidersGroup | None
  _magnetar_provider_runs: MetorialProviderRunsEndpoint | None
  _magnetar_tool_calls: MetorialToolCallsEndpoint | None
  _magnetar_sdk_initialized: bool

  def __init__(
    self,
    api_key: str | dict[str, Any] | None = None,
    api_host: str = "https://api.metorial.com",
    mcp_host: str = "https://connect.metorial.com",
    logger: logging.Logger | None = None,
    timeout: float = 30.0,
    max_retries: int = 3,
    enable_debug_logging: bool = False,
    **kwargs: Any,
  ) -> None:
    self.enable_debug_logging = enable_debug_logging

    if not enable_debug_logging:
      from . import _configure_sdk_logging

      _configure_sdk_logging()

    if isinstance(api_key, dict):
      config = api_key
      api_key = config.get("apiKey", "")
      api_host = config.get("apiHost", api_host)
      mcp_host = config.get("mcpHost", mcp_host)
      kwargs.update(
        {k: v for k, v in config.items() if k not in ["apiKey", "apiHost", "mcpHost"]}
      )

    if not api_key:
      raise ValueError("api_key is required")

    self.logger = logger or logging.getLogger(__name__)
    log_level = os.environ.get("METORIAL_LOG_LEVEL", "INFO").upper()
    if log_level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
      self.logger.setLevel(getattr(logging, log_level))

    if (
      api_host != "https://api.metorial.com"
      and mcp_host == "https://connect.metorial.com"
    ):
      mcp_host = api_host.replace("://api.", "://connect.")
    elif (
      mcp_host != "https://connect.metorial.com"
      and api_host == "https://api.metorial.com"
    ):
      api_host = mcp_host.replace("://connect.", "://api.")

    self._config_data = {
      "apiKey": api_key,
      "apiHost": api_host,
      "mcpHost": mcp_host,
      "timeout": timeout,
      "maxRetries": max_retries,
      **kwargs,
    }

    self._http_client = httpx.AsyncClient(
      limits=httpx.Limits(max_keepalive_connections=20, max_connections=100),
      timeout=httpx.Timeout(timeout),
    )

    self._magnetar_instance = None
    self._magnetar_publishers = None
    self._magnetar_providers = None
    self._magnetar_provider_categories = None
    self._magnetar_provider_collections = None
    self._magnetar_provider_groups = None
    self._magnetar_provider_listings = None
    self._magnetar_provider_deployments = None
    self._magnetar_provider_setup_sessions = None
    self._magnetar_sessions = None
    self._magnetar_session_templates = None
    self._magnetar_provider_runs = None
    self._magnetar_tool_calls = None
    self._magnetar_custom_providers = None
    self._magnetar_sdk_initialized = False
    self._magnetar_sdk_init_error: Exception | None = None

  def _ensure_magnetar_sdk_initialized(self) -> None:
    if self._magnetar_sdk_initialized:
      return
    if self._magnetar_sdk_init_error is not None:
      return

    try:
      sdk = create_magnetar_sdk(self._config_data)
      self._magnetar_instance = sdk.instance
      self._magnetar_publishers = sdk.publishers
      self._magnetar_providers = sdk.providers
      self._magnetar_provider_categories = sdk.provider_categories
      self._magnetar_provider_collections = sdk.provider_collections
      self._magnetar_provider_groups = sdk.provider_groups
      self._magnetar_provider_listings = sdk.provider_listings
      self._magnetar_provider_deployments = sdk.provider_deployments
      self._magnetar_provider_setup_sessions = sdk.provider_setup_sessions
      self._magnetar_sessions = sdk.sessions
      self._magnetar_session_templates = sdk.session_templates
      self._magnetar_provider_runs = sdk.provider_runs
      self._magnetar_tool_calls = sdk.tool_calls
      self._magnetar_custom_providers = sdk.custom_providers
      self._magnetar_sdk_initialized = True
    except Exception as e:
      self.logger.warning(f"Failed to initialize Magnetar SDK endpoints: {e}")
      self._magnetar_sdk_init_error = e

  @property
  def instance(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_instance

  @property
  def providers(self) -> MagnetarProvidersGroup | None:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_providers

  @property
  def publishers(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_publishers

  @property
  def provider_categories(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_categories

  @property
  def provider_collections(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_collections

  @property
  def provider_groups(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_groups

  @property
  def provider_listings(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_listings

  @property
  def provider_deployments(self) -> MagnetarProviderDeploymentsGroup | None:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_deployments

  @property
  def provider_setup_sessions(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_setup_sessions

  @property
  def sessions(self) -> MagnetarSessionsGroup | None:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_sessions

  @property
  def session_templates(self) -> MagnetarSessionTemplatesGroup | None:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_session_templates

  @property
  def provider_runs(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_runs

  @property
  def tool_calls(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_tool_calls

  @property
  def custom_providers(self) -> Any:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_custom_providers

  @property
  def magnetar_sessions(self) -> MagnetarSessionsGroup | None:
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_sessions

  @property
  def _config(self) -> dict[str, Any]:
    return self._config_data

  @property
  def mcp(self) -> dict[str, Any]:
    return {
      "createSession": self.create_magnetar_mcp_session,
      "withSession": getattr(self, "with_magnetar_session", None),
      "createConnection": getattr(self, "create_magnetar_mcp_connection", None),
    }

  def create_magnetar_mcp_session(
    self, init: MagnetarMcpSessionInit | dict[str, Any]
  ) -> MetorialSession:
    try:
      providers = init.get("providers", [])
      mcp_init: dict[str, Any] = {
        "providers": providers,
        "client": {
          "name": init.get("client", {}).get("name", "metorial-python"),
          "version": init.get("client", {}).get("version", "1.0.0"),
        },
      }
      if "metadata" in init:
        mcp_init["metadata"] = init["metadata"]

      mcp_session = MetorialMagnetarMcpSession(
        sdk=cast(MagnetarCoreSDK, self),
        init=cast(MagnetarMcpSessionInit, mcp_init),
      )
      return SessionFactory.create_session(mcp_session)
    except Exception as e:
      self.logger.error(f"Failed to create Magnetar MCP session: {e}")
      from metorial.exceptions import MetorialAPIError

      raise MetorialAPIError(f"Failed to create Magnetar MCP session: {e}") from e

  def create_mock_session(self) -> MetorialSession:
    create_mock = getattr(SessionFactory, "create_mock_session", None)
    if create_mock is None:
      raise NotImplementedError("create_mock_session is not available")
    result = create_mock()
    if not isinstance(result, MetorialSession):
      raise TypeError("create_mock_session did not return a MetorialSession")
    return result

  async def close(self) -> None:
    try:
      await self._http_client.aclose()
    except Exception as e:
      self.logger.debug(f"HTTP client close warning: {e}")
