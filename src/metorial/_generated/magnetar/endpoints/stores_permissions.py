from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceStoresPermissionsGetOutput, DashboardInstanceStoresPermissionsGetOutput

class MetorialStoresPermissionsEndpoint(BaseMetorialEndpoint):
    """A store is a shared collection of files and documents. Participants get read or write access to its contents."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, store_id: str) -> DashboardInstanceStoresPermissionsGetOutput:
        """
    Get store permissions
    Returns what the caller can do with a store.

    :param store_id: str
    :return: DashboardInstanceStoresPermissionsGetOutput
    """
        request = MetorialRequest(
            path=['stores', store_id, 'permissions']
        )
        return self._get(request).transform(mapDashboardInstanceStoresPermissionsGetOutput.from_dict)