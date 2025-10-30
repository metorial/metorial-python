"""
Metorial Base Client
"""

import asyncio
import os
import time
import logging
from typing import Optional, Union, Dict, Any, TYPE_CHECKING
import httpx
from metorial_mcp_session import MetorialMcpSession, MetorialMcpSessionInit
from .session import MetorialSession, SessionFactory
from .sdk import create_metorial_sdk

if TYPE_CHECKING:
  from .sdk import ServersGroup, SessionsGroup, ProviderOauthGroup
  from mt_2025_01_01_pulsar.endpoints.instance import MetorialInstanceEndpoint
  from mt_2025_01_01_pulsar.endpoints.secrets import MetorialSecretsEndpoint
  from mt_2025_01_01_pulsar.endpoints.files import MetorialFilesEndpoint
  from mt_2025_01_01_pulsar.endpoints.links import MetorialLinksEndpoint


class MetorialBase:
  """Base class with shared initialization and configuration logic."""

  # Type annotations for IDE support - using non-string annotations for better resolution
  if TYPE_CHECKING:
    instance: Optional[MetorialInstanceEndpoint]
    secrets: Optional[MetorialSecretsEndpoint]
    servers: Optional[ServersGroup]
    sessions: Optional[SessionsGroup]
    files: Optional[MetorialFilesEndpoint]
    links: Optional[MetorialLinksEndpoint]
    oauth: Optional[ProviderOauthGroup]

  def __init__(
    self,
    api_key: Union[str, Dict[str, Any], None] = None,
    api_host: str = "https://api.metorial.com",
    mcp_host: str = "https://mcp.metorial.com",
    logger: Optional[logging.Logger] = None,
    timeout: float = 30.0,
    max_retries: int = 3,
    enable_debug_logging: bool = False,
    **kwargs,
  ):
    """Initialize Metorial client with enhanced configuration."""

    # Store debug logging preference
    self.enable_debug_logging = enable_debug_logging

    self._session_promises: Dict[str, asyncio.Task] = {}
    self._session_cache: Dict[str, MetorialSession] = {}

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

    # Initialize endpoints using SDK builder
    try:
      sdk = create_metorial_sdk(self._config_data)
      self._instance = sdk.instance
      self._secrets = sdk.secrets
      self._servers = sdk.servers
      self._sessions = sdk.sessions
      self._files = sdk.files
      self._links = sdk.links
      self._oauth = sdk.oauth
    except Exception as e:
      self.logger.warning(f"Failed to initialize SDK endpoints: {e}")

      # Fallback to None values if SDK initialization fails
      self._instance = None
      self._secrets = None
      self._servers = None
      self._sessions = None
      self._files = None
      self._links = None
      self._oauth = None

  @property
  def instance(self) -> Optional["MetorialInstanceEndpoint"]:
    return self._instance

  @property
  def secrets(self) -> Optional["MetorialSecretsEndpoint"]:
    return self._secrets

  @property
  def servers(self) -> Optional["ServersGroup"]:
    return self._servers

  @property
  def sessions(self) -> Optional["SessionsGroup"]:
    return self._sessions

  @property
  def files(self) -> Optional["MetorialFilesEndpoint"]:
    return self._files

  @property
  def links(self) -> Optional["MetorialLinksEndpoint"]:
    return self._links

  @property
  def oauth(self):
    """Access to OAuth-related endpoints with wait_for_completion method."""
    if self._oauth is None:
      return None

    # Add wait_for_completion method to oauth interface
    class OAuthWithWaitForCompletion:
      def __init__(self, oauth_group, metorial_instance):
        self._oauth = oauth_group
        self._metorial = metorial_instance

        # Delegate all oauth group methods
        for attr_name in ["connections", "sessions", "profiles", "authentications"]:
          if hasattr(oauth_group, attr_name):
            setattr(self, attr_name, getattr(oauth_group, attr_name))

      async def wait_for_completion(self, sessions, options=None):
        """Wait for OAuth sessions to complete authentication (like TypeScript version)."""
        poll_interval = (
          max((options or {}).get("pollInterval", 5000), 2000) / 1000
        )  # Convert to seconds, min 2s
        timeout = (options or {}).get(
          "timeout", 600000
        ) / 1000  # Convert to seconds, default 10 min
        start_time = time.time()

        if not sessions:
          return

        while True:
          if time.time() - start_time > timeout:
            raise Exception(f"OAuth authentication timeout after {timeout} seconds")

          try:
            all_completed = True
            failed_sessions = []

            for session in sessions:
              try:
                session_id = session.id if hasattr(session, "id") else session["id"]
                status = self.sessions.get(session_id)

                if status.status == "failed":
                  failed_sessions.append(session)
                elif status.status != "completed":
                  all_completed = False
              except Exception:
                all_completed = False  # Session check failed, keep polling

            if failed_sessions:
              raise Exception(
                f"OAuth authentication failed for {len(failed_sessions)} session(s)"
              )

            if all_completed:
              return

            # Wait before next poll
            await asyncio.sleep(poll_interval)

          except Exception as error:
            if "OAuth authentication" in str(error):
              raise  # Re-raise OAuth-specific errors
            # For other errors, continue polling
            await asyncio.sleep(poll_interval)

    return OAuthWithWaitForCompletion(self._oauth, self)

  @property
  def _config(self):
    return self._config_data

  @property
  def mcp(self):
    return {
      "createSession": self.create_mcp_session,
      "withSession": self.with_session,  # type: ignore[attr-defined]
      "withProviderSession": self.with_provider_session,  # type: ignore[attr-defined]
      "createConnection": self.create_mcp_connection,  # type: ignore[attr-defined]
    }

  def create_mcp_session(self, init: MetorialMcpSessionInit) -> MetorialSession:
    # Create cache key based on deployment configuration
    deployment_ids = []
    oauth_sessions = []

    server_deployment_data = init.get("serverDeployments", [])
    for dep in server_deployment_data:
      if isinstance(dep, dict):
        dep_id = dep.get("id") or dep.get("serverDeploymentId")
        oauth_id = dep.get("oauthSessionId")
        if dep_id:
          deployment_ids.append(dep_id)
        if oauth_id:
          oauth_sessions.append(oauth_id)
      else:
        deployment_ids.append(dep)

    # Create cache key from sorted deployment config
    cache_key = f"{':'.join(sorted(deployment_ids))}|{':'.join(sorted(oauth_sessions))}"

    if cache_key in self._session_cache:
      cached_session = self._session_cache[cache_key]
      self.logger.debug(f"♻️ Reusing cached session for deployments: {deployment_ids}")
      return cached_session

    try:
      deployments = []
      for dep in server_deployment_data:
        if isinstance(dep, dict):
          deployment_obj = {}
          if "id" in dep:
            deployment_obj["id"] = dep["id"]
          elif "serverDeploymentId" in dep:
            deployment_obj["id"] = dep["serverDeploymentId"]

          if "oauthSessionId" in dep:
            deployment_obj["oauthSessionId"] = dep["oauthSessionId"]

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

      mcp_session = MetorialMcpSession(sdk=self, init=mcp_init)  # type: ignore[arg-type]
      session = SessionFactory.create_session(mcp_session)

      self._session_cache[cache_key] = session
      self.logger.debug(
        f"🆕 Created and cached new session for deployments: {deployment_ids}"
      )

      return session
    except Exception as e:
      self.logger.error(f"Failed to create MCP session: {e}")
      from metorial_exceptions import MetorialSDKError

      raise MetorialSDKError(f"Failed to create MCP session: {e}")  # type: ignore[arg-type]

  def create_mock_session(self) -> MetorialSession:
    """Create a mock session for testing and development."""
    return SessionFactory.create_mock_session()  # type: ignore[no-any-return,attr-defined]

  async def close(self):
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
