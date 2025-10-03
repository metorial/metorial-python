"""
Typed endpoint classes for better IDE support
"""

from typing import TYPE_CHECKING
from metorial_util_endpoint import MetorialEndpointManager

if TYPE_CHECKING:
  from mt_2025_01_01_pulsar.endpoints.servers_deployments import (
    MetorialServersDeploymentsEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.servers_variants import (
    MetorialServersVariantsEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.servers_versions import (
    MetorialServersVersionsEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.servers_implementations import (
    MetorialServersImplementationsEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.servers_capabilities import (
    MetorialServersCapabilitiesEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.server_runs import MetorialServerRunsEndpoint
  from mt_2025_01_01_pulsar.endpoints.sessions_messages import (
    MetorialSessionsMessagesEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.sessions_connections import (
    MetorialSessionsConnectionsEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections_authentications import (
    MetorialProviderOauthConnectionsAuthenticationsEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections_profiles import (
    MetorialProviderOauthConnectionsProfilesEndpoint,
  )
  from mt_2025_01_01_pulsar.endpoints.provider_oauth_sessions import (
    MetorialProviderOauthSessionsEndpoint,
  )


if TYPE_CHECKING:
  # Import base endpoint classes for type checking only
  from mt_2025_01_01_pulsar.endpoints.servers import (
    MetorialServersEndpoint as _MetorialServersEndpointBase,
  )
  from mt_2025_01_01_pulsar.endpoints.sessions import (
    MetorialSessionsEndpoint as _MetorialSessionsEndpointBase,
  )
  from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections import (
    MetorialProviderOauthConnectionsEndpoint as _MetorialProviderOauthConnectionsEndpointBase,
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
    from mt_2025_01_01_pulsar.endpoints.servers import MetorialServersEndpoint
    from mt_2025_01_01_pulsar.endpoints.servers_deployments import (
      MetorialServersDeploymentsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.servers_variants import (
      MetorialServersVariantsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.servers_versions import (
      MetorialServersVersionsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.servers_implementations import (
      MetorialServersImplementationsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.servers_capabilities import (
      MetorialServersCapabilitiesEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.server_runs import (
      MetorialServerRunsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.server_run_errors import (
      MetorialServerRunErrorsEndpoint,
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
    self.runs.errors = MetorialServerRunErrorsEndpoint(manager)

  def __getattr__(self, name):
    """Delegate unknown attributes to the base servers endpoint"""
    return getattr(self._base_servers, name)


class TypedMetorialSessionsEndpoint(_TypedSessionsBase):
  """Typed sessions endpoint with sub-endpoints"""

  # Type annotations for IDE support
  messages: "MetorialSessionsMessagesEndpoint"
  connections: "MetorialSessionsConnectionsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from mt_2025_01_01_pulsar.endpoints.sessions import MetorialSessionsEndpoint
    from mt_2025_01_01_pulsar.endpoints.sessions_messages import (
      MetorialSessionsMessagesEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.sessions_connections import (
      MetorialSessionsConnectionsEndpoint,
    )

    # Create the base sessions endpoint to inherit its methods
    self._base_sessions = MetorialSessionsEndpoint(manager)

    # Add sub-endpoints
    self.messages = MetorialSessionsMessagesEndpoint(manager)
    self.connections = MetorialSessionsConnectionsEndpoint(manager)

  def __getattr__(self, name):
    """Delegate unknown attributes to the base sessions endpoint"""
    return getattr(self._base_sessions, name)


class TypedMetorialProviderOauthConnectionsEndpoint(_TypedProviderOauthConnectionsBase):
  """Typed connections endpoint with nested authentications and profiles"""

  # Type annotations for IDE support
  authentications: "MetorialProviderOauthConnectionsAuthenticationsEndpoint"
  profiles: "MetorialProviderOauthConnectionsProfilesEndpoint"

  def __init__(self, base_endpoint, manager: MetorialEndpointManager):
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections_authentications import (
      MetorialProviderOauthConnectionsAuthenticationsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections_profiles import (
      MetorialProviderOauthConnectionsProfilesEndpoint,
    )

    # Store base endpoint for delegation
    self._base = base_endpoint

    # Add sub-endpoints
    self.authentications = MetorialProviderOauthConnectionsAuthenticationsEndpoint(
      manager
    )
    self.profiles = MetorialProviderOauthConnectionsProfilesEndpoint(manager)

  def __getattr__(self, name):
    """Delegate unknown attributes to the base connections endpoint"""
    return getattr(self._base, name)


class TypedMetorialProviderOauthEndpoint:
  """Typed provider OAuth endpoint with sub-endpoints"""

  # Type annotations for IDE support
  connections: "MetorialProviderOauthConnectionsEndpoint"
  sessions: "MetorialProviderOauthSessionsEndpoint"
  profiles: "MetorialProviderOauthConnectionsProfilesEndpoint"
  authentications: "MetorialProviderOauthConnectionsAuthenticationsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections import (
      MetorialProviderOauthConnectionsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_sessions import (
      MetorialProviderOauthSessionsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections_profiles import (
      MetorialProviderOauthConnectionsProfilesEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections_authentications import (
      MetorialProviderOauthConnectionsAuthenticationsEndpoint,
    )

    self.connections = MetorialProviderOauthConnectionsEndpoint(manager)
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
