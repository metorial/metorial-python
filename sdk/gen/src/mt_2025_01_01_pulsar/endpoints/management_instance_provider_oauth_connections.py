from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderOauthConnectionsListOutput, DashboardInstanceProviderOauthConnectionsListOutput, mapDashboardInstanceProviderOauthConnectionsListQuery, DashboardInstanceProviderOauthConnectionsListQuery, mapDashboardInstanceProviderOauthConnectionsCreateOutput, DashboardInstanceProviderOauthConnectionsCreateOutput, mapDashboardInstanceProviderOauthConnectionsCreateBody, DashboardInstanceProviderOauthConnectionsCreateBody, mapDashboardInstanceProviderOauthConnectionsGetOutput, DashboardInstanceProviderOauthConnectionsGetOutput, mapDashboardInstanceProviderOauthConnectionsUpdateOutput, DashboardInstanceProviderOauthConnectionsUpdateOutput, mapDashboardInstanceProviderOauthConnectionsUpdateBody, DashboardInstanceProviderOauthConnectionsUpdateBody, mapDashboardInstanceProviderOauthConnectionsDeleteOutput, DashboardInstanceProviderOauthConnectionsDeleteOutput

class MetorialManagementInstanceProviderOauthConnectionsEndpoint(BaseMetorialEndpoint):
    """Manage provider OAuth connection information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, query: DashboardInstanceProviderOauthConnectionsListQuery = None):
        """
    List provider OAuth connections
    List all provider OAuth connections

    :param instanceId: str
    :param query: DashboardInstanceProviderOauthConnectionsListQuery
    :return: DashboardInstanceProviderOauthConnectionsListOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections'],
            query=mapDashboardInstanceProviderOauthConnectionsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceProviderOauthConnectionsListOutput.from_dict)

    def create(self, instanceId: str, body: DashboardInstanceProviderOauthConnectionsCreateBody):
        """
    Create provider OAuth connection
    Create a new provider OAuth connection

    :param instanceId: str
    :param body: DashboardInstanceProviderOauthConnectionsCreateBody
    :return: DashboardInstanceProviderOauthConnectionsCreateOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections'],
            body=mapDashboardInstanceProviderOauthConnectionsCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardInstanceProviderOauthConnectionsCreateOutput.from_dict)

    def get(self, instanceId: str, connectionId: str):
        """
    Get provider OAuth connection
    Get information for a specific provider OAuth connection

    :param instanceId: str
    :param connectionId: str
    :return: DashboardInstanceProviderOauthConnectionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections', connectionId]
        )
        return self._get(request).transform(mapDashboardInstanceProviderOauthConnectionsGetOutput.from_dict)

    def update(self, instanceId: str, connectionId: str, body: DashboardInstanceProviderOauthConnectionsUpdateBody):
        """
    Update provider OAuth connection
    Update a provider OAuth connection

    :param instanceId: str
    :param connectionId: str
    :param body: DashboardInstanceProviderOauthConnectionsUpdateBody
    :return: DashboardInstanceProviderOauthConnectionsUpdateOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections', connectionId],
            body=mapDashboardInstanceProviderOauthConnectionsUpdateBody.to_dict(body),
        )
        return self._patch(request).transform(mapDashboardInstanceProviderOauthConnectionsUpdateOutput.from_dict)

    def delete(self, instanceId: str, connectionId: str):
        """
    Delete provider OAuth connection
    Delete a provider OAuth connection

    :param instanceId: str
    :param connectionId: str
    :return: DashboardInstanceProviderOauthConnectionsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'provider-oauth', 'connections', connectionId]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderOauthConnectionsDeleteOutput.from_dict)