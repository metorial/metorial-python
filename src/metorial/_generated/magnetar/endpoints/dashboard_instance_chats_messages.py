from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsMessagesListOutput, DashboardInstanceChatsMessagesListOutput, mapDashboardInstanceChatsMessagesListQuery, DashboardInstanceChatsMessagesListQuery, mapDashboardInstanceChatsMessagesGetOutput, DashboardInstanceChatsMessagesGetOutput, mapDashboardInstanceChatsMessagesGetQuery, DashboardInstanceChatsMessagesGetQuery, mapDashboardInstanceChatsMessagesCreateOutput, DashboardInstanceChatsMessagesCreateOutput, mapDashboardInstanceChatsMessagesCreateBody, DashboardInstanceChatsMessagesCreateBody, mapDashboardInstanceChatsMessagesUpdateOutput, DashboardInstanceChatsMessagesUpdateOutput, mapDashboardInstanceChatsMessagesUpdateBody, DashboardInstanceChatsMessagesUpdateBody, mapDashboardInstanceChatsMessagesDeleteOutput, DashboardInstanceChatsMessagesDeleteOutput, mapDashboardInstanceChatsMessagesDeleteQuery, DashboardInstanceChatsMessagesDeleteQuery, mapDashboardInstanceChatsMessagesReadOutput, DashboardInstanceChatsMessagesReadOutput, mapDashboardInstanceChatsMessagesReadBody, DashboardInstanceChatsMessagesReadBody

class MetorialDashboardInstanceChatsMessagesEndpoint(BaseMetorialEndpoint):
    """Chat messages are the individual messages sent within a chat channel."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, chat_id: str, *, channel_id: str, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, thread_id: Optional[str] = None, search: Optional[str] = None) -> DashboardInstanceChatsMessagesListOutput:
        """
    List chat messages
    Returns a paginated list of messages in a chat channel.

    :param instance_id: str
    :param chat_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param channel_id: str
    :param thread_id: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceChatsMessagesListOutput
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
        query_dict["channel_id"] = channel_id
        if thread_id is not None:
            query_dict["thread_id"] = thread_id
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'messages'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsMessagesListOutput.from_dict)

    def get(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str) -> DashboardInstanceChatsMessagesGetOutput:
        """
    Get chat message
    Retrieves a specific chat message.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :return: DashboardInstanceChatsMessagesGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["channel_id"] = channel_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'messages', message_id],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsMessagesGetOutput.from_dict)

    def create(self, instance_id: str, chat_id: str, *, channel_id: str, parts: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]], thread_id: Optional[str] = None, alt_text: Optional[str] = None, attachments: Optional[List[Dict[str, Any]]] = None, reply_message_id: Optional[str] = None, ephemeral_target_user_id: Optional[str] = None) -> DashboardInstanceChatsMessagesCreateOutput:
        """
    Send chat message
    Sends a new message to a chat channel.

    :param instance_id: str
    :param chat_id: str
    :param channel_id: str
    :param thread_id: Optional[str] (optional)
    :param parts: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]
    :param alt_text: Optional[str] (optional)
    :param attachments: Optional[List[Dict[str, Any]]] (optional)
    :param reply_message_id: Optional[str] (optional)
    :param ephemeral_target_user_id: Optional[str] (optional)
    :return: DashboardInstanceChatsMessagesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["channel_id"] = channel_id
        if thread_id is not None:
            body_dict["thread_id"] = thread_id
        body_dict["parts"] = parts
        if alt_text is not None:
            body_dict["alt_text"] = alt_text
        if attachments is not None:
            body_dict["attachments"] = attachments
        if reply_message_id is not None:
            body_dict["reply_message_id"] = reply_message_id
        if ephemeral_target_user_id is not None:
            body_dict["ephemeral_target_user_id"] = ephemeral_target_user_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'messages'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatsMessagesCreateOutput.from_dict)

    def update(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str, parts: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]], alt_text: Optional[str] = None) -> DashboardInstanceChatsMessagesUpdateOutput:
        """
    Edit chat message
    Edits a specific chat message.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :param parts: List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]
    :param alt_text: Optional[str] (optional)
    :return: DashboardInstanceChatsMessagesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["channel_id"] = channel_id
        body_dict["parts"] = parts
        if alt_text is not None:
            body_dict["alt_text"] = alt_text

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'messages', message_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceChatsMessagesUpdateOutput.from_dict)

    def delete(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str) -> DashboardInstanceChatsMessagesDeleteOutput:
        """
    Delete chat message
    Deletes a specific chat message.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :return: DashboardInstanceChatsMessagesDeleteOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["channel_id"] = channel_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'messages', message_id],
            query=query_dict
        )
        return self._delete(request).transform(mapDashboardInstanceChatsMessagesDeleteOutput.from_dict)

    def read(self, instance_id: str, chat_id: str, message_id: str, *, channel_id: str, thread_id: Optional[str] = None) -> DashboardInstanceChatsMessagesReadOutput:
        """
    Mark chat message read
    Marks a specific chat message as read.

    :param instance_id: str
    :param chat_id: str
    :param message_id: str
    :param channel_id: str
    :param thread_id: Optional[str] (optional)
    :return: DashboardInstanceChatsMessagesReadOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["channel_id"] = channel_id
        if thread_id is not None:
            body_dict["thread_id"] = thread_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'chats', chat_id, 'messages', message_id, 'read'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatsMessagesReadOutput.from_dict)