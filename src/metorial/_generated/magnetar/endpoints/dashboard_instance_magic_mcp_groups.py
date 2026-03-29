from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMagicMcpGroupsListOutput, DashboardInstanceMagicMcpGroupsListOutput, mapDashboardInstanceMagicMcpGroupsListQuery, DashboardInstanceMagicMcpGroupsListQuery, mapDashboardInstanceMagicMcpGroupsGetOutput, DashboardInstanceMagicMcpGroupsGetOutput, mapDashboardInstanceMagicMcpGroupsCreateOutput, DashboardInstanceMagicMcpGroupsCreateOutput, mapDashboardInstanceMagicMcpGroupsCreateBody, DashboardInstanceMagicMcpGroupsCreateBody, mapDashboardInstanceMagicMcpGroupsDeleteOutput, DashboardInstanceMagicMcpGroupsDeleteOutput, mapDashboardInstanceMagicMcpGroupsUpdateOutput, DashboardInstanceMagicMcpGroupsUpdateOutput, mapDashboardInstanceMagicMcpGroupsUpdateBody, DashboardInstanceMagicMcpGroupsUpdateBody, mapDashboardInstanceMagicMcpGroupsAddServersOutput, DashboardInstanceMagicMcpGroupsAddServersOutput, mapDashboardInstanceMagicMcpGroupsAddServersBody, DashboardInstanceMagicMcpGroupsAddServersBody, mapDashboardInstanceMagicMcpGroupsRemoveServersOutput, DashboardInstanceMagicMcpGroupsRemoveServersOutput, mapDashboardInstanceMagicMcpGroupsRemoveServersBody, DashboardInstanceMagicMcpGroupsRemoveServersBody

class MetorialDashboardInstanceMagicMcpGroupsEndpoint(BaseMetorialEndpoint):
    """Magic MCP groups categorize servers and can be bound to token access."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstanceMagicMcpGroupsListOutput:
        """
    List magic MCP groups
    Returns a paginated list of magic MCP groups.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceMagicMcpGroupsListOutput
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
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpGroupsListOutput.from_dict)

    def get(self, instance_id: str, magic_mcp_group_id: str) -> DashboardInstanceMagicMcpGroupsGetOutput:
        """
    Get magic MCP group
    Retrieves a specific magic MCP group.

    :param instance_id: str
    :param magic_mcp_group_id: str
    :return: DashboardInstanceMagicMcpGroupsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups', magic_mcp_group_id]
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpGroupsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceMagicMcpGroupsCreateOutput:
        """
    Create magic MCP group
    Creates a magic MCP group.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMagicMcpGroupsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpGroupsCreateOutput.from_dict)

    def delete(self, instance_id: str, magic_mcp_group_id: str) -> DashboardInstanceMagicMcpGroupsDeleteOutput:
        """
    Delete magic MCP group
    Deletes a magic MCP group.

    :param instance_id: str
    :param magic_mcp_group_id: str
    :return: DashboardInstanceMagicMcpGroupsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups', magic_mcp_group_id]
        )
        return self._delete(request).transform(mapDashboardInstanceMagicMcpGroupsDeleteOutput.from_dict)

    def update(self, instance_id: str, magic_mcp_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceMagicMcpGroupsUpdateOutput:
        """
    Update magic MCP group
    Updates a magic MCP group.

    :param instance_id: str
    :param magic_mcp_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMagicMcpGroupsUpdateOutput
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
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups', magic_mcp_group_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceMagicMcpGroupsUpdateOutput.from_dict)

    def add_servers(self, instance_id: str, magic_mcp_group_id: str, *, magic_mcp_server_ids: List[str]) -> DashboardInstanceMagicMcpGroupsAddServersOutput:
        """
    Add servers to magic MCP group
    Adds magic MCP servers to a group.

    :param instance_id: str
    :param magic_mcp_group_id: str
    :param magic_mcp_server_ids: List[str]
    :return: DashboardInstanceMagicMcpGroupsAddServersOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["magic_mcp_server_ids"] = magic_mcp_server_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups', magic_mcp_group_id, 'add-servers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpGroupsAddServersOutput.from_dict)

    def remove_servers(self, instance_id: str, magic_mcp_group_id: str, *, magic_mcp_server_ids: List[str]) -> DashboardInstanceMagicMcpGroupsRemoveServersOutput:
        """
    Remove servers from magic MCP group
    Removes magic MCP servers from a group.

    :param instance_id: str
    :param magic_mcp_group_id: str
    :param magic_mcp_server_ids: List[str]
    :return: DashboardInstanceMagicMcpGroupsRemoveServersOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["magic_mcp_server_ids"] = magic_mcp_server_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'magic-mcp-groups', magic_mcp_group_id, 'remove-servers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpGroupsRemoveServersOutput.from_dict)