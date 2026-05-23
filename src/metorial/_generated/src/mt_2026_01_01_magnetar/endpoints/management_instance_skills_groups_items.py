from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsGroupsItemsListOutput, DashboardInstanceSkillsGroupsItemsListOutput, mapDashboardInstanceSkillsGroupsItemsListQuery, DashboardInstanceSkillsGroupsItemsListQuery, mapDashboardInstanceSkillsGroupsItemsGetOutput, DashboardInstanceSkillsGroupsItemsGetOutput, mapDashboardInstanceSkillsGroupsItemsCreateOutput, DashboardInstanceSkillsGroupsItemsCreateOutput, mapDashboardInstanceSkillsGroupsItemsCreateBody, DashboardInstanceSkillsGroupsItemsCreateBody, mapDashboardInstanceSkillsGroupsItemsDeleteOutput, DashboardInstanceSkillsGroupsItemsDeleteOutput

class MetorialManagementInstanceSkillsGroupsItemsEndpoint(BaseMetorialEndpoint):
    """Skill group items link groups to skills."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_group_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, skill_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsGroupsItemsListOutput:
        """
    List skill group items
    Returns a paginated list of items for a skill group.

    :param instance_id: str
    :param skill_group_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param skill_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsGroupsItemsListOutput
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
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if skill_id is not None:
            query_dict["skill_id"] = skill_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-groups', skill_group_id, 'items'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsGroupsItemsListOutput.from_dict)

    def get(self, instance_id: str, skill_group_id: str, skill_group_item_id: str) -> DashboardInstanceSkillsGroupsItemsGetOutput:
        """
    Get skill group item
    Retrieves a specific skill group item.

    :param instance_id: str
    :param skill_group_id: str
    :param skill_group_item_id: str
    :return: DashboardInstanceSkillsGroupsItemsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-groups', skill_group_id, 'items', skill_group_item_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsGroupsItemsGetOutput.from_dict)

    def create(self, instance_id: str, skill_group_id: str, *, skill_id: str) -> DashboardInstanceSkillsGroupsItemsCreateOutput:
        """
    Create skill group item
    Adds a skill to a skill group.

    :param instance_id: str
    :param skill_group_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsGroupsItemsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["skill_id"] = skill_id

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-groups', skill_group_id, 'items'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsGroupsItemsCreateOutput.from_dict)

    def delete(self, instance_id: str, skill_group_id: str, skill_group_item_id: str) -> DashboardInstanceSkillsGroupsItemsDeleteOutput:
        """
    Delete skill group item
    Archives a skill group item.

    :param instance_id: str
    :param skill_group_id: str
    :param skill_group_item_id: str
    :return: DashboardInstanceSkillsGroupsItemsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-groups', skill_group_id, 'items', skill_group_item_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsGroupsItemsDeleteOutput.from_dict)