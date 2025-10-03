from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapServersListingsListOutput,
  ServersListingsListOutput,
  mapServersListingsListQuery,
  ServersListingsListQuery,
  mapServersListingsGetOutput,
  ServersListingsGetOutput,
  mapServersListingsGetQuery,
  ServersListingsGetQuery,
)


class MetorialServersListingsEndpoint(BaseMetorialEndpoint):
  """Provides access to public server listings, including metadata, filtering, and ranking."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    search: Optional[str] = None,
    collection_id: Optional[Union[List[str], str]] = None,
    category_id: Optional[Union[List[str], str]] = None,
    profile_id: Optional[Union[List[str], str]] = None,
    instance_id: Optional[str] = None,
    order_by_rank: Optional[bool] = None,
    is_public: Optional[bool] = None,
    only_from_organization: Optional[bool] = None
  ) -> ServersListingsListOutput:
    """
    List server listings
    Returns a paginated list of server listings, filterable by collection, category, profile, or instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param collection_id: Optional[Union[List[str], str]] (optional)
    :param category_id: Optional[Union[List[str], str]] (optional)
    :param profile_id: Optional[Union[List[str], str]] (optional)
    :param instance_id: Optional[str] (optional)
    :param order_by_rank: Optional[bool] (optional)
    :param is_public: Optional[bool] (optional)
    :param only_from_organization: Optional[bool] (optional)
    :return: ServersListingsListOutput
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
    if collection_id is not None:
      query_dict["collection_id"] = collection_id
    if category_id is not None:
      query_dict["category_id"] = category_id
    if profile_id is not None:
      query_dict["profile_id"] = profile_id
    if instance_id is not None:
      query_dict["instance_id"] = instance_id
    if order_by_rank is not None:
      query_dict["order_by_rank"] = order_by_rank
    if is_public is not None:
      query_dict["is_public"] = is_public
    if only_from_organization is not None:
      query_dict["only_from_organization"] = only_from_organization

    request = MetorialRequest(path=["server-listings"], query=query_dict)
    return self._get(request).transform(mapServersListingsListOutput.from_dict)

  def get(
    self, server_listing_id: str, *, instance_id: Optional[str] = None
  ) -> ServersListingsGetOutput:
    """
    Get server listing
    Returns metadata and readme content for a specific server listing.

    :param server_listing_id: str
    :param instance_id: Optional[str] (optional)
    :return: ServersListingsGetOutput
    """
    # Build query parameters from keyword arguments
    query_dict = {}
    if instance_id is not None:
      query_dict["instance_id"] = instance_id

    request = MetorialRequest(
      path=["server-listings", server_listing_id], query=query_dict
    )
    return self._get(request).transform(mapServersListingsGetOutput.from_dict)
