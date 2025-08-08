from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServersCapabilitiesListOutput, DashboardInstanceServersCapabilitiesListOutput, mapDashboardInstanceServersCapabilitiesListQuery, DashboardInstanceServersCapabilitiesListQuery

class MetorialServersCapabilitiesEndpoint(BaseMetorialEndpoint):
    """Describes the capabilities, i.e., the tools, resources, and prompts, that certain servers support."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: DashboardInstanceServersCapabilitiesListQuery = None):
        """
    List server capabilities
    Returns a list of server capabilities, filterable by server attributes such as deployment, variant, or version.

    :param query: DashboardInstanceServersCapabilitiesListQuery
    :return: DashboardInstanceServersCapabilitiesListOutput
    """
        request = MetorialRequest(
            path=['server-capabilities'],
            query=mapDashboardInstanceServersCapabilitiesListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServersCapabilitiesListOutput.from_dict)