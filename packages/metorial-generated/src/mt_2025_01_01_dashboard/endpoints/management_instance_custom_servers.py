from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersListOutput,
  DashboardInstanceCustomServersListOutput,
  mapDashboardInstanceCustomServersListQuery,
  DashboardInstanceCustomServersListQuery,
  mapDashboardInstanceCustomServersCreateOutput,
  DashboardInstanceCustomServersCreateOutput,
  mapDashboardInstanceCustomServersCreateBody,
  DashboardInstanceCustomServersCreateBody,
  mapDashboardInstanceCustomServersUpdateOutput,
  DashboardInstanceCustomServersUpdateOutput,
  mapDashboardInstanceCustomServersUpdateBody,
  DashboardInstanceCustomServersUpdateBody,
  mapDashboardInstanceCustomServersDeleteOutput,
  DashboardInstanceCustomServersDeleteOutput,
  mapDashboardInstanceCustomServersGetOutput,
  DashboardInstanceCustomServersGetOutput,
)


class MetorialManagementInstanceCustomServersEndpoint(BaseMetorialEndpoint):
  """Manager custom servers"""

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
    type: Optional[Union[List[str], str]] = None
  ) -> DashboardInstanceCustomServersListOutput:
    """
    List custom servers
    List all custom servers

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[List[str], str]] (optional)
    :return: DashboardInstanceCustomServersListOutput
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
    if type is not None:
      query_dict["type"] = type

    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersListOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    *,
    name: str,
    implementation: Union[Dict[str, Any], Dict[str, Any]],
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceCustomServersCreateOutput:
    """
    Create custom server
    Create a new custom server

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param implementation: Union[Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstanceCustomServersCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    body_dict["implementation"] = implementation

    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardInstanceCustomServersCreateOutput.from_dict
    )

  def update(
    self,
    instance_id: str,
    custom_server_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceCustomServersUpdateOutput:
    """
    Update custom server
    Update a custom server

    :param instance_id: str
    :param custom_server_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCustomServersUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata

    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers", custom_server_id],
      body=body_dict,
    )
    return self._patch(request).transform(
      mapDashboardInstanceCustomServersUpdateOutput.from_dict
    )

  def delete(
    self, instance_id: str, custom_server_id: str
  ) -> DashboardInstanceCustomServersDeleteOutput:
    """
    Delete custom server
    Delete a custom server

    :param instance_id: str
    :param custom_server_id: str
    :return: DashboardInstanceCustomServersDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers", custom_server_id]
    )
    return self._delete(request).transform(
      mapDashboardInstanceCustomServersDeleteOutput.from_dict
    )

  def get(
    self, instance_id: str, custom_server_id: str
  ) -> DashboardInstanceCustomServersGetOutput:
    """
    Get custom server
    Get information for a specific custom server

    :param instance_id: str
    :param custom_server_id: str
    :return: DashboardInstanceCustomServersGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers", custom_server_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersGetOutput.from_dict
    )
