from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsEventsListOutput, DashboardInstanceSessionsEventsListOutput, mapDashboardInstanceSessionsEventsListQuery, DashboardInstanceSessionsEventsListQuery, mapDashboardInstanceSessionsEventsGetOutput, DashboardInstanceSessionsEventsGetOutput

class MetorialSessionsEventsEndpoint(BaseMetorialEndpoint):
    """Session events represent significant occurrences during a session, such as errors or state changes. This read-only resource provides visibility into session activity."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None, session_connection_id: Optional[Union[str, List[str]]] = None, provider_run_id: Optional[Union[str, List[str]]] = None, session_message_id: Optional[Union[str, List[str]]] = None, session_error_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionsEventsListOutput:
        """
    List session events
    Returns a paginated list of events for a session.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param session_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_run_id: Optional[Union[str, List[str]]] (optional)
    :param session_message_id: Optional[Union[str, List[str]]] (optional)
    :param session_error_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsEventsListOutput
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
        if session_message_id is not None:
            query_dict["session_message_id"] = session_message_id
        if session_error_id is not None:
            query_dict["session_error_id"] = session_error_id

        request = MetorialRequest(
            path=['session-events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsEventsListOutput.from_dict)

    def get(self, session_event_id: str) -> DashboardInstanceSessionsEventsGetOutput:
        """
    Get session event
    Retrieves a specific event from a session.

    :param session_event_id: str
    :return: DashboardInstanceSessionsEventsGetOutput
    """
        request = MetorialRequest(
            path=['session-events', session_event_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsEventsGetOutput.from_dict)
