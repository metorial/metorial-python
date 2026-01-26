from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceMagicMcpSessionsListOutput,
  DashboardInstanceMagicMcpSessionsListOutput,
  mapDashboardInstanceMagicMcpSessionsListQuery,
  DashboardInstanceMagicMcpSessionsListQuery,
  mapDashboardInstanceMagicMcpSessionsGetOutput,
  DashboardInstanceMagicMcpSessionsGetOutput,
)


class MetorialDashboardInstanceMagicMcpSessionsEndpoint(BaseMetorialEndpoint):
  """Magic MCP sessions are created when a user connects to a magic MCP session using a valid magic MCP token."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceMagicMcpSessionsListOutput:
    """
    List magic MCP session
    List all magic MCP session

    :param instance_id: str
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
      path=["dashboard", "instances", instance_id, "magic-mcp-sessions"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceMagicMcpSessionsListOutput.from_dict
    )

  def get(
    self, instance_id: str, magic_mcp_session_id: str
  ) -> DashboardInstanceMagicMcpSessionsGetOutput:
    """
    Get magic MCP session
    Get the information of a specific magic MCP session

    :param instance_id: str
    :param magic_mcp_session_id: str
    :return: DashboardInstanceMagicMcpSessionsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instance_id,
        "magic-mcp-sessions",
        magic_mcp_session_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceMagicMcpSessionsGetOutput.from_dict
    )
