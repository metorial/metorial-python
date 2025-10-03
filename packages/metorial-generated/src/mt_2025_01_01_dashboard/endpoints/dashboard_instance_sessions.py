from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceSessionsListOutput,
  DashboardInstanceSessionsListOutput,
  mapDashboardInstanceSessionsListQuery,
  DashboardInstanceSessionsListQuery,
  mapDashboardInstanceSessionsGetOutput,
  DashboardInstanceSessionsGetOutput,
  mapDashboardInstanceSessionsCreateOutput,
  DashboardInstanceSessionsCreateOutput,
  mapDashboardInstanceSessionsCreateBody,
  DashboardInstanceSessionsCreateBody,
  mapDashboardInstanceSessionsDeleteOutput,
  DashboardInstanceSessionsDeleteOutput,
)


class MetorialDashboardInstanceSessionsEndpoint(BaseMetorialEndpoint):
  """Before you can connect to an MCP server, you need to create a session. Each session can be linked to one or more server deployments, allowing you to connect to multiple servers simultaneously. Once you have created a session, you can use the provided MCP URL to connect to the server deployments via MCP."""

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
    status: Optional[Union[str, List[str]]] = None,
    server_id: Optional[Union[str, List[str]]] = None,
    server_variant_id: Optional[Union[str, List[str]]] = None,
    server_implementation_id: Optional[Union[str, List[str]]] = None,
    server_deployment_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceSessionsListOutput:
    """
    List sessions
    List all sessions

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param server_id: Optional[Union[str, List[str]]] (optional)
    :param server_variant_id: Optional[Union[str, List[str]]] (optional)
    :param server_implementation_id: Optional[Union[str, List[str]]] (optional)
    :param server_deployment_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsListOutput
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
    if server_id is not None:
      query_dict["server_id"] = server_id
    if server_variant_id is not None:
      query_dict["server_variant_id"] = server_variant_id
    if server_implementation_id is not None:
      query_dict["server_implementation_id"] = server_implementation_id
    if server_deployment_id is not None:
      query_dict["server_deployment_id"] = server_deployment_id

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "sessions"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceSessionsListOutput.from_dict
    )

  def get(
    self, instance_id: str, session_id: str
  ) -> DashboardInstanceSessionsGetOutput:
    """
    Get session
    Get the information of a specific session

    :param instance_id: str
    :param session_id: str
    :return: DashboardInstanceSessionsGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "sessions", session_id]
    )
    return self._get(request).transform(mapDashboardInstanceSessionsGetOutput.from_dict)

  def create(
    self,
    instance_id: str,
    *,
    server_deployments: List[Union[Dict[str, Any], str, Dict[str, Any]]]
  ) -> DashboardInstanceSessionsCreateOutput:
    """
    Create session
    Create a new session

    :param instance_id: str
    :param server_deployments: List[Union[Dict[str, Any], str, Dict[str, Any]]]
    :return: DashboardInstanceSessionsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["server_deployments"] = server_deployments

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "sessions"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardInstanceSessionsCreateOutput.from_dict
    )

  def delete(
    self, instance_id: str, session_id: str
  ) -> DashboardInstanceSessionsDeleteOutput:
    """
    Delete session
    Delete a session

    :param instance_id: str
    :param session_id: str
    :return: DashboardInstanceSessionsDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "sessions", session_id]
    )
    return self._delete(request).transform(
      mapDashboardInstanceSessionsDeleteOutput.from_dict
    )
