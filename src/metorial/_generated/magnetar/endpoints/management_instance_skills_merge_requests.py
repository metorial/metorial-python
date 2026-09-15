from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMergeRequestsListOutput, DashboardInstanceSkillsMergeRequestsListOutput, mapDashboardInstanceSkillsMergeRequestsListQuery, DashboardInstanceSkillsMergeRequestsListQuery, mapDashboardInstanceSkillsMergeRequestsCreateOutput, DashboardInstanceSkillsMergeRequestsCreateOutput, mapDashboardInstanceSkillsMergeRequestsCreateBody, DashboardInstanceSkillsMergeRequestsCreateBody, mapDashboardInstanceSkillsMergeRequestsGetOutput, DashboardInstanceSkillsMergeRequestsGetOutput, mapDashboardInstanceSkillsMergeRequestsPerformOutput, DashboardInstanceSkillsMergeRequestsPerformOutput, mapDashboardInstanceSkillsMergeRequestsCloseOutput, DashboardInstanceSkillsMergeRequestsCloseOutput, mapDashboardInstanceSkillsMergeRequestsRollbackOutput, DashboardInstanceSkillsMergeRequestsRollbackOutput

class MetorialManagementInstanceSkillsMergeRequestsEndpoint(BaseMetorialEndpoint):
    """Review, resolve, and apply changes between skills."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, source_skill_id: Optional[Union[str, List[str]]] = None, target_skill_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, created_by_actor_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsMergeRequestsListOutput:
        """
    List skill merge requests
    Returns a paginated list of skill merge requests.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param source_skill_id: Optional[Union[str, List[str]]] (optional)
    :param target_skill_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param created_by_actor_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsMergeRequestsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if source_skill_id is not None:
            query_dict["source_skill_id"] = source_skill_id
        if target_skill_id is not None:
            query_dict["target_skill_id"] = target_skill_id
        if status is not None:
            query_dict["status"] = status
        if created_by_actor_id is not None:
            query_dict["created_by_actor_id"] = created_by_actor_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-merge-requests'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsListOutput.from_dict)

    def create(self, instance_id: str, *, source_skill_id: str, title: str, target_skill_id: Optional[str] = None, description: Optional[str] = None) -> DashboardInstanceSkillsMergeRequestsCreateOutput:
        """
    Create skill merge request
    Creates a merge request from one skill into another.

    :param instance_id: str
    :param source_skill_id: str
    :param target_skill_id: Optional[str] (optional)
    :param title: str
    :param description: Optional[str] (optional)
    :return: DashboardInstanceSkillsMergeRequestsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["source_skill_id"] = source_skill_id
        if target_skill_id is not None:
            body_dict["target_skill_id"] = target_skill_id
        body_dict["title"] = title
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-merge-requests'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMergeRequestsCreateOutput.from_dict)

    def get(self, instance_id: str, skill_merge_request_id: str) -> DashboardInstanceSkillsMergeRequestsGetOutput:
        """
    Get skill merge request
    Retrieves a skill merge request.

    :param instance_id: str
    :param skill_merge_request_id: str
    :return: DashboardInstanceSkillsMergeRequestsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-merge-requests', skill_merge_request_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsGetOutput.from_dict)

    def perform(self, instance_id: str, skill_merge_request_id: str) -> DashboardInstanceSkillsMergeRequestsPerformOutput:
        """
    Perform skill merge request
    Queues application of a resolved skill merge request.

    :param instance_id: str
    :param skill_merge_request_id: str
    :return: DashboardInstanceSkillsMergeRequestsPerformOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'perform']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMergeRequestsPerformOutput.from_dict)

    def close(self, instance_id: str, skill_merge_request_id: str) -> DashboardInstanceSkillsMergeRequestsCloseOutput:
        """
    Close skill merge request
    Closes an open skill merge request without applying it.

    :param instance_id: str
    :param skill_merge_request_id: str
    :return: DashboardInstanceSkillsMergeRequestsCloseOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'close']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMergeRequestsCloseOutput.from_dict)

    def rollback(self, instance_id: str, skill_merge_request_id: str) -> DashboardInstanceSkillsMergeRequestsRollbackOutput:
        """
    Rollback skill merge request
    Restores the target skill to its state before a completed merge.

    :param instance_id: str
    :param skill_merge_request_id: str
    :return: DashboardInstanceSkillsMergeRequestsRollbackOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'rollback']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMergeRequestsRollbackOutput.from_dict)