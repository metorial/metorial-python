from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersListOutput,
  DashboardInstanceCustomServersListOutput,
  mapDashboardInstanceCustomServersListQuery,
  DashboardInstanceCustomServersListQuery,
  mapDashboardInstanceCustomServersCreateOutput,
  DashboardInstanceCustomServersCreateOutput,
  mapDashboardInstanceCustomServersCreateBody,
  DashboardInstanceCustomServersCreateBody,
  mapDashboardInstanceCustomServersUpdateOutput,
  DashboardInstanceCustomServersUpdateOutput,
  mapDashboardInstanceCustomServersUpdateBody,
  DashboardInstanceCustomServersUpdateBody,
  mapDashboardInstanceCustomServersDeleteOutput,
  DashboardInstanceCustomServersDeleteOutput,
  mapDashboardInstanceCustomServersGetOutput,
  DashboardInstanceCustomServersGetOutput,
)


class MetorialManagementInstanceCustomServersEndpoint(BaseMetorialEndpoint):
  """Manager custom servers"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, instanceId: str, query: DashboardInstanceCustomServersListQuery = None
  ) -> DashboardInstanceCustomServersListOutput:
    """
    List custom servers
    List all custom servers

    :param instanceId: str
    :param query: DashboardInstanceCustomServersListQuery
    :return: DashboardInstanceCustomServersListOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers"],
      query=mapDashboardInstanceCustomServersListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersListOutput.from_dict
    )

  def create(
    self, instanceId: str, body: DashboardInstanceCustomServersCreateBody
  ) -> DashboardInstanceCustomServersCreateOutput:
    """
    Create custom server
    Create a new custom server

    :param instanceId: str
    :param body: DashboardInstanceCustomServersCreateBody
    :return: DashboardInstanceCustomServersCreateOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers"],
      body=mapDashboardInstanceCustomServersCreateBody.to_dict(body),
    )
    return self._post(request).transform(
      mapDashboardInstanceCustomServersCreateOutput.from_dict
    )

  def update(
    self,
    instanceId: str,
    customServerId: str,
    body: DashboardInstanceCustomServersUpdateBody,
  ) -> DashboardInstanceCustomServersUpdateOutput:
    """
    Update custom server
    Update a custom server

    :param instanceId: str
    :param customServerId: str
    :param body: DashboardInstanceCustomServersUpdateBody
    :return: DashboardInstanceCustomServersUpdateOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers", customServerId],
      body=mapDashboardInstanceCustomServersUpdateBody.to_dict(body),
    )
    return self._patch(request).transform(
      mapDashboardInstanceCustomServersUpdateOutput.from_dict
    )

  def delete(
    self, instanceId: str, customServerId: str
  ) -> DashboardInstanceCustomServersDeleteOutput:
    """
    Delete custom server
    Delete a custom server

    :param instanceId: str
    :param customServerId: str
    :return: DashboardInstanceCustomServersDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers", customServerId]
    )
    return self._delete(request).transform(
      mapDashboardInstanceCustomServersDeleteOutput.from_dict
    )

  def get(
    self, instanceId: str, customServerId: str
  ) -> DashboardInstanceCustomServersGetOutput:
    """
    Get custom server
    Get information for a specific custom server

    :param instanceId: str
    :param customServerId: str
    :return: DashboardInstanceCustomServersGetOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "custom-servers", customServerId]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersGetOutput.from_dict
    )
