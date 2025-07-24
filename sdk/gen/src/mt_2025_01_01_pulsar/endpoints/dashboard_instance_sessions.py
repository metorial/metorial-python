from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsListOutput, DashboardInstanceSessionsListOutput, mapDashboardInstanceSessionsListQuery, DashboardInstanceSessionsListQuery, mapDashboardInstanceSessionsGetOutput, DashboardInstanceSessionsGetOutput, mapDashboardInstanceSessionsCreateOutput, DashboardInstanceSessionsCreateOutput, mapDashboardInstanceSessionsCreateBody, DashboardInstanceSessionsCreateBody, mapDashboardInstanceSessionsDeleteOutput, DashboardInstanceSessionsDeleteOutput

class MetorialDashboardInstanceSessionsEndpoint(BaseMetorialEndpoint):
    """Before you can connect to an MCP server, you need to create a session. Each session can be linked to one or more server deployments, allowing you to connect to multiple servers simultaneously. Once you have created a session, you can use the provided MCP URL to connect to the server deployments via MCP."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, query: DashboardInstanceSessionsListQuery = None):
        """
    List sessions
    List all sessions

    :param instanceId: str
    :param query: DashboardInstanceSessionsListQuery
    :return: DashboardInstanceSessionsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'sessions'],
            query=mapDashboardInstanceSessionsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceSessionsListOutput.from_dict)

    def get(self, instanceId: str, sessionId: str):
        """
    Get session
    Get the information of a specific session

    :param instanceId: str
    :param sessionId: str
    :return: DashboardInstanceSessionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'sessions', sessionId]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsGetOutput.from_dict)

    def create(self, instanceId: str, body: DashboardInstanceSessionsCreateBody):
        """
    Create session
    Create a new session

    :param instanceId: str
    :param body: DashboardInstanceSessionsCreateBody
    :return: DashboardInstanceSessionsCreateOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'sessions'],
            body=mapDashboardInstanceSessionsCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardInstanceSessionsCreateOutput.from_dict)

    def delete(self, instanceId: str, sessionId: str):
        """
    Delete session
    Delete a session

    :param instanceId: str
    :param sessionId: str
    :return: DashboardInstanceSessionsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'sessions', sessionId]
        )
        return self._delete(request).transform(mapDashboardInstanceSessionsDeleteOutput.from_dict)