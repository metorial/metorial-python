from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServerRunErrorGroupsListOutput,
  DashboardInstanceServerRunErrorGroupsListOutput,
  mapDashboardInstanceServerRunErrorGroupsListQuery,
  DashboardInstanceServerRunErrorGroupsListQuery,
  mapDashboardInstanceServerRunErrorGroupsGetOutput,
  DashboardInstanceServerRunErrorGroupsGetOutput,
)


class MetorialManagementInstanceServerRunErrorGroupsEndpoint(BaseMetorialEndpoint):
  """Read and write server run error group information"""

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
    server_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceServerRunErrorGroupsListOutput:
    """
    List server run error groups
    List all server run error groups

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param server_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceServerRunErrorGroupsListOutput
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
    if server_id is not None:
      query_dict["server_id"] = server_id

    request = MetorialRequest(
      path=["instances", instance_id, "server-run-error-groups"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceServerRunErrorGroupsListOutput.from_dict
    )

  def get(
    self, instance_id: str, server_run_error_group_id: str
  ) -> DashboardInstanceServerRunErrorGroupsGetOutput:
    """
    Get server run error group
    Get the information of a specific server run error group

    :param instance_id: str
    :param server_run_error_group_id: str
    :return: DashboardInstanceServerRunErrorGroupsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "server-run-error-groups",
        server_run_error_group_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceServerRunErrorGroupsGetOutput.from_dict
    )
