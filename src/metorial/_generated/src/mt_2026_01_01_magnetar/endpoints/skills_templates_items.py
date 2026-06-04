from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsTemplatesItemsListOutput, DashboardInstanceSkillsTemplatesItemsListOutput, mapDashboardInstanceSkillsTemplatesItemsListQuery, DashboardInstanceSkillsTemplatesItemsListQuery, mapDashboardInstanceSkillsTemplatesItemsGetOutput, DashboardInstanceSkillsTemplatesItemsGetOutput, mapDashboardInstanceSkillsTemplatesItemsCreateOutput, DashboardInstanceSkillsTemplatesItemsCreateOutput, mapDashboardInstanceSkillsTemplatesItemsCreateBody, DashboardInstanceSkillsTemplatesItemsCreateBody, mapDashboardInstanceSkillsTemplatesItemsDeleteOutput, DashboardInstanceSkillsTemplatesItemsDeleteOutput

class MetorialSkillsTemplatesItemsEndpoint(BaseMetorialEndpoint):
    """Skill template items link template definitions to provider and integration items."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, skill_template_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSkillsTemplatesItemsListOutput:
        """
    List skill template items
    Returns a paginated list of items for a skill template.

    :param skill_template_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSkillsTemplatesItemsListOutput
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
            path=['skill-templates', skill_template_id, 'items'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsTemplatesItemsListOutput.from_dict)

    def get(self, skill_template_id: str, skill_template_item_id: str) -> DashboardInstanceSkillsTemplatesItemsGetOutput:
        """
    Get skill template item
    Retrieves a specific skill template item.

    :param skill_template_id: str
    :param skill_template_item_id: str
    :return: DashboardInstanceSkillsTemplatesItemsGetOutput
    """
        request = MetorialRequest(
            path=['skill-templates', skill_template_id, 'items', skill_template_item_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsTemplatesItemsGetOutput.from_dict)

    def create(self, skill_template_id: str) -> DashboardInstanceSkillsTemplatesItemsCreateOutput:
        """
    Create skill template item
    Adds a provider or integration item to a skill template.

    :param skill_template_id: str
    :return: DashboardInstanceSkillsTemplatesItemsCreateOutput
    """
        request = MetorialRequest(
            path=['skill-templates', skill_template_id, 'items']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsTemplatesItemsCreateOutput.from_dict)

    def delete(self, skill_template_id: str, skill_template_item_id: str) -> DashboardInstanceSkillsTemplatesItemsDeleteOutput:
        """
    Delete skill template item
    Deletes a skill template item.

    :param skill_template_id: str
    :param skill_template_item_id: str
    :return: DashboardInstanceSkillsTemplatesItemsDeleteOutput
    """
        request = MetorialRequest(
            path=['skill-templates', skill_template_id, 'items', skill_template_item_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsTemplatesItemsDeleteOutput.from_dict)