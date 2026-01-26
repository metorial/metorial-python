from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceMagicMcpServersListOutput,
  DashboardInstanceMagicMcpServersListOutput,
  mapDashboardInstanceMagicMcpServersListQuery,
  DashboardInstanceMagicMcpServersListQuery,
  mapDashboardInstanceMagicMcpServersGetOutput,
  DashboardInstanceMagicMcpServersGetOutput,
  mapDashboardInstanceMagicMcpServersCreateOutput,
  DashboardInstanceMagicMcpServersCreateOutput,
  mapDashboardInstanceMagicMcpServersCreateBody,
  DashboardInstanceMagicMcpServersCreateBody,
  mapDashboardInstanceMagicMcpServersDeleteOutput,
  DashboardInstanceMagicMcpServersDeleteOutput,
  mapDashboardInstanceMagicMcpServersUpdateOutput,
  DashboardInstanceMagicMcpServersUpdateOutput,
  mapDashboardInstanceMagicMcpServersUpdateBody,
  DashboardInstanceMagicMcpServersUpdateBody,
)


class MetorialManagementInstanceMagicMcpServersEndpoint(BaseMetorialEndpoint):
  """Before you can connect to an MCP server, you need to create a magic MCP server."""

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
    session_id: Optional[Union[str, List[str]]] = None,
    search: Optional[str] = None
  ) -> DashboardInstanceMagicMcpServersListOutput:
    """
    List magic MCP server
    List all magic MCP server

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
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceMagicMcpServersListOutput
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
    if search is not None:
      query_dict["search"] = search

    request = MetorialRequest(
      path=["instances", instance_id, "magic-mcp-servers"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceMagicMcpServersListOutput.from_dict
    )

  def get(
    self, instance_id: str, magic_mcp_server_id: str
  ) -> DashboardInstanceMagicMcpServersGetOutput:
    """
    Get magic MCP server
    Get the information of a specific magic MCP server

    :param instance_id: str
    :param magic_mcp_server_id: str
    :return: DashboardInstanceMagicMcpServersGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "magic-mcp-servers", magic_mcp_server_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceMagicMcpServersGetOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    *,
    server_implementation: Dict[str, Any] = None,
    server_implementation_id: str = None,
    server_variant_id: str = None,
    server_id: str = None
  ) -> DashboardInstanceMagicMcpServersCreateOutput:
    """
    Create magic MCP server
    Create a new magic MCP server

    :param instance_id: str
    :param server_implementation: Dict[str, Any] (optional)
    :param server_implementation_id: str (optional)
    :param server_variant_id: str (optional)
    :param server_id: str (optional)
    :return: DashboardInstanceMagicMcpServersCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if server_implementation is not None:
      body_dict["server_implementation"] = server_implementation
    if server_implementation_id is not None:
      body_dict["server_implementation_id"] = server_implementation_id
    if server_variant_id is not None:
      body_dict["server_variant_id"] = server_variant_id
    if server_id is not None:
      body_dict["server_id"] = server_id

    request = MetorialRequest(
      path=["instances", instance_id, "magic-mcp-servers"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardInstanceMagicMcpServersCreateOutput.from_dict
    )

  def delete(
    self, instance_id: str, magic_mcp_server_id: str
  ) -> DashboardInstanceMagicMcpServersDeleteOutput:
    """
    Delete magic MCP server
    Delete a specific magic MCP server

    :param instance_id: str
    :param magic_mcp_server_id: str
    :return: DashboardInstanceMagicMcpServersDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "magic-mcp-servers", magic_mcp_server_id]
    )
    return self._delete(request).transform(
      mapDashboardInstanceMagicMcpServersDeleteOutput.from_dict
    )

  def update(
    self,
    instance_id: str,
    magic_mcp_server_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    aliases: Optional[List[str]] = None
  ) -> DashboardInstanceMagicMcpServersUpdateOutput:
    """
    Update magic MCP server
    Update the information of a specific magic MCP server

    :param instance_id: str
    :param magic_mcp_server_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param aliases: Optional[List[str]] (optional)
    :return: DashboardInstanceMagicMcpServersUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    if aliases is not None:
      body_dict["aliases"] = aliases

    request = MetorialRequest(
      path=["instances", instance_id, "magic-mcp-servers", magic_mcp_server_id],
      body=body_dict,
    )
    return self._patch(request).transform(
      mapDashboardInstanceMagicMcpServersUpdateOutput.from_dict
    )
