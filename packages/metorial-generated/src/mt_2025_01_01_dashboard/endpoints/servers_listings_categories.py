from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapServersListingsCategoriesListOutput,
  ServersListingsCategoriesListOutput,
  mapServersListingsCategoriesListQuery,
  ServersListingsCategoriesListQuery,
  mapServersListingsCategoriesGetOutput,
  ServersListingsCategoriesGetOutput,
)


class MetorialServersListingsCategoriesEndpoint(BaseMetorialEndpoint):
  """Provides access to server listing categories, used for organizing and filtering server listings."""

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
  ) -> ServersListingsCategoriesListOutput:
    """
    List server listing categories
    Returns a list of all available server listing categories.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: ServersListingsCategoriesListOutput
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

    request = MetorialRequest(path=["server-listing-categories"], query=query_dict)
    return self._get(request).transform(
      mapServersListingsCategoriesListOutput.from_dict
    )

  def get(self, server_listing_category_id: str) -> ServersListingsCategoriesGetOutput:
    """
    Get server listing category
    Returns information for a specific server listing category.

    :param server_listing_category_id: str
    :return: ServersListingsCategoriesGetOutput
    """
    request = MetorialRequest(
      path=["server-listing-categories", server_listing_category_id]
    )
    return self._get(request).transform(mapServersListingsCategoriesGetOutput.from_dict)
