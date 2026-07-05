from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsExportsListOutput, DashboardInstanceSkillsExportsListOutput, mapDashboardInstanceSkillsExportsListQuery, DashboardInstanceSkillsExportsListQuery, mapDashboardInstanceSkillsExportsGetOutput, DashboardInstanceSkillsExportsGetOutput, mapDashboardInstanceSkillsExportsCreateOutput, DashboardInstanceSkillsExportsCreateOutput, mapDashboardInstanceSkillsExportsCreateBody, DashboardInstanceSkillsExportsCreateBody

class MetorialManagementInstanceSkillsExportsEndpoint(BaseMetorialEndpoint):
    """Export skills, skill plugins, and skill marketplaces as zip files."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, target: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSkillsExportsListOutput:
        """
    List skill exports
    Returns a paginated list of skill exports.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param target: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSkillsExportsListOutput
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
        if target is not None:
            query_dict["target"] = target
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-exports'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsExportsListOutput.from_dict)

    def get(self, instance_id: str, skill_export_id: str) -> DashboardInstanceSkillsExportsGetOutput:
        """
    Get skill export
    Retrieves a skill export.

    :param instance_id: str
    :param skill_export_id: str
    :return: DashboardInstanceSkillsExportsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-exports', skill_export_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsExportsGetOutput.from_dict)

    def create(self, instance_id: str, *, target: str, skill_id: Optional[str] = None, skill_plugin_id: Optional[str] = None, skill_marketplace_id: Optional[str] = None) -> DashboardInstanceSkillsExportsCreateOutput:
        """
    Create skill export
    Creates a skill, plugin, or marketplace export.

    :param instance_id: str
    :param target: str
    :param skill_id: Optional[str] (optional)
    :param skill_plugin_id: Optional[str] (optional)
    :param skill_marketplace_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsExportsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["target"] = target
        if skill_id is not None:
            body_dict["skill_id"] = skill_id
        if skill_plugin_id is not None:
            body_dict["skill_plugin_id"] = skill_plugin_id
        if skill_marketplace_id is not None:
            body_dict["skill_marketplace_id"] = skill_marketplace_id

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-exports'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsExportsCreateOutput.from_dict)