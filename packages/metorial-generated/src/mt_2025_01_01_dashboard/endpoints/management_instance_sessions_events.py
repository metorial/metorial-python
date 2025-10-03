from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceSessionsEventsListOutput,
  DashboardInstanceSessionsEventsListOutput,
  mapDashboardInstanceSessionsEventsListQuery,
  DashboardInstanceSessionsEventsListQuery,
  mapDashboardInstanceSessionsEventsGetOutput,
  DashboardInstanceSessionsEventsGetOutput,
)


class MetorialManagementInstanceSessionsEventsEndpoint(BaseMetorialEndpoint):
  """Read and write session event information"""

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
    order: Optional[str] = None,
    server_run_id: Optional[Union[str, List[str]]] = None,
    server_session_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceSessionsEventsListOutput:
    """
    List session events
    List all events for a specific session

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param server_run_id: Optional[Union[str, List[str]]] (optional)
    :param server_session_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsEventsListOutput
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
    if server_run_id is not None:
      query_dict["server_run_id"] = server_run_id
    if server_session_id is not None:
      query_dict["server_session_id"] = server_session_id

    request = MetorialRequest(
      path=["instances", instance_id, "sessions", session_id, "events"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsEventsListOutput.from_dict
    )

  def get(
    self, instance_id: str, session_id: str, session_event_id: str
  ) -> DashboardInstanceSessionsEventsGetOutput:
    """
    Get session event
    Get details of a specific session event

    :param instance_id: str
    :param session_id: str
    :param session_event_id: str
    :return: DashboardInstanceSessionsEventsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "sessions",
        session_id,
        "events",
        session_event_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsEventsGetOutput.from_dict
    )
