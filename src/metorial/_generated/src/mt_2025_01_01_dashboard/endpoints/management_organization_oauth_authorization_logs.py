from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthAuthorizationLogsListOutput, DashboardOrganizationsOauthAuthorizationLogsListOutput, mapDashboardOrganizationsOauthAuthorizationLogsListQuery, DashboardOrganizationsOauthAuthorizationLogsListQuery

class MetorialManagementOrganizationOauthAuthorizationLogsEndpoint(BaseMetorialEndpoint):
    """Inspect OAuth authorization requests for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, app_id: Optional[Union[str, List[str]]] = None, user_id: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsOauthAuthorizationLogsListOutput:
        """
    List organization OAuth authorization logs
    Returns a paginated list of OAuth authorization requests for the organization.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param app_id: Optional[Union[str, List[str]]] (optional)
    :param user_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsOauthAuthorizationLogsListOutput
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
        if app_id is not None:
            query_dict["app_id"] = app_id
        if user_id is not None:
            query_dict["user_id"] = user_id

        request = MetorialRequest(
            path=['organization', 'oauth', 'authorization-logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthAuthorizationLogsListOutput.from_dict)