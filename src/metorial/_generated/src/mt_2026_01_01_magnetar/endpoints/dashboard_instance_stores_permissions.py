from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceStoresPermissionsGetOutput, DashboardInstanceStoresPermissionsGetOutput

class MetorialDashboardInstanceStoresPermissionsEndpoint(BaseMetorialEndpoint):
    """Create and manage instance stores backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, store_id: str) -> DashboardInstanceStoresPermissionsGetOutput:
        """
    Get store permissions
    Returns the effective Cargo permissions for the current actor on a specific store.

    :param instance_id: str
    :param store_id: str
    :return: DashboardInstanceStoresPermissionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'stores', store_id, 'permissions']
        )
        return self._get(request).transform(mapDashboardInstanceStoresPermissionsGetOutput.from_dict)