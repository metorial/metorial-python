from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAuthAppGetOutput, DashboardInstancePortalsAuthAppGetOutput

class MetorialPortalsAuthAppEndpoint(BaseMetorialEndpoint):
    """Manage the Ares-backed authentication configuration for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, portal_id: str) -> DashboardInstancePortalsAuthAppGetOutput:
        """
    Get portal auth app
    Returns the Ares app configuration for a portal.

    :param portal_id: str
    :return: DashboardInstancePortalsAuthAppGetOutput
    """
        request = MetorialRequest(
            path=['portals', portal_id, 'auth', 'app']
        )
        return self._get(request).transform(mapDashboardInstancePortalsAuthAppGetOutput.from_dict)