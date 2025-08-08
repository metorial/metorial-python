from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsCreateOutput, DashboardOrganizationsCreateOutput, mapDashboardOrganizationsCreateBody, DashboardOrganizationsCreateBody, mapDashboardOrganizationsListOutput, DashboardOrganizationsListOutput, mapDashboardOrganizationsListQuery, DashboardOrganizationsListQuery, mapDashboardOrganizationsGetOutput, DashboardOrganizationsGetOutput, mapDashboardOrganizationsUpdateOutput, DashboardOrganizationsUpdateOutput, mapDashboardOrganizationsUpdateBody, DashboardOrganizationsUpdateBody, mapDashboardOrganizationsDeleteOutput, DashboardOrganizationsDeleteOutput, mapDashboardOrganizationsGetMembershipOutput, DashboardOrganizationsGetMembershipOutput

class MetorialDashboardOrganizationsEndpoint(BaseMetorialEndpoint):
    """Read and write organization information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, body: DashboardOrganizationsCreateBody):
        """
    Create organization
    Create a new organization

    :param body: DashboardOrganizationsCreateBody
    :return: DashboardOrganizationsCreateOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations'],
            body=mapDashboardOrganizationsCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardOrganizationsCreateOutput.from_dict)

    def list(self, query: DashboardOrganizationsListQuery = None):
        """
    List organizations
    List all organizations

    :param query: DashboardOrganizationsListQuery
    :return: DashboardOrganizationsListOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations'],
            query=mapDashboardOrganizationsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapDashboardOrganizationsListOutput.from_dict)

    def get(self, organizationId: str):
        """
    Get organization
    Get the current organization information

    :param organizationId: str
    :return: DashboardOrganizationsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organizationId]
        )
        return self._get(request).transform(mapDashboardOrganizationsGetOutput.from_dict)

    def update(self, organizationId: str, body: DashboardOrganizationsUpdateBody):
        """
    Update organization
    Update the current organization information

    :param organizationId: str
    :param body: DashboardOrganizationsUpdateBody
    :return: DashboardOrganizationsUpdateOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organizationId],
            body=mapDashboardOrganizationsUpdateBody.to_dict(body),
        )
        return self._patch(request).transform(mapDashboardOrganizationsUpdateOutput.from_dict)

    def delete(self, organizationId: str):
        """
    Delete organization
    Delete the current organization

    :param organizationId: str
    :return: DashboardOrganizationsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organizationId]
        )
        return self._delete(request).transform(mapDashboardOrganizationsDeleteOutput.from_dict)

    def get_membership(self, organizationId: str):
        """
    Get organization
    Get the current organization information

    :param organizationId: str
    :return: DashboardOrganizationsGetMembershipOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organizationId, 'membership']
        )
        return self._get(request).transform(mapDashboardOrganizationsGetMembershipOutput.from_dict)