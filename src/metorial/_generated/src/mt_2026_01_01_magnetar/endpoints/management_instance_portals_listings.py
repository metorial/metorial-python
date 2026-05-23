from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsListingsListOutput, DashboardInstancePortalsListingsListOutput, mapDashboardInstancePortalsListingsListQuery, DashboardInstancePortalsListingsListQuery, mapDashboardInstancePortalsListingsGetOutput, DashboardInstancePortalsListingsGetOutput, mapDashboardInstancePortalsListingsCreateOutput, DashboardInstancePortalsListingsCreateOutput, mapDashboardInstancePortalsListingsCreateBody, DashboardInstancePortalsListingsCreateBody, mapDashboardInstancePortalsListingsUpdateOutput, DashboardInstancePortalsListingsUpdateOutput, mapDashboardInstancePortalsListingsUpdateBody, DashboardInstancePortalsListingsUpdateBody, mapDashboardInstancePortalsListingsDeleteOutput, DashboardInstancePortalsListingsDeleteOutput

class MetorialManagementInstancePortalsListingsEndpoint(BaseMetorialEndpoint):
    """Read the shared listings available on a portal surface."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, consumer_surface_provider_group_id: Optional[Union[str, List[str]]] = None, provider_template_id: Optional[Union[str, List[str]]] = None, magic_mcp_server_id: Optional[Union[str, List[str]]] = None, skill_id: Optional[Union[str, List[str]]] = None, skill_template_id: Optional[Union[str, List[str]]] = None, skill_group_id: Optional[Union[str, List[str]]] = None, skill_marketplace_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None) -> DashboardInstancePortalsListingsListOutput:
        """
    List portal listings
    Returns a paginated list of shared listings for a portal.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param consumer_surface_provider_group_id: Optional[Union[str, List[str]]] (optional)
    :param provider_template_id: Optional[Union[str, List[str]]] (optional)
    :param magic_mcp_server_id: Optional[Union[str, List[str]]] (optional)
    :param skill_id: Optional[Union[str, List[str]]] (optional)
    :param skill_template_id: Optional[Union[str, List[str]]] (optional)
    :param skill_group_id: Optional[Union[str, List[str]]] (optional)
    :param skill_marketplace_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstancePortalsListingsListOutput
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
        if consumer_surface_provider_group_id is not None:
            query_dict["consumer_surface_provider_group_id"] = consumer_surface_provider_group_id
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
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'listings'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsListingsListOutput.from_dict)

    def get(self, instance_id: str, portal_id: str, listing_id: str) -> DashboardInstancePortalsListingsGetOutput:
        """
    Get portal listing
    Retrieves one shared listing for a portal.

    :param instance_id: str
    :param portal_id: str
    :param listing_id: str
    :return: DashboardInstancePortalsListingsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'listings', listing_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsListingsGetOutput.from_dict)

    def create(self, instance_id: str, portal_id: str, *, access: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], name: Optional[str] = None, description: Optional[str] = None, readme: Optional[str] = None) -> DashboardInstancePortalsListingsCreateOutput:
        """
    Create portal listing
    Creates a shared listing for a portal.

    :param instance_id: str
    :param portal_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param readme: Optional[str] (optional)
    :param access: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstancePortalsListingsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if readme is not None:
            body_dict["readme"] = readme
        body_dict["access"] = access

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'listings'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsListingsCreateOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, listing_id: str, *, name: Optional[str] = None, description: Optional[str] = None, readme: Optional[str] = None) -> DashboardInstancePortalsListingsUpdateOutput:
        """
    Update portal listing
    Updates listing metadata for a portal listing.

    :param instance_id: str
    :param portal_id: str
    :param listing_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param readme: Optional[str] (optional)
    :return: DashboardInstancePortalsListingsUpdateOutput
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
            path=['instances', instance_id, 'portals', portal_id, 'listings', listing_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsListingsUpdateOutput.from_dict)

    def delete(self, instance_id: str, portal_id: str, listing_id: str) -> DashboardInstancePortalsListingsDeleteOutput:
        """
    Delete portal listing
    Deletes a portal listing and all consumer access attached to it.

    :param instance_id: str
    :param portal_id: str
    :param listing_id: str
    :return: DashboardInstancePortalsListingsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'listings', listing_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsListingsDeleteOutput.from_dict)