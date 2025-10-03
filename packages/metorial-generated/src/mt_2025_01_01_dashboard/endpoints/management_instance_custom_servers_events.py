from typing import Any, Dict, List, Optional, Union
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


class MetorialManagementInstanceCustomServersEventsEndpoint(BaseMetorialEndpoint):
  """Manager custom server events"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    custom_server_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    version_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceCustomServersEventsListOutput:
    """
    List custom server events
    List all custom server events

    :param instance_id: str
    :param custom_server_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param version_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCustomServersEventsListOutput
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
    if version_id is not None:
      query_dict["version_id"] = version_id

    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers", custom_server_id, "events"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersEventsListOutput.from_dict
    )

  def get(
    self, instance_id: str, custom_server_id: str, custom_server_event_id: str
  ) -> DashboardInstanceCustomServersEventsGetOutput:
    """
    Get custom server event
    Get information for a specific custom server event

    :param instance_id: str
    :param custom_server_id: str
    :param custom_server_event_id: str
    :return: DashboardInstanceCustomServersEventsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "custom-servers",
        custom_server_id,
        "events",
        custom_server_event_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersEventsGetOutput.from_dict
    )
