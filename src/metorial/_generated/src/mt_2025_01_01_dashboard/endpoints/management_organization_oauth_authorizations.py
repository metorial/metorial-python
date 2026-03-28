from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthAuthorizationsListOutput, DashboardOrganizationsOauthAuthorizationsListOutput, mapDashboardOrganizationsOauthAuthorizationsListQuery, DashboardOrganizationsOauthAuthorizationsListQuery, mapDashboardOrganizationsOauthAuthorizationsGetOutput, DashboardOrganizationsOauthAuthorizationsGetOutput, mapDashboardOrganizationsOauthAuthorizationsRevokeOutput, DashboardOrganizationsOauthAuthorizationsRevokeOutput

class MetorialManagementOrganizationOauthAuthorizationsEndpoint(BaseMetorialEndpoint):
    """Inspect and revoke OAuth authorizations for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, installation_id: Optional[Union[str, List[str]]] = None, app_id: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsOauthAuthorizationsListOutput:
        """
    List organization OAuth authorizations
    Returns a paginated list of OAuth authorizations for the organization.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param installation_id: Optional[Union[str, List[str]]] (optional)
    :param app_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsOauthAuthorizationsListOutput
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
        if installation_id is not None:
            query_dict["installation_id"] = installation_id
        if app_id is not None:
            query_dict["app_id"] = app_id

        request = MetorialRequest(
            path=['organization', 'oauth', 'authorizations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthAuthorizationsListOutput.from_dict)

    def get(self, oauth_authorization_id: str) -> DashboardOrganizationsOauthAuthorizationsGetOutput:
        """
    Get organization OAuth authorization
    Retrieves a specific OAuth authorization for the organization.

    :param oauth_authorization_id: str
    :return: DashboardOrganizationsOauthAuthorizationsGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'authorizations', oauth_authorization_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthAuthorizationsGetOutput.from_dict)

    def revoke(self, oauth_authorization_id: str) -> DashboardOrganizationsOauthAuthorizationsRevokeOutput:
        """
    Revoke organization OAuth authorization
    Revokes a specific OAuth authorization for the organization.

    :param oauth_authorization_id: str
    :return: DashboardOrganizationsOauthAuthorizationsRevokeOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'authorizations', oauth_authorization_id, 'revoke']
        )
        return self._post(request).transform(mapDashboardOrganizationsOauthAuthorizationsRevokeOutput.from_dict)