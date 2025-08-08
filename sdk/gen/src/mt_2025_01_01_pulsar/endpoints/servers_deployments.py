from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceServersDeploymentsListOutput, DashboardInstanceServersDeploymentsListOutput, mapDashboardInstanceServersDeploymentsListQuery, DashboardInstanceServersDeploymentsListQuery, mapDashboardInstanceServersDeploymentsGetOutput, DashboardInstanceServersDeploymentsGetOutput, mapDashboardInstanceServersDeploymentsCreateOutput, DashboardInstanceServersDeploymentsCreateOutput, mapDashboardInstanceServersDeploymentsCreateBody, DashboardInstanceServersDeploymentsCreateBody, mapDashboardInstanceServersDeploymentsUpdateOutput, DashboardInstanceServersDeploymentsUpdateOutput, mapDashboardInstanceServersDeploymentsUpdateBody, DashboardInstanceServersDeploymentsUpdateBody, mapDashboardInstanceServersDeploymentsDeleteOutput, DashboardInstanceServersDeploymentsDeleteOutput

class MetorialServersDeploymentsEndpoint(BaseMetorialEndpoint):
    """A server deployment represents a specific instance of an MCP server that can be connected to. It contains configuration for the MCP server, such as API keys for the underlying MCP server."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: DashboardInstanceServersDeploymentsListQuery = None):
        """
    List server deployments
    Retrieve a list of server deployments within the instance. Supports filtering by status, server, variant, and session.

    :param query: DashboardInstanceServersDeploymentsListQuery
    :return: DashboardInstanceServersDeploymentsListOutput
    """
        request = MetorialRequest(
            path=['server-deployments'],
            query=mapDashboardInstanceServersDeploymentsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardInstanceServersDeploymentsListOutput.from_dict)

    def get(self, serverDeploymentId: str):
        """
    Get server deployment
    Fetch detailed information about a specific server deployment.

    :param serverDeploymentId: str
    :return: DashboardInstanceServersDeploymentsGetOutput
    """
        request = MetorialRequest(
            path=['server-deployments', serverDeploymentId]
        )
        return self._get(request).transform(mapDashboardInstanceServersDeploymentsGetOutput.from_dict)

    def create(self, body: DashboardInstanceServersDeploymentsCreateBody):
        """
    Create server deployment
    Create a new server deployment using an existing or newly defined server implementation.

    :param body: DashboardInstanceServersDeploymentsCreateBody
    :return: DashboardInstanceServersDeploymentsCreateOutput
    """
        request = MetorialRequest(
            path=['server-deployments'],
            body=mapDashboardInstanceServersDeploymentsCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardInstanceServersDeploymentsCreateOutput.from_dict)

    def update(self, serverDeploymentId: str, body: DashboardInstanceServersDeploymentsUpdateBody):
        """
    Update server deployment
    Update metadata, configuration, or other properties of a server deployment.

    :param serverDeploymentId: str
    :param body: DashboardInstanceServersDeploymentsUpdateBody
    :return: DashboardInstanceServersDeploymentsUpdateOutput
    """
        request = MetorialRequest(
            path=['server-deployments', serverDeploymentId],
            body=mapDashboardInstanceServersDeploymentsUpdateBody.to_dict(body),
        )
        return self._patch(request).transform(mapDashboardInstanceServersDeploymentsUpdateOutput.from_dict)

    def delete(self, serverDeploymentId: str):
        """
    Delete server deployment
    Delete a server deployment from the instance.

    :param serverDeploymentId: str
    :return: DashboardInstanceServersDeploymentsDeleteOutput
    """
        request = MetorialRequest(
            path=['server-deployments', serverDeploymentId]
        )
        return self._delete(request).transform(mapDashboardInstanceServersDeploymentsDeleteOutput.from_dict)