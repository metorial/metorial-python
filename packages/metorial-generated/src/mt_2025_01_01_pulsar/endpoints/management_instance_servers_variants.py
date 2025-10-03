from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServersVariantsListOutput,
  DashboardInstanceServersVariantsListOutput,
  mapDashboardInstanceServersVariantsListQuery,
  DashboardInstanceServersVariantsListQuery,
  mapDashboardInstanceServersVariantsGetOutput,
  DashboardInstanceServersVariantsGetOutput,
)


class MetorialManagementInstanceServersVariantsEndpoint(BaseMetorialEndpoint):
  """Server variants define different instances of a server, each with its own configuration and capabilities. By default, Metorial picks the best variant automatically, but you can specify a variant if needed."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    server_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardInstanceServersVariantsListOutput:
    """
    List server variants
    Retrieve all variants for a given server

    :param instance_id: str
    :param server_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceServersVariantsListOutput
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

    request = MetorialRequest(
      path=["instances", instance_id, "servers", server_id, "variants"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceServersVariantsListOutput.from_dict
    )

  def get(
    self, instance_id: str, server_id: str, server_variant_id: str
  ) -> DashboardInstanceServersVariantsGetOutput:
    """
    Get server variant
    Retrieve details for a specific server variant

    :param instance_id: str
    :param server_id: str
    :param server_variant_id: str
    :return: DashboardInstanceServersVariantsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "servers",
        server_id,
        "variants",
        server_variant_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceServersVariantsGetOutput.from_dict
    )
