from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsSecurityReviewRevisionsListOutput, DashboardInstanceSkillsSecurityReviewRevisionsListOutput, mapDashboardInstanceSkillsSecurityReviewRevisionsListQuery, DashboardInstanceSkillsSecurityReviewRevisionsListQuery, mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutput, DashboardInstanceSkillsSecurityReviewRevisionsGetOutput

class MetorialManagementInstanceSkillsSecurityReviewRevisionsEndpoint(BaseMetorialEndpoint):
    """A security review assesses what a skill makes an agent do and whether its files can be trusted. Everyone who can read a skill can read its review."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSkillsSecurityReviewRevisionsListOutput:
        """
    List skill security review revisions
    Returns the most recent finished revisions of a skill's security review.

    :param instance_id: str
    :param skill_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSkillsSecurityReviewRevisionsListOutput
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
            path=['instances', instance_id, 'skills', skill_id, 'security-review', 'revisions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsSecurityReviewRevisionsListOutput.from_dict)

    def get(self, instance_id: str, skill_id: str, revision_id: str) -> DashboardInstanceSkillsSecurityReviewRevisionsGetOutput:
        """
    Get skill security review revision
    Retrieves a single revision of a skill's security review.

    :param instance_id: str
    :param skill_id: str
    :param revision_id: str
    :return: DashboardInstanceSkillsSecurityReviewRevisionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'security-review', 'revisions', revision_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsSecurityReviewRevisionsGetOutput.from_dict)