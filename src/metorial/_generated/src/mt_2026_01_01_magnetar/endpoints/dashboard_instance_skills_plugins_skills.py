from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsPluginsSkillsListOutput, DashboardInstanceSkillsPluginsSkillsListOutput, mapDashboardInstanceSkillsPluginsSkillsListQuery, DashboardInstanceSkillsPluginsSkillsListQuery, mapDashboardInstanceSkillsPluginsSkillsAddOutput, DashboardInstanceSkillsPluginsSkillsAddOutput, mapDashboardInstanceSkillsPluginsSkillsAddBody, DashboardInstanceSkillsPluginsSkillsAddBody, mapDashboardInstanceSkillsPluginsSkillsGetOutput, DashboardInstanceSkillsPluginsSkillsGetOutput, mapDashboardInstanceSkillsPluginsSkillsUpdateOutput, DashboardInstanceSkillsPluginsSkillsUpdateOutput, mapDashboardInstanceSkillsPluginsSkillsUpdateBody, DashboardInstanceSkillsPluginsSkillsUpdateBody, mapDashboardInstanceSkillsPluginsSkillsRemoveOutput, DashboardInstanceSkillsPluginsSkillsRemoveOutput

class MetorialDashboardInstanceSkillsPluginsSkillsEndpoint(BaseMetorialEndpoint):
    """Manage skill links for skill plugins."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_plugin_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, skill_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, skill_configuration_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsPluginsSkillsListOutput:
        """
    List skill plugin skills
    Returns skills linked to a skill plugin.

    :param instance_id: str
    :param skill_plugin_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param skill_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param skill_configuration_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsPluginsSkillsListOutput
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
        if skill_id is not None:
            query_dict["skill_id"] = skill_id
        if status is not None:
            query_dict["status"] = status
        if skill_configuration_id is not None:
            query_dict["skill_configuration_id"] = skill_configuration_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id, 'skills'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsPluginsSkillsListOutput.from_dict)

    def add(self, instance_id: str, skill_plugin_id: str, *, skill_id: str, identifier: Optional[str] = None, client_name: Optional[str] = None, client_description: Optional[str] = None, client_metadata: Optional[Dict[str, Any]] = None, license: Optional[str] = None, compatibility: Optional[str] = None, skill_configuration_id: Optional[str] = None) -> DashboardInstanceSkillsPluginsSkillsAddOutput:
        """
    Add skill plugin skill
    Adds a skill to a skill plugin.

    :param instance_id: str
    :param skill_plugin_id: str
    :param skill_id: str
    :param identifier: Optional[str] (optional)
    :param client_name: Optional[str] (optional)
    :param client_description: Optional[str] (optional)
    :param client_metadata: Optional[Dict[str, Any]] (optional)
    :param license: Optional[str] (optional)
    :param compatibility: Optional[str] (optional)
    :param skill_configuration_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsPluginsSkillsAddOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["skill_id"] = skill_id
        if identifier is not None:
            body_dict["identifier"] = identifier
        if client_name is not None:
            body_dict["client_name"] = client_name
        if client_description is not None:
            body_dict["client_description"] = client_description
        if client_metadata is not None:
            body_dict["client_metadata"] = client_metadata
        if license is not None:
            body_dict["license"] = license
        if compatibility is not None:
            body_dict["compatibility"] = compatibility
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id, 'skills'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsPluginsSkillsAddOutput.from_dict)

    def get(self, instance_id: str, skill_plugin_id: str, skill_plugin_skill_id: str) -> DashboardInstanceSkillsPluginsSkillsGetOutput:
        """
    Get skill plugin skill
    Retrieves a skill plugin skill link.

    :param instance_id: str
    :param skill_plugin_id: str
    :param skill_plugin_skill_id: str
    :return: DashboardInstanceSkillsPluginsSkillsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id, 'skills', skill_plugin_skill_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsPluginsSkillsGetOutput.from_dict)

    def update(self, instance_id: str, skill_plugin_id: str, skill_plugin_skill_id: str, *, client_name: Optional[str] = None, client_description: Optional[str] = None, client_metadata: Optional[Dict[str, Any]] = None, license: Optional[str] = None, compatibility: Optional[str] = None, skill_configuration_id: Optional[str] = None) -> DashboardInstanceSkillsPluginsSkillsUpdateOutput:
        """
    Update skill plugin skill
    Updates a skill plugin skill link.

    :param instance_id: str
    :param skill_plugin_id: str
    :param skill_plugin_skill_id: str
    :param client_name: Optional[str] (optional)
    :param client_description: Optional[str] (optional)
    :param client_metadata: Optional[Dict[str, Any]] (optional)
    :param license: Optional[str] (optional)
    :param compatibility: Optional[str] (optional)
    :param skill_configuration_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsPluginsSkillsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if client_name is not None:
            body_dict["client_name"] = client_name
        if client_description is not None:
            body_dict["client_description"] = client_description
        if client_metadata is not None:
            body_dict["client_metadata"] = client_metadata
        if license is not None:
            body_dict["license"] = license
        if compatibility is not None:
            body_dict["compatibility"] = compatibility
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id, 'skills', skill_plugin_skill_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsPluginsSkillsUpdateOutput.from_dict)

    def remove(self, instance_id: str, skill_plugin_id: str, skill_plugin_skill_id: str) -> DashboardInstanceSkillsPluginsSkillsRemoveOutput:
        """
    Remove skill plugin skill
    Removes a skill from a skill plugin.

    :param instance_id: str
    :param skill_plugin_id: str
    :param skill_plugin_skill_id: str
    :return: DashboardInstanceSkillsPluginsSkillsRemoveOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-plugins', skill_plugin_id, 'skills', skill_plugin_skill_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsPluginsSkillsRemoveOutput.from_dict)