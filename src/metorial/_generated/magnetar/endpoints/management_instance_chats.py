from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsListOutput, DashboardInstanceChatsListOutput, mapDashboardInstanceChatsListQuery, DashboardInstanceChatsListQuery, mapDashboardInstanceChatsGetOutput, DashboardInstanceChatsGetOutput

class MetorialManagementInstanceChatsEndpoint(BaseMetorialEndpoint):
    """A chat represents a single connected chat surface, such as a Slack or Microsoft Teams tenant, running on a chat instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, chat_connection_id: Optional[Union[str, List[str]]] = None, chat_instance_id: Optional[Union[str, List[str]]] = None, chat_instance_provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatsListOutput:
        """
    List chats
    Returns a paginated list of chats.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param chat_connection_id: Optional[Union[str, List[str]]] (optional)
    :param chat_instance_id: Optional[Union[str, List[str]]] (optional)
    :param chat_instance_provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceChatsListOutput
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
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if chat_connection_id is not None:
            query_dict["chat_connection_id"] = chat_connection_id
        if chat_instance_id is not None:
            query_dict["chat_instance_id"] = chat_instance_id
        if chat_instance_provider_id is not None:
            query_dict["chat_instance_provider_id"] = chat_instance_provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'chats'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsListOutput.from_dict)

    def get(self, instance_id: str, chat_id: str) -> DashboardInstanceChatsGetOutput:
        """
    Get chat
    Retrieves a specific chat.

    :param instance_id: str
    :param chat_id: str
    :return: DashboardInstanceChatsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id]
        )
        return self._get(request).transform(mapDashboardInstanceChatsGetOutput.from_dict)