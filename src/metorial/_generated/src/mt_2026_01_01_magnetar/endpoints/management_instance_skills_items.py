from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsItemsListOutput, DashboardInstanceSkillsItemsListOutput, mapDashboardInstanceSkillsItemsListQuery, DashboardInstanceSkillsItemsListQuery, mapDashboardInstanceSkillsItemsGetOutput, DashboardInstanceSkillsItemsGetOutput, mapDashboardInstanceSkillsItemsCreateOutput, DashboardInstanceSkillsItemsCreateOutput, mapDashboardInstanceSkillsItemsCreateBody, DashboardInstanceSkillsItemsCreateBody, mapDashboardInstanceSkillsItemsDeleteOutput, DashboardInstanceSkillsItemsDeleteOutput

class MetorialManagementInstanceSkillsItemsEndpoint(BaseMetorialEndpoint):
    """Skill items attach integrations and providers to skills."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsItemsListOutput:
        """
    List skill items
    Returns a paginated list of items for a skill.

    :param instance_id: str
    :param skill_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsItemsListOutput
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
        if type is not None:
            query_dict["type"] = type
        if id is not None:
            query_dict["id"] = id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'items'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsItemsListOutput.from_dict)

    def get(self, instance_id: str, skill_id: str, skill_item_id: str) -> DashboardInstanceSkillsItemsGetOutput:
        """
    Get skill item
    Retrieves a specific skill item.

    :param instance_id: str
    :param skill_id: str
    :param skill_item_id: str
    :return: DashboardInstanceSkillsItemsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'items', skill_item_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsItemsGetOutput.from_dict)

    def create(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsItemsCreateOutput:
        """
    Create skill item
    Creates a new item on a skill.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsItemsCreateOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'items']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsItemsCreateOutput.from_dict)

    def delete(self, instance_id: str, skill_id: str, skill_item_id: str) -> DashboardInstanceSkillsItemsDeleteOutput:
        """
    Delete skill item
    Archives a skill item.

    :param instance_id: str
    :param skill_id: str
    :param skill_item_id: str
    :return: DashboardInstanceSkillsItemsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'items', skill_item_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsItemsDeleteOutput.from_dict)