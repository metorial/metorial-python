from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderCollectionsListOutput, DashboardInstanceProviderCollectionsListOutput, mapDashboardInstanceProviderCollectionsListQuery, DashboardInstanceProviderCollectionsListQuery, mapDashboardInstanceProviderCollectionsGetOutput, DashboardInstanceProviderCollectionsGetOutput

class MetorialManagementInstanceProviderCollectionsEndpoint(BaseMetorialEndpoint):
    """A collection is a curated set of providers like 'Featured', 'Most Popular', or 'New Arrivals'."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_listing_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderCollectionsListOutput:
        """
    List provider collections
    Returns a paginated list of provider collections.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_listing_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProviderCollectionsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_listing_id is not None:
            query_dict["provider_listing_id"] = provider_listing_id

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-collections'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderCollectionsListOutput.from_dict)

    def get(self, instance_id: str, provider_collection_id: str) -> DashboardInstanceProviderCollectionsGetOutput:
        """
    Get provider collection
    Retrieves a specific provider collection by ID.

    :param instance_id: str
    :param provider_collection_id: str
    :return: DashboardInstanceProviderCollectionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-collections', provider_collection_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderCollectionsGetOutput.from_dict)