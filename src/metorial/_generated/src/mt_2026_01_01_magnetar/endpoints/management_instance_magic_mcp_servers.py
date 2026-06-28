from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMagicMcpServersListOutput, DashboardInstanceMagicMcpServersListOutput, mapDashboardInstanceMagicMcpServersListQuery, DashboardInstanceMagicMcpServersListQuery, mapDashboardInstanceMagicMcpServersGetOutput, DashboardInstanceMagicMcpServersGetOutput, mapDashboardInstanceMagicMcpServersToolsOutput, DashboardInstanceMagicMcpServersToolsOutput, mapDashboardInstanceMagicMcpServersCreateOutput, DashboardInstanceMagicMcpServersCreateOutput, mapDashboardInstanceMagicMcpServersCreateBody, DashboardInstanceMagicMcpServersCreateBody, mapDashboardInstanceMagicMcpServersDeleteOutput, DashboardInstanceMagicMcpServersDeleteOutput, mapDashboardInstanceMagicMcpServersUpdateOutput, DashboardInstanceMagicMcpServersUpdateOutput, mapDashboardInstanceMagicMcpServersUpdateBody, DashboardInstanceMagicMcpServersUpdateBody

class MetorialManagementInstanceMagicMcpServersEndpoint(BaseMetorialEndpoint):
    """Magic MCP servers are stable MCP entrypoints backed by one Subspace session template."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, magic_mcp_group_id: Optional[Union[str, List[str]]] = None, provider_template_id: Optional[Union[str, List[str]]] = None, integration_instance_id: Optional[Union[str, List[str]]] = None, owner: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, consumer_id: Optional[Union[str, List[str]]] = None, consumer_profile_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, preconfigured_only: Optional[bool] = None) -> DashboardInstanceMagicMcpServersListOutput:
        """
    List magic MCP servers
    Returns a paginated list of magic MCP servers.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param magic_mcp_group_id: Optional[Union[str, List[str]]] (optional)
    :param provider_template_id: Optional[Union[str, List[str]]] (optional)
    :param integration_instance_id: Optional[Union[str, List[str]]] (optional)
    :param owner: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_profile_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param preconfigured_only: Optional[bool] (optional)
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
        if magic_mcp_group_id is not None:
            query_dict["magic_mcp_group_id"] = magic_mcp_group_id
        if provider_template_id is not None:
            query_dict["provider_template_id"] = provider_template_id
        if integration_instance_id is not None:
            query_dict["integration_instance_id"] = integration_instance_id
        if owner is not None:
            query_dict["owner"] = owner
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if consumer_profile_id is not None:
            query_dict["consumer_profile_id"] = consumer_profile_id
        if search is not None:
            query_dict["search"] = search
        if id is not None:
            query_dict["id"] = id
        if preconfigured_only is not None:
            query_dict["preconfigured_only"] = preconfigured_only

        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-servers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpServersListOutput.from_dict)

    def get(self, instance_id: str, magic_mcp_server_id: str) -> DashboardInstanceMagicMcpServersGetOutput:
        """
    Get magic MCP server
    Retrieves a specific magic MCP server.

    :param instance_id: str
    :param magic_mcp_server_id: str
    :return: DashboardInstanceMagicMcpServersGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-servers', magic_mcp_server_id]
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpServersGetOutput.from_dict)

    def tools(self, instance_id: str, magic_mcp_server_id: str) -> DashboardInstanceMagicMcpServersToolsOutput:
        """
    List magic MCP server tools
    Returns the effective set of tools available through the providers backing a magic MCP server.

    :param instance_id: str
    :param magic_mcp_server_id: str
    :return: DashboardInstanceMagicMcpServersToolsOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-servers', magic_mcp_server_id, 'tools']
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpServersToolsOutput.from_dict)

    def create(self, instance_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_template_id: Optional[str] = None, integration_instance_id: Optional[str] = None, consumer_profile_id: Optional[str] = None) -> DashboardInstanceMagicMcpServersCreateOutput:
        """
    Create magic MCP server
    Creates a magic MCP server with a new session template. A Subspace session is created automatically on first connection and then reused.

    :param instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_template_id: Optional[str] (optional)
    :param integration_instance_id: Optional[str] (optional)
    :param consumer_profile_id: Optional[str] (optional)
    :return: DashboardInstanceMagicMcpServersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if provider_template_id is not None:
            body_dict["provider_template_id"] = provider_template_id
        if integration_instance_id is not None:
            body_dict["integration_instance_id"] = integration_instance_id
        if consumer_profile_id is not None:
            body_dict["consumer_profile_id"] = consumer_profile_id

        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-servers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpServersCreateOutput.from_dict)

    def delete(self, instance_id: str, magic_mcp_server_id: str) -> DashboardInstanceMagicMcpServersDeleteOutput:
        """
    Delete magic MCP server
    Archives a magic MCP server.

    :param instance_id: str
    :param magic_mcp_server_id: str
    :return: DashboardInstanceMagicMcpServersDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-servers', magic_mcp_server_id]
        )
        return self._delete(request).transform(mapDashboardInstanceMagicMcpServersDeleteOutput.from_dict)

    def update(self, instance_id: str, magic_mcp_server_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, aliases: Optional[List[str]] = None) -> DashboardInstanceMagicMcpServersUpdateOutput:
        """
    Update magic MCP server
    Updates a magic MCP server.

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
            path=['instances', instance_id, 'magic-mcp-servers', magic_mcp_server_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceMagicMcpServersUpdateOutput.from_dict)