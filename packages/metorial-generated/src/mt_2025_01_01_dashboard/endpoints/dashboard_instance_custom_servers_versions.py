from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersVersionsListOutput,
  DashboardInstanceCustomServersVersionsListOutput,
  mapDashboardInstanceCustomServersVersionsListQuery,
  DashboardInstanceCustomServersVersionsListQuery,
  mapDashboardInstanceCustomServersVersionsCreateOutput,
  DashboardInstanceCustomServersVersionsCreateOutput,
  mapDashboardInstanceCustomServersVersionsCreateBody,
  DashboardInstanceCustomServersVersionsCreateBody,
  mapDashboardInstanceCustomServersVersionsGetOutput,
  DashboardInstanceCustomServersVersionsGetOutput,
)


class MetorialDashboardInstanceCustomServersVersionsEndpoint(BaseMetorialEndpoint):
  """Manager custom server versions"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    custom_server_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardInstanceCustomServersVersionsListOutput:
    """
    List custom server versions
    List all custom server versions

    :param instance_id: str
    :param custom_server_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceCustomServersVersionsListOutput
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
      path=[
        "dashboard",
        "instances",
        instance_id,
        "custom-servers",
        custom_server_id,
        "versions",
      ],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersVersionsListOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    custom_server_id: str,
    *,
    implementation: Union[Dict[str, Any], Dict[str, Any]]
  ) -> DashboardInstanceCustomServersVersionsCreateOutput:
    """
    Create custom server version
    Create a new custom server version

    :param instance_id: str
    :param custom_server_id: str
    :param implementation: Union[Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstanceCustomServersVersionsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["implementation"] = implementation

    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instance_id,
        "custom-servers",
        custom_server_id,
        "versions",
      ],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardInstanceCustomServersVersionsCreateOutput.from_dict
    )

  def get(
    self, instance_id: str, custom_server_id: str, custom_server_version_id: str
  ) -> DashboardInstanceCustomServersVersionsGetOutput:
    """
    Get custom server version
    Get information for a specific custom server version

    :param instance_id: str
    :param custom_server_id: str
    :param custom_server_version_id: str
    :return: DashboardInstanceCustomServersVersionsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instance_id,
        "custom-servers",
        custom_server_id,
        "versions",
        custom_server_version_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersVersionsGetOutput.from_dict
    )
