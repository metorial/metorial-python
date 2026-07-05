from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMarketplacesPluginsListOutput, DashboardInstanceSkillsMarketplacesPluginsListOutput, mapDashboardInstanceSkillsMarketplacesPluginsListQuery, DashboardInstanceSkillsMarketplacesPluginsListQuery, mapDashboardInstanceSkillsMarketplacesPluginsAddOutput, DashboardInstanceSkillsMarketplacesPluginsAddOutput, mapDashboardInstanceSkillsMarketplacesPluginsAddBody, DashboardInstanceSkillsMarketplacesPluginsAddBody, mapDashboardInstanceSkillsMarketplacesPluginsGetOutput, DashboardInstanceSkillsMarketplacesPluginsGetOutput, mapDashboardInstanceSkillsMarketplacesPluginsRemoveOutput, DashboardInstanceSkillsMarketplacesPluginsRemoveOutput

class MetorialDashboardInstanceSkillsMarketplacesPluginsEndpoint(BaseMetorialEndpoint):
    """Manage plugin links for skill marketplaces."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_marketplace_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, skill_plugin_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, skill_configuration_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsMarketplacesPluginsListOutput:
        """
    List skill marketplace plugins
    Returns plugins linked to a skill marketplace.

    :param instance_id: str
    :param skill_marketplace_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param skill_plugin_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param skill_configuration_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsMarketplacesPluginsListOutput
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
        if skill_plugin_id is not None:
            query_dict["skill_plugin_id"] = skill_plugin_id
        if status is not None:
            query_dict["status"] = status
        if skill_configuration_id is not None:
            query_dict["skill_configuration_id"] = skill_configuration_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-marketplaces', skill_marketplace_id, 'plugins'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMarketplacesPluginsListOutput.from_dict)

    def add(self, instance_id: str, skill_marketplace_id: str, *, skill_plugin_id: str, skill_configuration_id: Optional[str] = None, identifier: Optional[str] = None) -> DashboardInstanceSkillsMarketplacesPluginsAddOutput:
        """
    Add skill marketplace plugin
    Adds a skill plugin to a skill marketplace.

    :param instance_id: str
    :param skill_marketplace_id: str
    :param skill_plugin_id: str
    :param skill_configuration_id: Optional[str] (optional)
    :param identifier: Optional[str] (optional)
    :return: DashboardInstanceSkillsMarketplacesPluginsAddOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["skill_plugin_id"] = skill_plugin_id
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id
        if identifier is not None:
            body_dict["identifier"] = identifier

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-marketplaces', skill_marketplace_id, 'plugins'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMarketplacesPluginsAddOutput.from_dict)

    def get(self, instance_id: str, skill_marketplace_id: str, skill_marketplace_plugin_id: str) -> DashboardInstanceSkillsMarketplacesPluginsGetOutput:
        """
    Get skill marketplace plugin
    Retrieves a skill marketplace plugin link.

    :param instance_id: str
    :param skill_marketplace_id: str
    :param skill_marketplace_plugin_id: str
    :return: DashboardInstanceSkillsMarketplacesPluginsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-marketplaces', skill_marketplace_id, 'plugins', skill_marketplace_plugin_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMarketplacesPluginsGetOutput.from_dict)

    def remove(self, instance_id: str, skill_marketplace_id: str, skill_marketplace_plugin_id: str) -> DashboardInstanceSkillsMarketplacesPluginsRemoveOutput:
        """
    Remove skill marketplace plugin
    Removes a skill plugin from a skill marketplace.

    :param instance_id: str
    :param skill_marketplace_id: str
    :param skill_marketplace_plugin_id: str
    :return: DashboardInstanceSkillsMarketplacesPluginsRemoveOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-marketplaces', skill_marketplace_id, 'plugins', skill_marketplace_plugin_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsMarketplacesPluginsRemoveOutput.from_dict)