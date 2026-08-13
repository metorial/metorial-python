"""
Magnetar SDK core implementation with typed endpoint groups and configuration.

Each endpoint "group" subclasses its generated base endpoint so that base
resource methods (``list``/``get``/``create``/...) are inherited with full
typing, and exposes its sub-endpoints as concretely typed attributes. This
gives the whole client surface full static inference with no ``Any`` and no
dynamic ``__getattr__`` delegation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from metorial._endpoint import MetorialEndpointManager
from metorial._generated.magnetar.endpoints.callbacks import (
  MetorialCallbacksEndpoint,
)
from metorial._generated.magnetar.endpoints.callbacks_destinations import (
  MetorialCallbacksDestinationsEndpoint,
)
from metorial._generated.magnetar.endpoints.callbacks_events import (
  MetorialCallbacksEventsEndpoint,
)
from metorial._generated.magnetar.endpoints.callbacks_instances import (
  MetorialCallbacksInstancesEndpoint,
)
from metorial._generated.magnetar.endpoints.custom_providers import (
  MetorialCustomProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.custom_providers_deployments import (
  MetorialCustomProvidersDeploymentsEndpoint,
)
from metorial._generated.magnetar.endpoints.custom_providers_versions import (
  MetorialCustomProvidersVersionsEndpoint,
)
from metorial._generated.magnetar.endpoints.documents import (
  MetorialDocumentsEndpoint,
)
from metorial._generated.magnetar.endpoints.documents_participants import (
  MetorialDocumentsParticipantsEndpoint,
)
from metorial._generated.magnetar.endpoints.documents_versions import (
  MetorialDocumentsVersionsEndpoint,
)
from metorial._generated.magnetar.endpoints.files import (
  MetorialFilesEndpoint,
)
from metorial._generated.magnetar.endpoints.files_links import (
  MetorialFilesLinksEndpoint,
)
from metorial._generated.magnetar.endpoints.instance import (
  MetorialInstanceEndpoint as MagnetarInstanceEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations import (
  MetorialIntegrationsEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations_instance_groups import (
  MetorialIntegrationsInstanceGroupsEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations_instance_groups_providers import (
  MetorialIntegrationsInstanceGroupsProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations_instances import (
  MetorialIntegrationsInstancesEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations_instances_providers import (
  MetorialIntegrationsInstancesProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations_providers import (
  MetorialIntegrationsProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.integrations_setup_sessions import (
  MetorialIntegrationsSetupSessionsEndpoint,
)
from metorial._generated.magnetar.endpoints.magic_mcp_endpoints import (
  MetorialMagicMcpEndpointsEndpoint,
)
from metorial._generated.magnetar.endpoints.magic_mcp_groups import (
  MetorialMagicMcpGroupsEndpoint,
)
from metorial._generated.magnetar.endpoints.magic_mcp_servers import (
  MetorialMagicMcpServersEndpoint,
)
from metorial._generated.magnetar.endpoints.magic_mcp_servers_providers import (
  MetorialMagicMcpServersProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.magic_mcp_sessions import (
  MetorialMagicMcpSessionsEndpoint,
)
from metorial._generated.magnetar.endpoints.magic_mcp_tokens import (
  MetorialMagicMcpTokensEndpoint,
)
from metorial._generated.magnetar.endpoints.portals import (
  MetorialPortalsEndpoint,
)
from metorial._generated.magnetar.endpoints.portals_access import (
  MetorialPortalsAccessEndpoint,
)
from metorial._generated.magnetar.endpoints.portals_access_requests import (
  MetorialPortalsAccessRequestsEndpoint,
)
from metorial._generated.magnetar.endpoints.portals_consumer_groups import (
  MetorialPortalsConsumerGroupsEndpoint,
)
from metorial._generated.magnetar.endpoints.portals_consumer_invites import (
  MetorialPortalsConsumerInvitesEndpoint,
)
from metorial._generated.magnetar.endpoints.portals_consumer_profiles import (
  MetorialPortalsConsumerProfilesEndpoint,
)
from metorial._generated.magnetar.endpoints.portals_listings import (
  MetorialPortalsListingsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments import (
  MetorialProviderDeploymentsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_auth_configs import (
  MetorialProviderDeploymentsAuthConfigsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_auth_configs_exports import (
  MetorialProviderDeploymentsAuthConfigsExportsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_auth_configs_imports import (
  MetorialProviderDeploymentsAuthConfigsImportsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_auth_credentials import (
  MetorialProviderDeploymentsAuthCredentialsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_config_vaults import (
  MetorialProviderDeploymentsConfigVaultsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_configs import (
  MetorialProviderDeploymentsConfigsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_deployments_setup_sessions import (
  MetorialProviderDeploymentsSetupSessionsEndpoint,
)
from metorial._generated.magnetar.endpoints.provider_runs import (
  MetorialProviderRunsEndpoint,
)
from metorial._generated.magnetar.endpoints.providers import (
  MetorialProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.providers_auth_methods import (
  MetorialProvidersAuthMethodsEndpoint,
)
from metorial._generated.magnetar.endpoints.providers_specifications import (
  MetorialProvidersSpecificationsEndpoint,
)
from metorial._generated.magnetar.endpoints.providers_tools import (
  MetorialProvidersToolsEndpoint,
)
from metorial._generated.magnetar.endpoints.providers_triggers import (
  MetorialProvidersTriggersEndpoint,
)
from metorial._generated.magnetar.endpoints.providers_versions import (
  MetorialProvidersVersionsEndpoint,
)
from metorial._generated.magnetar.endpoints.publishers import (
  MetorialPublishersEndpoint,
)
from metorial._generated.magnetar.endpoints.session_templates import (
  MetorialSessionTemplatesEndpoint,
)
from metorial._generated.magnetar.endpoints.session_templates_providers import (
  MetorialSessionTemplatesProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.sessions import (
  MetorialSessionsEndpoint,
)
from metorial._generated.magnetar.endpoints.sessions_connections import (
  MetorialSessionsConnectionsEndpoint,
)
from metorial._generated.magnetar.endpoints.sessions_errors import (
  MetorialSessionsErrorsEndpoint,
)
from metorial._generated.magnetar.endpoints.sessions_messages import (
  MetorialSessionsMessagesEndpoint,
)
from metorial._generated.magnetar.endpoints.sessions_participants import (
  MetorialSessionsParticipantsEndpoint,
)
from metorial._generated.magnetar.endpoints.sessions_providers import (
  MetorialSessionsProvidersEndpoint,
)
from metorial._generated.magnetar.endpoints.skills import (
  MetorialSkillsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_agents import (
  MetorialSkillsAgentsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_configurations import (
  MetorialSkillsConfigurationsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_exports import (
  MetorialSkillsExportsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_groups import (
  MetorialSkillsGroupsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_groups_items import (
  MetorialSkillsGroupsItemsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_items import (
  MetorialSkillsItemsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_marketplaces import (
  MetorialSkillsMarketplacesEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_marketplaces_plugins import (
  MetorialSkillsMarketplacesPluginsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_participants import (
  MetorialSkillsParticipantsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_plugins import (
  MetorialSkillsPluginsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_plugins_skills import (
  MetorialSkillsPluginsSkillsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_templates import (
  MetorialSkillsTemplatesEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_templates_items import (
  MetorialSkillsTemplatesItemsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_versions import (
  MetorialSkillsVersionsEndpoint,
)
from metorial._generated.magnetar.endpoints.skills_versions_snapshot import (
  MetorialSkillsVersionsSnapshotEndpoint,
)
from metorial._generated.magnetar.endpoints.stores import (
  MetorialStoresEndpoint,
)
from metorial._generated.magnetar.endpoints.stores_items import (
  MetorialStoresItemsEndpoint,
)
from metorial._generated.magnetar.endpoints.stores_participants import (
  MetorialStoresParticipantsEndpoint,
)
from metorial._generated.magnetar.endpoints.tool_calls import (
  MetorialToolCallsEndpoint,
)
from metorial._sdk_builder import MetorialSDKBuilder
from metorial._sdk_shared import SDKConfig, get_api_host, get_headers

# ── Nested endpoint groups ────────────────────────────────────────────────────


class MagnetarProviderDeploymentsAuthConfigsGroup(
  MetorialProviderDeploymentsAuthConfigsEndpoint
):
  """Provider deployment auth configs with imports/exports sub-endpoints."""

  imports: MetorialProviderDeploymentsAuthConfigsImportsEndpoint
  exports: MetorialProviderDeploymentsAuthConfigsExportsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.imports = MetorialProviderDeploymentsAuthConfigsImportsEndpoint(manager)
    self.exports = MetorialProviderDeploymentsAuthConfigsExportsEndpoint(manager)


class MagnetarIntegrationsInstancesGroup(MetorialIntegrationsInstancesEndpoint):
  """Integration instances with providers sub-endpoint."""

  providers: MetorialIntegrationsInstancesProvidersEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.providers = MetorialIntegrationsInstancesProvidersEndpoint(manager)


class MagnetarIntegrationsInstanceGroupsGroup(
  MetorialIntegrationsInstanceGroupsEndpoint
):
  """Integration instance-groups with providers sub-endpoint."""

  providers: MetorialIntegrationsInstanceGroupsProvidersEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.providers = MetorialIntegrationsInstanceGroupsProvidersEndpoint(manager)


class MagnetarSkillsTemplatesGroup(MetorialSkillsTemplatesEndpoint):
  """Skill templates with items sub-endpoint."""

  items: MetorialSkillsTemplatesItemsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.items = MetorialSkillsTemplatesItemsEndpoint(manager)


class MagnetarSkillsMarketplacesGroup(MetorialSkillsMarketplacesEndpoint):
  """Skill marketplaces with plugins sub-endpoint."""

  plugins: MetorialSkillsMarketplacesPluginsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.plugins = MetorialSkillsMarketplacesPluginsEndpoint(manager)


class MagnetarSkillsPluginsGroup(MetorialSkillsPluginsEndpoint):
  """Skill plugins with skills sub-endpoint."""

  skills: MetorialSkillsPluginsSkillsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.skills = MetorialSkillsPluginsSkillsEndpoint(manager)


class MagnetarSkillsVersionsGroup(MetorialSkillsVersionsEndpoint):
  """Skill versions with snapshot sub-endpoint."""

  snapshot: MetorialSkillsVersionsSnapshotEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.snapshot = MetorialSkillsVersionsSnapshotEndpoint(manager)


class MagnetarSkillsGroupsGroup(MetorialSkillsGroupsEndpoint):
  """Skill groups with items sub-endpoint."""

  items: MetorialSkillsGroupsItemsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.items = MetorialSkillsGroupsItemsEndpoint(manager)


class MagnetarMagicMcpServersGroup(MetorialMagicMcpServersEndpoint):
  """Magic-MCP servers with providers sub-endpoint."""

  providers: MetorialMagicMcpServersProvidersEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.providers = MetorialMagicMcpServersProvidersEndpoint(manager)


# ── Top-level endpoint groups ─────────────────────────────────────────────────


class MagnetarProvidersGroup(MetorialProvidersEndpoint):
  """Providers endpoint group with typed sub-endpoints."""

  versions: MetorialProvidersVersionsEndpoint
  tools: MetorialProvidersToolsEndpoint
  auth_methods: MetorialProvidersAuthMethodsEndpoint
  specifications: MetorialProvidersSpecificationsEndpoint
  triggers: MetorialProvidersTriggersEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.versions = MetorialProvidersVersionsEndpoint(manager)
    self.tools = MetorialProvidersToolsEndpoint(manager)
    self.auth_methods = MetorialProvidersAuthMethodsEndpoint(manager)
    self.specifications = MetorialProvidersSpecificationsEndpoint(manager)
    self.triggers = MetorialProvidersTriggersEndpoint(manager)


class MagnetarProviderDeploymentsGroup(MetorialProviderDeploymentsEndpoint):
  """Provider deployments endpoint group with typed sub-endpoints."""

  configs: MetorialProviderDeploymentsConfigsEndpoint
  config_vaults: MetorialProviderDeploymentsConfigVaultsEndpoint
  auth_configs: MagnetarProviderDeploymentsAuthConfigsGroup
  auth_credentials: MetorialProviderDeploymentsAuthCredentialsEndpoint
  setup_sessions: MetorialProviderDeploymentsSetupSessionsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.configs = MetorialProviderDeploymentsConfigsEndpoint(manager)
    self.config_vaults = MetorialProviderDeploymentsConfigVaultsEndpoint(manager)
    self.auth_configs = MagnetarProviderDeploymentsAuthConfigsGroup(manager)
    self.auth_credentials = MetorialProviderDeploymentsAuthCredentialsEndpoint(manager)
    self.setup_sessions = MetorialProviderDeploymentsSetupSessionsEndpoint(manager)


class MagnetarSessionsGroup(MetorialSessionsEndpoint):
  """Magnetar sessions endpoint group with typed sub-endpoints."""

  messages: MetorialSessionsMessagesEndpoint
  connections: MetorialSessionsConnectionsEndpoint
  providers: MetorialSessionsProvidersEndpoint
  participants: MetorialSessionsParticipantsEndpoint
  errors: MetorialSessionsErrorsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.messages = MetorialSessionsMessagesEndpoint(manager)
    self.connections = MetorialSessionsConnectionsEndpoint(manager)
    self.providers = MetorialSessionsProvidersEndpoint(manager)
    self.participants = MetorialSessionsParticipantsEndpoint(manager)
    self.errors = MetorialSessionsErrorsEndpoint(manager)


class MagnetarSessionTemplatesGroup(MetorialSessionTemplatesEndpoint):
  """Session templates endpoint group with typed sub-endpoints."""

  providers: MetorialSessionTemplatesProvidersEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.providers = MetorialSessionTemplatesProvidersEndpoint(manager)


class MagnetarCustomProvidersGroup(MetorialCustomProvidersEndpoint):
  """Custom providers endpoint group with typed sub-endpoints."""

  versions: MetorialCustomProvidersVersionsEndpoint
  deployments: MetorialCustomProvidersDeploymentsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.versions = MetorialCustomProvidersVersionsEndpoint(manager)
    self.deployments = MetorialCustomProvidersDeploymentsEndpoint(manager)


class MagnetarIntegrationsGroup(MetorialIntegrationsEndpoint):
  """Integrations endpoint group with typed sub-endpoints."""

  providers: MetorialIntegrationsProvidersEndpoint
  instances: MagnetarIntegrationsInstancesGroup
  instance_groups: MagnetarIntegrationsInstanceGroupsGroup
  setup_sessions: MetorialIntegrationsSetupSessionsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.providers = MetorialIntegrationsProvidersEndpoint(manager)
    self.instances = MagnetarIntegrationsInstancesGroup(manager)
    self.instance_groups = MagnetarIntegrationsInstanceGroupsGroup(manager)
    self.setup_sessions = MetorialIntegrationsSetupSessionsEndpoint(manager)


class MagnetarDocumentsGroup(MetorialDocumentsEndpoint):
  """Documents endpoint group with typed sub-endpoints."""

  versions: MetorialDocumentsVersionsEndpoint
  participants: MetorialDocumentsParticipantsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.versions = MetorialDocumentsVersionsEndpoint(manager)
    self.participants = MetorialDocumentsParticipantsEndpoint(manager)


class MagnetarStoresGroup(MetorialStoresEndpoint):
  """Stores endpoint group with typed sub-endpoints."""

  items: MetorialStoresItemsEndpoint
  participants: MetorialStoresParticipantsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.items = MetorialStoresItemsEndpoint(manager)
    self.participants = MetorialStoresParticipantsEndpoint(manager)


class MagnetarFilesGroup(MetorialFilesEndpoint):
  """Files endpoint group with links sub-endpoint."""

  links: MetorialFilesLinksEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.links = MetorialFilesLinksEndpoint(manager)


class MagnetarSkillsGroup(MetorialSkillsEndpoint):
  """Skills endpoint group with typed sub-endpoints."""

  configurations: MetorialSkillsConfigurationsEndpoint
  agents: MetorialSkillsAgentsEndpoint
  items: MetorialSkillsItemsEndpoint
  participants: MetorialSkillsParticipantsEndpoint
  exports: MetorialSkillsExportsEndpoint
  templates: MagnetarSkillsTemplatesGroup
  marketplaces: MagnetarSkillsMarketplacesGroup
  plugins: MagnetarSkillsPluginsGroup
  versions: MagnetarSkillsVersionsGroup
  groups: MagnetarSkillsGroupsGroup

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.configurations = MetorialSkillsConfigurationsEndpoint(manager)
    self.agents = MetorialSkillsAgentsEndpoint(manager)
    self.items = MetorialSkillsItemsEndpoint(manager)
    self.participants = MetorialSkillsParticipantsEndpoint(manager)
    self.exports = MetorialSkillsExportsEndpoint(manager)
    self.templates = MagnetarSkillsTemplatesGroup(manager)
    self.marketplaces = MagnetarSkillsMarketplacesGroup(manager)
    self.plugins = MagnetarSkillsPluginsGroup(manager)
    self.versions = MagnetarSkillsVersionsGroup(manager)
    self.groups = MagnetarSkillsGroupsGroup(manager)


class MagnetarCallbacksGroup(MetorialCallbacksEndpoint):
  """Callbacks endpoint group with typed sub-endpoints."""

  destinations: MetorialCallbacksDestinationsEndpoint
  events: MetorialCallbacksEventsEndpoint
  instances: MetorialCallbacksInstancesEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.destinations = MetorialCallbacksDestinationsEndpoint(manager)
    self.events = MetorialCallbacksEventsEndpoint(manager)
    self.instances = MetorialCallbacksInstancesEndpoint(manager)


class MagnetarMagicMcpGroup:
  """Magic-MCP namespace (no base endpoint), mirrors Node's ``magicMcp`` object."""

  servers: MagnetarMagicMcpServersGroup
  groups: MetorialMagicMcpGroupsEndpoint
  sessions: MetorialMagicMcpSessionsEndpoint
  tokens: MetorialMagicMcpTokensEndpoint
  endpoints: MetorialMagicMcpEndpointsEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    self.servers = MagnetarMagicMcpServersGroup(manager)
    self.groups = MetorialMagicMcpGroupsEndpoint(manager)
    self.sessions = MetorialMagicMcpSessionsEndpoint(manager)
    self.tokens = MetorialMagicMcpTokensEndpoint(manager)
    self.endpoints = MetorialMagicMcpEndpointsEndpoint(manager)


