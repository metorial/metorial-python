from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatWorkspacesListOutput, DashboardInstanceChatWorkspacesListOutput, mapDashboardInstanceChatWorkspacesListQuery, DashboardInstanceChatWorkspacesListQuery, mapDashboardInstanceChatWorkspacesGetOutput, DashboardInstanceChatWorkspacesGetOutput, mapDashboardInstanceChatWorkspacesGetQuery, DashboardInstanceChatWorkspacesGetQuery

class MetorialManagementInstanceChatWorkspacesEndpoint(BaseMetorialEndpoint):
    """Chat workspaces group channels together, for chat providers that organize conversations that way."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, chat_instance_id: str, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None) -> DashboardInstanceChatWorkspacesListOutput:
        """
    List chat workspaces
    Returns a paginated list of workspaces for a chat instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param chat_instance_id: str
    :param search: Optional[str] (optional)
    :return: DashboardInstanceChatWorkspacesListOutput
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
        query_dict["chat_instance_id"] = chat_instance_id
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'workspaces'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatWorkspacesListOutput.from_dict)

    def get(self, instance_id: str, chat_workspace_id: str, *, chat_instance_id: str) -> DashboardInstanceChatWorkspacesGetOutput:
        """
    Get chat workspace
    Retrieves a specific chat workspace.

    :param instance_id: str
    :param chat_workspace_id: str
    :param chat_instance_id: str
    :return: DashboardInstanceChatWorkspacesGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["chat_instance_id"] = chat_instance_id

        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'workspaces', chat_workspace_id],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatWorkspacesGetOutput.from_dict)