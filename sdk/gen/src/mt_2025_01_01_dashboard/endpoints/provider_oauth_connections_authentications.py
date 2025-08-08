from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutput, DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput, mapDashboardInstanceProviderOauthConnectionsAuthenticationsListQuery, DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery, mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput, DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput

class MetorialProviderOauthConnectionsAuthenticationsEndpoint(BaseMetorialEndpoint):
    """Manage provider OAuth connection authentication information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, connectionId: str, query: DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery = None):
        """
    List provider OAuth connection authentications
    List provider OAuth connection authentications for a specific connection

    :param connectionId: str
    :param query: DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery
    :return: DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput
    """
        request = MetorialRequest(
            path=['provider-oauth', 'connections', connectionId, 'authentications'],
            query=mapDashboardInstanceProviderOauthConnectionsAuthenticationsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutput.from_dict)

    def get(self, connectionId: str, authenticationId: str):
        """
    Get provider OAuth connection authentication
    Get the information of a specific provider OAuth connection authentication

    :param connectionId: str
    :param authenticationId: str
    :return: DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput
    """
        request = MetorialRequest(
            path=['provider-oauth', 'connections', connectionId, 'authentications', authenticationId]
        )
        return self._get(request).transform(mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput.from_dict)