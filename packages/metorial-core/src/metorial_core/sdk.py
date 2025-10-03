"""
Metorial SDK core implementation with typed endpoints and configuration.
"""

from dataclasses import dataclass
from typing import TypedDict, Dict, Any, TYPE_CHECKING

from .sdk_builder import MetorialSDKBuilder
from metorial_util_endpoint import MetorialEndpointManager

from mt_2025_01_01_pulsar.endpoints.instance import MetorialInstanceEndpoint
from mt_2025_01_01_pulsar.endpoints.secrets import MetorialSecretsEndpoint

from mt_2025_01_01_pulsar.endpoints.servers import MetorialServersEndpoint

from mt_2025_01_01_pulsar.endpoints.sessions import MetorialSessionsEndpoint
from mt_2025_01_01_pulsar.endpoints.files import MetorialFilesEndpoint
from mt_2025_01_01_pulsar.endpoints.links import MetorialLinksEndpoint

if TYPE_CHECKING:
  # Import for type checking to inherit all methods from base endpoints
  from .typed_endpoints import (
    TypedMetorialServersEndpoint as _TypedServersBase,
    TypedMetorialSessionsEndpoint as _TypedSessionsBase,
    TypedMetorialProviderOauthConnectionsEndpoint as _TypedProviderOauthConnectionsBase,
  )
  from mt_2025_01_01_pulsar.endpoints.server_runs import (
    MetorialServerRunsEndpoint as _TypedServerRunsBase,
  )

  # No base for ProviderOauth since it's just a grouping construct
  _TypedProviderOauthBase = object
else:
  # At runtime, use object as base for all
  _TypedServersBase = object
  _TypedSessionsBase = object
  _TypedProviderOauthBase = object
  _TypedProviderOauthConnectionsBase = object
  _TypedServerRunsBase = object


class SDKConfig(TypedDict):
  apiKey: str
  apiVersion: str
  apiHost: str


class _DelegatingGroup:
  """Base: forwards any missing attr to _root endpoint."""

  __slots__ = ("_root",)

  def __init__(self, root):
    # remember the real endpoint
    self._root = root

    # bind every public method that root actually provides, so
    # editors see completion & it won’t crash if one is missing
    for name in dir(root):
      if name.startswith("_"):
        continue
      attr = getattr(root, name)
      if callable(attr):
        # only bind if we haven't already set it on the subclass
        # (avoids stomping on explicit sub‐resource attributes)
        if not hasattr(self, name):
          setattr(self, name, attr)

  def __getattr__(self, name):
    # fall back to real endpoint for anything else
    return getattr(self._root, name)


class SessionsGroup(_DelegatingGroup, _TypedSessionsBase):
  __slots__ = ("messages", "connections", "list", "get", "create", "delete")

  def __init__(self, root, messages, connections):
    super().__init__(root)
    self.messages = messages
    self.connections = connections


class ProviderOauthConnectionsGroup(
  _DelegatingGroup, _TypedProviderOauthConnectionsBase
):
  __slots__ = (
    "authentications",
    "profiles",
    "list",
    "get",
    "create",
    "update",
    "delete",
  )

  def __init__(self, root, authentications, profiles):
    super().__init__(root)
    self.authentications = authentications
    self.profiles = profiles


class ProviderOauthGroup(_DelegatingGroup, _TypedProviderOauthBase):
  __slots__ = ("connections", "sessions", "profiles", "authentications")

  def __init__(
    self,
    root,
    connections_endpoint,
    sessions_endpoint,
    profiles_endpoint,
    authentications_endpoint,
  ):
    super().__init__(root)
    # Use direct endpoint classes instead of wrapper groups for better autocomplete
    self.connections = connections_endpoint
    self.sessions = sessions_endpoint
    self.profiles = profiles_endpoint
    self.authentications = authentications_endpoint


class RunsGroup(_DelegatingGroup, _TypedServerRunsBase):
  __slots__ = ("errors", "list", "get")

  def __init__(self, root, errors):
    super().__init__(root)
    self.errors = errors


class ServersGroup(_DelegatingGroup, _TypedServersBase):
  __slots__ = (
    "variants",
    "versions",
    "deployments",
    "implementations",
    "capabilities",
    "runs",
    "get",  # Add base methods to __slots__
  )

  def __init__(
    self, root, variants, versions, deployments, implementations, capabilities, runs
  ):
    super().__init__(root)
    self.variants = variants
    self.versions = versions
    self.deployments = deployments
    self.implementations = implementations
    self.capabilities = capabilities
    self.runs = runs


