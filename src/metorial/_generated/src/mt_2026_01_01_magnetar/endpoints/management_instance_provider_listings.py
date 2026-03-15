from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderListingsListOutput, DashboardInstanceProviderListingsListOutput, mapDashboardInstanceProviderListingsListQuery, DashboardInstanceProviderListingsListQuery, mapDashboardInstanceProviderListingsGetOutput, DashboardInstanceProviderListingsGetOutput

class MetorialManagementInstanceProviderListingsEndpoint(BaseMetorialEndpoint):
    """A listing is a provider enriched with marketplace metadata."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, provider_category_id: Optional[Union[str, List[str]]] = None, provider_collection_id: Optional[Union[str, List[str]]] = None, provider_group_id: Optional[Union[str, List[str]]] = None, publisher_id: Optional[Union[str, List[str]]] = None, is_owner: Optional[bool] = None, is_public: Optional[bool] = None, is_verified: Optional[bool] = None, is_official: Optional[bool] = None, is_metorial: Optional[bool] = None) -> DashboardInstanceProviderListingsListOutput:
        """
    List provider listings
    Returns a paginated list of provider listings.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param provider_category_id: Optional[Union[str, List[str]]] (optional)
    :param provider_collection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_group_id: Optional[Union[str, List[str]]] (optional)
    :param publisher_id: Optional[Union[str, List[str]]] (optional)
    :param is_owner: Optional[bool] (optional)
    :param is_public: Optional[bool] (optional)
    :param is_verified: Optional[bool] (optional)
    :param is_official: Optional[bool] (optional)
    :param is_metorial: Optional[bool] (optional)
    :return: DashboardInstanceProviderListingsListOutput
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
        if provider_category_id is not None:
            query_dict["provider_category_id"] = provider_category_id
        if provider_collection_id is not None:
            query_dict["provider_collection_id"] = provider_collection_id
        if provider_group_id is not None:
            query_dict["provider_group_id"] = provider_group_id
        if publisher_id is not None:
            query_dict["publisher_id"] = publisher_id
        if is_owner is not None:
            query_dict["is_owner"] = is_owner
        if is_public is not None:
            query_dict["is_public"] = is_public
        if is_verified is not None:
            query_dict["is_verified"] = is_verified
        if is_official is not None:
            query_dict["is_official"] = is_official
        if is_metorial is not None:
            query_dict["is_metorial"] = is_metorial

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-listings'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderListingsListOutput.from_dict)

    def get(self, instance_id: str, provider_listing_id: str) -> DashboardInstanceProviderListingsGetOutput:
        """
    Get provider listing
    Retrieves a specific provider listing by ID.

    :param instance_id: str
    :param provider_listing_id: str
    :return: DashboardInstanceProviderListingsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-listings', provider_listing_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderListingsGetOutput.from_dict)