from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthAppsClientSecretsCreateOutput, DashboardOrganizationsOauthAppsClientSecretsCreateOutput, mapDashboardOrganizationsOauthAppsClientSecretsDeleteOutput, DashboardOrganizationsOauthAppsClientSecretsDeleteOutput

class MetorialManagementOrganizationOauthAppsClientSecretsEndpoint(BaseMetorialEndpoint):
    """Create and manage OAuth applications for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, oauth_application_id: str) -> DashboardOrganizationsOauthAppsClientSecretsCreateOutput:
        """
    Create OAuth application client secret
    Creates a new client secret for an OAuth application.

    :param oauth_application_id: str
    :return: DashboardOrganizationsOauthAppsClientSecretsCreateOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'apps', oauth_application_id, 'client-secrets']
        )
        return self._post(request).transform(mapDashboardOrganizationsOauthAppsClientSecretsCreateOutput.from_dict)

    def delete(self, oauth_application_id: str, oauth_application_client_secret_id: str) -> DashboardOrganizationsOauthAppsClientSecretsDeleteOutput:
        """
    Delete OAuth application client secret
    Deletes a client secret from an OAuth application.

    :param oauth_application_id: str
    :param oauth_application_client_secret_id: str
    :return: DashboardOrganizationsOauthAppsClientSecretsDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'apps', oauth_application_id, 'client-secrets', oauth_application_client_secret_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsOauthAppsClientSecretsDeleteOutput.from_dict)