from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsVersionsListOutput, DashboardInstanceSkillsVersionsListOutput, mapDashboardInstanceSkillsVersionsListQuery, DashboardInstanceSkillsVersionsListQuery, mapDashboardInstanceSkillsVersionsGetOutput, DashboardInstanceSkillsVersionsGetOutput

class MetorialDashboardInstanceSkillsVersionsEndpoint(BaseMetorialEndpoint):
    """Inspect version history and snapshots for a skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSkillsVersionsListOutput:
        """
    List skill versions
    Returns a paginated list of versions for a specific skill.

    :param instance_id: str
    :param skill_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSkillsVersionsListOutput
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
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsVersionsListOutput.from_dict)

    def get(self, instance_id: str, skill_id: str, skill_version_id: str) -> DashboardInstanceSkillsVersionsGetOutput:
        """
    Get skill version by ID
    Retrieves a specific skill version by its ID.

    :param instance_id: str
    :param skill_id: str
    :param skill_version_id: str
    :return: DashboardInstanceSkillsVersionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'versions', skill_version_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsVersionsGetOutput.from_dict)