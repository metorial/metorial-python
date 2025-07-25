from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServerRunErrorsListOutput, DashboardInstanceServerRunErrorsListOutput, mapDashboardInstanceServerRunErrorsListQuery, DashboardInstanceServerRunErrorsListQuery, mapDashboardInstanceServerRunErrorsGetOutput, DashboardInstanceServerRunErrorsGetOutput

class MetorialDashboardInstanceServerRunErrorsEndpoint(BaseMetorialEndpoint):
    """Sometimes, an MCP server may fail to run correctly, resulting in an error. Metorial captures these errors to help you diagnose issues with your server runs. You may also want to check the Metorial dashboard for more details on the error."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, query: DashboardInstanceServerRunErrorsListQuery = None):
        """
    List server run errors
    List all server run errors

    :param instanceId: str
    :param query: DashboardInstanceServerRunErrorsListQuery
    :return: DashboardInstanceServerRunErrorsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'server-run-errors'],
            query=mapDashboardInstanceServerRunErrorsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServerRunErrorsListOutput.from_dict)

    def get(self, instanceId: str, serverRunErrorId: str):
        """
    Get server run error
    Get the information of a specific server run error

    :param instanceId: str
    :param serverRunErrorId: str
    :return: DashboardInstanceServerRunErrorsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'server-run-errors', serverRunErrorId]
        )
        return self._get(request).transform(mapDashboardInstanceServerRunErrorsGetOutput.from_dict)