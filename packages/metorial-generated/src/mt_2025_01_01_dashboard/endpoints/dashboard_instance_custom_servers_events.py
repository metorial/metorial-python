from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersEventsListOutput,
  DashboardInstanceCustomServersEventsListOutput,
  mapDashboardInstanceCustomServersEventsListQuery,
  DashboardInstanceCustomServersEventsListQuery,
  mapDashboardInstanceCustomServersEventsGetOutput,
  DashboardInstanceCustomServersEventsGetOutput,
)


class MetorialDashboardInstanceCustomServersEventsEndpoint(BaseMetorialEndpoint):
  """Manager custom server events"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instanceId: str,
    customServerId: str,
    query: DashboardInstanceCustomServersEventsListQuery = None,
  ) -> DashboardInstanceCustomServersEventsListOutput:
    """
    List custom server events
    List all custom server events

    :param instanceId: str
    :param customServerId: str
    :param query: DashboardInstanceCustomServersEventsListQuery
    :return: DashboardInstanceCustomServersEventsListOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "events",
      ],
      query=mapDashboardInstanceCustomServersEventsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersEventsListOutput.from_dict
    )

  def get(
    self, instanceId: str, customServerId: str, customServerEventId: str
  ) -> DashboardInstanceCustomServersEventsGetOutput:
    """
    Get custom server event
    Get information for a specific custom server event

    :param instanceId: str
    :param customServerId: str
    :param customServerEventId: str
    :return: DashboardInstanceCustomServersEventsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "events",
        customServerEventId,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersEventsGetOutput.from_dict
    )
