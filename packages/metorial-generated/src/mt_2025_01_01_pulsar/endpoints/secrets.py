from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSecretsListOutput, DashboardInstanceSecretsListOutput, mapDashboardInstanceSecretsListQuery, DashboardInstanceSecretsListQuery, mapDashboardInstanceSecretsGetOutput, DashboardInstanceSecretsGetOutput

class MetorialSecretsEndpoint(BaseMetorialEndpoint):
    """Secrets represent sensitive information securely stored by Metorial. Secrets are automatically created by Metorial, for example for server deployment configurations."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: DashboardInstanceSecretsListQuery = None):
        """
    List secrets
    Returns a paginated list of secrets for the instance, optionally filtered by type or status.

    :param query: DashboardInstanceSecretsListQuery
    :return: DashboardInstanceSecretsListOutput
    """
        request = MetorialRequest(
            path=['secrets'],
            query=mapDashboardInstanceSecretsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceSecretsListOutput.from_dict)

    def get(self, secretId: str):
        """
    Get secret by ID
    Retrieves detailed information about a specific secret by ID.

    :param secretId: str
    :return: DashboardInstanceSecretsGetOutput
    """
        request = MetorialRequest(
            path=['secrets', secretId]
        )
        return self._get(request).transform(mapDashboardInstanceSecretsGetOutput.from_dict)