@dataclass(frozen=True)
class SDK:
  _config: SDKConfig
  instance: MetorialInstanceEndpoint
  secrets: MetorialSecretsEndpoint
  servers: "ServersGroup"
  sessions: "SessionsGroup"
  files: MetorialFilesEndpoint
  links: MetorialLinksEndpoint
  oauth: "ProviderOauthGroup"


def get_config(soft: Dict[str, Any]) -> Dict[str, Any]:
  """Get configuration with default API version."""
  return {**soft, "apiVersion": soft.get("apiVersion", "2025 - 01 - 01-pulsar")}


def get_headers(config: Dict[str, Any]) -> Dict[str, str]:
  """Get authorization headers for API requests."""
  return {"Authorization": f"Bearer {config['apiKey']}"}


def create_auth_headers(
  api_key: str, content_type: str = "application/json"
) -> Dict[str, str]:
  """Create authorization headers with optional content type."""

  headers = {"Authorization": f"Bearer {api_key}"}
  if content_type:
    headers["Content-Type"] = content_type
  return headers


def get_api_host(config: Dict[str, Any]) -> str:
  """Get API host URL with default fallback."""
  return config.get("apiHost", "https://api.metorial.com")  # type: ignore[no-any-return]


def get_endpoints(manager: MetorialEndpointManager) -> Dict[str, Any]:
  """Create and configure all SDK endpoints with proper typing."""
  endpoints: Dict[str, Any] = {
    "instance": MetorialInstanceEndpoint(manager),
    "secrets": MetorialSecretsEndpoint(manager),
    "files": MetorialFilesEndpoint(manager),
    "links": MetorialLinksEndpoint(manager),
  }

  # Use typed endpoints for better IDE support
  from .typed_endpoints import (
    TypedMetorialServersEndpoint,
    TypedMetorialSessionsEndpoint,
    TypedMetorialProviderOauthEndpoint,
  )

  servers = TypedMetorialServersEndpoint(manager)
  sessions = TypedMetorialSessionsEndpoint(manager)
  provider_oauth = TypedMetorialProviderOauthEndpoint(manager)

  endpoints["servers"] = servers
  endpoints["sessions"] = sessions
  endpoints["oauth"] = provider_oauth
  return endpoints


_create = (
  MetorialSDKBuilder.create("metorial", "2025 - 01 - 01-pulsar")
  .set_get_api_host(get_api_host)
  .set_get_headers(get_headers)
  .build(get_config)
)


def _to_typed_sdk(raw: Dict[str, Any]) -> SDK:
  """Convert raw SDK data to typed SDK instance with grouping."""

  _cfg = raw["_config"]

  servers_root = raw["servers"]
  sessions_root = raw["sessions"]
  provider_oauth_root = raw["oauth"]

  servers_group = ServersGroup(
    servers_root,
    servers_root.variants,
    servers_root.versions,
    servers_root.deployments,
    servers_root.implementations,
    servers_root.capabilities,
    RunsGroup(servers_root.runs, servers_root.runs.errors),
  )

  sessions_group = SessionsGroup(
    sessions_root,
    sessions_root.messages,
    sessions_root.connections,
  )

  # Use direct endpoint classes for better autocomplete (like servers sub-endpoints)
  provider_oauth_group = ProviderOauthGroup(
    provider_oauth_root,
    provider_oauth_root.connections,  # Direct endpoint class
    provider_oauth_root.sessions,  # Direct endpoint class
    provider_oauth_root.profiles,  # Direct endpoint class from TypedMetorialProviderOauthEndpoint
    provider_oauth_root.authentications,  # Direct endpoint class from TypedMetorialProviderOauthEndpoint
  )

  return SDK(
    _config=SDKConfig(
      apiKey=_cfg["apiKey"],
      apiVersion=_cfg["apiVersion"],
      apiHost=_cfg["apiHost"],
    ),
    instance=raw["instance"],
    secrets=raw["secrets"],
    servers=servers_group,
    sessions=sessions_group,
    files=raw["files"],
    links=raw["links"],
    oauth=provider_oauth_group,
  )


def create_metorial_sdk(config: Dict[str, Any]) -> SDK:
  """Create a configured Metorial SDK instance with typed endpoints."""

  raw = _create(get_endpoints)(config)
  return _to_typed_sdk(raw)
