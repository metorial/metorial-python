from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapServersListingsCollectionsListOutput, ServersListingsCollectionsListOutput, mapServersListingsCollectionsListQuery, ServersListingsCollectionsListQuery, mapServersListingsCollectionsGetOutput, ServersListingsCollectionsGetOutput

class MetorialServersListingsCollectionsEndpoint(BaseMetorialEndpoint):
    """Read and write server listing collection information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: ServersListingsCollectionsListQuery = None):
        """
    List server listing collections
    List all server listing collections

    :param query: ServersListingsCollectionsListQuery
    :return: ServersListingsCollectionsListOutput
    """
        request = MetorialRequest(
            path=['server-listing-collections'],
            query=mapServersListingsCollectionsListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapServersListingsCollectionsListOutput.from_dict)

    def get(self, serverListingCollectionId: str):
        """
    Get server listing collection
    Get the information of a specific server listing collection

    :param serverListingCollectionId: str
    :return: ServersListingsCollectionsGetOutput
    """
        request = MetorialRequest(
            path=['server-listing-collections', serverListingCollectionId]
        )
        return self._get(request).transform(mapServersListingsCollectionsGetOutput.from_dict)