from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceInstanceGetOutput,
  DashboardInstanceInstanceGetOutput,
)


class MetorialDashboardInstanceInstanceEndpoint(BaseMetorialEndpoint):
  """Instances are independent environments within Metorial, each with its own configuration and data. Each instance is a port of a Metorial project. You can for example create production, staging, and development instances for your project."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(self, instance_id: str) -> DashboardInstanceInstanceGetOutput:
    """
    Get instance details
    Retrieves metadata and configuration details for a specific instance.

    :param instance_id: str
    :return: DashboardInstanceInstanceGetOutput
    """
    request = MetorialRequest(path=["dashboard", "instances", instance_id, "instance"])
    return self._get(request).transform(mapDashboardInstanceInstanceGetOutput.from_dict)
