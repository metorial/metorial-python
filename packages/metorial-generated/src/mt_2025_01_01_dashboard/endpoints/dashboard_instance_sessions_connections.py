from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsConnectionsListOutput, DashboardInstanceSessionsConnectionsListOutput, mapDashboardInstanceSessionsConnectionsListQuery, DashboardInstanceSessionsConnectionsListQuery, mapDashboardInstanceSessionsConnectionsGetOutput, DashboardInstanceSessionsConnectionsGetOutput

class MetorialDashboardInstanceSessionsConnectionsEndpoint(BaseMetorialEndpoint):
    """Each time a new MCP connection to a server is established, a session connection is created. This allows you to track and manage the connections made during a session."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, sessionId: str, query: DashboardInstanceSessionsConnectionsListQuery = None):
        """
    List session connections
    List all session connections

    :param instanceId: str
    :param sessionId: str
    :param query: DashboardInstanceSessionsConnectionsListQuery
    :return: DashboardInstanceSessionsConnectionsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'sessions', sessionId, 'connections'],
            query=mapDashboardInstanceSessionsConnectionsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceSessionsConnectionsListOutput.from_dict)

    def get(self, instanceId: str, sessionId: str, sessionConnectionId: str):
        """
    Get session connection
    Get the information of a specific session connection

    :param instanceId: str
    :param sessionId: str
    :param sessionConnectionId: str
    :return: DashboardInstanceSessionsConnectionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'sessions', sessionId, 'connections', sessionConnectionId]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsConnectionsGetOutput.from_dict)