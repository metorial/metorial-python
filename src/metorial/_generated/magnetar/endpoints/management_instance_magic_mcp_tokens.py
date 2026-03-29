from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMagicMcpTokensListOutput, DashboardInstanceMagicMcpTokensListOutput, mapDashboardInstanceMagicMcpTokensListQuery, DashboardInstanceMagicMcpTokensListQuery, mapDashboardInstanceMagicMcpTokensGetOutput, DashboardInstanceMagicMcpTokensGetOutput, mapDashboardInstanceMagicMcpTokensCreateOutput, DashboardInstanceMagicMcpTokensCreateOutput, mapDashboardInstanceMagicMcpTokensCreateBody, DashboardInstanceMagicMcpTokensCreateBody, mapDashboardInstanceMagicMcpTokensDeleteOutput, DashboardInstanceMagicMcpTokensDeleteOutput, mapDashboardInstanceMagicMcpTokensUpdateOutput, DashboardInstanceMagicMcpTokensUpdateOutput, mapDashboardInstanceMagicMcpTokensUpdateBody, DashboardInstanceMagicMcpTokensUpdateBody, mapDashboardInstanceMagicMcpTokensAddGroupsOutput, DashboardInstanceMagicMcpTokensAddGroupsOutput, mapDashboardInstanceMagicMcpTokensAddGroupsBody, DashboardInstanceMagicMcpTokensAddGroupsBody, mapDashboardInstanceMagicMcpTokensRemoveGroupsOutput, DashboardInstanceMagicMcpTokensRemoveGroupsOutput, mapDashboardInstanceMagicMcpTokensRemoveGroupsBody, DashboardInstanceMagicMcpTokensRemoveGroupsBody

class MetorialManagementInstanceMagicMcpTokensEndpoint(BaseMetorialEndpoint):
    """Magic MCP tokens authorize access to Magic MCP servers via the /magic connection API."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, magic_mcp_group_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceMagicMcpTokensListOutput:
        """
    List magic MCP tokens
    Returns a paginated list of magic MCP tokens.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param magic_mcp_group_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceMagicMcpTokensListOutput
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

        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-tokens'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpTokensListOutput.from_dict)

    def get(self, instance_id: str, magic_mcp_token_id: str) -> DashboardInstanceMagicMcpTokensGetOutput:
        """
    Get magic MCP token
    Retrieves a specific magic MCP token.

    :param instance_id: str
    :param magic_mcp_token_id: str
    :return: DashboardInstanceMagicMcpTokensGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-tokens', magic_mcp_token_id]
        )
        return self._get(request).transform(mapDashboardInstanceMagicMcpTokensGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, group_ids: Optional[List[str]] = None) -> DashboardInstanceMagicMcpTokensCreateOutput:
        """
    Create magic MCP token
    Creates a new magic MCP token.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param group_ids: Optional[List[str]] (optional)
    :return: DashboardInstanceMagicMcpTokensCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if group_ids is not None:
            body_dict["group_ids"] = group_ids

        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-tokens'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpTokensCreateOutput.from_dict)

    def delete(self, instance_id: str, magic_mcp_token_id: str) -> DashboardInstanceMagicMcpTokensDeleteOutput:
        """
    Delete magic MCP token
    Deletes a magic MCP token.

    :param instance_id: str
    :param magic_mcp_token_id: str
    :return: DashboardInstanceMagicMcpTokensDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-tokens', magic_mcp_token_id]
        )
        return self._delete(request).transform(mapDashboardInstanceMagicMcpTokensDeleteOutput.from_dict)

    def update(self, instance_id: str, magic_mcp_token_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceMagicMcpTokensUpdateOutput:
        """
    Update magic MCP token
    Updates a magic MCP token.

    :param instance_id: str
    :param magic_mcp_token_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMagicMcpTokensUpdateOutput
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
            path=['instances', instance_id, 'magic-mcp-tokens', magic_mcp_token_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceMagicMcpTokensUpdateOutput.from_dict)

    def add_groups(self, instance_id: str, magic_mcp_token_id: str, *, magic_mcp_group_ids: List[str]) -> DashboardInstanceMagicMcpTokensAddGroupsOutput:
        """
    Add magic MCP groups to token
    Adds groups to a magic MCP token.

    :param instance_id: str
    :param magic_mcp_token_id: str
    :param magic_mcp_group_ids: List[str]
    :return: DashboardInstanceMagicMcpTokensAddGroupsOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["magic_mcp_group_ids"] = magic_mcp_group_ids

        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-tokens', magic_mcp_token_id, 'add-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpTokensAddGroupsOutput.from_dict)

    def remove_groups(self, instance_id: str, magic_mcp_token_id: str, *, magic_mcp_group_ids: List[str]) -> DashboardInstanceMagicMcpTokensRemoveGroupsOutput:
        """
    Remove magic MCP groups from token
    Removes groups from a magic MCP token.

    :param instance_id: str
    :param magic_mcp_token_id: str
    :param magic_mcp_group_ids: List[str]
    :return: DashboardInstanceMagicMcpTokensRemoveGroupsOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["magic_mcp_group_ids"] = magic_mcp_group_ids

        request = MetorialRequest(
            path=['instances', instance_id, 'magic-mcp-tokens', magic_mcp_token_id, 'remove-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceMagicMcpTokensRemoveGroupsOutput.from_dict)