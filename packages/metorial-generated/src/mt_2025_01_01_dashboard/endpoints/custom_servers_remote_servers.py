from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersRemoteServersListOutput,
  DashboardInstanceCustomServersRemoteServersListOutput,
  mapDashboardInstanceCustomServersRemoteServersListQuery,
  DashboardInstanceCustomServersRemoteServersListQuery,
  mapDashboardInstanceCustomServersRemoteServersGetOutput,
  DashboardInstanceCustomServersRemoteServersGetOutput,
)


class MetorialCustomServersRemoteServersEndpoint(BaseMetorialEndpoint):
  """Manager remote servers"""

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
  ) -> DashboardInstanceCustomServersRemoteServersListOutput:
    """
    List remote servers
    List all remote servers

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceCustomServersRemoteServersListOutput
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
      path=["custom-servers", "remote-servers"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersRemoteServersListOutput.from_dict
    )

  def get(
    self, remote_server_id: str
  ) -> DashboardInstanceCustomServersRemoteServersGetOutput:
    """
    Get remote server
    Get information for a specific remote server

    :param remote_server_id: str
    :return: DashboardInstanceCustomServersRemoteServersGetOutput
    """
    request = MetorialRequest(
      path=["custom-servers", "remote-servers", remote_server_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersRemoteServersGetOutput.from_dict
    )
