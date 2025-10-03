from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapServersListingsCollectionsListOutput,
  ServersListingsCollectionsListOutput,
  mapServersListingsCollectionsListQuery,
  ServersListingsCollectionsListQuery,
  mapServersListingsCollectionsGetOutput,
  ServersListingsCollectionsGetOutput,
)


class MetorialServersListingsCollectionsEndpoint(BaseMetorialEndpoint):
  """Read and write server listing collection information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> ServersListingsCollectionsListOutput:
    """
    List server listing collections
    List all server listing collections

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: ServersListingsCollectionsListOutput
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

    request = MetorialRequest(path=["server-listing-collections"], query=query_dict)
    return self._get(request).transform(
      mapServersListingsCollectionsListOutput.from_dict
    )

  def get(
    self, server_listing_collection_id: str
  ) -> ServersListingsCollectionsGetOutput:
    """
    Get server listing collection
    Get the information of a specific server listing collection

    :param server_listing_collection_id: str
    :return: ServersListingsCollectionsGetOutput
    """
    request = MetorialRequest(
      path=["server-listing-collections", server_listing_collection_id]
    )
    return self._get(request).transform(
      mapServersListingsCollectionsGetOutput.from_dict
    )
