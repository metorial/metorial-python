from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapServersListingsCategoriesListOutput, ServersListingsCategoriesListOutput, mapServersListingsCategoriesListQuery, ServersListingsCategoriesListQuery, mapServersListingsCategoriesGetOutput, ServersListingsCategoriesGetOutput

class MetorialServersListingsCategoriesEndpoint(BaseMetorialEndpoint):
    """Provides access to server listing categories, used for organizing and filtering server listings."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: ServersListingsCategoriesListQuery = None):
        """
    List server listing categories
    Returns a list of all available server listing categories.

    :param query: ServersListingsCategoriesListQuery
    :return: ServersListingsCategoriesListOutput
    """
        request = MetorialRequest(
            path=['server-listing-categories'],
            query=mapServersListingsCategoriesListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapServersListingsCategoriesListOutput.from_dict)

    def get(self, serverListingCategoryId: str):
        """
    Get server listing category
    Returns information for a specific server listing category.

    :param serverListingCategoryId: str
    :return: ServersListingsCategoriesGetOutput
    """
        request = MetorialRequest(
            path=['server-listing-categories', serverListingCategoryId]
        )
        return self._get(request).transform(mapServersListingsCategoriesGetOutput.from_dict)