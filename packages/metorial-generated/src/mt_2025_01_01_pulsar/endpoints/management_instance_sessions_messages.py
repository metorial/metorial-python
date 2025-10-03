from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceSessionsMessagesListOutput,
  DashboardInstanceSessionsMessagesListOutput,
  mapDashboardInstanceSessionsMessagesListQuery,
  DashboardInstanceSessionsMessagesListQuery,
  mapDashboardInstanceSessionsMessagesGetOutput,
  DashboardInstanceSessionsMessagesGetOutput,
)


class MetorialManagementInstanceSessionsMessagesEndpoint(BaseMetorialEndpoint):
  """When MCP servers and clients communicate, Metorial captures the messages they send. This allows you to see the raw messages exchanged between the server and client, which can be useful for debugging or understanding the communication flow."""

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
  ) -> DashboardInstanceSessionsMessagesListOutput:
    """
    List session messages
    List all messages for a specific session

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param server_run_id: Optional[Union[str, List[str]]] (optional)
    :param server_session_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsMessagesListOutput
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
      path=["instances", instance_id, "sessions", session_id, "messages"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsMessagesListOutput.from_dict
    )

  def get(
    self, instance_id: str, session_id: str, session_message_id: str
  ) -> DashboardInstanceSessionsMessagesGetOutput:
    """
    Get session message
    Get details of a specific session message

    :param instance_id: str
    :param session_id: str
    :param session_message_id: str
    :return: DashboardInstanceSessionsMessagesGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "sessions",
        session_id,
        "messages",
        session_message_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsMessagesGetOutput.from_dict
    )
