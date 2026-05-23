from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMagicMcpEndpointsListOutput, DashboardInstanceMagicMcpEndpointsListOutput, mapDashboardInstanceMagicMcpEndpointsListQuery, DashboardInstanceMagicMcpEndpointsListQuery, mapDashboardInstanceMagicMcpEndpointsGetOutput, DashboardInstanceMagicMcpEndpointsGetOutput, mapDashboardInstanceMagicMcpEndpointsCreateOutput, DashboardInstanceMagicMcpEndpointsCreateOutput, mapDashboardInstanceMagicMcpEndpointsCreateBody, DashboardInstanceMagicMcpEndpointsCreateBody, mapDashboardInstanceMagicMcpEndpointsDeleteOutput, DashboardInstanceMagicMcpEndpointsDeleteOutput, mapDashboardInstanceMagicMcpEndpointsUpdateOutput, DashboardInstanceMagicMcpEndpointsUpdateOutput, mapDashboardInstanceMagicMcpEndpointsUpdateBody, DashboardInstanceMagicMcpEndpointsUpdateBody, mapDashboardInstanceMagicMcpEndpointsAddServersOutput, DashboardInstanceMagicMcpEndpointsAddServersOutput, mapDashboardInstanceMagicMcpEndpointsAddServersBody, DashboardInstanceMagicMcpEndpointsAddServersBody, mapDashboardInstanceMagicMcpEndpointsRemoveServersOutput, DashboardInstanceMagicMcpEndpointsRemoveServersOutput, mapDashboardInstanceMagicMcpEndpointsRemoveServersBody, DashboardInstanceMagicMcpEndpointsRemoveServersBody

class MetorialDashboardInstanceMagicMcpEndpointsEndpoint(BaseMetorialEndpoint):
    """Magic MCP endpoints combine multiple Magic MCP servers behind one routed connection target."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, magic_mcp_server_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstanceMagicMcpEndpointsListOutput:
        """
    List magic MCP endpoints
    Returns a paginated list of magic MCP endpoints.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param magic_mcp_server_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceMagicMcpEndpointsListOutput
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
        if magic_mcp_server_id is not None:
            query_dict["magic_mcp_server_id"] = magic_mcp_server_id
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpEndpointsListOutput.from_dict)

    def get(self, instance_id: str, magic_mcp_endpoint_id: str) -> DashboardInstanceMagicMcpEndpointsGetOutput:
        """
    Get magic MCP endpoint
    Retrieves a specific magic MCP endpoint.

    :param instance_id: str
    :param magic_mcp_endpoint_id: str
    :return: DashboardInstanceMagicMcpEndpointsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints', magic_mcp_endpoint_id]
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpEndpointsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, consumer_profile_id: Optional[str] = None, skill_plugin_id: Optional[str] = None, magic_mcp_servers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceMagicMcpEndpointsCreateOutput:
        """
    Create magic MCP endpoint
    Creates a magic MCP endpoint.

    :param instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param consumer_profile_id: Optional[str] (optional)
    :param skill_plugin_id: Optional[str] (optional)
    :param magic_mcp_servers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceMagicMcpEndpointsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if consumer_profile_id is not None:
            body_dict["consumer_profile_id"] = consumer_profile_id
        if skill_plugin_id is not None:
            body_dict["skill_plugin_id"] = skill_plugin_id
        if magic_mcp_servers is not None:
            body_dict["magic_mcp_servers"] = magic_mcp_servers

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpEndpointsCreateOutput.from_dict)

    def delete(self, instance_id: str, magic_mcp_endpoint_id: str) -> DashboardInstanceMagicMcpEndpointsDeleteOutput:
        """
    Delete magic MCP endpoint
    Archives a magic MCP endpoint.

    :param instance_id: str
    :param magic_mcp_endpoint_id: str
    :return: DashboardInstanceMagicMcpEndpointsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints', magic_mcp_endpoint_id]
        )
        return self._delete(request).transform(mapDashboardInstanceMagicMcpEndpointsDeleteOutput.from_dict)

    def update(self, instance_id: str, magic_mcp_endpoint_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceMagicMcpEndpointsUpdateOutput:
        """
    Update magic MCP endpoint
    Updates a magic MCP endpoint.

    :param instance_id: str
    :param magic_mcp_endpoint_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMagicMcpEndpointsUpdateOutput
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
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints', magic_mcp_endpoint_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceMagicMcpEndpointsUpdateOutput.from_dict)

    def add_servers(self, instance_id: str, magic_mcp_endpoint_id: str, *, magic_mcp_servers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceMagicMcpEndpointsAddServersOutput:
        """
    Add servers to magic MCP endpoint
    Adds magic MCP servers to a magic MCP endpoint.

    :param instance_id: str
    :param magic_mcp_endpoint_id: str
    :param magic_mcp_servers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceMagicMcpEndpointsAddServersOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if magic_mcp_servers is not None:
            body_dict["magic_mcp_servers"] = magic_mcp_servers

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints', magic_mcp_endpoint_id, 'add-servers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpEndpointsAddServersOutput.from_dict)

    def remove_servers(self, instance_id: str, magic_mcp_endpoint_id: str, *, magic_mcp_server_ids: List[str]) -> DashboardInstanceMagicMcpEndpointsRemoveServersOutput:
        """
    Remove servers from magic MCP endpoint
    Removes magic MCP servers from a magic MCP endpoint.

    :param instance_id: str
    :param magic_mcp_endpoint_id: str
    :param magic_mcp_server_ids: List[str]
    :return: DashboardInstanceMagicMcpEndpointsRemoveServersOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["magic_mcp_server_ids"] = magic_mcp_server_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-endpoints', magic_mcp_endpoint_id, 'remove-servers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpEndpointsRemoveServersOutput.from_dict)