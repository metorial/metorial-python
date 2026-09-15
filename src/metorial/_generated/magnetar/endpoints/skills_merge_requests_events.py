from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMergeRequestsEventsListOutput, DashboardInstanceSkillsMergeRequestsEventsListOutput, mapDashboardInstanceSkillsMergeRequestsEventsListQuery, DashboardInstanceSkillsMergeRequestsEventsListQuery, mapDashboardInstanceSkillsMergeRequestsEventsGetOutput, DashboardInstanceSkillsMergeRequestsEventsGetOutput

class MetorialSkillsMergeRequestsEventsEndpoint(BaseMetorialEndpoint):
    """Inspect the activity history of skill merge requests."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, skill_merge_request_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsMergeRequestsEventsListOutput:
        """
    List skill merge request events
    Returns a paginated activity history for a skill merge request.

    :param skill_merge_request_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsMergeRequestsEventsListOutput
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
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['skill-merge-requests', skill_merge_request_id, 'events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsEventsListOutput.from_dict)

    def get(self, skill_merge_request_id: str, event_id: str) -> DashboardInstanceSkillsMergeRequestsEventsGetOutput:
        """
    Get skill merge request event
    Retrieves one event from a skill merge request activity history.

    :param skill_merge_request_id: str
    :param event_id: str
    :return: DashboardInstanceSkillsMergeRequestsEventsGetOutput
    """
        request = MetorialRequest(
            path=['skill-merge-requests', skill_merge_request_id, 'events', event_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsEventsGetOutput.from_dict)