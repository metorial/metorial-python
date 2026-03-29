from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsServiceAccountsClientSecretsCreateOutput, DashboardOrganizationsServiceAccountsClientSecretsCreateOutput, mapDashboardOrganizationsServiceAccountsClientSecretsDeleteOutput, DashboardOrganizationsServiceAccountsClientSecretsDeleteOutput

class MetorialManagementOrganizationServiceAccountsClientSecretsEndpoint(BaseMetorialEndpoint):
    """Create and manage service accounts for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, service_account_id: str) -> DashboardOrganizationsServiceAccountsClientSecretsCreateOutput:
        """
    Create service account client secret
    Creates a new client secret for a service account.

    :param service_account_id: str
    :return: DashboardOrganizationsServiceAccountsClientSecretsCreateOutput
    """
        request = MetorialRequest(
            path=['organization', 'service-accounts', service_account_id, 'client-secrets']
        )
        return self._post(request).transform(mapDashboardOrganizationsServiceAccountsClientSecretsCreateOutput.from_dict)

    def delete(self, service_account_id: str, oauth_application_client_secret_id: str) -> DashboardOrganizationsServiceAccountsClientSecretsDeleteOutput:
        """
    Delete service account client secret
    Deletes a client secret from a service account.

    :param service_account_id: str
    :param oauth_application_client_secret_id: str
    :return: DashboardOrganizationsServiceAccountsClientSecretsDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'service-accounts', service_account_id, 'client-secrets', oauth_application_client_secret_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsServiceAccountsClientSecretsDeleteOutput.from_dict)