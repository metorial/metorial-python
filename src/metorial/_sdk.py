"""
Metorial SDK core implementation with typed endpoints and configuration.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, TypedDict

from metorial._endpoint import MetorialEndpointManager
from metorial._generated.pulsar.endpoints.files import MetorialFilesEndpoint
from metorial._generated.pulsar.endpoints.instance import MetorialInstanceEndpoint
from metorial._generated.pulsar.endpoints.links import MetorialLinksEndpoint
from metorial._generated.pulsar.endpoints.provider_oauth_connections import (
  MetorialProviderOauthConnectionsEndpoint,
)
from metorial._generated.pulsar.endpoints.provider_oauth_connections_authentications import (
  MetorialProviderOauthConnectionsAuthenticationsEndpoint,
)
from metorial._generated.pulsar.endpoints.provider_oauth_connections_profiles import (
  MetorialProviderOauthConnectionsProfilesEndpoint,
)
from metorial._generated.pulsar.endpoints.provider_oauth_sessions import (
  MetorialProviderOauthSessionsEndpoint,
)
from metorial._generated.pulsar.endpoints.secrets import MetorialSecretsEndpoint
from metorial._generated.pulsar.endpoints.server_run_errors import (
  MetorialServerRunErrorsEndpoint,
)
from metorial._generated.pulsar.endpoints.server_runs import (
  MetorialServerRunsEndpoint,
)
from metorial._generated.pulsar.endpoints.servers_capabilities import (
  MetorialServersCapabilitiesEndpoint,
)
from metorial._generated.pulsar.endpoints.servers_deployments import (
  MetorialServersDeploymentsEndpoint,
)
from metorial._generated.pulsar.endpoints.servers_implementations import (
  MetorialServersImplementationsEndpoint,
)
from metorial._generated.pulsar.endpoints.servers_variants import (
  MetorialServersVariantsEndpoint,
)
from metorial._generated.pulsar.endpoints.servers_versions import (
  MetorialServersVersionsEndpoint,
)
from metorial._generated.pulsar.endpoints.sessions_connections import (
  MetorialSessionsConnectionsEndpoint,
)
from metorial._generated.pulsar.endpoints.sessions_messages import (
  MetorialSessionsMessagesEndpoint,
)
from metorial._sdk_builder import MetorialSDKBuilder

if TYPE_CHECKING:
  from metorial._typed_endpoints import (
    TypedMetorialProviderOauthConnectionsEndpoint as _TypedProviderOauthConnectionsBase,
  )
  from metorial._typed_endpoints import (
    TypedMetorialServersEndpoint as _TypedServersBase,
  )
  from metorial._typed_endpoints import (
    TypedMetorialSessionsEndpoint as _TypedSessionsBase,
  )

  # No base for ProviderOauth since it's just a grouping construct
  _TypedProviderOauthBase = object
  _TypedServerRunsBase = MetorialServerRunsEndpoint
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

  def __init__(self, root: object) -> None:
    # remember the real endpoint
    self._root = root

    # bind every public method that root actually provides, so
    # editors see completion & it won't crash if one is missing
    for name in dir(root):
      if name.startswith("_"):
        continue
      attr = getattr(root, name)
      # only bind if callable and we haven't already set it on the subclass
      # (avoids stomping on explicit sub‐resource attributes)
      if callable(attr) and not hasattr(self, name):
        setattr(self, name, attr)

  def __getattr__(self, name: str) -> Any:
    # fall back to real endpoint for anything else
    return getattr(self._root, name)


class SessionsGroup(_DelegatingGroup, _TypedSessionsBase):
  """Sessions endpoint group with typed sub-endpoints."""

  __slots__ = ("messages", "connections", "list", "get", "create", "delete")

  # Type annotations for IDE support
  messages: MetorialSessionsMessagesEndpoint
  connections: MetorialSessionsConnectionsEndpoint

  def __init__(
    self,
    root: object,
    messages: MetorialSessionsMessagesEndpoint,
    connections: MetorialSessionsConnectionsEndpoint,
  ) -> None:
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

  def __init__(
    self,
    root: object,
    authentications: "MetorialProviderOauthConnectionsAuthenticationsEndpoint",
    profiles: "MetorialProviderOauthConnectionsProfilesEndpoint",
  ) -> None:
    super().__init__(root)
    self.authentications = authentications
    self.profiles = profiles


class ProviderOauthGroup(_DelegatingGroup, _TypedProviderOauthBase):
  """Provider OAuth endpoint group with typed sub-endpoints."""

  __slots__ = ("connections", "sessions", "profiles", "authentications")

  # Type annotations for IDE support
  connections: MetorialProviderOauthConnectionsEndpoint
  sessions: MetorialProviderOauthSessionsEndpoint
  profiles: MetorialProviderOauthConnectionsProfilesEndpoint
  authentications: MetorialProviderOauthConnectionsAuthenticationsEndpoint

  def __init__(
    self,
    root: object,
    connections_endpoint: MetorialProviderOauthConnectionsEndpoint,
    sessions_endpoint: MetorialProviderOauthSessionsEndpoint,
    profiles_endpoint: MetorialProviderOauthConnectionsProfilesEndpoint,
    authentications_endpoint: MetorialProviderOauthConnectionsAuthenticationsEndpoint,
  ) -> None:
    super().__init__(root)
    # Use direct endpoint classes instead of wrapper groups for better autocomplete
    self.connections = connections_endpoint
    self.sessions = sessions_endpoint
    self.profiles = profiles_endpoint
    self.authentications = authentications_endpoint


class RunsGroup(_DelegatingGroup, _TypedServerRunsBase):
  """Server runs endpoint group with errors sub-endpoint."""

  __slots__ = ("errors", "list", "get")

  # Type annotations for IDE support
  errors: MetorialServerRunErrorsEndpoint

  def __init__(
    self, root: MetorialServerRunsEndpoint, errors: MetorialServerRunErrorsEndpoint
  ) -> None:
    super().__init__(root)
    self.errors = errors


class ServersGroup(_DelegatingGroup, _TypedServersBase):
  """Servers endpoint group with typed sub-endpoints."""

  __slots__ = (
    "variants",
    "versions",
    "deployments",
    "implementations",
    "capabilities",
    "runs",
    "get",  # Add base methods to __slots__
  )

  # Type annotations for IDE support
  variants: MetorialServersVariantsEndpoint
  versions: MetorialServersVersionsEndpoint
  deployments: MetorialServersDeploymentsEndpoint
  implementations: MetorialServersImplementationsEndpoint
  capabilities: MetorialServersCapabilitiesEndpoint
  runs: RunsGroup

  def __init__(
    self,
    root: object,
    variants: MetorialServersVariantsEndpoint,
    versions: MetorialServersVersionsEndpoint,
    deployments: MetorialServersDeploymentsEndpoint,
    implementations: MetorialServersImplementationsEndpoint,
    capabilities: MetorialServersCapabilitiesEndpoint,
    runs: RunsGroup,
  ) -> None:
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


def get_config(soft: dict[str, Any]) -> dict[str, Any]:
  """Get configuration with default API version."""
  return {**soft, "apiVersion": soft.get("apiVersion", "2025 - 01 - 01-pulsar")}


def get_headers(config: dict[str, Any]) -> dict[str, str]:
  """Get authorization headers for API requests."""
  return {"Authorization": f"Bearer {config['apiKey']}"}


def create_auth_headers(
  api_key: str, content_type: str = "application/json"
) -> dict[str, str]:
  """Create authorization headers with optional content type."""

  headers = {"Authorization": f"Bearer {api_key}"}
  if content_type:
    headers["Content-Type"] = content_type
  return headers


def get_api_host(config: dict[str, Any]) -> str:
  """Get API host URL with default fallback."""
  api_host = config.get("apiHost")
  return api_host if isinstance(api_host, str) else "https://api.metorial.com"


def get_endpoints(manager: MetorialEndpointManager) -> dict[str, Any]:
  """Create and configure all SDK endpoints with proper typing."""
  endpoints: dict[str, Any] = {
    "instance": MetorialInstanceEndpoint(manager),
    "secrets": MetorialSecretsEndpoint(manager),
    "files": MetorialFilesEndpoint(manager),
    "links": MetorialLinksEndpoint(manager),
  }

  # Use typed endpoints for better IDE support
  from metorial._typed_endpoints import (
    TypedMetorialProviderOauthEndpoint,
    TypedMetorialServersEndpoint,
    TypedMetorialSessionsEndpoint,
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


def _to_typed_sdk(raw: dict[str, Any]) -> SDK:
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


def create_metorial_sdk(config: dict[str, Any]) -> SDK:
  """Create a configured Metorial SDK instance with typed endpoints."""

  raw = _create(get_endpoints)(config)
  return _to_typed_sdk(raw)