class MagnetarPortalsGroup(MetorialPortalsEndpoint):
  """Portals endpoint group with typed sub-endpoints."""

  access: MetorialPortalsAccessEndpoint
  access_requests: MetorialPortalsAccessRequestsEndpoint
  listings: MetorialPortalsListingsEndpoint
  consumer_groups: MetorialPortalsConsumerGroupsEndpoint
  consumer_invites: MetorialPortalsConsumerInvitesEndpoint
  consumer_profiles: MetorialPortalsConsumerProfilesEndpoint

  def __init__(self, manager: MetorialEndpointManager) -> None:
    super().__init__(manager)
    self.access = MetorialPortalsAccessEndpoint(manager)
    self.access_requests = MetorialPortalsAccessRequestsEndpoint(manager)
    self.listings = MetorialPortalsListingsEndpoint(manager)
    self.consumer_groups = MetorialPortalsConsumerGroupsEndpoint(manager)
    self.consumer_invites = MetorialPortalsConsumerInvitesEndpoint(manager)
    self.consumer_profiles = MetorialPortalsConsumerProfilesEndpoint(manager)


@dataclass(frozen=True)
class MagnetarSDK:
  _config: SDKConfig
  instance: MagnetarInstanceEndpoint
  publishers: MetorialPublishersEndpoint
  providers: MagnetarProvidersGroup
  provider_deployments: MagnetarProviderDeploymentsGroup
  provider_setup_sessions: MetorialProviderDeploymentsSetupSessionsEndpoint
  sessions: MagnetarSessionsGroup
  session_templates: MagnetarSessionTemplatesGroup
  provider_runs: MetorialProviderRunsEndpoint
  tool_calls: MetorialToolCallsEndpoint
  custom_providers: MagnetarCustomProvidersGroup
  integrations: MagnetarIntegrationsGroup
  documents: MagnetarDocumentsGroup
  stores: MagnetarStoresGroup
  files: MagnetarFilesGroup
  skills: MagnetarSkillsGroup
  callbacks: MagnetarCallbacksGroup
  magic_mcp: MagnetarMagicMcpGroup
  portals: MagnetarPortalsGroup


