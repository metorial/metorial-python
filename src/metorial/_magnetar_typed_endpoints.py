"""
Typed endpoint classes for Magnetar API - better IDE support
"""

from typing import TYPE_CHECKING, Any

from metorial._endpoint import MetorialEndpointManager

if TYPE_CHECKING:
  from metorial._generated.magnetar.endpoints.custom_providers_commits import (
    MetorialCustomProvidersCommitsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.custom_providers_deployments import (
    MetorialCustomProvidersDeploymentsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.custom_providers_environments import (
    MetorialCustomProvidersEnvironmentsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.custom_providers_versions import (
    MetorialCustomProvidersVersionsEndpoint,
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
  from metorial._generated.magnetar.endpoints.providers_auth_methods import (
    MetorialProvidersAuthMethodsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.providers_specifications import (
    MetorialProvidersSpecificationsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.providers_tools import (
    MetorialProvidersToolsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.providers_versions import (
    MetorialProvidersVersionsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.session_templates_providers import (
    MetorialSessionTemplatesProvidersEndpoint,
  )
  from metorial._generated.magnetar.endpoints.sessions_connections import (
    MetorialSessionsConnectionsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.sessions_error_groups import (
    MetorialSessionsErrorGroupsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.sessions_errors import (
    MetorialSessionsErrorsEndpoint,
  )
  from metorial._generated.magnetar.endpoints.sessions_events import (
    MetorialSessionsEventsEndpoint,
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


class TypedMagnetarProvidersEndpoint:
  """Typed providers endpoint with all sub-endpoints"""

  versions: "MetorialProvidersVersionsEndpoint"
  tools: "MetorialProvidersToolsEndpoint"
  auth_methods: "MetorialProvidersAuthMethodsEndpoint"
  specifications: "MetorialProvidersSpecificationsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
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
    from metorial._generated.magnetar.endpoints.providers_versions import (
      MetorialProvidersVersionsEndpoint,
    )

    self._base = MetorialProvidersEndpoint(manager)
    self.versions = MetorialProvidersVersionsEndpoint(manager)
    self.tools = MetorialProvidersToolsEndpoint(manager)
    self.auth_methods = MetorialProvidersAuthMethodsEndpoint(manager)
    self.specifications = MetorialProvidersSpecificationsEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._base, name)


class TypedMagnetarAuthConfigsEndpoint:
  """Typed auth configs endpoint with imports/exports sub-endpoints"""

  imports: "MetorialProviderDeploymentsAuthConfigsImportsEndpoint"
  exports: "MetorialProviderDeploymentsAuthConfigsExportsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from metorial._generated.magnetar.endpoints.provider_deployments_auth_configs import (
      MetorialProviderDeploymentsAuthConfigsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.provider_deployments_auth_configs_exports import (
      MetorialProviderDeploymentsAuthConfigsExportsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.provider_deployments_auth_configs_imports import (
      MetorialProviderDeploymentsAuthConfigsImportsEndpoint,
    )

    self._base = MetorialProviderDeploymentsAuthConfigsEndpoint(manager)
    self.imports = MetorialProviderDeploymentsAuthConfigsImportsEndpoint(manager)
    self.exports = MetorialProviderDeploymentsAuthConfigsExportsEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._base, name)


class TypedMagnetarProviderDeploymentsEndpoint:
  """Typed provider deployments endpoint with all sub-endpoints"""

  configs: "MetorialProviderDeploymentsConfigsEndpoint"
  config_vaults: "MetorialProviderDeploymentsConfigVaultsEndpoint"
  auth_configs: TypedMagnetarAuthConfigsEndpoint
  auth_credentials: "MetorialProviderDeploymentsAuthCredentialsEndpoint"
  setup_sessions: "MetorialProviderDeploymentsSetupSessionsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from metorial._generated.magnetar.endpoints.provider_deployments import (
      MetorialProviderDeploymentsEndpoint,
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

    self._base = MetorialProviderDeploymentsEndpoint(manager)
    self.configs = MetorialProviderDeploymentsConfigsEndpoint(manager)
    self.config_vaults = MetorialProviderDeploymentsConfigVaultsEndpoint(manager)
    self.auth_configs = TypedMagnetarAuthConfigsEndpoint(manager)
    self.auth_credentials = MetorialProviderDeploymentsAuthCredentialsEndpoint(manager)
    self.setup_sessions = MetorialProviderDeploymentsSetupSessionsEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._base, name)


class TypedMagnetarCustomProvidersEndpoint:
  """Typed custom providers endpoint with all sub-endpoints"""

  versions: "MetorialCustomProvidersVersionsEndpoint"
  deployments: "MetorialCustomProvidersDeploymentsEndpoint"
  environments: "MetorialCustomProvidersEnvironmentsEndpoint"
  commits: "MetorialCustomProvidersCommitsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from metorial._generated.magnetar.endpoints.custom_providers import (
      MetorialCustomProvidersEndpoint,
    )
    from metorial._generated.magnetar.endpoints.custom_providers_commits import (
      MetorialCustomProvidersCommitsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.custom_providers_deployments import (
      MetorialCustomProvidersDeploymentsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.custom_providers_environments import (
      MetorialCustomProvidersEnvironmentsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.custom_providers_versions import (
      MetorialCustomProvidersVersionsEndpoint,
    )

    self._base = MetorialCustomProvidersEndpoint(manager)
    self.versions = MetorialCustomProvidersVersionsEndpoint(manager)
    self.deployments = MetorialCustomProvidersDeploymentsEndpoint(manager)
    self.environments = MetorialCustomProvidersEnvironmentsEndpoint(manager)
    self.commits = MetorialCustomProvidersCommitsEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._base, name)


class TypedMagnetarSessionsEndpoint:
  """Typed Magnetar sessions endpoint with sub-endpoints"""

  messages: "MetorialSessionsMessagesEndpoint"
  connections: "MetorialSessionsConnectionsEndpoint"
  events: "MetorialSessionsEventsEndpoint"
  providers: "MetorialSessionsProvidersEndpoint"
  participants: "MetorialSessionsParticipantsEndpoint"
  errors: "MetorialSessionsErrorsEndpoint"
  error_groups: "MetorialSessionsErrorGroupsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from metorial._generated.magnetar.endpoints.sessions import (
      MetorialSessionsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.sessions_connections import (
      MetorialSessionsConnectionsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.sessions_error_groups import (
      MetorialSessionsErrorGroupsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.sessions_errors import (
      MetorialSessionsErrorsEndpoint,
    )
    from metorial._generated.magnetar.endpoints.sessions_events import (
      MetorialSessionsEventsEndpoint,
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

    self._base = MetorialSessionsEndpoint(manager)
    self.messages = MetorialSessionsMessagesEndpoint(manager)
    self.connections = MetorialSessionsConnectionsEndpoint(manager)
    self.events = MetorialSessionsEventsEndpoint(manager)
    self.providers = MetorialSessionsProvidersEndpoint(manager)
    self.participants = MetorialSessionsParticipantsEndpoint(manager)
    self.errors = MetorialSessionsErrorsEndpoint(manager)
    self.error_groups = MetorialSessionsErrorGroupsEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._base, name)


class TypedMagnetarSessionTemplatesEndpoint:
  """Typed session templates endpoint with sub-endpoints"""

  providers: "MetorialSessionTemplatesProvidersEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from metorial._generated.magnetar.endpoints.session_templates import (
      MetorialSessionTemplatesEndpoint,
    )
    from metorial._generated.magnetar.endpoints.session_templates_providers import (
      MetorialSessionTemplatesProvidersEndpoint,
    )

    self._base = MetorialSessionTemplatesEndpoint(manager)
    self.providers = MetorialSessionTemplatesProvidersEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._base, name)


__all__ = [
  "TypedMagnetarProvidersEndpoint",
  "TypedMagnetarProviderDeploymentsEndpoint",
  "TypedMagnetarCustomProvidersEndpoint",
  "TypedMagnetarSessionsEndpoint",
  "TypedMagnetarSessionTemplatesEndpoint",
]
