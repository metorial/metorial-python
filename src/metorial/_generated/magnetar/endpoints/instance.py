from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceInstanceGetOutput, DashboardInstanceInstanceGetOutput

class MetorialInstanceEndpoint(BaseMetorialEndpoint):
    """An instance is an isolated environment within a Metorial project. Instances are created via the dashboard (since API keys are scoped to instances). Common setups include production, staging, and development instances."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> DashboardInstanceInstanceGetOutput:
        """
    Get instance details
    Retrieves metadata and configuration details for a specific instance.


    :return: DashboardInstanceInstanceGetOutput
    """
        request = MetorialRequest(
            path=['instance']
        )
        return self._get(request).transform(mapDashboardInstanceInstanceGetOutput.from_dict)