def get_magnetar_config(soft: dict[str, Any]) -> dict[str, Any]:
  """Get configuration with Magnetar API version."""
  return {**soft, "apiVersion": "2026-01-01-magnetar"}


def get_magnetar_endpoints(manager: MetorialEndpointManager) -> dict[str, Any]:
  """Create and configure all Magnetar SDK endpoint groups."""
  return {
    "instance": MagnetarInstanceEndpoint(manager),
    "publishers": MetorialPublishersEndpoint(manager),
    "providers": MagnetarProvidersGroup(manager),
    "provider_deployments": MagnetarProviderDeploymentsGroup(manager),
    "provider_setup_sessions": MetorialProviderDeploymentsSetupSessionsEndpoint(
      manager
    ),
    "sessions": MagnetarSessionsGroup(manager),
    "session_templates": MagnetarSessionTemplatesGroup(manager),
    "provider_runs": MetorialProviderRunsEndpoint(manager),
    "tool_calls": MetorialToolCallsEndpoint(manager),
    "custom_providers": MagnetarCustomProvidersGroup(manager),
    "integrations": MagnetarIntegrationsGroup(manager),
    "documents": MagnetarDocumentsGroup(manager),
    "stores": MagnetarStoresGroup(manager),
    "files": MagnetarFilesGroup(manager),
    "skills": MagnetarSkillsGroup(manager),
    "callbacks": MagnetarCallbacksGroup(manager),
    "magic_mcp": MagnetarMagicMcpGroup(manager),
    "portals": MagnetarPortalsGroup(manager),
  }


_magnetar_create = (
  MetorialSDKBuilder.create("metorial", "2026-01-01-magnetar")
  .set_get_api_host(get_api_host)
  .set_get_headers(get_headers)
  .build(get_magnetar_config)
)


def _to_magnetar_typed_sdk(raw: dict[str, Any]) -> MagnetarSDK:
  """Assemble the typed Magnetar SDK from the builder's raw endpoint map."""
  _cfg = raw["_config"]

  return MagnetarSDK(
    _config=SDKConfig(
      apiKey=_cfg["apiKey"],
      apiVersion=_cfg["apiVersion"],
      apiHost=_cfg["apiHost"],
    ),
    instance=raw["instance"],
    publishers=raw["publishers"],
    providers=raw["providers"],
    provider_deployments=raw["provider_deployments"],
    provider_setup_sessions=raw["provider_setup_sessions"],
    sessions=raw["sessions"],
    session_templates=raw["session_templates"],
    provider_runs=raw["provider_runs"],
    tool_calls=raw["tool_calls"],
    custom_providers=raw["custom_providers"],
    integrations=raw["integrations"],
    documents=raw["documents"],
    stores=raw["stores"],
    files=raw["files"],
    skills=raw["skills"],
    callbacks=raw["callbacks"],
    magic_mcp=raw["magic_mcp"],
    portals=raw["portals"],
  )


def create_magnetar_sdk(config: dict[str, Any]) -> MagnetarSDK:
  """Create a configured Magnetar SDK instance with typed endpoint groups."""
  raw = _magnetar_create(get_magnetar_endpoints)(config)
  return _to_magnetar_typed_sdk(raw)
