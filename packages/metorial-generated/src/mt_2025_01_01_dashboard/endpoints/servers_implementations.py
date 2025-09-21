from typing import Optional, Dict, Any, List, Union
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
    self, query: DashboardInstanceServersImplementationsListQuery = None
  ) -> DashboardInstanceServersImplementationsListOutput:
    """
    List server implementations
    Retrieve all server implementations in the instance. Supports filtering by status, server, or variant.

    :param query: DashboardInstanceServersImplementationsListQuery
    :return: DashboardInstanceServersImplementationsListOutput
    """
    request = MetorialRequest(
      path=["server-implementations"],
      query=mapDashboardInstanceServersImplementationsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceServersImplementationsListOutput.from_dict
    )

  def get(
    self, serverImplementationId: str
  ) -> DashboardInstanceServersImplementationsGetOutput:
    """
    Get server implementation
    Fetch detailed information about a specific server implementation.

    :param serverImplementationId: str
    :return: DashboardInstanceServersImplementationsGetOutput
    """
    request = MetorialRequest(path=["server-implementations", serverImplementationId])
    return self._get(request).transform(
      mapDashboardInstanceServersImplementationsGetOutput.from_dict
    )

  def create(self) -> DashboardInstanceServersImplementationsCreateOutput:
    """
    Create server implementation
    Create a new server implementation for a specific server or server variant.


    :return: DashboardInstanceServersImplementationsCreateOutput
    """
    {}

    request = MetorialRequest(
      path=["server-implementations"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardInstanceServersImplementationsCreateOutput.from_dict
    )

  def update(
    self,
    serverImplementationId: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    get_launch_params: Optional[str] = None
  ) -> DashboardInstanceServersImplementationsUpdateOutput:
    """
    Update server implementation
    Update metadata, launch parameters, or other fields of a server implementation.

    :param serverImplementationId: str
    :param name: str (optional)
    :param description: str (optional)
    :param metadata: Dict[str, Any] (optional)
    :param get_launch_params: str (optional)
    :return: DashboardInstanceServersImplementationsUpdateOutput
    """
    _params = {
      "name": name,
      "description": description,
      "metadata": metadata,
      "get_launch_params": get_launch_params,
    }
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["server-implementations", serverImplementationId],
      body=body,
    )
    return self._patch(request).transform(
      mapDashboardInstanceServersImplementationsUpdateOutput.from_dict
    )

  def delete(
    self, serverImplementationId: str
  ) -> DashboardInstanceServersImplementationsDeleteOutput:
    """
    Delete server implementation
    Delete a specific server implementation from the instance.

    :param serverImplementationId: str
    :return: DashboardInstanceServersImplementationsDeleteOutput
    """
    request = MetorialRequest(path=["server-implementations", serverImplementationId])
    return self._delete(request).transform(
      mapDashboardInstanceServersImplementationsDeleteOutput.from_dict
    )
