"""
Metorial Base Client
"""

import os
import logging
from typing import Optional, Union, Dict, Any
import httpx
from metorial_mcp_session import MetorialMcpSession, MetorialMcpSessionInit
from .session import MetorialSession, SessionFactory
from .sdk import create_metorial_sdk


class MetorialBase:
  """Base class with shared initialization and configuration logic."""

  def __init__(
    self,
    api_key: Union[str, Dict[str, Any], None] = None,
    api_host: str = "https://api.metorial.com",
    mcp_host: str = "https://mcp.metorial.com",
    logger: Optional[logging.Logger] = None,
    timeout: float = 30.0,
    max_retries: int = 3,
    **kwargs,
  ):
    """Initialize Metorial client with enhanced configuration."""

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
    except Exception as e:
      self.logger.warning(f"Failed to initialize SDK endpoints: {e}")

      # Fallback to None values if SDK initialization fails
      self._instance = None
      self._secrets = None
      self._servers = None
      self._sessions = None
      self._files = None
      self._links = None

  @property
  def instance(self):
    return self._instance

  @property
  def secrets(self):
    return self._secrets

  @property
  def servers(self):
    return self._servers

  @property
  def sessions(self):
    return self._sessions

  @property
  def files(self):
    return self._files

  @property
  def links(self):
    return self._links

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
    """Create MCP session with enhanced error handling"""
    try:
      server_deployment_ids = init.get("serverDeployments", [])
      if isinstance(server_deployment_ids, list) and server_deployment_ids:
        ids = [
          dep["id"] if isinstance(dep, dict) else dep for dep in server_deployment_ids
        ]
      else:
        ids = []

      # Create MCP session init object
      mcp_init = {
        "serverDeployments": [{"id": dep_id} for dep_id in ids],
        "client": {
          "name": init.get("client", {}).get("name", "metorial-python"),
          "version": init.get("client", {}).get("version", "1.0.0"),
        },
      }

      mcp_session = MetorialMcpSession(sdk=self, init=mcp_init)  # type: ignore[arg-type]  # Pass the SDK instance

      return SessionFactory.create_session(mcp_session)
    except Exception as e:
      self.logger.error(f"Failed to create MCP session: {e}")
      from metorial_core.lib.exceptions import MetorialSDKError

      raise MetorialSDKError(f"Failed to create MCP session: {e}")  # type: ignore[arg-type]

  def create_mock_session(self) -> MetorialSession:
    """Create a mock session for testing and development."""
    return SessionFactory.create_mock_session()  # type: ignore[no-any-return,attr-defined]

  async def close(self):
    """Close HTTP client and cleanup resources"""
    await self._http_client.aclose()
