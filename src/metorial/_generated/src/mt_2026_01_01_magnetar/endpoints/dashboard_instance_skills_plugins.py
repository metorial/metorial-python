from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsPluginsListOutput, DashboardInstanceSkillsPluginsListOutput, mapDashboardInstanceSkillsPluginsListQuery, DashboardInstanceSkillsPluginsListQuery, mapDashboardInstanceSkillsPluginsGetOutput, DashboardInstanceSkillsPluginsGetOutput, mapDashboardInstanceSkillsPluginsCreateOutput, DashboardInstanceSkillsPluginsCreateOutput, mapDashboardInstanceSkillsPluginsCreateBody, DashboardInstanceSkillsPluginsCreateBody, mapDashboardInstanceSkillsPluginsUpdateOutput, DashboardInstanceSkillsPluginsUpdateOutput, mapDashboardInstanceSkillsPluginsUpdateBody, DashboardInstanceSkillsPluginsUpdateBody, mapDashboardInstanceSkillsPluginsArchiveOutput, DashboardInstanceSkillsPluginsArchiveOutput, mapDashboardInstanceSkillsPluginsSyncOutput, DashboardInstanceSkillsPluginsSyncOutput, mapDashboardInstanceSkillsPluginsSyncBody, DashboardInstanceSkillsPluginsSyncBody

class MetorialDashboardInstanceSkillsPluginsEndpoint(BaseMetorialEndpoint):
    """Manage skill plugins for an instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, skill_marketplace_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, category: Optional[str] = None, search: Optional[str] = None, skill_configuration_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsPluginsListOutput:
        """
    List skill plugins
    Returns a paginated list of skill plugins.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param skill_marketplace_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param category: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param skill_configuration_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsPluginsListOutput
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
        if skill_marketplace_id is not None:
            query_dict["skill_marketplace_id"] = skill_marketplace_id
        if status is not None:
            query_dict["status"] = status
        if category is not None:
            query_dict["category"] = category
        if search is not None:
            query_dict["search"] = search
        if skill_configuration_id is not None:
            query_dict["skill_configuration_id"] = skill_configuration_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsPluginsListOutput.from_dict)

    def get(self, instance_id: str, skill_plugin_id: str) -> DashboardInstanceSkillsPluginsGetOutput:
        """
    Get skill plugin
    Retrieves a skill plugin.

    :param instance_id: str
    :param skill_plugin_id: str
    :return: DashboardInstanceSkillsPluginsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsPluginsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, long_description: Optional[str] = None, category: Optional[str] = None, image_file_id: Optional[str] = None, skill_configuration_id: Optional[str] = None) -> DashboardInstanceSkillsPluginsCreateOutput:
        """
    Create skill plugin
    Creates a skill plugin.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param long_description: Optional[str] (optional)
    :param category: Optional[str] (optional)
    :param image_file_id: Optional[str] (optional)
    :param skill_configuration_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsPluginsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if long_description is not None:
            body_dict["long_description"] = long_description
        if category is not None:
            body_dict["category"] = category
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsPluginsCreateOutput.from_dict)

    def update(self, instance_id: str, skill_plugin_id: str, *, name: Optional[str] = None, description: Optional[str] = None, long_description: Optional[str] = None, category: Optional[str] = None, image_file_id: Optional[str] = None, skill_configuration_id: Optional[str] = None) -> DashboardInstanceSkillsPluginsUpdateOutput:
        """
    Update skill plugin
    Updates a skill plugin.

    :param instance_id: str
    :param skill_plugin_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param long_description: Optional[str] (optional)
    :param category: Optional[str] (optional)
    :param image_file_id: Optional[str] (optional)
    :param skill_configuration_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsPluginsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if long_description is not None:
            body_dict["long_description"] = long_description
        if category is not None:
            body_dict["category"] = category
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsPluginsUpdateOutput.from_dict)

    def archive(self, instance_id: str, skill_plugin_id: str) -> DashboardInstanceSkillsPluginsArchiveOutput:
        """
    Archive skill plugin
    Archives a skill plugin.

    :param instance_id: str
    :param skill_plugin_id: str
    :return: DashboardInstanceSkillsPluginsArchiveOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsPluginsArchiveOutput.from_dict)

    def sync(self, instance_id: str, skill_plugin_id: str) -> DashboardInstanceSkillsPluginsSyncOutput:
        """
    Sync skill plugin
    Forces a skill plugin sync.

    :param instance_id: str
    :param skill_plugin_id: str
    :return: DashboardInstanceSkillsPluginsSyncOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id, 'sync']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsPluginsSyncOutput.from_dict)