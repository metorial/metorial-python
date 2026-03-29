from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsServiceAccountsListOutput, DashboardOrganizationsServiceAccountsListOutput, mapDashboardOrganizationsServiceAccountsListQuery, DashboardOrganizationsServiceAccountsListQuery, mapDashboardOrganizationsServiceAccountsGetOutput, DashboardOrganizationsServiceAccountsGetOutput, mapDashboardOrganizationsServiceAccountsCreateOutput, DashboardOrganizationsServiceAccountsCreateOutput, mapDashboardOrganizationsServiceAccountsCreateBody, DashboardOrganizationsServiceAccountsCreateBody, mapDashboardOrganizationsServiceAccountsUpdateOutput, DashboardOrganizationsServiceAccountsUpdateOutput, mapDashboardOrganizationsServiceAccountsUpdateBody, DashboardOrganizationsServiceAccountsUpdateBody, mapDashboardOrganizationsServiceAccountsDeleteOutput, DashboardOrganizationsServiceAccountsDeleteOutput

class MetorialDashboardOrganizationsServiceAccountsEndpoint(BaseMetorialEndpoint):
    """Create and manage service accounts for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsServiceAccountsListOutput:
        """
    List organization service accounts
    Returns a paginated list of service accounts owned by the organization.

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsServiceAccountsListOutput
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
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'service-accounts'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsServiceAccountsListOutput.from_dict)

    def get(self, organization_id: str, service_account_id: str) -> DashboardOrganizationsServiceAccountsGetOutput:
        """
    Get organization service account
    Retrieves a specific service account owned by the organization.

    :param organization_id: str
    :param service_account_id: str
    :return: DashboardOrganizationsServiceAccountsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'service-accounts', service_account_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsServiceAccountsGetOutput.from_dict)

    def create(self, organization_id: str, *, name: str, scopes: List[str], description: Optional[str] = None) -> DashboardOrganizationsServiceAccountsCreateOutput:
        """
    Create organization service account
    Creates a new service account for machine-to-machine authentication.

    :param organization_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param scopes: List[str]
    :return: DashboardOrganizationsServiceAccountsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        body_dict["scopes"] = scopes

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'service-accounts'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsServiceAccountsCreateOutput.from_dict)

    def update(self, organization_id: str, service_account_id: str, *, name: Optional[str] = None, description: Optional[str] = None, scopes: Optional[List[str]] = None) -> DashboardOrganizationsServiceAccountsUpdateOutput:
        """
    Update organization service account
    Updates an existing service account owned by the organization.

    :param organization_id: str
    :param service_account_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param scopes: Optional[List[str]] (optional)
    :return: DashboardOrganizationsServiceAccountsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if scopes is not None:
            body_dict["scopes"] = scopes

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'service-accounts', service_account_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsServiceAccountsUpdateOutput.from_dict)

    def delete(self, organization_id: str, service_account_id: str) -> DashboardOrganizationsServiceAccountsDeleteOutput:
        """
    Delete organization service account
    Archives a service account owned by the organization.

    :param organization_id: str
    :param service_account_id: str
    :return: DashboardOrganizationsServiceAccountsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'service-accounts', service_account_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsServiceAccountsDeleteOutput.from_dict)