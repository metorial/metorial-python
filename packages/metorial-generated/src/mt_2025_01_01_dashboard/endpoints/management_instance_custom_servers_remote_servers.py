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


class MetorialManagementInstanceCustomServersRemoteServersEndpoint(
  BaseMetorialEndpoint
):
  """Manager remote servers"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instanceId: str,
    query: DashboardInstanceCustomServersRemoteServersListQuery = None,
  ) -> DashboardInstanceCustomServersRemoteServersListOutput:
    """
    List remote servers
    List all remote servers

    :param instanceId: str
    :param query: DashboardInstanceCustomServersRemoteServersListQuery
    :return: DashboardInstanceCustomServersRemoteServersListOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers", "remote-servers"],
      query=mapDashboardInstanceCustomServersRemoteServersListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersRemoteServersListOutput.from_dict
    )

  def get(
    self, instanceId: str, remoteServerId: str
  ) -> DashboardInstanceCustomServersRemoteServersGetOutput:
    """
    Get remote server
    Get information for a specific remote server

    :param instanceId: str
    :param remoteServerId: str
    :return: DashboardInstanceCustomServersRemoteServersGetOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers", "remote-servers", remoteServerId]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersRemoteServersGetOutput.from_dict
    )
