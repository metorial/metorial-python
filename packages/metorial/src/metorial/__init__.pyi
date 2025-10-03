"""
Type stub file to ensure IDE autocomplete works properly for the Metorial class
"""
from typing import Optional, Dict, Any
from metorial_core.base import MetorialBase
from metorial_core.sdk import ServersGroup, SessionsGroup, ProviderOauthGroup
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
from mt_2025_01_01_pulsar.endpoints.instance import MetorialInstanceEndpoint
from mt_2025_01_01_pulsar.endpoints.secrets import MetorialSecretsEndpoint
from mt_2025_01_01_pulsar.endpoints.files import MetorialFilesEndpoint
from mt_2025_01_01_pulsar.endpoints.links import MetorialLinksEndpoint

class Metorial(MetorialBase):
  def __init__(
    self,
    api_key: Optional[str] = None,
    api_host: str = "https://api.metorial.com",
    **kwargs: Any
  ) -> None: ...

  # Explicit property declarations for IDE autocomplete
  @property
  def instance(self) -> Optional[MetorialInstanceEndpoint]: ...
  @property
  def secrets(self) -> Optional[MetorialSecretsEndpoint]: ...
  @property
  def servers(self) -> Optional[ServersGroup]: ...
  @property
  def sessions(self) -> Optional[SessionsGroup]: ...
  @property
  def files(self) -> Optional[MetorialFilesEndpoint]: ...
  @property
  def links(self) -> Optional[MetorialLinksEndpoint]: ...
  @property
  def oauth(self) -> Optional[ProviderOauthGroup]: ...

class ProviderOauthGroup:
  connections: MetorialProviderOauthConnectionsEndpoint
  sessions: MetorialProviderOauthSessionsEndpoint
  profiles: MetorialProviderOauthConnectionsProfilesEndpoint
  authentications: MetorialProviderOauthConnectionsAuthenticationsEndpoint

class MetorialSync(MetorialBase):
  def __init__(
    self,
    api_key: Optional[str] = None,
    api_host: str = "https://api.metorial.com",
    **kwargs: Any
  ) -> None: ...

  # Explicit property declarations for IDE autocomplete
  @property
  def instance(self) -> Optional[MetorialInstanceEndpoint]: ...
  @property
  def secrets(self) -> Optional[MetorialSecretsEndpoint]: ...
  @property
  def servers(self) -> Optional[ServersGroup]: ...
  @property
  def sessions(self) -> Optional[SessionsGroup]: ...
  @property
  def files(self) -> Optional[MetorialFilesEndpoint]: ...
  @property
  def links(self) -> Optional[MetorialLinksEndpoint]: ...
  @property
  def oauth(self) -> Optional[ProviderOauthGroup]: ...
