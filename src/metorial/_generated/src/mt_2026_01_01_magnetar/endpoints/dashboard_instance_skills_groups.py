from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsGroupsListOutput, DashboardInstanceSkillsGroupsListOutput, mapDashboardInstanceSkillsGroupsListQuery, DashboardInstanceSkillsGroupsListQuery, mapDashboardInstanceSkillsGroupsGetOutput, DashboardInstanceSkillsGroupsGetOutput, mapDashboardInstanceSkillsGroupsCreateOutput, DashboardInstanceSkillsGroupsCreateOutput, mapDashboardInstanceSkillsGroupsCreateBody, DashboardInstanceSkillsGroupsCreateBody, mapDashboardInstanceSkillsGroupsUpdateOutput, DashboardInstanceSkillsGroupsUpdateOutput, mapDashboardInstanceSkillsGroupsUpdateBody, DashboardInstanceSkillsGroupsUpdateBody, mapDashboardInstanceSkillsGroupsDeleteOutput, DashboardInstanceSkillsGroupsDeleteOutput

class MetorialDashboardInstanceSkillsGroupsEndpoint(BaseMetorialEndpoint):
    """Skill groups organize skills into reusable collections."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, skill_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsGroupsListOutput:
        """
    List skill groups
    Returns a paginated list of skill groups.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param skill_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsGroupsListOutput
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
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if skill_id is not None:
            query_dict["skill_id"] = skill_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsGroupsListOutput.from_dict)

    def get(self, instance_id: str, skill_group_id: str) -> DashboardInstanceSkillsGroupsGetOutput:
        """
    Get skill group
    Retrieves a specific skill group.

    :param instance_id: str
    :param skill_group_id: str
    :return: DashboardInstanceSkillsGroupsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-groups', skill_group_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsGroupsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, skill_ids: Optional[List[str]] = None) -> DashboardInstanceSkillsGroupsCreateOutput:
        """
    Create skill group
    Creates a skill group.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param skill_ids: Optional[List[str]] (optional)
    :return: DashboardInstanceSkillsGroupsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if skill_ids is not None:
            body_dict["skill_ids"] = skill_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsGroupsCreateOutput.from_dict)

    def update(self, instance_id: str, skill_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, skill_ids: Optional[List[str]] = None) -> DashboardInstanceSkillsGroupsUpdateOutput:
        """
    Update skill group
    Updates a skill group.

    :param instance_id: str
    :param skill_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param skill_ids: Optional[List[str]] (optional)
    :return: DashboardInstanceSkillsGroupsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if skill_ids is not None:
            body_dict["skill_ids"] = skill_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-groups', skill_group_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsGroupsUpdateOutput.from_dict)

    def delete(self, instance_id: str, skill_group_id: str) -> DashboardInstanceSkillsGroupsDeleteOutput:
        """
    Delete skill group
    Archives a skill group.

    :param instance_id: str
    :param skill_group_id: str
    :return: DashboardInstanceSkillsGroupsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-groups', skill_group_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsGroupsDeleteOutput.from_dict)