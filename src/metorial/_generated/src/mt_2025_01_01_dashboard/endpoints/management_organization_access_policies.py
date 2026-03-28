from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsAccessPoliciesListOutput, DashboardOrganizationsAccessPoliciesListOutput, mapDashboardOrganizationsAccessPoliciesListQuery, DashboardOrganizationsAccessPoliciesListQuery, mapDashboardOrganizationsAccessPoliciesGetOutput, DashboardOrganizationsAccessPoliciesGetOutput, mapDashboardOrganizationsAccessPoliciesVersionsOutput, DashboardOrganizationsAccessPoliciesVersionsOutput, mapDashboardOrganizationsAccessPoliciesVersionsQuery, DashboardOrganizationsAccessPoliciesVersionsQuery, mapDashboardOrganizationsAccessPoliciesCreateOutput, DashboardOrganizationsAccessPoliciesCreateOutput, mapDashboardOrganizationsAccessPoliciesCreateBody, DashboardOrganizationsAccessPoliciesCreateBody, mapDashboardOrganizationsAccessPoliciesUpdateOutput, DashboardOrganizationsAccessPoliciesUpdateOutput, mapDashboardOrganizationsAccessPoliciesUpdateBody, DashboardOrganizationsAccessPoliciesUpdateBody, mapDashboardOrganizationsAccessPoliciesDeleteOutput, DashboardOrganizationsAccessPoliciesDeleteOutput

class MetorialManagementOrganizationAccessPoliciesEndpoint(BaseMetorialEndpoint):
    """Manage organization access policies"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsAccessPoliciesListOutput:
        """
    List access policies
    List organization access policies

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsAccessPoliciesListOutput
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
            path=['organization', 'access-policies'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsAccessPoliciesListOutput.from_dict)

    def get(self, access_policy_id: str) -> DashboardOrganizationsAccessPoliciesGetOutput:
        """
    Get access policy
    Get a single organization access policy

    :param access_policy_id: str
    :return: DashboardOrganizationsAccessPoliciesGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'access-policies', access_policy_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsAccessPoliciesGetOutput.from_dict)

    def versions(self, access_policy_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardOrganizationsAccessPoliciesVersionsOutput:
        """
    List access policy versions
    List version history for an organization access policy

    :param access_policy_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsAccessPoliciesVersionsOutput
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
            path=['organization', 'access-policies', access_policy_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsAccessPoliciesVersionsOutput.from_dict)

    def create(self, *, name: str, document: Dict[str, Any], description: Optional[str] = None, message: Optional[str] = None) -> DashboardOrganizationsAccessPoliciesCreateOutput:
        """
    Create access policy
    Create an organization access policy

    :param name: str
    :param description: Optional[str] (optional)
    :param document: Dict[str, Any]
    :param message: Optional[str] (optional)
    :return: DashboardOrganizationsAccessPoliciesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        body_dict["document"] = document
        if message is not None:
            body_dict["message"] = message

        request = MetorialRequest(
            path=['organization', 'access-policies'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsAccessPoliciesCreateOutput.from_dict)

    def update(self, access_policy_id: str, *, name: Optional[str] = None, description: Optional[str] = None, document: Optional[Dict[str, Any]] = None, message: Optional[str] = None) -> DashboardOrganizationsAccessPoliciesUpdateOutput:
        """
    Update access policy
    Update an organization access policy

    :param access_policy_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param document: Optional[Dict[str, Any]] (optional)
    :param message: Optional[str] (optional)
    :return: DashboardOrganizationsAccessPoliciesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if document is not None:
            body_dict["document"] = document
        if message is not None:
            body_dict["message"] = message

        request = MetorialRequest(
            path=['organization', 'access-policies', access_policy_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsAccessPoliciesUpdateOutput.from_dict)

    def delete(self, access_policy_id: str) -> DashboardOrganizationsAccessPoliciesDeleteOutput:
        """
    Delete access policy
    Delete an organization access policy

    :param access_policy_id: str
    :return: DashboardOrganizationsAccessPoliciesDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'access-policies', access_policy_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsAccessPoliciesDeleteOutput.from_dict)