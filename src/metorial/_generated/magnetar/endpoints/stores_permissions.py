from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceStoresPermissionsGetOutput, DashboardInstanceStoresPermissionsGetOutput

class MetorialStoresPermissionsEndpoint(BaseMetorialEndpoint):
    """Create and manage instance stores backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, store_id: str) -> DashboardInstanceStoresPermissionsGetOutput:
        """
    Get store permissions
    Returns the effective Cargo permissions for the current actor on a specific store.

    :param store_id: str
    :return: DashboardInstanceStoresPermissionsGetOutput
    """
        request = MetorialRequest(
            path=['stores', store_id, 'permissions']
        )
        return self._get(request).transform(mapDashboardInstanceStoresPermissionsGetOutput.from_dict)