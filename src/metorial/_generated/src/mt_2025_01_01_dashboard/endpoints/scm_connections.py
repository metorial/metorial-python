from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceScmConnectionsListOutput, DashboardInstanceScmConnectionsListOutput, mapDashboardInstanceScmConnectionsListQuery, DashboardInstanceScmConnectionsListQuery, mapDashboardInstanceScmConnectionsGetOutput, DashboardInstanceScmConnectionsGetOutput, mapDashboardInstanceScmConnectionsCreateOutput, DashboardInstanceScmConnectionsCreateOutput, mapDashboardInstanceScmConnectionsCreateBody, DashboardInstanceScmConnectionsCreateBody

class MetorialScmConnectionsEndpoint(BaseMetorialEndpoint):
    """Manage source control connections for an instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceScmConnectionsListOutput:
        """
    List SCM connections
    Returns a paginated list of SCM connections.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceScmConnectionsListOutput
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
            path=['scm', 'connections'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceScmConnectionsListOutput.from_dict)

    def get(self, scm_connection_id: str) -> DashboardInstanceScmConnectionsGetOutput:
        """
    Get SCM connection
    Retrieves a specific SCM connection by ID.

    :param scm_connection_id: str
    :return: DashboardInstanceScmConnectionsGetOutput
    """
        request = MetorialRequest(
            path=['scm', 'connections', scm_connection_id]
        )
        return self._get(request).transform(mapDashboardInstanceScmConnectionsGetOutput.from_dict)

    def create(self, *, redirect_url: Optional[str] = None) -> DashboardInstanceScmConnectionsCreateOutput:
        """
    Create SCM connection
    Initiates an SCM connection setup session.

    :param redirect_url: Optional[str] (optional)
    :return: DashboardInstanceScmConnectionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if redirect_url is not None:
            body_dict["redirect_url"] = redirect_url

        request = MetorialRequest(
            path=['scm', 'connections'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceScmConnectionsCreateOutput.from_dict)