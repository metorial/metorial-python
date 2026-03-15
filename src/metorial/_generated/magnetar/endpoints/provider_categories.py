from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderCategoriesListOutput, DashboardInstanceProviderCategoriesListOutput, mapDashboardInstanceProviderCategoriesListQuery, DashboardInstanceProviderCategoriesListQuery, mapDashboardInstanceProviderCategoriesGetOutput, DashboardInstanceProviderCategoriesGetOutput

class MetorialProviderCategoriesEndpoint(BaseMetorialEndpoint):
    """A category groups providers by function like 'Developer Tools' or 'ERPs'."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_listing_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderCategoriesListOutput:
        """
    List provider categories
    Returns a paginated list of provider categories.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_listing_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProviderCategoriesListOutput
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
            path=['provider-categories'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderCategoriesListOutput.from_dict)

    def get(self, provider_category_id: str) -> DashboardInstanceProviderCategoriesGetOutput:
        """
    Get provider category
    Retrieves a specific provider category by ID.

    :param provider_category_id: str
    :return: DashboardInstanceProviderCategoriesGetOutput
    """
        request = MetorialRequest(
            path=['provider-categories', provider_category_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderCategoriesGetOutput.from_dict)