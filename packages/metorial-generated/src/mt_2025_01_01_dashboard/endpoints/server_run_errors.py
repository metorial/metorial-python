from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServerRunErrorsListOutput,
  DashboardInstanceServerRunErrorsListOutput,
  mapDashboardInstanceServerRunErrorsListQuery,
  DashboardInstanceServerRunErrorsListQuery,
  mapDashboardInstanceServerRunErrorsGetOutput,
  DashboardInstanceServerRunErrorsGetOutput,
)


class MetorialServerRunErrorsEndpoint(BaseMetorialEndpoint):
  """Sometimes, an MCP server may fail to run correctly, resulting in an error. Metorial captures these errors to help you diagnose issues with your server runs. You may also want to check the Metorial dashboard for more details on the error."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    server_session_id: Optional[Union[str, List[str]]] = None,
    server_implementation_id: Optional[Union[str, List[str]]] = None,
    server_deployment_id: Optional[Union[str, List[str]]] = None,
    server_run_id: Optional[Union[str, List[str]]] = None,
    server_run_error_group_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceServerRunErrorsListOutput:
    """
    List server run errors
    List all server run errors

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param server_session_id: Optional[Union[str, List[str]]] (optional)
    :param server_implementation_id: Optional[Union[str, List[str]]] (optional)
    :param server_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param server_run_id: Optional[Union[str, List[str]]] (optional)
    :param server_run_error_group_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceServerRunErrorsListOutput
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
    if server_session_id is not None:
      query_dict["server_session_id"] = server_session_id
    if server_implementation_id is not None:
      query_dict["server_implementation_id"] = server_implementation_id
    if server_deployment_id is not None:
      query_dict["server_deployment_id"] = server_deployment_id
    if server_run_id is not None:
      query_dict["server_run_id"] = server_run_id
    if server_run_error_group_id is not None:
      query_dict["server_run_error_group_id"] = server_run_error_group_id

    request = MetorialRequest(path=["server-run-errors"], query=query_dict)
    return self._get(request).transform(
      mapDashboardInstanceServerRunErrorsListOutput.from_dict
    )

  def get(self, server_run_error_id: str) -> DashboardInstanceServerRunErrorsGetOutput:
    """
    Get server run error
    Get the information of a specific server run error

    :param server_run_error_id: str
    :return: DashboardInstanceServerRunErrorsGetOutput
    """
    request = MetorialRequest(path=["server-run-errors", server_run_error_id])
    return self._get(request).transform(
      mapDashboardInstanceServerRunErrorsGetOutput.from_dict
    )
