from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAuthAppGetOutput, DashboardInstancePortalsAuthAppGetOutput

class MetorialManagementInstancePortalsAuthAppEndpoint(BaseMetorialEndpoint):
    """Manage the Ares-backed authentication configuration for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, portal_id: str) -> DashboardInstancePortalsAuthAppGetOutput:
        """
    Get portal auth app
    Returns the Ares app configuration for a portal.

    :param instance_id: str
    :param portal_id: str
    :return: DashboardInstancePortalsAuthAppGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'auth', 'app']
        )
        return self._get(request).transform(mapDashboardInstancePortalsAuthAppGetOutput.from_dict)