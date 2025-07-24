from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapServersListingsListOutput, ServersListingsListOutput, mapServersListingsListQuery, ServersListingsListQuery, mapServersListingsGetOutput, ServersListingsGetOutput

class MetorialServersListingsEndpoint(BaseMetorialEndpoint):
    """Provides access to public server listings, including metadata, filtering, and ranking."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: ServersListingsListQuery = None):
        """
    List server listings
    Returns a paginated list of server listings, filterable by collection, category, profile, or instance.

    :param query: ServersListingsListQuery
    :return: ServersListingsListOutput
    """
        request = MetorialRequest(
            path=['server-listings'],
            query=mapServersListingsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapServersListingsListOutput.from_dict)

    def get(self, serverListingId: str):
        """
    Get server listing
    Returns metadata and readme content for a specific server listing.

    :param serverListingId: str
    :return: ServersListingsGetOutput
    """
        request = MetorialRequest(
            path=['server-listings', serverListingId]
        )
        return self._get(request).transform(mapServersListingsGetOutput.from_dict)