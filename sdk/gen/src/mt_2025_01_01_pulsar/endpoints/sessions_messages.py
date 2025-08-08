from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsMessagesListOutput, DashboardInstanceSessionsMessagesListOutput, mapDashboardInstanceSessionsMessagesListQuery, DashboardInstanceSessionsMessagesListQuery, mapDashboardInstanceSessionsMessagesGetOutput, DashboardInstanceSessionsMessagesGetOutput

class MetorialSessionsMessagesEndpoint(BaseMetorialEndpoint):
    """When MCP servers and clients communicate, Metorial captures the messages they send. This allows you to see the raw messages exchanged between the server and client, which can be useful for debugging or understanding the communication flow."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, sessionId: str, query: DashboardInstanceSessionsMessagesListQuery = None):
        """
    List session messages
    List all messages for a specific session

    :param sessionId: str
    :param query: DashboardInstanceSessionsMessagesListQuery
    :return: DashboardInstanceSessionsMessagesListOutput
    """
        request = MetorialRequest(
            path=['sessions', sessionId, 'messages'],
            query=mapDashboardInstanceSessionsMessagesListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceSessionsMessagesListOutput.from_dict)

    def get(self, sessionId: str, sessionMessageId: str):
        """
    Get session message
    Get details of a specific session message

    :param sessionId: str
    :param sessionMessageId: str
    :return: DashboardInstanceSessionsMessagesGetOutput
    """
        request = MetorialRequest(
            path=['sessions', sessionId, 'messages', sessionMessageId]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsMessagesGetOutput.from_dict)