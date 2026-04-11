from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMagicMcpServersProvidersListOutput, DashboardInstanceMagicMcpServersProvidersListOutput, mapDashboardInstanceMagicMcpServersProvidersListQuery, DashboardInstanceMagicMcpServersProvidersListQuery, mapDashboardInstanceMagicMcpServersProvidersGetOutput, DashboardInstanceMagicMcpServersProvidersGetOutput, mapDashboardInstanceMagicMcpServersProvidersCreateOutput, DashboardInstanceMagicMcpServersProvidersCreateOutput, mapDashboardInstanceMagicMcpServersProvidersCreateBody, DashboardInstanceMagicMcpServersProvidersCreateBody, mapDashboardInstanceMagicMcpServersProvidersUpdateOutput, DashboardInstanceMagicMcpServersProvidersUpdateOutput, mapDashboardInstanceMagicMcpServersProvidersUpdateBody, DashboardInstanceMagicMcpServersProvidersUpdateBody, mapDashboardInstanceMagicMcpServersProvidersDeleteOutput, DashboardInstanceMagicMcpServersProvidersDeleteOutput

class MetorialMagicMcpServersProvidersEndpoint(BaseMetorialEndpoint):
    """Magic MCP server providers define which providers are included in the setup session template backing a magic MCP server."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, magic_mcp_server_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceMagicMcpServersProvidersListOutput:
        """
    List magic MCP server providers
    Returns a paginated list of providers configured for a magic MCP server.

    :param magic_mcp_server_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMagicMcpServersProvidersListOutput
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
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['magic-mcp-servers', magic_mcp_server_id, 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpServersProvidersListOutput.from_dict)

    def get(self, magic_mcp_server_id: str, magic_mcp_server_provider_id: str) -> DashboardInstanceMagicMcpServersProvidersGetOutput:
        """
    Get magic MCP server provider
    Retrieves a specific provider configuration from a magic MCP server.

    :param magic_mcp_server_id: str
    :param magic_mcp_server_provider_id: str
    :return: DashboardInstanceMagicMcpServersProvidersGetOutput
    """
        request = MetorialRequest(
            path=['magic-mcp-servers', magic_mcp_server_id, 'providers', magic_mcp_server_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpServersProvidersGetOutput.from_dict)

    def create(self, magic_mcp_server_id: str, *, provider_deployment_id: Optional[str] = None, provider_config_id: Optional[str] = None, provider_config_vault_id: Optional[str] = None, provider_auth_config_id: Optional[str] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceMagicMcpServersProvidersCreateOutput:
        """
    Create magic MCP server provider
    Adds a new provider configuration to a magic MCP server.

    :param magic_mcp_server_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param provider_config_vault_id: Optional[str] (optional)
    :param provider_auth_config_id: Optional[str] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceMagicMcpServersProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if provider_config_vault_id is not None:
            body_dict["provider_config_vault_id"] = provider_config_vault_id
        if provider_auth_config_id is not None:
            body_dict["provider_auth_config_id"] = provider_auth_config_id
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['magic-mcp-servers', magic_mcp_server_id, 'providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpServersProvidersCreateOutput.from_dict)

    def update(self, magic_mcp_server_id: str, magic_mcp_server_provider_id: str, *, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceMagicMcpServersProvidersUpdateOutput:
        """
    Update magic MCP server provider
    Updates a provider configuration in a magic MCP server.

    :param magic_mcp_server_id: str
    :param magic_mcp_server_provider_id: str
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceMagicMcpServersProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['magic-mcp-servers', magic_mcp_server_id, 'providers', magic_mcp_server_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceMagicMcpServersProvidersUpdateOutput.from_dict)

    def delete(self, magic_mcp_server_id: str, magic_mcp_server_provider_id: str) -> DashboardInstanceMagicMcpServersProvidersDeleteOutput:
        """
    Delete magic MCP server provider
    Removes a provider configuration from a magic MCP server.

    :param magic_mcp_server_id: str
    :param magic_mcp_server_provider_id: str
    :return: DashboardInstanceMagicMcpServersProvidersDeleteOutput
    """
        request = MetorialRequest(
            path=['magic-mcp-servers', magic_mcp_server_id, 'providers', magic_mcp_server_provider_id]
        )
        return self._delete(request).transform(mapDashboardInstanceMagicMcpServersProvidersDeleteOutput.from_dict)