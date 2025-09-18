from metorial_core.metorial import Metorial as _Metorial
from metorial_core.typed_endpoints import (
  TypedMetorialServersEndpoint,
  TypedMetorialSessionsEndpoint,
)

from mt_2025_01_01_pulsar.endpoints.secrets import MetorialSecretsEndpoint
from mt_2025_01_01_pulsar.endpoints.files import MetorialFilesEndpoint
from mt_2025_01_01_pulsar.endpoints.links import MetorialLinksEndpoint
from mt_2025_01_01_pulsar.endpoints.instance import MetorialInstanceEndpoint

class Metorial(_Metorial):
  """Metorial SDK client with full type annotations"""

  # Main endpoint groups
  servers: TypedMetorialServersEndpoint
  secrets: MetorialSecretsEndpoint
  files: MetorialFilesEndpoint
  sessions: TypedMetorialSessionsEndpoint
  instance: MetorialInstanceEndpoint
  links: MetorialLinksEndpoint
