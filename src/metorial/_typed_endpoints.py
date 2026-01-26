"""
Typed endpoint classes for better IDE support
"""

from typing import TYPE_CHECKING, Any

from metorial._endpoint import MetorialEndpointManager

if TYPE_CHECKING:
  from metorial._generated.pulsar.endpoints.provider_oauth_connections_authentications import (
    MetorialProviderOauthConnectionsAuthenticationsEndpoint,
  )
  from metorial._generated.pulsar.endpoints.provider_oauth_connections_profiles import (
    MetorialProviderOauthConnectionsProfilesEndpoint,
  )
  from metorial._generated.pulsar.endpoints.provider_oauth_sessions import (
    MetorialProviderOauthSessionsEndpoint,
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


if TYPE_CHECKING:
  # Import base endpoint classes for type checking only
  from metorial._generated.pulsar.endpoints.provider_oauth_connections import (
    MetorialProviderOauthConnectionsEndpoint as _MetorialProviderOauthConnectionsEndpointBase,
  )
  from metorial._generated.pulsar.endpoints.servers import (
    MetorialServersEndpoint as _MetorialServersEndpointBase,
  )
  from metorial._generated.pulsar.endpoints.sessions import (
    MetorialSessionsEndpoint as _MetorialSessionsEndpointBase,
  )

  # For type checkers, make the typed endpoints inherit from base to get all methods
  _TypedServersBase = _MetorialServersEndpointBase
  _TypedSessionsBase = _MetorialSessionsEndpointBase
  _TypedProviderOauthConnectionsBase = _MetorialProviderOauthConnectionsEndpointBase
else:
  # At runtime, just use object as base
  _TypedServersBase = object
  _TypedSessionsBase = object
  _TypedProviderOauthConnectionsBase = object


class TypedMetorialServersEndpoint(_TypedServersBase):
  """Typed servers endpoint with all sub-endpoints"""

  # Type annotations for IDE support - sub-endpoints
  variants: "MetorialServersVariantsEndpoint"
  versions: "MetorialServersVersionsEndpoint"
  deployments: "MetorialServersDeploymentsEndpoint"
  implementations: "MetorialServersImplementationsEndpoint"
  capabilities: "MetorialServersCapabilitiesEndpoint"
  runs: "MetorialServerRunsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    # Import here to avoid circular imports
    from metorial._generated.pulsar.endpoints.server_run_errors import (
      MetorialServerRunErrorsEndpoint,
    )
    from metorial._generated.pulsar.endpoints.server_runs import (
      MetorialServerRunsEndpoint,
    )
    from metorial._generated.pulsar.endpoints.servers import MetorialServersEndpoint
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

    # Create the base servers endpoint to inherit its methods
    self._base_servers = MetorialServersEndpoint(manager)

    # Add sub-endpoints
    self.variants = MetorialServersVariantsEndpoint(manager)
    self.versions = MetorialServersVersionsEndpoint(manager)
    self.deployments = MetorialServersDeploymentsEndpoint(manager)
    self.implementations = MetorialServersImplementationsEndpoint(manager)
    self.capabilities = MetorialServersCapabilitiesEndpoint(manager)

    self.runs = MetorialServerRunsEndpoint(manager)
    setattr(self.runs, "errors", MetorialServerRunErrorsEndpoint(manager))  # noqa: B010

  def __getattr__(self, name: str) -> Any:
    """Delegate unknown attributes to the base servers endpoint"""
    return getattr(self._base_servers, name)


class TypedMetorialSessionsEndpoint(_TypedSessionsBase):
  """Typed sessions endpoint with sub-endpoints"""

  # Type annotations for IDE support
  messages: "MetorialSessionsMessagesEndpoint"
  connections: "MetorialSessionsConnectionsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from metorial._generated.pulsar.endpoints.sessions import MetorialSessionsEndpoint
    from metorial._generated.pulsar.endpoints.sessions_connections import (
      MetorialSessionsConnectionsEndpoint,
    )
    from metorial._generated.pulsar.endpoints.sessions_messages import (
      MetorialSessionsMessagesEndpoint,
    )

    # Create the base sessions endpoint to inherit its methods
    self._base_sessions = MetorialSessionsEndpoint(manager)

    # Add sub-endpoints
    self.messages = MetorialSessionsMessagesEndpoint(manager)
    self.connections = MetorialSessionsConnectionsEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    """Delegate unknown attributes to the base sessions endpoint"""
    return getattr(self._base_sessions, name)


class TypedMetorialProviderOauthConnectionsEndpoint(_TypedProviderOauthConnectionsBase):
  """Typed connections endpoint with nested authentications and profiles"""

  # Type annotations for IDE support
  authentications: "MetorialProviderOauthConnectionsAuthenticationsEndpoint"
  profiles: "MetorialProviderOauthConnectionsProfilesEndpoint"

  def __init__(self, base_endpoint: object, manager: MetorialEndpointManager) -> None:
    from metorial._generated.pulsar.endpoints.provider_oauth_connections_authentications import (
      MetorialProviderOauthConnectionsAuthenticationsEndpoint,
    )
    from metorial._generated.pulsar.endpoints.provider_oauth_connections_profiles import (
      MetorialProviderOauthConnectionsProfilesEndpoint,
    )

    # Store base endpoint for delegation
    self._base = base_endpoint

    # Add sub-endpoints
    self.authentications = MetorialProviderOauthConnectionsAuthenticationsEndpoint(
      manager
    )
    self.profiles = MetorialProviderOauthConnectionsProfilesEndpoint(manager)

  def __getattr__(self, name: str) -> Any:
    """Delegate unknown attributes to the base connections endpoint"""
    return getattr(self._base, name)


class TypedMetorialProviderOauthEndpoint:
  """Typed provider OAuth endpoint with sub-endpoints"""

  # Type annotations for IDE support
  connections: "TypedMetorialProviderOauthConnectionsEndpoint"
  sessions: "MetorialProviderOauthSessionsEndpoint"
  profiles: "MetorialProviderOauthConnectionsProfilesEndpoint"
  authentications: "MetorialProviderOauthConnectionsAuthenticationsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
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

    base_connections = MetorialProviderOauthConnectionsEndpoint(manager)
    self.connections = TypedMetorialProviderOauthConnectionsEndpoint(
      base_connections, manager
    )
    self.sessions = MetorialProviderOauthSessionsEndpoint(manager)
    self.profiles = MetorialProviderOauthConnectionsProfilesEndpoint(manager)
    self.authentications = MetorialProviderOauthConnectionsAuthenticationsEndpoint(
      manager
    )


__all__ = [
  "TypedMetorialServersEndpoint",
  "TypedMetorialSessionsEndpoint",
  "TypedMetorialProviderOauthEndpoint",
  "TypedMetorialProviderOauthConnectionsEndpoint",
]
