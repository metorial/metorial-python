from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthScopesListOutput, DashboardOrganizationsOauthScopesListOutput

class MetorialDashboardOrganizationsOauthScopesEndpoint(BaseMetorialEndpoint):
    """Read all OAuth scopes that can be requested by organization applications"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str) -> DashboardOrganizationsOauthScopesListOutput:
        """
    List OAuth scopes
    Returns all available OAuth scopes that organization-owned OAuth applications may request.

    :param organization_id: str
    :return: DashboardOrganizationsOauthScopesListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'oauth', 'scopes']
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthScopesListOutput.from_dict)