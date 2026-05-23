from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceConversationsMessagesListOutput, DashboardInstanceConversationsMessagesListOutput, mapDashboardInstanceConversationsMessagesListQuery, DashboardInstanceConversationsMessagesListQuery, mapDashboardInstanceConversationsMessagesCreateOutput, DashboardInstanceConversationsMessagesCreateOutput, mapDashboardInstanceConversationsMessagesCreateBody, DashboardInstanceConversationsMessagesCreateBody, mapDashboardInstanceConversationsMessagesGetOutput, DashboardInstanceConversationsMessagesGetOutput

class MetorialConversationsMessagesEndpoint(BaseMetorialEndpoint):
    """Assistant and conversation endpoints"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, assistant_conversation_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceConversationsMessagesListOutput:
        """
    List assistant messages
    List messages in a specific assistant conversation.

    :param assistant_conversation_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceConversationsMessagesListOutput
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
            path=['conversations', assistant_conversation_id, 'messages'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceConversationsMessagesListOutput.from_dict)

    def create(self, assistant_conversation_id: str, *, message: Dict[str, Any], parent_message_id: Optional[str] = None, model_id: Optional[str] = None) -> DashboardInstanceConversationsMessagesCreateOutput:
        """
    Create assistant message
    Create a user message and assistant request in a specific conversation.

    :param assistant_conversation_id: str
    :param message: Dict[str, Any]
    :param parent_message_id: Optional[str] (optional)
    :param model_id: Optional[str] (optional)
    :return: DashboardInstanceConversationsMessagesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["message"] = message
        if parent_message_id is not None:
            body_dict["parent_message_id"] = parent_message_id
        if model_id is not None:
            body_dict["model_id"] = model_id

        request = MetorialRequest(
            path=['conversations', assistant_conversation_id, 'messages'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceConversationsMessagesCreateOutput.from_dict)

    def get(self, assistant_conversation_id: str, assistant_message_id: str) -> DashboardInstanceConversationsMessagesGetOutput:
        """
    Get assistant message
    Get a specific assistant message.

    :param assistant_conversation_id: str
    :param assistant_message_id: str
    :return: DashboardInstanceConversationsMessagesGetOutput
    """
        request = MetorialRequest(
            path=['conversations', assistant_conversation_id, 'messages', assistant_message_id]
        )
        return self._get(request).transform(mapDashboardInstanceConversationsMessagesGetOutput.from_dict)