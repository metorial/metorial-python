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


class TypedMetorialServersEndpoint:
  """Typed servers endpoint with all sub-endpoints"""

  # Type annotations for IDE support
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


class TypedMetorialSessionsEndpoint:
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


class TypedMetorialProviderOauthConnectionsEndpoint:
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
    self.authentications = MetorialProviderOauthConnectionsAuthenticationsEndpoint(manager)
    self.profiles = MetorialProviderOauthConnectionsProfilesEndpoint(manager)
  
  def __getattr__(self, name):
    """Delegate unknown attributes to the base connections endpoint"""
    return getattr(self._base, name)


class TypedMetorialProviderOauthEndpoint:
  """Typed provider OAuth endpoint with sub-endpoints"""

  # Type annotations for IDE support
  connections: "TypedMetorialProviderOauthConnectionsEndpoint"
  sessions: "MetorialProviderOauthSessionsEndpoint"

  def __init__(self, manager: MetorialEndpointManager):
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_connections import (
      MetorialProviderOauthConnectionsEndpoint,
    )
    from mt_2025_01_01_pulsar.endpoints.provider_oauth_sessions import (
      MetorialProviderOauthSessionsEndpoint,
    )

    # Create connections endpoint with typed sub-endpoints
    base_connections = MetorialProviderOauthConnectionsEndpoint(manager)
    self.connections = TypedMetorialProviderOauthConnectionsEndpoint(base_connections, manager)

    # Create sessions endpoint
    self.sessions = MetorialProviderOauthSessionsEndpoint(manager)


__all__ = [
  "TypedMetorialServersEndpoint", 
  "TypedMetorialSessionsEndpoint", 
  "TypedMetorialProviderOauthEndpoint",
  "TypedMetorialProviderOauthConnectionsEndpoint",
]
