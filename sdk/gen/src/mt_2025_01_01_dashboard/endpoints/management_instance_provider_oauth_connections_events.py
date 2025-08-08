from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderOauthConnectionsEventsListOutput, DashboardInstanceProviderOauthConnectionsEventsListOutput, mapDashboardInstanceProviderOauthConnectionsEventsListQuery, DashboardInstanceProviderOauthConnectionsEventsListQuery, mapDashboardInstanceProviderOauthConnectionsEventsGetOutput, DashboardInstanceProviderOauthConnectionsEventsGetOutput

class MetorialManagementInstanceProviderOauthConnectionsEventsEndpoint(BaseMetorialEndpoint):
    """Manage provider OAuth connection event information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, connectionId: str, query: DashboardInstanceProviderOauthConnectionsEventsListQuery = None):
        """
    List provider OAuth connection events
    List provider OAuth connection events for a specific connection

    :param instanceId: str
    :param connectionId: str
    :param query: DashboardInstanceProviderOauthConnectionsEventsListQuery
    :return: DashboardInstanceProviderOauthConnectionsEventsListOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections', connectionId, 'events'],
            query=mapDashboardInstanceProviderOauthConnectionsEventsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceProviderOauthConnectionsEventsListOutput.from_dict)

    def get(self, instanceId: str, connectionId: str, eventId: str):
        """
    Get provider OAuth connection event
    Get the information of a specific provider OAuth connection event

    :param instanceId: str
    :param connectionId: str
    :param eventId: str
    :return: DashboardInstanceProviderOauthConnectionsEventsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections', connectionId, 'events', eventId]
        )
        return self._get(request).transform(mapDashboardInstanceProviderOauthConnectionsEventsGetOutput.from_dict)