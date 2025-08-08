from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServersVariantsListOutput, DashboardInstanceServersVariantsListOutput, mapDashboardInstanceServersVariantsListQuery, DashboardInstanceServersVariantsListQuery, mapDashboardInstanceServersVariantsGetOutput, DashboardInstanceServersVariantsGetOutput

class MetorialDashboardInstanceServersVariantsEndpoint(BaseMetorialEndpoint):
    """Server variants define different instances of a server, each with its own configuration and capabilities. By default, Metorial picks the best variant automatically, but you can specify a variant if needed."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, serverId: str, query: DashboardInstanceServersVariantsListQuery = None):
        """
    List server variants
    Retrieve all variants for a given server

    :param instanceId: str
    :param serverId: str
    :param query: DashboardInstanceServersVariantsListQuery
    :return: DashboardInstanceServersVariantsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'servers', serverId, 'variants'],
            query=mapDashboardInstanceServersVariantsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServersVariantsListOutput.from_dict)

    def get(self, instanceId: str, serverId: str, serverVariantId: str):
        """
    Get server variant
    Retrieve details for a specific server variant

    :param instanceId: str
    :param serverId: str
    :param serverVariantId: str
    :return: DashboardInstanceServersVariantsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instanceId, 'servers', serverId, 'variants', serverVariantId]
        )
        return self._get(request).transform(mapDashboardInstanceServersVariantsGetOutput.from_dict)