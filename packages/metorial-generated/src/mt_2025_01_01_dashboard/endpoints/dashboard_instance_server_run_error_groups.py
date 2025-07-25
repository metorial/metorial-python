from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServerRunErrorGroupsListOutput, DashboardInstanceServerRunErrorGroupsListOutput, mapDashboardInstanceServerRunErrorGroupsListQuery, DashboardInstanceServerRunErrorGroupsListQuery, mapDashboardInstanceServerRunErrorGroupsGetOutput, DashboardInstanceServerRunErrorGroupsGetOutput

class MetorialDashboardInstanceServerRunErrorGroupsEndpoint(BaseMetorialEndpoint):
    """Read and write server run error group information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, query: DashboardInstanceServerRunErrorGroupsListQuery = None):
        """
    List server run error groups
    List all server run error groups

    :param instanceId: str
    :param query: DashboardInstanceServerRunErrorGroupsListQuery
    :return: DashboardInstanceServerRunErrorGroupsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'server-run-error-groups'],
            query=mapDashboardInstanceServerRunErrorGroupsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServerRunErrorGroupsListOutput.from_dict)

    def get(self, instanceId: str, serverRunErrorGroupId: str):
        """
    Get server run error group
    Get the information of a specific server run error group

    :param instanceId: str
    :param serverRunErrorGroupId: str
    :return: DashboardInstanceServerRunErrorGroupsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'server-run-error-groups', serverRunErrorGroupId]
        )
        return self._get(request).transform(mapDashboardInstanceServerRunErrorGroupsGetOutput.from_dict)