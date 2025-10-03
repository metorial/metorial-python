from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServerRunsListOutput,
  DashboardInstanceServerRunsListOutput,
  mapDashboardInstanceServerRunsListQuery,
  DashboardInstanceServerRunsListQuery,
  mapDashboardInstanceServerRunsGetOutput,
  DashboardInstanceServerRunsGetOutput,
)


class MetorialDashboardInstanceServerRunsEndpoint(BaseMetorialEndpoint):
  """Each time an MCP server is executed by the Metorial platform, a server run is created. This allows you to track the execution of MCP servers, including their status and associated sessions. Metorial may create multiple server runs for a single session or session connection."""

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
    server_session_id: Optional[Union[str, List[str]]] = None,
    server_implementation_id: Optional[Union[str, List[str]]] = None,
    server_deployment_id: Optional[Union[str, List[str]]] = None,
    session_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceServerRunsListOutput:
    """
    List server runs
    List all server runs

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param server_session_id: Optional[Union[str, List[str]]] (optional)
    :param server_implementation_id: Optional[Union[str, List[str]]] (optional)
    :param server_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceServerRunsListOutput
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
    if server_session_id is not None:
      query_dict["server_session_id"] = server_session_id
    if server_implementation_id is not None:
      query_dict["server_implementation_id"] = server_implementation_id
    if server_deployment_id is not None:
      query_dict["server_deployment_id"] = server_deployment_id
    if session_id is not None:
      query_dict["session_id"] = session_id

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "server-runs"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceServerRunsListOutput.from_dict
    )

  def get(
    self, instance_id: str, server_run_id: str
  ) -> DashboardInstanceServerRunsGetOutput:
    """
    Get server run
    Get the information of a specific server run

    :param instance_id: str
    :param server_run_id: str
    :return: DashboardInstanceServerRunsGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "server-runs", server_run_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceServerRunsGetOutput.from_dict
    )
