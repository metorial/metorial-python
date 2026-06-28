from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsParticipantsListOutput, DashboardInstanceSessionsParticipantsListOutput, mapDashboardInstanceSessionsParticipantsListQuery, DashboardInstanceSessionsParticipantsListQuery, mapDashboardInstanceSessionsParticipantsGetOutput, DashboardInstanceSessionsParticipantsGetOutput

class MetorialSessionsParticipantsEndpoint(BaseMetorialEndpoint):
    """Session participants represent the clients and other entities that are connected to a session. This read-only resource tracks who is participating in a session."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, agent_id: Optional[Union[str, List[str]]] = None, actor_id: Optional[Union[str, List[str]]] = None, consumer_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, agent_instance_id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_connection_id: Optional[Union[str, List[str]]] = None, session_message_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsParticipantsListOutput:
        """
    List session participants
    Returns a paginated list of participants in a session.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param agent_id: Optional[Union[str, List[str]]] (optional)
    :param actor_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param agent_instance_id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_connection_id: Optional[Union[str, List[str]]] (optional)
    :param session_message_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
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
        if id is not None:
            query_dict["id"] = id
        if agent_id is not None:
            query_dict["agent_id"] = agent_id
        if actor_id is not None:
            query_dict["actor_id"] = actor_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if agent_instance_id is not None:
            query_dict["agent_instance_id"] = agent_instance_id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if session_connection_id is not None:
            query_dict["session_connection_id"] = session_connection_id
        if session_message_id is not None:
            query_dict["session_message_id"] = session_message_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['session-participants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsParticipantsListOutput.from_dict)

    def get(self, session_participant_id: str) -> DashboardInstanceSessionsParticipantsGetOutput:
        """
    Get session participant
    Retrieves a specific participant in a session.

    :param session_participant_id: str
    :return: DashboardInstanceSessionsParticipantsGetOutput
    """
        request = MetorialRequest(
            path=['session-participants', session_participant_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsParticipantsGetOutput.from_dict)