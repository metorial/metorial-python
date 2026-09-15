from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsChannelsMembersListOutput, DashboardInstanceChatsChannelsMembersListOutput, mapDashboardInstanceChatsChannelsMembersListQuery, DashboardInstanceChatsChannelsMembersListQuery, mapDashboardInstanceChatsChannelsMembersGetOutput, DashboardInstanceChatsChannelsMembersGetOutput

class MetorialManagementInstanceChatsChannelsMembersEndpoint(BaseMetorialEndpoint):
    """Chat channels are the conversations within a chat, such as Slack channels or Microsoft Teams channels."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, chat_id: str, channel_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceChatsChannelsMembersListOutput:
        """
    List chat channel members
    Returns a paginated list of members of a chat channel.

    :param instance_id: str
    :param chat_id: str
    :param channel_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceChatsChannelsMembersListOutput
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

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'channels', channel_id, 'members'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsChannelsMembersListOutput.from_dict)

    def get(self, instance_id: str, chat_id: str, channel_id: str, user_id: str) -> DashboardInstanceChatsChannelsMembersGetOutput:
        """
    Get chat channel member
    Retrieves a specific member of a chat channel.

    :param instance_id: str
    :param chat_id: str
    :param channel_id: str
    :param user_id: str
    :return: DashboardInstanceChatsChannelsMembersGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'channels', channel_id, 'members', user_id]
        )
        return self._get(request).transform(mapDashboardInstanceChatsChannelsMembersGetOutput.from_dict)