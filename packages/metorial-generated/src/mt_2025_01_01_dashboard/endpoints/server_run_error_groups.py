from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServerRunErrorGroupsListOutput, DashboardInstanceServerRunErrorGroupsListOutput, mapDashboardInstanceServerRunErrorGroupsListQuery, DashboardInstanceServerRunErrorGroupsListQuery, mapDashboardInstanceServerRunErrorGroupsGetOutput, DashboardInstanceServerRunErrorGroupsGetOutput

class MetorialServerRunErrorGroupsEndpoint(BaseMetorialEndpoint):
    """Read and write server run error group information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: DashboardInstanceServerRunErrorGroupsListQuery = None):
        """
    List server run error groups
    List all server run error groups

    :param query: DashboardInstanceServerRunErrorGroupsListQuery
    :return: DashboardInstanceServerRunErrorGroupsListOutput
    """
        request = MetorialRequest(
            path=['server-run-error-groups'],
            query=mapDashboardInstanceServerRunErrorGroupsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServerRunErrorGroupsListOutput.from_dict)

    def get(self, serverRunErrorGroupId: str):
        """
    Get server run error group
    Get the information of a specific server run error group

    :param serverRunErrorGroupId: str
    :return: DashboardInstanceServerRunErrorGroupsGetOutput
    """
        request = MetorialRequest(
            path=['server-run-error-groups', serverRunErrorGroupId]
        )
        return self._get(request).transform(mapDashboardInstanceServerRunErrorGroupsGetOutput.from_dict)