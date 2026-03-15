"""
Metorial Base Client
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from typing import TYPE_CHECKING, Any, cast, overload

import httpx

from metorial._magnetar_sdk import (
  MagnetarCustomProvidersGroup,
  MagnetarProviderDeploymentsGroup,
  MagnetarProvidersGroup,
  MagnetarSessionsGroup,
  MagnetarSessionTemplatesGroup,
  create_magnetar_sdk,
)
from metorial._sdk import (
  ProviderOauthGroup,
  ServersGroup,
  SessionsGroup,
  create_metorial_sdk,
)
from metorial._session import MetorialSession, SessionFactory
from metorial.mcp import (
  MagnetarMcpSessionInit,
  MetorialMagnetarMcpSession,
  MetorialMcpSession,
  MetorialMcpSessionInit,
)
from metorial.mcp.magnetar_mcp_session import MagnetarCoreSDK
from metorial.mcp.mcp_session import MetorialCoreSDK

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
  from metorial._generated.pulsar.endpoints.files import MetorialFilesEndpoint
  from metorial._generated.pulsar.endpoints.instance import MetorialInstanceEndpoint
  from metorial._generated.pulsar.endpoints.links import MetorialLinksEndpoint
  from metorial._generated.pulsar.endpoints.secrets import MetorialSecretsEndpoint


class OAuthWithWaitForCompletion:
  """OAuth group with wait_for_completion method for polling OAuth session status.

  Provides typed access to OAuth sub-endpoints with IDE intellisense support.
  """

  def __init__(self, oauth_group: ProviderOauthGroup) -> None:
    self._oauth = oauth_group
    # Delegate all oauth group methods with proper types
    self.connections = oauth_group.connections
    self.sessions = oauth_group.sessions
    self.profiles = oauth_group.profiles
    self.authentications = oauth_group.authentications

  async def wait_for_completion(
    self, sessions: list[Any], options: dict[str, Any] | None = None
  ) -> None:
    """Wait for OAuth sessions to complete authentication.

    Args:
        sessions: List of OAuth session objects with 'id' attribute or dict with 'id' key
        options: Optional dict with 'pollInterval' (ms) and 'timeout' (ms) settings
    """
    poll_interval = max((options or {}).get("pollInterval", 5000), 2000) / 1000
    timeout = (options or {}).get("timeout", 600000) / 1000
    start_time = time.time()

    if not sessions:
      return

    while True:
      if time.time() - start_time > timeout:
        raise TimeoutError(f"OAuth authentication timeout after {timeout} seconds")

      try:
        all_completed = True
        failed_sessions = []

        for session in sessions:
          try:
            session_id = session.id if hasattr(session, "id") else session["id"]
            status = self._oauth.sessions.get(session_id)

            if status.status == "failed":
              failed_sessions.append(session)
            elif status.status != "completed":
              all_completed = False
          except (KeyError, AttributeError, TypeError) as e:
            logger = logging.getLogger(__name__)
            logger.debug(f"Error checking session {session_id}: {e}")
            all_completed = False

        if failed_sessions:
          raise RuntimeError(
            f"OAuth authentication failed for {len(failed_sessions)} session(s)"
          )

        if all_completed:
          return

        await asyncio.sleep(poll_interval)

      except (TimeoutError, RuntimeError):
        raise
      except Exception as e:
        logger = logging.getLogger(__name__)
        logger.debug(f"Transient error during OAuth polling: {e}")
        await asyncio.sleep(poll_interval)


# Type alias for session cache key (tuple-based for proper hashing)
SessionCacheKey = tuple[tuple[str, ...], tuple[str, ...]]


class _PulsarV1Namespace:
  """Legacy Pulsar API namespace (v1)."""

  def __init__(self, base: MetorialBase) -> None:
    self._base = base

  @property
  def instance(self) -> Any:
    self._base._ensure_sdk_initialized()
    return self._base._instance

  @property
  def secrets(self) -> Any:
    self._base._ensure_sdk_initialized()
    return self._base._secrets

  @property
  def servers(self) -> Any:
    self._base._ensure_sdk_initialized()
    return self._base._servers

  @property
  def sessions(self) -> Any:
    self._base._ensure_sdk_initialized()
    return self._base._sessions

  @property
  def files(self) -> Any:
    self._base._ensure_sdk_initialized()
    return self._base._files

  @property
  def links(self) -> Any:
    self._base._ensure_sdk_initialized()
    return self._base._links

  @property
  def oauth(self) -> OAuthWithWaitForCompletion | None:
    return self._base.oauth

  @property
  def _config(self) -> dict[str, Any]:
    return self._base._config

  @property
  def mcp(self) -> dict[str, Any]:
    return {
      "createSession": self._base.create_mcp_session,
      "withSession": getattr(self._base, "with_session", None),
      "withProviderSession": getattr(self._base, "with_provider_session", None),
      "createConnection": getattr(self._base, "create_mcp_connection", None),
    }


class MetorialBase:
  """Base class with shared initialization and configuration logic.

  Endpoints are lazily initialized on first access to avoid
  initializing unused endpoints.
  """

  # Instance variables declared for type checking (lazily initialized)
  _instance: MetorialInstanceEndpoint | None
  _secrets: MetorialSecretsEndpoint | None
  _servers: ServersGroup | None
  _sessions: SessionsGroup | None
  _files: MetorialFilesEndpoint | None
  _links: MetorialLinksEndpoint | None
  _oauth: ProviderOauthGroup | None
  _sdk_initialized: bool

  # Magnetar SDK (lazily initialized)
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
    mcp_host: str = "https://mcp.metorial.com",
    logger: logging.Logger | None = None,
    timeout: float = 30.0,
    max_retries: int = 3,
    enable_debug_logging: bool = False,
    **kwargs: Any,
  ):
    """Initialize Metorial client with enhanced configuration."""

    # Store debug logging preference
    self.enable_debug_logging = enable_debug_logging

    self._session_promises: dict[SessionCacheKey, asyncio.Task[Any]] = {}
    self._session_cache: dict[SessionCacheKey, MetorialSession] = {}

    # Configure logging based on debug setting
    if not enable_debug_logging:
      # Ensure SDK logging is quiet by default (run on each initialization)
      from . import _configure_sdk_logging

      _configure_sdk_logging()
    else:
      # Enable debug logging for troubleshooting
      _debug_loggers = [
        "metorial_core.base",
        "metorial_core.lib.clients.async_client",
        "metorial_mcp_session.mcp_session",
        "metorial.mcp.client",
        "mcp.client.sse",
      ]
      for logger_name in _debug_loggers:
        logger_obj = logging.getLogger(logger_name)
        logger_obj.setLevel(logging.DEBUG)
        logger_obj.propagate = True

    # Support both direct parameters and config dict
    if isinstance(api_key, dict):
      config = api_key
      api_key = config.get("apiKey", "")
      api_host = config.get("apiHost", "https://api.metorial.com")
      mcp_host = config.get("mcpHost", "https://mcp.metorial.com")
      kwargs.update(
        {k: v for k, v in config.items() if k not in ["apiKey", "apiHost", "mcpHost"]}
      )

    if not api_key:
      raise ValueError("api_key is required")

    self.logger = logger or logging.getLogger(__name__)

    # Check for environment variable to control logging level
    log_level = os.environ.get("METORIAL_LOG_LEVEL", "INFO").upper()
    if log_level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
      self.logger.setLevel(getattr(logging, log_level))

    # derive one host from the other if only one is provided
    if api_host != "https://api.metorial.com" or mcp_host != "https://mcp.metorial.com":
      original_api_host = api_host
      original_mcp_host = mcp_host

      if (
        api_host != "https://api.metorial.com"
        and mcp_host == "https://mcp.metorial.com"
      ):
        mcp_host = api_host.replace("api.", "mcp.")
        self.logger.warning(
          f"⚠️ MCP host auto-derived from API host: '{original_mcp_host}' → '{mcp_host}'"
        )
      elif (
        mcp_host != "https://mcp.metorial.com"
        and api_host == "https://api.metorial.com"
      ):
        api_host = mcp_host.replace("mcp.", "api.")
        self.logger.warning(
          f"⚠️ API host auto-derived from MCP host: '{original_api_host}' → '{api_host}'"
        )

    # Warn about configuration conflicts
    if timeout < 1:
      self.logger.warning(
        f"⚠️ Very short timeout configured: {timeout}s (may cause connection issues)"
      )
    if max_retries > 10:
      self.logger.warning(
        f"⚠️ High retry count configured: {max_retries} (may cause long delays)"
      )

    # Check for conflicting timeout settings
    if "request_timeout" in kwargs and kwargs["request_timeout"] != timeout:
      self.logger.warning(
        f"⚠️ Conflicting timeout settings: timeout={timeout}s, request_timeout={kwargs['request_timeout']}s"
      )

    self._config_data = {
      "apiKey": api_key,
      "apiHost": api_host,
      "mcpHost": mcp_host,
      "timeout": timeout,
      "maxRetries": max_retries,
      **kwargs,
    }

    # Enhanced HTTP client with connection pooling
    self._http_client = httpx.AsyncClient(
      limits=httpx.Limits(max_keepalive_connections=20, max_connections=100),
      timeout=httpx.Timeout(timeout),
    )

    # Logging setup (logger already initialized above)
    if not self.logger.handlers:
      handler = logging.StreamHandler()
      formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
      )
      handler.setFormatter(formatter)
      self.logger.addHandler(handler)
      self.logger.setLevel(logging.INFO)

    # Initialize endpoint placeholders (lazily populated on first access)
    self._instance = None
    self._secrets = None
    self._servers = None
    self._sessions = None
    self._files = None
    self._links = None
    self._oauth = None
    self._sdk_initialized = False
    self._sdk_init_error: Exception | None = None

    # Magnetar SDK initialization
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

  def _ensure_sdk_initialized(self) -> None:
    """Lazily initialize the SDK on first endpoint access."""
    if self._sdk_initialized:
      return

    if self._sdk_init_error is not None:
      # Don't retry if SDK initialization already failed
      return

    try:
      sdk = create_metorial_sdk(self._config_data)
      self._instance = sdk.instance
      self._secrets = sdk.secrets
      self._servers = sdk.servers
      self._sessions = sdk.sessions
      self._files = sdk.files
      self._links = sdk.links
      self._oauth = sdk.oauth
      self._sdk_initialized = True
    except Exception as e:
      self.logger.warning(f"Failed to initialize SDK endpoints: {e}")
      self._sdk_init_error = e

  def _ensure_magnetar_sdk_initialized(self) -> None:
    """Lazily initialize the Magnetar SDK on first endpoint access."""
    if self._magnetar_sdk_initialized:
      return

    if self._magnetar_sdk_init_error is not None:
      return

    try:
      mag_sdk = create_magnetar_sdk(self._config_data)
      self._magnetar_instance = mag_sdk.instance
      self._magnetar_publishers = mag_sdk.publishers
      self._magnetar_providers = mag_sdk.providers
      self._magnetar_provider_categories = mag_sdk.provider_categories
      self._magnetar_provider_collections = mag_sdk.provider_collections
      self._magnetar_provider_groups = mag_sdk.provider_groups
      self._magnetar_provider_listings = mag_sdk.provider_listings
      self._magnetar_provider_deployments = mag_sdk.provider_deployments
      self._magnetar_provider_setup_sessions = mag_sdk.provider_setup_sessions
      self._magnetar_sessions = mag_sdk.sessions
      self._magnetar_session_templates = mag_sdk.session_templates
      self._magnetar_provider_runs = mag_sdk.provider_runs
      self._magnetar_tool_calls = mag_sdk.tool_calls
      self._magnetar_custom_providers = mag_sdk.custom_providers
      self._magnetar_sdk_initialized = True
    except Exception as e:
      self.logger.warning(f"Failed to initialize Magnetar SDK endpoints: {e}")
      self._magnetar_sdk_init_error = e

  @property
  def instance(self) -> Any:
    """Get Magnetar instance endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_instance

  @property
  def secrets(self) -> MetorialSecretsEndpoint | None:
    """Get secrets endpoint (lazily initialized)."""
    self._ensure_sdk_initialized()
    return self._secrets

  @property
  def servers(self) -> ServersGroup | None:
    """Get servers endpoint group (lazily initialized)."""
    self._ensure_sdk_initialized()
    return self._servers

  @property
  def sessions(self) -> MagnetarSessionsGroup | None:
    """Get Magnetar sessions endpoint group (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_sessions

  @property
  def files(self) -> MetorialFilesEndpoint | None:
    """Get files endpoint (lazily initialized)."""
    self._ensure_sdk_initialized()
    return self._files

  @property
  def links(self) -> MetorialLinksEndpoint | None:
    """Get links endpoint (lazily initialized)."""
    self._ensure_sdk_initialized()
    return self._links

  @property
  def oauth(self) -> OAuthWithWaitForCompletion | None:
    """Access to OAuth-related endpoints with wait_for_completion method (lazily initialized).

    Returns:
        OAuthWithWaitForCompletion object with connections, sessions, profiles,
        authentications sub-endpoints and wait_for_completion() method.
    """
    self._ensure_sdk_initialized()
    if self._oauth is None:
      return None
    return OAuthWithWaitForCompletion(self._oauth)

  @property
  def providers(self) -> MagnetarProvidersGroup | None:
    """Get Magnetar providers endpoint group (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_providers

  @property
  def publishers(self) -> Any:
    """Get Magnetar publishers endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_publishers

  @property
  def provider_categories(self) -> Any:
    """Get Magnetar provider categories endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_categories

  @property
  def provider_collections(self) -> Any:
    """Get Magnetar provider collections endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_collections

  @property
  def provider_groups(self) -> Any:
    """Get Magnetar provider groups endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_groups

  @property
  def provider_listings(self) -> Any:
    """Get Magnetar provider listings endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_listings

  @property
  def provider_deployments(self) -> MagnetarProviderDeploymentsGroup | None:
    """Get Magnetar provider deployments endpoint group (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_deployments

  @property
  def provider_setup_sessions(self) -> Any:
    """Get Magnetar provider setup sessions endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_setup_sessions

  @property
  def session_templates(self) -> MagnetarSessionTemplatesGroup | None:
    """Get Magnetar session templates endpoint group (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_session_templates

  @property
  def provider_runs(self) -> Any:
    """Get Magnetar provider runs endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_provider_runs

  @property
  def tool_calls(self) -> Any:
    """Get Magnetar tool calls endpoint (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_tool_calls

  @property
  def custom_providers(self) -> Any:
    """Get Magnetar custom providers endpoint group (lazily initialized)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_custom_providers

  @property
  def magnetar_sessions(self) -> MagnetarSessionsGroup | None:
    """Get Magnetar sessions API (for MagnetarCoreSDK protocol compliance)."""
    self._ensure_magnetar_sdk_initialized()
    return self._magnetar_sessions

  @property
  def v1(self) -> _PulsarV1Namespace:
    """Access legacy Pulsar API (v1)."""
    return _PulsarV1Namespace(self)

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

  @overload
  def create_mcp_session(self, init: MetorialMcpSessionInit) -> MetorialSession: ...

  @overload
  def create_mcp_session(self, init: dict[str, Any]) -> MetorialSession: ...

  def create_mcp_session(
    self, init: MetorialMcpSessionInit | dict[str, Any]
  ) -> MetorialSession:
    # Create cache key based on deployment configuration
    deployment_ids: list[str] = []
    oauth_sessions: list[str] = []

    server_deployment_data = init.get("serverDeployments", [])
    for dep in server_deployment_data:
      if isinstance(dep, dict):
        dep_id = (
          dep.get("id")
          or dep.get("server_deployment_id")
          or dep.get("serverDeploymentId")
        )
        oauth_id = dep.get("oauth_session_id") or dep.get("oauthSessionId")
        if dep_id:
          deployment_ids.append(str(dep_id))
        if oauth_id:
          oauth_sessions.append(str(oauth_id))
      else:
        deployment_ids.append(str(dep))

    # Create cache key using tuple-based hashable key (prevents string collision)
    cache_key: SessionCacheKey = (
      tuple(sorted(deployment_ids)),
      tuple(sorted(oauth_sessions)),
    )

    if cache_key in self._session_cache:
      cached_session = self._session_cache[cache_key]
      self.logger.debug(f"♻️ Reusing cached session for deployments: {deployment_ids}")
      return cached_session

    try:
      deployments: list[dict[str, Any]] = []
      for dep in server_deployment_data:
        if isinstance(dep, dict):
          # Cast to dict[str, Any] to handle snake_case and camelCase keys
          dep_dict: dict[str, Any] = dict(dep)
          deployment_obj: dict[str, Any] = {}
          if "id" in dep_dict:
            deployment_obj["id"] = dep_dict["id"]
          elif "server_deployment_id" in dep_dict:
            deployment_obj["id"] = dep_dict["server_deployment_id"]
          elif "serverDeploymentId" in dep_dict:
            deployment_obj["id"] = dep_dict["serverDeploymentId"]

          # Handle oauth_session_id (snake_case preferred) or oauthSessionId
          if "oauth_session_id" in dep_dict:
            deployment_obj["oauthSessionId"] = dep_dict["oauth_session_id"]
          elif "oauthSessionId" in dep_dict:
            deployment_obj["oauthSessionId"] = dep_dict["oauthSessionId"]

          deployments.append(deployment_obj)
        else:
          deployments.append({"id": dep})

      mcp_init = {
        "serverDeployments": deployments,
        "client": {
          "name": init.get("client", {}).get("name", "metorial-python"),
          "version": init.get("client", {}).get("version", "1.0.0"),
        },
      }

      # Wrap self so that .sessions returns the Pulsar sessions API,
      # not the Magnetar one (which MetorialBase.sessions returns by default).
      self._ensure_sdk_initialized()

      class _PulsarSDKView:
        """Lightweight wrapper exposing Pulsar endpoints for the MCP session."""

        def __init__(inner, base: MetorialBase) -> None:  # noqa: N805
          inner._base = base

        @property
        def _config(inner) -> dict[str, Any]:  # noqa: N805
          return inner._base._config

        @property
        def sessions(inner) -> Any:  # noqa: N805
          return inner._base._sessions

        @property
        def servers(inner) -> Any:  # noqa: N805
          return inner._base._servers

      mcp_session = MetorialMcpSession(
        sdk=cast(MetorialCoreSDK, _PulsarSDKView(self)),
        init=cast(MetorialMcpSessionInit, mcp_init),
      )
      session = SessionFactory.create_session(mcp_session)

      self._session_cache[cache_key] = session
      self.logger.debug(
        f"🆕 Created and cached new session for deployments: {deployment_ids}"
      )

      return session
    except Exception as e:
      self.logger.error(f"Failed to create MCP session: {e}")
      from metorial.exceptions import MetorialAPIError

      raise MetorialAPIError(f"Failed to create MCP session: {e}") from e

  def create_magnetar_mcp_session(
    self, init: MagnetarMcpSessionInit | dict[str, Any]
  ) -> MetorialSession:
    """Create a Magnetar MCP session using providers."""
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
    """Create a mock session for testing and development."""
    create_mock = getattr(SessionFactory, "create_mock_session", None)
    if create_mock is None:
      raise NotImplementedError("create_mock_session is not available")
    result = create_mock()
    if not isinstance(result, MetorialSession):
      raise TypeError("create_mock_session did not return a MetorialSession")
    return result

  async def close(self) -> None:
    # Close all cached sessions gracefully with timeout
    if hasattr(self, "_session_cache"):
      close_tasks = []
      for session in list(self._session_cache.values()):
        try:
          close_tasks.append(session.close())
        except Exception:
          continue

      if close_tasks:
        try:
          await asyncio.wait_for(
            asyncio.gather(*close_tasks, return_exceptions=True), timeout=5.0
          )
        except asyncio.TimeoutError:
          self.logger.debug("Session cleanup timeout - continuing")
        except Exception as e:
          self.logger.debug(f"Session cleanup warning: {e}")

    # Clear caches safely
    if hasattr(self, "_session_cache"):
      self._session_cache.clear()
    if hasattr(self, "_session_promises"):
      self._session_promises.clear()

    # Close HTTP client gracefully
    try:
      await self._http_client.aclose()
    except Exception as e:
      self.logger.debug(f"HTTP client close warning: {e}")
