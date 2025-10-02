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


class MetorialCustomServersEventsEndpoint(BaseMetorialEndpoint):
  """Manager custom server events"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    customServerId: str,
    query: DashboardInstanceCustomServersEventsListQuery = None,
  ) -> DashboardInstanceCustomServersEventsListOutput:
    """
    List custom server events
    List all custom server events

    :param customServerId: str
    :param query: DashboardInstanceCustomServersEventsListQuery
    :return: DashboardInstanceCustomServersEventsListOutput
    """
    request = MetorialRequest(
      path=["custom-servers", customServerId, "events"],
      query=mapDashboardInstanceCustomServersEventsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersEventsListOutput.from_dict
    )

  def get(
    self, customServerId: str, customServerEventId: str
  ) -> DashboardInstanceCustomServersEventsGetOutput:
    """
    Get custom server event
    Get information for a specific custom server event

    :param customServerId: str
    :param customServerEventId: str
    :return: DashboardInstanceCustomServersEventsGetOutput
    """
    request = MetorialRequest(
      path=["custom-servers", customServerId, "events", customServerEventId]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersEventsGetOutput.from_dict
    )
