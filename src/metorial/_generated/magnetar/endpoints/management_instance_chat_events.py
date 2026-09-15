from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatEventsListOutput, DashboardInstanceChatEventsListOutput, mapDashboardInstanceChatEventsListQuery, DashboardInstanceChatEventsListQuery, mapDashboardInstanceChatEventsGetOutput, DashboardInstanceChatEventsGetOutput

class MetorialManagementInstanceChatEventsEndpoint(BaseMetorialEndpoint):
    """Chat events record what happened on a chat, such as a new message, reaction, or membership change."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, chat_id: Optional[Union[str, List[str]]] = None, chat_connection_id: Optional[Union[str, List[str]]] = None, chat_instance_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, occurred_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatEventsListOutput:
        """
    List chat events
    Returns a paginated list of chat events.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param chat_id: Optional[Union[str, List[str]]] (optional)
    :param chat_connection_id: Optional[Union[str, List[str]]] (optional)
    :param chat_instance_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param occurred_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceChatEventsListOutput
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
        if chat_id is not None:
            query_dict["chat_id"] = chat_id
        if chat_connection_id is not None:
            query_dict["chat_connection_id"] = chat_connection_id
        if chat_instance_id is not None:
            query_dict["chat_instance_id"] = chat_instance_id
        if type is not None:
            query_dict["type"] = type
        if created_at is not None:
            query_dict["created_at"] = created_at
        if occurred_at is not None:
            query_dict["occurred_at"] = occurred_at

        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatEventsListOutput.from_dict)

    def get(self, instance_id: str, chat_event_id: str) -> DashboardInstanceChatEventsGetOutput:
        """
    Get chat event
    Retrieves a specific chat event.

    :param instance_id: str
    :param chat_event_id: str
    :return: DashboardInstanceChatEventsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'events', chat_event_id]
        )
        return self._get(request).transform(mapDashboardInstanceChatEventsGetOutput.from_dict)