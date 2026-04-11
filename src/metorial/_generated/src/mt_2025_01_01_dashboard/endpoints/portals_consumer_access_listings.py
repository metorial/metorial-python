from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsConsumerAccessListingsListOutput, DashboardInstancePortalsConsumerAccessListingsListOutput, mapDashboardInstancePortalsConsumerAccessListingsListQuery, DashboardInstancePortalsConsumerAccessListingsListQuery, mapDashboardInstancePortalsConsumerAccessListingsGetOutput, DashboardInstancePortalsConsumerAccessListingsGetOutput

class MetorialPortalsConsumerAccessListingsEndpoint(BaseMetorialEndpoint):
    """Read the shared consumer access listings available on a portal surface."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, consumer_surface_provider_group_id: Optional[Union[str, List[str]]] = None, provider_template_id: Optional[Union[str, List[str]]] = None, magic_mcp_server_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None) -> DashboardInstancePortalsConsumerAccessListingsListOutput:
        """
    List portal consumer access listings
    Returns a paginated list of shared consumer access listings for a portal.

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
    :param type: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstancePortalsConsumerAccessListingsListOutput
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
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['portals', portal_id, 'consumer-access-listings'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerAccessListingsListOutput.from_dict)

    def get(self, portal_id: str, consumer_access_listing_id: str) -> DashboardInstancePortalsConsumerAccessListingsGetOutput:
        """
    Get portal consumer access listing
    Retrieves one shared consumer access listing for a portal.

    :param portal_id: str
    :param consumer_access_listing_id: str
    :return: DashboardInstancePortalsConsumerAccessListingsGetOutput
    """
        request = MetorialRequest(
            path=['portals', portal_id, 'consumer-access-listings', consumer_access_listing_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerAccessListingsGetOutput.from_dict)