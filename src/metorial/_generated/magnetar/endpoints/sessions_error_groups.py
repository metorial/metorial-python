from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsErrorGroupsListOutput, DashboardInstanceSessionsErrorGroupsListOutput, mapDashboardInstanceSessionsErrorGroupsListQuery, DashboardInstanceSessionsErrorGroupsListQuery, mapDashboardInstanceSessionsErrorGroupsGetOutput, DashboardInstanceSessionsErrorGroupsGetOutput

class MetorialSessionsErrorGroupsEndpoint(BaseMetorialEndpoint):
    """Session error groups aggregate similar errors that occurred during a session. This read-only resource helps identify patterns in errors."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, session_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[str] = None) -> DashboardInstanceSessionsErrorGroupsListOutput:
        """
    List session error groups
    Returns a paginated list of error groups for a session.

    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[str] (optional)
    :return: DashboardInstanceSessionsErrorGroupsListOutput
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
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['sessions', session_id, 'error-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsErrorGroupsListOutput.from_dict)

    def get(self, session_id: str, session_error_group_id: str) -> DashboardInstanceSessionsErrorGroupsGetOutput:
        """
    Get session error group
    Retrieves a specific error group for a session.

    :param session_id: str
    :param session_error_group_id: str
    :return: DashboardInstanceSessionsErrorGroupsGetOutput
    """
        request = MetorialRequest(
            path=['sessions', session_id, 'error-groups', session_error_group_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsErrorGroupsGetOutput.from_dict)
