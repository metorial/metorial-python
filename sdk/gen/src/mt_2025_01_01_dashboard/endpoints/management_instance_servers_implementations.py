from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServersImplementationsListOutput, DashboardInstanceServersImplementationsListOutput, mapDashboardInstanceServersImplementationsListQuery, DashboardInstanceServersImplementationsListQuery, mapDashboardInstanceServersImplementationsGetOutput, DashboardInstanceServersImplementationsGetOutput, mapDashboardInstanceServersImplementationsCreateOutput, DashboardInstanceServersImplementationsCreateOutput, mapDashboardInstanceServersImplementationsCreateBody, DashboardInstanceServersImplementationsCreateBody, mapDashboardInstanceServersImplementationsUpdateOutput, DashboardInstanceServersImplementationsUpdateOutput, mapDashboardInstanceServersImplementationsUpdateBody, DashboardInstanceServersImplementationsUpdateBody, mapDashboardInstanceServersImplementationsDeleteOutput, DashboardInstanceServersImplementationsDeleteOutput

class MetorialManagementInstanceServersImplementationsEndpoint(BaseMetorialEndpoint):
    """Server implementations allow you to customize predefined MCP servers with specific configurations, launch parameters, and metadata. You can create server deployments based on these implementations to connect to the underlying MCP servers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, query: DashboardInstanceServersImplementationsListQuery = None):
        """
    List server implementations
    Retrieve all server implementations in the instance. Supports filtering by status, server, or variant.

    :param instanceId: str
    :param query: DashboardInstanceServersImplementationsListQuery
    :return: DashboardInstanceServersImplementationsListOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'server-implementations'],
            query=mapDashboardInstanceServersImplementationsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServersImplementationsListOutput.from_dict)

    def get(self, instanceId: str, serverImplementationId: str):
        """
    Get server implementation
    Fetch detailed information about a specific server implementation.

    :param instanceId: str
    :param serverImplementationId: str
    :return: DashboardInstanceServersImplementationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'server-implementations', serverImplementationId]
        )
        return self._get(request).transform(mapDashboardInstanceServersImplementationsGetOutput.from_dict)

    def create(self, instanceId: str, body: DashboardInstanceServersImplementationsCreateBody):
        """
    Create server implementation
    Create a new server implementation for a specific server or server variant.

    :param instanceId: str
    :param body: DashboardInstanceServersImplementationsCreateBody
    :return: DashboardInstanceServersImplementationsCreateOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'server-implementations'],
            body=mapDashboardInstanceServersImplementationsCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardInstanceServersImplementationsCreateOutput.from_dict)

    def update(self, instanceId: str, serverImplementationId: str, body: DashboardInstanceServersImplementationsUpdateBody):
        """
    Update server implementation
    Update metadata, launch parameters, or other fields of a server implementation.

    :param instanceId: str
    :param serverImplementationId: str
    :param body: DashboardInstanceServersImplementationsUpdateBody
    :return: DashboardInstanceServersImplementationsUpdateOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'server-implementations', serverImplementationId],
            body=mapDashboardInstanceServersImplementationsUpdateBody.to_dict(body),
        )
        return self._patch(request).transform(mapDashboardInstanceServersImplementationsUpdateOutput.from_dict)

    def delete(self, instanceId: str, serverImplementationId: str):
        """
    Delete server implementation
    Delete a specific server implementation from the instance.

    :param instanceId: str
    :param serverImplementationId: str
    :return: DashboardInstanceServersImplementationsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'server-implementations', serverImplementationId]
        )
        return self._delete(request).transform(mapDashboardInstanceServersImplementationsDeleteOutput.from_dict)