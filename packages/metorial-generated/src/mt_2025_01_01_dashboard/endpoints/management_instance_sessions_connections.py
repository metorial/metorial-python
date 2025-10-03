from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceSessionsConnectionsListOutput,
  DashboardInstanceSessionsConnectionsListOutput,
  mapDashboardInstanceSessionsConnectionsListQuery,
  DashboardInstanceSessionsConnectionsListQuery,
  mapDashboardInstanceSessionsConnectionsGetOutput,
  DashboardInstanceSessionsConnectionsGetOutput,
)


class MetorialManagementInstanceSessionsConnectionsEndpoint(BaseMetorialEndpoint):
  """Each time a new MCP connection to a server is established, a session connection is created. This allows you to track and manage the connections made during a session."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    session_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardInstanceSessionsConnectionsListOutput:
    """
    List session connections
    List all session connections

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSessionsConnectionsListOutput
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
      path=["instances", instance_id, "sessions", session_id, "connections"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsConnectionsListOutput.from_dict
    )

  def get(
    self, instance_id: str, session_id: str, session_connection_id: str
  ) -> DashboardInstanceSessionsConnectionsGetOutput:
    """
    Get session connection
    Get the information of a specific session connection

    :param instance_id: str
    :param session_id: str
    :param session_connection_id: str
    :return: DashboardInstanceSessionsConnectionsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "sessions",
        session_id,
        "connections",
        session_connection_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsConnectionsGetOutput.from_dict
    )
