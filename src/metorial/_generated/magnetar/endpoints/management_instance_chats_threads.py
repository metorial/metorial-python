from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatsThreadsListOutput, DashboardInstanceChatsThreadsListOutput, mapDashboardInstanceChatsThreadsListQuery, DashboardInstanceChatsThreadsListQuery, mapDashboardInstanceChatsThreadsGetOutput, DashboardInstanceChatsThreadsGetOutput, mapDashboardInstanceChatsThreadsGetQuery, DashboardInstanceChatsThreadsGetQuery

class MetorialManagementInstanceChatsThreadsEndpoint(BaseMetorialEndpoint):
    """Chat threads group replies to a message within a chat channel."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, chat_id: str, *, channel_id: str, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[str] = None) -> DashboardInstanceChatsThreadsListOutput:
        """
    List chat threads
    Returns a paginated list of threads in a chat channel.

    :param instance_id: str
    :param chat_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param channel_id: str
    :param type: Optional[str] (optional)
    :return: DashboardInstanceChatsThreadsListOutput
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
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'threads'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsThreadsListOutput.from_dict)

    def get(self, instance_id: str, chat_id: str, thread_id: str, *, channel_id: str) -> DashboardInstanceChatsThreadsGetOutput:
        """
    Get chat thread
    Retrieves a specific chat thread.

    :param instance_id: str
    :param chat_id: str
    :param thread_id: str
    :param channel_id: str
    :return: DashboardInstanceChatsThreadsGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["channel_id"] = channel_id

        request = MetorialRequest(
            path=['instances', instance_id, 'chats', chat_id, 'threads', thread_id],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatsThreadsGetOutput.from_dict)