from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthScopesListOutput, DashboardOrganizationsOauthScopesListOutput

class MetorialManagementOrganizationOauthScopesEndpoint(BaseMetorialEndpoint):
    """Read all OAuth scopes that can be requested by organization applications"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self) -> DashboardOrganizationsOauthScopesListOutput:
        """
    List OAuth scopes
    Returns all available OAuth scopes that organization-owned OAuth applications may request.


    :return: DashboardOrganizationsOauthScopesListOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'scopes']
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthScopesListOutput.from_dict)