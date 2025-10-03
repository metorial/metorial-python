from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServersVersionsListOutput,
  DashboardInstanceServersVersionsListOutput,
  mapDashboardInstanceServersVersionsListQuery,
  DashboardInstanceServersVersionsListQuery,
  mapDashboardInstanceServersVersionsGetOutput,
  DashboardInstanceServersVersionsGetOutput,
)


class MetorialManagementInstanceServersVersionsEndpoint(BaseMetorialEndpoint):
  """Servers in Metorial are version controlled. Metorial automatically updates servers to the latest version when available. These endpoints help you keep track of server versions in the Metorial catalog."""

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
    order: Optional[str] = None,
    variant_id: Optional[str] = None
  ) -> DashboardInstanceServersVersionsListOutput:
    """
    List server versions
    Retrieve all versions for a given server

    :param instance_id: str
    :param server_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param variant_id: Optional[str] (optional)
    :return: DashboardInstanceServersVersionsListOutput
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
    if variant_id is not None:
      query_dict["variant_id"] = variant_id

    request = MetorialRequest(
      path=["instances", instance_id, "servers", server_id, "versions"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceServersVersionsListOutput.from_dict
    )

  def get(
    self, instance_id: str, server_id: str, server_version_id: str
  ) -> DashboardInstanceServersVersionsGetOutput:
    """
    Get server version
    Retrieve details for a specific server version

    :param instance_id: str
    :param server_id: str
    :param server_version_id: str
    :return: DashboardInstanceServersVersionsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "servers",
        server_id,
        "versions",
        server_version_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceServersVersionsGetOutput.from_dict
    )
