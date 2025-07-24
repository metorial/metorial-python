from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsInstancesListOutput, DashboardOrganizationsInstancesListOutput, mapDashboardOrganizationsInstancesListQuery, DashboardOrganizationsInstancesListQuery, mapDashboardOrganizationsInstancesGetOutput, DashboardOrganizationsInstancesGetOutput, mapDashboardOrganizationsInstancesCreateOutput, DashboardOrganizationsInstancesCreateOutput, mapDashboardOrganizationsInstancesCreateBody, DashboardOrganizationsInstancesCreateBody, mapDashboardOrganizationsInstancesDeleteOutput, DashboardOrganizationsInstancesDeleteOutput, mapDashboardOrganizationsInstancesUpdateOutput, DashboardOrganizationsInstancesUpdateOutput, mapDashboardOrganizationsInstancesUpdateBody, DashboardOrganizationsInstancesUpdateBody

class MetorialManagementOrganizationInstancesEndpoint(BaseMetorialEndpoint):
    """Read and write instance information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: DashboardOrganizationsInstancesListQuery = None):
        """
    List organization instances
    List all organization instances

    :param query: DashboardOrganizationsInstancesListQuery
    :return: DashboardOrganizationsInstancesListOutput
    """
        request = MetorialRequest(
            path=['organization', 'instances'],
            query=mapDashboardOrganizationsInstancesListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardOrganizationsInstancesListOutput.from_dict)

    def get(self, instanceId: str):
        """
    Get organization instance
    Get the information of a specific organization instance

    :param instanceId: str
    :return: DashboardOrganizationsInstancesGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'instances', instanceId]
        )
        return self._get(request).transform(mapDashboardOrganizationsInstancesGetOutput.from_dict)

    def create(self, body: DashboardOrganizationsInstancesCreateBody):
        """
    Create organization instance
    Create a new organization instance

    :param body: DashboardOrganizationsInstancesCreateBody
    :return: DashboardOrganizationsInstancesCreateOutput
    """
        request = MetorialRequest(
            path=['organization', 'instances'],
            body=mapDashboardOrganizationsInstancesCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardOrganizationsInstancesCreateOutput.from_dict)

    def delete(self, instanceId: str):
        """
    Delete organization instance
    Remove an organization instance

    :param instanceId: str
    :return: DashboardOrganizationsInstancesDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'instances', instanceId]
        )
        return self._delete(request).transform(mapDashboardOrganizationsInstancesDeleteOutput.from_dict)

    def update(self, instanceId: str, body: DashboardOrganizationsInstancesUpdateBody):
        """
    Update organization instance
    Update the role of an organization instance

    :param instanceId: str
    :param body: DashboardOrganizationsInstancesUpdateBody
    :return: DashboardOrganizationsInstancesUpdateOutput
    """
        request = MetorialRequest(
            path=['organization', 'instances', instanceId],
            body=mapDashboardOrganizationsInstancesUpdateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardOrganizationsInstancesUpdateOutput.from_dict)