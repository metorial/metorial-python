from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsParticipantsListOutput, DashboardInstanceSessionsParticipantsListOutput, mapDashboardInstanceSessionsParticipantsListQuery, DashboardInstanceSessionsParticipantsListQuery, mapDashboardInstanceSessionsParticipantsGetOutput, DashboardInstanceSessionsParticipantsGetOutput

class MetorialDashboardInstanceSessionsParticipantsEndpoint(BaseMetorialEndpoint):
    """Session participants represent the clients and other entities that are connected to a session. This read-only resource tracks who is participating in a session."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, session_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[str] = None) -> DashboardInstanceSessionsParticipantsListOutput:
        """
    List session participants
    Returns a paginated list of participants in a session.

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[str] (optional)
    :return: DashboardInstanceSessionsParticipantsListOutput
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

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sessions', session_id, 'participants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsParticipantsListOutput.from_dict)

    def get(self, instance_id: str, session_id: str, session_participant_id: str) -> DashboardInstanceSessionsParticipantsGetOutput:
        """
    Get session participant
    Retrieves a specific participant in a session.

    :param instance_id: str
    :param session_id: str
    :param session_participant_id: str
    :return: DashboardInstanceSessionsParticipantsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sessions', session_id, 'participants', session_participant_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsParticipantsGetOutput.from_dict)
