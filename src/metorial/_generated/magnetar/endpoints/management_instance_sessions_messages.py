from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsMessagesListOutput, DashboardInstanceSessionsMessagesListOutput, mapDashboardInstanceSessionsMessagesListQuery, DashboardInstanceSessionsMessagesListQuery, mapDashboardInstanceSessionsMessagesGetOutput, DashboardInstanceSessionsMessagesGetOutput

class MetorialManagementInstanceSessionsMessagesEndpoint(BaseMetorialEndpoint):
    """Session messages represent the MCP protocol messages exchanged during a session. This read-only resource provides visibility into the communication between clients and providers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, session_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[str] = None, session_provider_id: Optional[Union[str, List[str]]] = None, provider_run_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionsMessagesListOutput:
        """
    List session messages
    Returns a paginated list of messages for a session.

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[str] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_run_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsMessagesListOutput
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
        if type is not None:
            query_dict["type"] = type
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id
        if provider_run_id is not None:
            query_dict["provider_run_id"] = provider_run_id

        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id, 'messages'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsMessagesListOutput.from_dict)

    def get(self, instance_id: str, session_id: str, session_message_id: str) -> DashboardInstanceSessionsMessagesGetOutput:
        """
    Get session message
    Retrieves a specific message from a session.

    :param instance_id: str
    :param session_id: str
    :param session_message_id: str
    :return: DashboardInstanceSessionsMessagesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id, 'messages', session_message_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsMessagesGetOutput.from_dict)
