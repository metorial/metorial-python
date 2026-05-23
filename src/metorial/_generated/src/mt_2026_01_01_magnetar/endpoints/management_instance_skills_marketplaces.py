from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMarketplacesListOutput, DashboardInstanceSkillsMarketplacesListOutput, mapDashboardInstanceSkillsMarketplacesListQuery, DashboardInstanceSkillsMarketplacesListQuery, mapDashboardInstanceSkillsMarketplacesGetOutput, DashboardInstanceSkillsMarketplacesGetOutput, mapDashboardInstanceSkillsMarketplacesCreateOutput, DashboardInstanceSkillsMarketplacesCreateOutput, mapDashboardInstanceSkillsMarketplacesCreateBody, DashboardInstanceSkillsMarketplacesCreateBody, mapDashboardInstanceSkillsMarketplacesUpdateOutput, DashboardInstanceSkillsMarketplacesUpdateOutput, mapDashboardInstanceSkillsMarketplacesUpdateBody, DashboardInstanceSkillsMarketplacesUpdateBody, mapDashboardInstanceSkillsMarketplacesArchiveOutput, DashboardInstanceSkillsMarketplacesArchiveOutput, mapDashboardInstanceSkillsMarketplacesSyncOutput, DashboardInstanceSkillsMarketplacesSyncOutput, mapDashboardInstanceSkillsMarketplacesSyncBody, DashboardInstanceSkillsMarketplacesSyncBody

class MetorialManagementInstanceSkillsMarketplacesEndpoint(BaseMetorialEndpoint):
    """Manage skill marketplaces for an instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, skill_configuration_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsMarketplacesListOutput:
        """
    List skill marketplaces
    Returns a paginated list of skill marketplaces.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param skill_configuration_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsMarketplacesListOutput
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
        if status is not None:
            query_dict["status"] = status
        if skill_configuration_id is not None:
            query_dict["skill_configuration_id"] = skill_configuration_id
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-marketplaces'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMarketplacesListOutput.from_dict)

    def get(self, instance_id: str, skill_marketplace_id: str) -> DashboardInstanceSkillsMarketplacesGetOutput:
        """
    Get skill marketplace
    Retrieves a skill marketplace.

    :param instance_id: str
    :param skill_marketplace_id: str
    :return: DashboardInstanceSkillsMarketplacesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-marketplaces', skill_marketplace_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMarketplacesGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, image_file_id: Optional[str] = None, skill_configuration_id: Optional[str] = None) -> DashboardInstanceSkillsMarketplacesCreateOutput:
        """
    Create skill marketplace
    Creates a skill marketplace.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param image_file_id: Optional[str] (optional)
    :param skill_configuration_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsMarketplacesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-marketplaces'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMarketplacesCreateOutput.from_dict)

    def update(self, instance_id: str, skill_marketplace_id: str, *, name: Optional[str] = None, description: Optional[str] = None, image_file_id: Optional[str] = None, skill_configuration_id: Optional[str] = None) -> DashboardInstanceSkillsMarketplacesUpdateOutput:
        """
    Update skill marketplace
    Updates a skill marketplace.

    :param instance_id: str
    :param skill_marketplace_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param image_file_id: Optional[str] (optional)
    :param skill_configuration_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsMarketplacesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id
        if skill_configuration_id is not None:
            body_dict["skill_configuration_id"] = skill_configuration_id

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-marketplaces', skill_marketplace_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsMarketplacesUpdateOutput.from_dict)

    def archive(self, instance_id: str, skill_marketplace_id: str) -> DashboardInstanceSkillsMarketplacesArchiveOutput:
        """
    Archive skill marketplace
    Archives a skill marketplace.

    :param instance_id: str
    :param skill_marketplace_id: str
    :return: DashboardInstanceSkillsMarketplacesArchiveOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-marketplaces', skill_marketplace_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsMarketplacesArchiveOutput.from_dict)

    def sync(self, instance_id: str, skill_marketplace_id: str) -> DashboardInstanceSkillsMarketplacesSyncOutput:
        """
    Sync skill marketplace
    Forces a skill marketplace sync.

    :param instance_id: str
    :param skill_marketplace_id: str
    :return: DashboardInstanceSkillsMarketplacesSyncOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-marketplaces', skill_marketplace_id, 'sync']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMarketplacesSyncOutput.from_dict)