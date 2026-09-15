from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsMessagesReactionsListOutput, DashboardInstanceChatsMessagesReactionsListOutput, mapDashboardInstanceChatsMessagesReactionsListQuery, DashboardInstanceChatsMessagesReactionsListQuery, mapDashboardInstanceChatsMessagesReactionsCreateOutput, DashboardInstanceChatsMessagesReactionsCreateOutput, mapDashboardInstanceChatsMessagesReactionsCreateBody, DashboardInstanceChatsMessagesReactionsCreateBody, mapDashboardInstanceChatsMessagesReactionsDeleteOutput, DashboardInstanceChatsMessagesReactionsDeleteOutput, mapDashboardInstanceChatsMessagesReactionsDeleteQuery, DashboardInstanceChatsMessagesReactionsDeleteQuery

class MetorialManagementInstanceChatsMessagesReactionsEndpoint(BaseMetorialEndpoint):
    """Chat messages are the individual messages sent within a chat channel."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str) -> DashboardInstanceChatsMessagesReactionsListOutput:
        """
    List chat message reactions
    Returns the reactions left on a specific chat message.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :return: DashboardInstanceChatsMessagesReactionsListOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["channel_id"] = channel_id

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'messages', message_id, 'reactions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsMessagesReactionsListOutput.from_dict)

    def create(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str, emoji: Union[str, Dict[str, Any], Dict[str, Any]]) -> DashboardInstanceChatsMessagesReactionsCreateOutput:
        """
    Add chat message reaction
    Adds a reaction to a specific chat message.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :param emoji: Union[str, Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstanceChatsMessagesReactionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["channel_id"] = channel_id
        body_dict["emoji"] = emoji

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'messages', message_id, 'reactions'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatsMessagesReactionsCreateOutput.from_dict)

    def delete(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str, emoji: str) -> DashboardInstanceChatsMessagesReactionsDeleteOutput:
        """
    Remove chat message reaction
    Removes a reaction from a specific chat message.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :param emoji: str
    :return: DashboardInstanceChatsMessagesReactionsDeleteOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["channel_id"] = channel_id
        query_dict["emoji"] = emoji

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'messages', message_id, 'reactions'],
            query=query_dict
        )
        return self._delete(request).transform(mapDashboardInstanceChatsMessagesReactionsDeleteOutput.from_dict)