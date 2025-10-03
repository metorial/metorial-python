from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServersImplementationsListOutput,
  DashboardInstanceServersImplementationsListOutput,
  mapDashboardInstanceServersImplementationsListQuery,
  DashboardInstanceServersImplementationsListQuery,
  mapDashboardInstanceServersImplementationsGetOutput,
  DashboardInstanceServersImplementationsGetOutput,
  mapDashboardInstanceServersImplementationsCreateOutput,
  DashboardInstanceServersImplementationsCreateOutput,
  mapDashboardInstanceServersImplementationsCreateBody,
  DashboardInstanceServersImplementationsCreateBody,
  mapDashboardInstanceServersImplementationsUpdateOutput,
  DashboardInstanceServersImplementationsUpdateOutput,
  mapDashboardInstanceServersImplementationsUpdateBody,
  DashboardInstanceServersImplementationsUpdateBody,
  mapDashboardInstanceServersImplementationsDeleteOutput,
  DashboardInstanceServersImplementationsDeleteOutput,
)


class MetorialServersImplementationsEndpoint(BaseMetorialEndpoint):
  """Server implementations allow you to customize predefined MCP servers with specific configurations, launch parameters, and metadata. You can create server deployments based on these implementations to connect to the underlying MCP servers."""

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
    status: Optional[Union[str, List[str]]] = None,
    server_id: Optional[Union[str, List[str]]] = None,
    server_variant_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceServersImplementationsListOutput:
    """
    List server implementations
    Retrieve all server implementations in the instance. Supports filtering by status, server, or variant.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param server_id: Optional[Union[str, List[str]]] (optional)
    :param server_variant_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceServersImplementationsListOutput
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

    request = MetorialRequest(path=["server-implementations"], query=query_dict)
    return self._get(request).transform(
      mapDashboardInstanceServersImplementationsListOutput.from_dict
    )

  def get(
    self, server_implementation_id: str
  ) -> DashboardInstanceServersImplementationsGetOutput:
    """
    Get server implementation
    Fetch detailed information about a specific server implementation.

    :param server_implementation_id: str
    :return: DashboardInstanceServersImplementationsGetOutput
    """
    request = MetorialRequest(path=["server-implementations", server_implementation_id])
    return self._get(request).transform(
      mapDashboardInstanceServersImplementationsGetOutput.from_dict
    )

  def create(
    self,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    get_launch_params: Optional[str] = None,
    server_id: str = None,
    server_variant_id: str = None
  ) -> DashboardInstanceServersImplementationsCreateOutput:
    """
    Create server implementation
    Create a new server implementation for a specific server or server variant.

    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param get_launch_params: Optional[str] (optional)
    :param server_id: str (optional)
    :param server_variant_id: str (optional)
    :return: DashboardInstanceServersImplementationsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    if get_launch_params is not None:
      body_dict["get_launch_params"] = get_launch_params
    if server_id is not None:
      body_dict["server_id"] = server_id
    if server_variant_id is not None:
      body_dict["server_variant_id"] = server_variant_id

    request = MetorialRequest(path=["server-implementations"], body=body_dict)
    return self._post(request).transform(
      mapDashboardInstanceServersImplementationsCreateOutput.from_dict
    )

  def update(
    self,
    server_implementation_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    get_launch_params: Optional[str] = None
  ) -> DashboardInstanceServersImplementationsUpdateOutput:
    """
    Update server implementation
    Update metadata, launch parameters, or other fields of a server implementation.

    :param server_implementation_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param get_launch_params: Optional[str] (optional)
    :return: DashboardInstanceServersImplementationsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    if get_launch_params is not None:
      body_dict["get_launch_params"] = get_launch_params

    request = MetorialRequest(
      path=["server-implementations", server_implementation_id], body=body_dict
    )
    return self._patch(request).transform(
      mapDashboardInstanceServersImplementationsUpdateOutput.from_dict
    )

  def delete(
    self, server_implementation_id: str
  ) -> DashboardInstanceServersImplementationsDeleteOutput:
    """
    Delete server implementation
    Delete a specific server implementation from the instance.

    :param server_implementation_id: str
    :return: DashboardInstanceServersImplementationsDeleteOutput
    """
    request = MetorialRequest(path=["server-implementations", server_implementation_id])
    return self._delete(request).transform(
      mapDashboardInstanceServersImplementationsDeleteOutput.from_dict
    )
