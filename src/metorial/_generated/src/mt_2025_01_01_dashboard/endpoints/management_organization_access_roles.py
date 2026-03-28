from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsAccessRolesListOutput, DashboardOrganizationsAccessRolesListOutput, mapDashboardOrganizationsAccessRolesListQuery, DashboardOrganizationsAccessRolesListQuery, mapDashboardOrganizationsAccessRolesGetOutput, DashboardOrganizationsAccessRolesGetOutput, mapDashboardOrganizationsAccessRolesVersionsOutput, DashboardOrganizationsAccessRolesVersionsOutput, mapDashboardOrganizationsAccessRolesVersionsQuery, DashboardOrganizationsAccessRolesVersionsQuery, mapDashboardOrganizationsAccessRolesCreateOutput, DashboardOrganizationsAccessRolesCreateOutput, mapDashboardOrganizationsAccessRolesCreateBody, DashboardOrganizationsAccessRolesCreateBody, mapDashboardOrganizationsAccessRolesUpdateOutput, DashboardOrganizationsAccessRolesUpdateOutput, mapDashboardOrganizationsAccessRolesUpdateBody, DashboardOrganizationsAccessRolesUpdateBody, mapDashboardOrganizationsAccessRolesDeleteOutput, DashboardOrganizationsAccessRolesDeleteOutput

class MetorialManagementOrganizationAccessRolesEndpoint(BaseMetorialEndpoint):
    """Manage organization access roles"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsAccessRolesListOutput:
        """
    List access roles
    List organization access roles

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsAccessRolesListOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if limit is not None:
            query_dict["limit"] = limit
        if after is not None:
            query_dict["after"] = after
        if before is not None:
            query_dict["before"] = before
        if cursor is not None:
            query_dict["cursor"] = cursor
        if order is not None:
            query_dict["order"] = order

        request = MetorialRequest(
            path=['organization', 'access-roles'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsAccessRolesListOutput.from_dict)

    def get(self, access_role_id: str) -> DashboardOrganizationsAccessRolesGetOutput:
        """
    Get access role
    Get a single organization access role

    :param access_role_id: str
    :return: DashboardOrganizationsAccessRolesGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'access-roles', access_role_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsAccessRolesGetOutput.from_dict)

    def versions(self, access_role_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsAccessRolesVersionsOutput:
        """
    List access role versions
    List version history for an organization access role

    :param access_role_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsAccessRolesVersionsOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if limit is not None:
            query_dict["limit"] = limit
        if after is not None:
            query_dict["after"] = after
        if before is not None:
            query_dict["before"] = before
        if cursor is not None:
            query_dict["cursor"] = cursor
        if order is not None:
            query_dict["order"] = order

        request = MetorialRequest(
            path=['organization', 'access-roles', access_role_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsAccessRolesVersionsOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None, scopes: Optional[List[str]] = None, message: Optional[str] = None) -> DashboardOrganizationsAccessRolesCreateOutput:
        """
    Create access role
    Create an organization access role

    :param name: str
    :param description: Optional[str] (optional)
    :param scopes: Optional[List[str]] (optional)
    :param message: Optional[str] (optional)
    :return: DashboardOrganizationsAccessRolesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if scopes is not None:
            body_dict["scopes"] = scopes
        if message is not None:
            body_dict["message"] = message

        request = MetorialRequest(
            path=['organization', 'access-roles'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsAccessRolesCreateOutput.from_dict)

    def update(self, access_role_id: str, *, name: Optional[str] = None, description: Optional[str] = None, scopes: Optional[List[str]] = None, message: Optional[str] = None) -> DashboardOrganizationsAccessRolesUpdateOutput:
        """
    Update access role
    Update an organization access role

    :param access_role_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param scopes: Optional[List[str]] (optional)
    :param message: Optional[str] (optional)
    :return: DashboardOrganizationsAccessRolesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if scopes is not None:
            body_dict["scopes"] = scopes
        if message is not None:
            body_dict["message"] = message

        request = MetorialRequest(
            path=['organization', 'access-roles', access_role_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsAccessRolesUpdateOutput.from_dict)

    def delete(self, access_role_id: str) -> DashboardOrganizationsAccessRolesDeleteOutput:
        """
    Delete access role
    Delete an organization access role

    :param access_role_id: str
    :return: DashboardOrganizationsAccessRolesDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'access-roles', access_role_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsAccessRolesDeleteOutput.from_dict)