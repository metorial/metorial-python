from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsEventsListOutput, DashboardInstanceSessionsEventsListOutput, mapDashboardInstanceSessionsEventsListQuery, DashboardInstanceSessionsEventsListQuery, mapDashboardInstanceSessionsEventsGetOutput, DashboardInstanceSessionsEventsGetOutput

class MetorialManagementInstanceSessionsEventsEndpoint(BaseMetorialEndpoint):
    """Read and write session event information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, sessionId: str, query: DashboardInstanceSessionsEventsListQuery = None):
        """
    List session events
    List all events for a specific session

    :param instanceId: str
    :param sessionId: str
    :param query: DashboardInstanceSessionsEventsListQuery
    :return: DashboardInstanceSessionsEventsListOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'sessions', sessionId, 'events'],
            query=mapDashboardInstanceSessionsEventsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceSessionsEventsListOutput.from_dict)

    def get(self, instanceId: str, sessionId: str, sessionEventId: str):
        """
    Get session event
    Get details of a specific session event

    :param instanceId: str
    :param sessionId: str
    :param sessionEventId: str
    :return: DashboardInstanceSessionsEventsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'sessions', sessionId, 'events', sessionEventId]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsEventsGetOutput.from_dict)