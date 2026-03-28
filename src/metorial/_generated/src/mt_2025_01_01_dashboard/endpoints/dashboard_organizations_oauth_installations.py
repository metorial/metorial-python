from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthInstallationsListOutput, DashboardOrganizationsOauthInstallationsListOutput, mapDashboardOrganizationsOauthInstallationsListQuery, DashboardOrganizationsOauthInstallationsListQuery, mapDashboardOrganizationsOauthInstallationsGetOutput, DashboardOrganizationsOauthInstallationsGetOutput, mapDashboardOrganizationsOauthInstallationsRevokeOutput, DashboardOrganizationsOauthInstallationsRevokeOutput

class MetorialDashboardOrganizationsOauthInstallationsEndpoint(BaseMetorialEndpoint):
    """Inspect and revoke OAuth app installations for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, app_id: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsOauthInstallationsListOutput:
        """
    List organization OAuth installations
    Returns a paginated list of OAuth installations for the organization.

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param app_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsOauthInstallationsListOutput
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
        if app_id is not None:
            query_dict["app_id"] = app_id

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'oauth', 'installations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthInstallationsListOutput.from_dict)

    def get(self, organization_id: str, oauth_installation_id: str) -> DashboardOrganizationsOauthInstallationsGetOutput:
        """
    Get organization OAuth installation
    Retrieves a specific OAuth installation for the organization.

    :param organization_id: str
    :param oauth_installation_id: str
    :return: DashboardOrganizationsOauthInstallationsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'oauth', 'installations', oauth_installation_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthInstallationsGetOutput.from_dict)

    def revoke(self, organization_id: str, oauth_installation_id: str) -> DashboardOrganizationsOauthInstallationsRevokeOutput:
        """
    Revoke organization OAuth installation
    Revokes a specific OAuth installation for the organization.

    :param organization_id: str
    :param oauth_installation_id: str
    :return: DashboardOrganizationsOauthInstallationsRevokeOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'oauth', 'installations', oauth_installation_id, 'revoke']
        )
        return self._post(request).transform(mapDashboardOrganizationsOauthInstallationsRevokeOutput.from_dict)