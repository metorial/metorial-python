from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsMessagesListOutput, DashboardInstanceSessionsMessagesListOutput, mapDashboardInstanceSessionsMessagesListQuery, DashboardInstanceSessionsMessagesListQuery, mapDashboardInstanceSessionsMessagesGetOutput, DashboardInstanceSessionsMessagesGetOutput

class MetorialSessionsMessagesEndpoint(BaseMetorialEndpoint):
    """Session messages represent the MCP protocol messages exchanged during a session. This read-only resource provides visibility into the communication between clients and providers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[Union[str, List[str]]] = None, source: Optional[Union[str, List[str]]] = None, hierarchy: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None, session_connection_id: Optional[Union[str, List[str]]] = None, provider_run_id: Optional[Union[str, List[str]]] = None, error_id: Optional[Union[str, List[str]]] = None, participant_id: Optional[Union[str, List[str]]] = None, parent_message_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsMessagesListOutput:
        """
    List session messages
    Returns a paginated list of messages for a session.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param source: Optional[Union[str, List[str]]] (optional)
    :param hierarchy: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param session_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_run_id: Optional[Union[str, List[str]]] (optional)
    :param error_id: Optional[Union[str, List[str]]] (optional)
    :param participant_id: Optional[Union[str, List[str]]] (optional)
    :param parent_message_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
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
        if source is not None:
            query_dict["source"] = source
        if hierarchy is not None:
            query_dict["hierarchy"] = hierarchy
        if id is not None:
            query_dict["id"] = id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id
        if session_connection_id is not None:
            query_dict["session_connection_id"] = session_connection_id
        if provider_run_id is not None:
            query_dict["provider_run_id"] = provider_run_id
        if error_id is not None:
            query_dict["error_id"] = error_id
        if participant_id is not None:
            query_dict["participant_id"] = participant_id
        if parent_message_id is not None:
            query_dict["parent_message_id"] = parent_message_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['session-messages'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsMessagesListOutput.from_dict)

    def get(self, session_message_id: str) -> DashboardInstanceSessionsMessagesGetOutput:
        """
    Get session message
    Retrieves a specific message from a session.

    :param session_message_id: str
    :return: DashboardInstanceSessionsMessagesGetOutput
    """
        request = MetorialRequest(
            path=['session-messages', session_message_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsMessagesGetOutput.from_dict)