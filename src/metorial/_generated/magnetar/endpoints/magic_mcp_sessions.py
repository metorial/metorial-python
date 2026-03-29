from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMagicMcpSessionsListOutput, DashboardInstanceMagicMcpSessionsListOutput, mapDashboardInstanceMagicMcpSessionsListQuery, DashboardInstanceMagicMcpSessionsListQuery, mapDashboardInstanceMagicMcpSessionsGetOutput, DashboardInstanceMagicMcpSessionsGetOutput

class MetorialMagicMcpSessionsEndpoint(BaseMetorialEndpoint):
    """Magic MCP sessions map a Magic MCP server to one Subspace session and are created on demand by the MCP connection API."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, magic_mcp_server_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceMagicMcpSessionsListOutput:
        """
    List magic MCP sessions
    Returns a paginated list of magic MCP sessions.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param magic_mcp_server_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceMagicMcpSessionsListOutput
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
        if magic_mcp_server_id is not None:
            query_dict["magic_mcp_server_id"] = magic_mcp_server_id

        request = MetorialRequest(
            path=['magic-mcp-sessions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpSessionsListOutput.from_dict)

    def get(self, magic_mcp_session_id: str) -> DashboardInstanceMagicMcpSessionsGetOutput:
        """
    Get magic MCP session
    Retrieves a specific magic MCP session.

    :param magic_mcp_session_id: str
    :return: DashboardInstanceMagicMcpSessionsGetOutput
    """
        request = MetorialRequest(
            path=['magic-mcp-sessions', magic_mcp_session_id]
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpSessionsGetOutput.from_dict)