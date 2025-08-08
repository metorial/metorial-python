from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceInstanceGetOutput, DashboardInstanceInstanceGetOutput

class MetorialInstanceEndpoint(BaseMetorialEndpoint):
    """Instances are independent environments within Metorial, each with its own configuration and data. Each instance is a port of a Metorial project. You can for example create production, staging, and development instances for your project."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self):
        """
    Get instance details
    Retrieves metadata and configuration details for a specific instance.


    :return: DashboardInstanceInstanceGetOutput
    """
        request = MetorialRequest(
            path=['instance']
        )
        return self._get(request).transform(mapDashboardInstanceInstanceGetOutput.from_dict)