from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsChannelsListOutput, DashboardInstanceChatsChannelsListOutput, mapDashboardInstanceChatsChannelsListQuery, DashboardInstanceChatsChannelsListQuery, mapDashboardInstanceChatsChannelsGetOutput, DashboardInstanceChatsChannelsGetOutput

class MetorialChatsChannelsEndpoint(BaseMetorialEndpoint):
    """Chat channels are the conversations within a chat, such as Slack channels or Microsoft Teams channels."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, chat_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, workspace_id: Optional[str] = None, type: Optional[str] = None, search: Optional[str] = None) -> DashboardInstanceChatsChannelsListOutput:
        """
    List chat channels
    Returns a paginated list of channels for a chat.

    :param chat_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param workspace_id: Optional[str] (optional)
    :param type: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceChatsChannelsListOutput
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
        if workspace_id is not None:
            query_dict["workspace_id"] = workspace_id
        if type is not None:
            query_dict["type"] = type
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['chats', chat_id, 'channels'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsChannelsListOutput.from_dict)

    def get(self, chat_id: str, channel_id: str) -> DashboardInstanceChatsChannelsGetOutput:
        """
    Get chat channel
    Retrieves a specific chat channel.

    :param chat_id: str
    :param channel_id: str
    :return: DashboardInstanceChatsChannelsGetOutput
    """
        request = MetorialRequest(
            path=['chats', chat_id, 'channels', channel_id]
        )
        return self._get(request).transform(mapDashboardInstanceChatsChannelsGetOutput.from_dict)