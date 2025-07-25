from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSecretsListOutput, DashboardInstanceSecretsListOutput, mapDashboardInstanceSecretsListQuery, DashboardInstanceSecretsListQuery, mapDashboardInstanceSecretsGetOutput, DashboardInstanceSecretsGetOutput

class MetorialManagementInstanceSecretsEndpoint(BaseMetorialEndpoint):
    """Secrets represent sensitive information securely stored by Metorial. Secrets are automatically created by Metorial, for example for server deployment configurations."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, query: DashboardInstanceSecretsListQuery = None):
        """
    List secrets
    Returns a paginated list of secrets for the instance, optionally filtered by type or status.

    :param instanceId: str
    :param query: DashboardInstanceSecretsListQuery
    :return: DashboardInstanceSecretsListOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'secrets'],
            query=mapDashboardInstanceSecretsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceSecretsListOutput.from_dict)

    def get(self, instanceId: str, secretId: str):
        """
    Get secret by ID
    Retrieves detailed information about a specific secret by ID.

    :param instanceId: str
    :param secretId: str
    :return: DashboardInstanceSecretsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'secrets', secretId]
        )
        return self._get(request).transform(mapDashboardInstanceSecretsGetOutput.from_dict)