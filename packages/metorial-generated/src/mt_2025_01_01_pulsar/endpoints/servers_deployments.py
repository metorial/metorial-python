from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServersDeploymentsListOutput,
  DashboardInstanceServersDeploymentsListOutput,
  mapDashboardInstanceServersDeploymentsListQuery,
  DashboardInstanceServersDeploymentsListQuery,
  mapDashboardInstanceServersDeploymentsGetOutput,
  DashboardInstanceServersDeploymentsGetOutput,
  mapDashboardInstanceServersDeploymentsCreateOutput,
  DashboardInstanceServersDeploymentsCreateOutput,
  mapDashboardInstanceServersDeploymentsCreateBody,
  DashboardInstanceServersDeploymentsCreateBody,
  mapDashboardInstanceServersDeploymentsUpdateOutput,
  DashboardInstanceServersDeploymentsUpdateOutput,
  mapDashboardInstanceServersDeploymentsUpdateBody,
  DashboardInstanceServersDeploymentsUpdateBody,
  mapDashboardInstanceServersDeploymentsDeleteOutput,
  DashboardInstanceServersDeploymentsDeleteOutput,
)


class MetorialServersDeploymentsEndpoint(BaseMetorialEndpoint):
  """A server deployment represents a specific instance of an MCP server that can be connected to. It contains configuration for the MCP server, such as API keys for the underlying MCP server."""

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
    server_variant_id: Optional[Union[str, List[str]]] = None,
    server_implementation_id: Optional[Union[str, List[str]]] = None,
    session_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceServersDeploymentsListOutput:
    """
    List server deployments
    Retrieve a list of server deployments within the instance. Supports filtering by status, server, variant, and session.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param server_id: Optional[Union[str, List[str]]] (optional)
    :param server_variant_id: Optional[Union[str, List[str]]] (optional)
    :param server_implementation_id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceServersDeploymentsListOutput
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
    if session_id is not None:
      query_dict["session_id"] = session_id

    request = MetorialRequest(path=["server-deployments"], query=query_dict)
    return self._get(request).transform(
      mapDashboardInstanceServersDeploymentsListOutput.from_dict
    )

  def get(
    self, server_deployment_id: str
  ) -> DashboardInstanceServersDeploymentsGetOutput:
    """
    Get server deployment
    Fetch detailed information about a specific server deployment.

    :param server_deployment_id: str
    :return: DashboardInstanceServersDeploymentsGetOutput
    """
    request = MetorialRequest(path=["server-deployments", server_deployment_id])
    return self._get(request).transform(
      mapDashboardInstanceServersDeploymentsGetOutput.from_dict
    )

  def create(
    self,
    *,
    config: Dict[str, Any],
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    oauth_config: Optional[Dict[str, Any]] = None,
    server_implementation: Dict[str, Any] = None,
    server_implementation_id: str = None,
    server_variant_id: str = None,
    server_id: str = None
  ) -> DashboardInstanceServersDeploymentsCreateOutput:
    """
    Create server deployment
    Create a new server deployment using an existing or newly defined server implementation.

    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param config: Dict[str, Any]
    :param oauth_config: Optional[Dict[str, Any]] (optional)
    :param server_implementation: Dict[str, Any] (optional)
    :param server_implementation_id: str (optional)
    :param server_variant_id: str (optional)
    :param server_id: str (optional)
    :return: DashboardInstanceServersDeploymentsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    body_dict["config"] = config
    if oauth_config is not None:
      body_dict["oauth_config"] = oauth_config
    if server_implementation is not None:
      body_dict["server_implementation"] = server_implementation
    if server_implementation_id is not None:
      body_dict["server_implementation_id"] = server_implementation_id
    if server_variant_id is not None:
      body_dict["server_variant_id"] = server_variant_id
    if server_id is not None:
      body_dict["server_id"] = server_id

    request = MetorialRequest(path=["server-deployments"], body=body_dict)
    return self._post(request).transform(
      mapDashboardInstanceServersDeploymentsCreateOutput.from_dict
    )

  def update(
    self,
    server_deployment_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    config: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceServersDeploymentsUpdateOutput:
    """
    Update server deployment
    Update metadata, configuration, or other properties of a server deployment.

    :param server_deployment_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param config: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceServersDeploymentsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    if config is not None:
      body_dict["config"] = config

    request = MetorialRequest(
      path=["server-deployments", server_deployment_id], body=body_dict
    )
    return self._patch(request).transform(
      mapDashboardInstanceServersDeploymentsUpdateOutput.from_dict
    )

  def delete(
    self, server_deployment_id: str
  ) -> DashboardInstanceServersDeploymentsDeleteOutput:
    """
    Delete server deployment
    Delete a server deployment from the instance.

    :param server_deployment_id: str
    :return: DashboardInstanceServersDeploymentsDeleteOutput
    """
    request = MetorialRequest(path=["server-deployments", server_deployment_id])
    return self._delete(request).transform(
      mapDashboardInstanceServersDeploymentsDeleteOutput.from_dict
    )
