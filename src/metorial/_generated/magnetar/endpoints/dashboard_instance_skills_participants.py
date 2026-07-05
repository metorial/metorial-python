from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsParticipantsListOutput, DashboardInstanceSkillsParticipantsListOutput, mapDashboardInstanceSkillsParticipantsListQuery, DashboardInstanceSkillsParticipantsListQuery, mapDashboardInstanceSkillsParticipantsGetOutput, DashboardInstanceSkillsParticipantsGetOutput

class MetorialDashboardInstanceSkillsParticipantsEndpoint(BaseMetorialEndpoint):
    """Inspect participants associated with an instance skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSkillsParticipantsListOutput:
        """
    List skill participants
    Returns a paginated list of participants for a specific skill.

    :param instance_id: str
    :param skill_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSkillsParticipantsListOutput
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
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'participants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsParticipantsListOutput.from_dict)

    def get(self, instance_id: str, skill_id: str, skill_participant_id: str) -> DashboardInstanceSkillsParticipantsGetOutput:
        """
    Get skill participant by ID
    Retrieves a specific participant within a skill.

    :param instance_id: str
    :param skill_id: str
    :param skill_participant_id: str
    :return: DashboardInstanceSkillsParticipantsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'participants', skill_participant_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsParticipantsGetOutput.from_dict)