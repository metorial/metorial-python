"""
Magnetar SDK core implementation with typed endpoints and configuration.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from metorial._endpoint import MetorialEndpointManager
from metorial._generated.magnetar.endpoints.instance import (
  MetorialInstanceEndpoint as MagnetarInstanceEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_categories import (
  MetorialProviderCategoriesEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_collections import (
  MetorialProviderCollectionsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_setup_sessions import (
  MetorialProviderDeploymentsSetupSessionsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_groups import (
  MetorialProviderGroupsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_listings import (
  MetorialProviderListingsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_runs import (
  MetorialProviderRunsEndpoint,
)
from metorial._generated.magnetar.endpoints.publishers import (
  MetorialPublishersEndpoint,
)
from metorial._sdk import SDKConfig, _DelegatingGroup, get_api_host, get_headers
from metorial._sdk_builder import MetorialSDKBuilder

if TYPE_CHECKING:
  from metorial._magnetar_typed_endpoints import (
    TypedMagnetarCustomProvidersEndpoint as _TypedCustomProvidersBase,
  )
  from metorial._magnetar_typed_endpoints import (
    TypedMagnetarProviderDeploymentsEndpoint as _TypedProviderDeploymentsBase,
  )
  from metorial._magnetar_typed_endpoints import (
    TypedMagnetarProvidersEndpoint as _TypedProvidersBase,
  )
  from metorial._magnetar_typed_endpoints import (
    TypedMagnetarSessionsEndpoint as _TypedSessionsBase,
  )
  from metorial._magnetar_typed_endpoints import (
    TypedMagnetarSessionTemplatesEndpoint as _TypedSessionTemplatesBase,
  )
else:
  _TypedProvidersBase = object
  _TypedProviderDeploymentsBase = object
  _TypedCustomProvidersBase = object
  _TypedSessionsBase = object
  _TypedSessionTemplatesBase = object


class MagnetarProvidersGroup(_DelegatingGroup, _TypedProvidersBase):
  """Providers endpoint group with typed sub-endpoints."""

  __slots__ = (
    "versions",
    "tools",
    "auth_methods",
    "specifications",
    "list",
    "get",
    "update",
  )

  def __init__(self, root: object, typed: Any) -> None:
    super().__init__(root)
    self.versions = typed.versions
    self.tools = typed.tools
    self.auth_methods = typed.auth_methods
    self.specifications = typed.specifications


class MagnetarProviderDeploymentsGroup(_DelegatingGroup, _TypedProviderDeploymentsBase):
  """Provider deployments endpoint group with typed sub-endpoints."""

  __slots__ = (
    "configs",
    "config_vaults",
    "auth_configs",
    "auth_credentials",
    "setup_sessions",
    "list",
    "get",
    "create",
    "update",
    "delete",
  )

  def __init__(self, root: object, typed: Any) -> None:
    super().__init__(root)
    self.configs = typed.configs
    self.config_vaults = typed.config_vaults
    self.auth_configs = typed.auth_configs
    self.auth_credentials = typed.auth_credentials
    self.setup_sessions = typed.setup_sessions


class MagnetarSessionsGroup(_DelegatingGroup, _TypedSessionsBase):
  """Magnetar sessions endpoint group with typed sub-endpoints."""

  __slots__ = (
    "messages",
    "connections",
    "events",
    "providers",
    "provider_runs",
    "participants",
    "errors",
    "error_groups",
    "list",
    "get",
    "create",
    "update",
    "delete",
  )

  def __init__(self, root: object, typed: Any) -> None:
    super().__init__(root)
    self.messages = typed.messages
    self.connections = typed.connections
    self.events = typed.events
    self.providers = typed.providers
    self.provider_runs = typed.provider_runs
    self.participants = typed.participants
    self.errors = typed.errors
    self.error_groups = typed.error_groups


class MagnetarSessionTemplatesGroup(_DelegatingGroup, _TypedSessionTemplatesBase):
  """Session templates endpoint group with typed sub-endpoints."""

  __slots__ = ("providers", "list", "get", "create", "update")

  def __init__(self, root: object, typed: Any) -> None:
    super().__init__(root)
    self.providers = typed.providers


class MagnetarCustomProvidersGroup(_DelegatingGroup, _TypedCustomProvidersBase):
  """Custom providers endpoint group with typed sub-endpoints."""

  __slots__ = (
    "versions",
    "deployments",
    "environments",
    "commits",
    "list",
    "get",
    "create",
    "update",
    "delete",
  )

  def __init__(self, root: object, typed: Any) -> None:
    super().__init__(root)
    self.versions = typed.versions
    self.deployments = typed.deployments
    self.environments = typed.environments
    self.commits = typed.commits


@dataclass(frozen=True)
class MagnetarSDK:
  _config: SDKConfig
  instance: MagnetarInstanceEndpoint
  publishers: MetorialPublishersEndpoint
  providers: MagnetarProvidersGroup
  provider_categories: MetorialProviderCategoriesEndpoint
  provider_collections: MetorialProviderCollectionsEndpoint
  provider_groups: MetorialProviderGroupsEndpoint
  provider_listings: MetorialProviderListingsEndpoint
  provider_deployments: MagnetarProviderDeploymentsGroup
  provider_setup_sessions: MetorialProviderDeploymentsSetupSessionsEndpoint
  sessions: MagnetarSessionsGroup
  session_templates: MagnetarSessionTemplatesGroup
  provider_runs: MetorialProviderRunsEndpoint
  custom_providers: MagnetarCustomProvidersGroup


def get_magnetar_config(soft: dict[str, Any]) -> dict[str, Any]:
  """Get configuration with Magnetar API version."""
  return {**soft, "apiVersion": "2026-01-01-magnetar"}


def get_magnetar_endpoints(manager: MetorialEndpointManager) -> dict[str, Any]:
  """Create and configure all Magnetar SDK endpoints."""
  from metorial._magnetar_typed_endpoints import (
    TypedMagnetarCustomProvidersEndpoint,
    TypedMagnetarProviderDeploymentsEndpoint,
    TypedMagnetarProvidersEndpoint,
    TypedMagnetarSessionsEndpoint,
    TypedMagnetarSessionTemplatesEndpoint,
  )

  return {
    "instance": MagnetarInstanceEndpoint(manager),
    "publishers": MetorialPublishersEndpoint(manager),
    "providers": TypedMagnetarProvidersEndpoint(manager),
    "provider_categories": MetorialProviderCategoriesEndpoint(manager),
    "provider_collections": MetorialProviderCollectionsEndpoint(manager),
    "provider_groups": MetorialProviderGroupsEndpoint(manager),
    "provider_listings": MetorialProviderListingsEndpoint(manager),
    "provider_deployments": TypedMagnetarProviderDeploymentsEndpoint(manager),
    "provider_setup_sessions": MetorialProviderDeploymentsSetupSessionsEndpoint(manager),
    "sessions": TypedMagnetarSessionsEndpoint(manager),
    "session_templates": TypedMagnetarSessionTemplatesEndpoint(manager),
    "provider_runs": MetorialProviderRunsEndpoint(manager),
    "custom_providers": TypedMagnetarCustomProvidersEndpoint(manager),
  }


_magnetar_create = (
  MetorialSDKBuilder.create("metorial", "2026-01-01-magnetar")
  .set_get_api_host(get_api_host)
  .set_get_headers(get_headers)
  .build(get_magnetar_config)
)


def _to_magnetar_typed_sdk(raw: dict[str, Any]) -> MagnetarSDK:
  """Convert raw SDK data to typed Magnetar SDK instance with grouping."""
  _cfg = raw["_config"]

  providers_root = raw["providers"]
  provider_deployments_root = raw["provider_deployments"]
  sessions_root = raw["sessions"]
  session_templates_root = raw["session_templates"]
  custom_providers_root = raw["custom_providers"]

  return MagnetarSDK(
    _config=SDKConfig(
      apiKey=_cfg["apiKey"],
      apiVersion=_cfg["apiVersion"],
      apiHost=_cfg["apiHost"],
    ),
    instance=raw["instance"],
    publishers=raw["publishers"],
    providers=MagnetarProvidersGroup(providers_root, providers_root),
    provider_categories=raw["provider_categories"],
    provider_collections=raw["provider_collections"],
    provider_groups=raw["provider_groups"],
    provider_listings=raw["provider_listings"],
    provider_deployments=MagnetarProviderDeploymentsGroup(
      provider_deployments_root, provider_deployments_root
    ),
    provider_setup_sessions=raw["provider_setup_sessions"],
    sessions=MagnetarSessionsGroup(sessions_root, sessions_root),
    session_templates=MagnetarSessionTemplatesGroup(
      session_templates_root, session_templates_root
    ),
    provider_runs=raw["provider_runs"],
    custom_providers=MagnetarCustomProvidersGroup(
      custom_providers_root, custom_providers_root
    ),
  )


def create_magnetar_sdk(config: dict[str, Any]) -> MagnetarSDK:
  """Create a configured Magnetar SDK instance with typed endpoints."""
  raw = _magnetar_create(get_magnetar_endpoints)(config)
  return _to_magnetar_typed_sdk(raw)
