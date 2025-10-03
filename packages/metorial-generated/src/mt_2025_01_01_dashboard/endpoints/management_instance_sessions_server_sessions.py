from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceSessionsServerSessionsListOutput,
  DashboardInstanceSessionsServerSessionsListOutput,
  mapDashboardInstanceSessionsServerSessionsListQuery,
  DashboardInstanceSessionsServerSessionsListQuery,
  mapDashboardInstanceSessionsServerSessionsGetOutput,
  DashboardInstanceSessionsServerSessionsGetOutput,
)


class MetorialManagementInstanceSessionsServerSessionsEndpoint(BaseMetorialEndpoint):
  """Read and write server session information"""

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
  ) -> DashboardInstanceSessionsServerSessionsListOutput:
    """
    List server sessions
    List all server sessions

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSessionsServerSessionsListOutput
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
      path=["instances", instance_id, "sessions", session_id, "server-sessions"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsServerSessionsListOutput.from_dict
    )

  def get(
    self, instance_id: str, session_id: str, server_session_id: str
  ) -> DashboardInstanceSessionsServerSessionsGetOutput:
    """
    Get server session
    Get the information of a specific server session

    :param instance_id: str
    :param session_id: str
    :param server_session_id: str
    :return: DashboardInstanceSessionsServerSessionsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "sessions",
        session_id,
        "server-sessions",
        server_session_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsServerSessionsGetOutput.from_dict
    )
