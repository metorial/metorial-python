from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersListingGetOutput,
  DashboardInstanceCustomServersListingGetOutput,
  mapDashboardInstanceCustomServersListingUpdateOutput,
  DashboardInstanceCustomServersListingUpdateOutput,
  mapDashboardInstanceCustomServersListingUpdateBody,
  DashboardInstanceCustomServersListingUpdateBody,
)


class MetorialDashboardInstanceCustomServersListingEndpoint(BaseMetorialEndpoint):
  """Manager custom servers"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(
    self, instanceId: str, customServerId: str
  ) -> DashboardInstanceCustomServersListingGetOutput:
    """
    Get custom server listing
    Get a custom server listing

    :param instanceId: str
    :param customServerId: str
    :return: DashboardInstanceCustomServersListingGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "listing",
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersListingGetOutput.from_dict
    )

  def update(
    self,
    instanceId: str,
    customServerId: str,
    body: DashboardInstanceCustomServersListingUpdateBody,
  ) -> DashboardInstanceCustomServersListingUpdateOutput:
    """
    Update custom server listing
    Update a custom server listing

    :param instanceId: str
    :param customServerId: str
    :param body: DashboardInstanceCustomServersListingUpdateBody
    :return: DashboardInstanceCustomServersListingUpdateOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "listing",
      ],
      body=mapDashboardInstanceCustomServersListingUpdateBody.to_dict(body),
    )
    return self._patch(request).transform(
      mapDashboardInstanceCustomServersListingUpdateOutput.from_dict
    )
