from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAccessListOutput, DashboardInstancePortalsAccessListOutput, mapDashboardInstancePortalsAccessListQuery, DashboardInstancePortalsAccessListQuery, mapDashboardInstancePortalsAccessGetOutput, DashboardInstancePortalsAccessGetOutput, mapDashboardInstancePortalsAccessCreateOutput, DashboardInstancePortalsAccessCreateOutput, mapDashboardInstancePortalsAccessCreateBody, DashboardInstancePortalsAccessCreateBody, mapDashboardInstancePortalsAccessUpdateOutput, DashboardInstancePortalsAccessUpdateOutput, mapDashboardInstancePortalsAccessUpdateBody, DashboardInstancePortalsAccessUpdateBody, mapDashboardInstancePortalsAccessDeleteOutput, DashboardInstancePortalsAccessDeleteOutput

class MetorialManagementInstancePortalsAccessEndpoint(BaseMetorialEndpoint):
    """Manage which consumer groups can access portal provider templates and MCP servers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, consumer_group_id: Optional[Union[str, List[str]]] = None, provider_template_id: Optional[Union[str, List[str]]] = None, magic_mcp_server_id: Optional[Union[str, List[str]]] = None, skill_id: Optional[Union[str, List[str]]] = None, skill_template_id: Optional[Union[str, List[str]]] = None, skill_group_id: Optional[Union[str, List[str]]] = None, skill_marketplace_id: Optional[Union[str, List[str]]] = None, consumer_access_listing_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None) -> DashboardInstancePortalsAccessListOutput:
        """
    List portal access
    Returns a paginated list of consumer access rules for a portal.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param consumer_group_id: Optional[Union[str, List[str]]] (optional)
    :param provider_template_id: Optional[Union[str, List[str]]] (optional)
    :param magic_mcp_server_id: Optional[Union[str, List[str]]] (optional)
    :param skill_id: Optional[Union[str, List[str]]] (optional)
    :param skill_template_id: Optional[Union[str, List[str]]] (optional)
    :param skill_group_id: Optional[Union[str, List[str]]] (optional)
    :param skill_marketplace_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_access_listing_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstancePortalsAccessListOutput
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
        if consumer_group_id is not None:
            query_dict["consumer_group_id"] = consumer_group_id
        if provider_template_id is not None:
            query_dict["provider_template_id"] = provider_template_id
        if magic_mcp_server_id is not None:
            query_dict["magic_mcp_server_id"] = magic_mcp_server_id
        if skill_id is not None:
            query_dict["skill_id"] = skill_id
        if skill_template_id is not None:
            query_dict["skill_template_id"] = skill_template_id
        if skill_group_id is not None:
            query_dict["skill_group_id"] = skill_group_id
        if skill_marketplace_id is not None:
            query_dict["skill_marketplace_id"] = skill_marketplace_id
        if consumer_access_listing_id is not None:
            query_dict["consumer_access_listing_id"] = consumer_access_listing_id
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'access'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsAccessListOutput.from_dict)

    def get(self, instance_id: str, portal_id: str, access_id: str) -> DashboardInstancePortalsAccessGetOutput:
        """
    Get portal access
    Retrieves a portal access rule by ID.

    :param instance_id: str
    :param portal_id: str
    :param access_id: str
    :return: DashboardInstancePortalsAccessGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'access', access_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsAccessGetOutput.from_dict)

    def create(self, instance_id: str, portal_id: str, *, consumer_group_id: str, access: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], name: Optional[str] = None, description: Optional[str] = None, readme: Optional[str] = None) -> DashboardInstancePortalsAccessCreateOutput:
        """
    Create portal access
    Creates a new consumer access rule for the portal.

    :param instance_id: str
    :param portal_id: str
    :param consumer_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param readme: Optional[str] (optional)
    :param access: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstancePortalsAccessCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["consumer_group_id"] = consumer_group_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if readme is not None:
            body_dict["readme"] = readme
        body_dict["access"] = access

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'access'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsAccessCreateOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, access_id: str, *, name: Optional[str] = None, description: Optional[str] = None, readme: Optional[str] = None) -> DashboardInstancePortalsAccessUpdateOutput:
        """
    Update portal access
    Updates the shared listing fields for a portal access rule.

    :param instance_id: str
    :param portal_id: str
    :param access_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param readme: Optional[str] (optional)
    :return: DashboardInstancePortalsAccessUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if readme is not None:
            body_dict["readme"] = readme

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'access', access_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsAccessUpdateOutput.from_dict)

    def delete(self, instance_id: str, portal_id: str, access_id: str) -> DashboardInstancePortalsAccessDeleteOutput:
        """
    Delete portal access
    Deletes a consumer access rule from the portal.

    :param instance_id: str
    :param portal_id: str
    :param access_id: str
    :return: DashboardInstancePortalsAccessDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'access', access_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsAccessDeleteOutput.from_dict)