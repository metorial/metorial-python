from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCallbacksNotificationsListOutput,
  DashboardInstanceCallbacksNotificationsListOutput,
  mapDashboardInstanceCallbacksNotificationsListQuery,
  DashboardInstanceCallbacksNotificationsListQuery,
  mapDashboardInstanceCallbacksNotificationsGetOutput,
  DashboardInstanceCallbacksNotificationsGetOutput,
)


class MetorialManagementInstanceCallbacksNotificationsEndpoint(BaseMetorialEndpoint):
  """Represents callbacks that you have uploaded to Metorial. Callbacks can be linked to various resources based on their purpose. Metorial can also automatically extract callbacks for you, for example for data exports."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    callback_id: Optional[Union[str, List[str]]] = None,
    event_id: Optional[Union[str, List[str]]] = None,
    destination_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceCallbacksNotificationsListOutput:
    """
    List callback notifications
    Returns a paginated list of callback notifications for a specific callback.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :param event_id: Optional[Union[str, List[str]]] (optional)
    :param destination_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCallbacksNotificationsListOutput
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
    if callback_id is not None:
      query_dict["callback_id"] = callback_id
    if event_id is not None:
      query_dict["event_id"] = event_id
    if destination_id is not None:
      query_dict["destination_id"] = destination_id

    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-notifications"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceCallbacksNotificationsListOutput.from_dict
    )

  def get(
    self, instance_id: str, notification_id: str
  ) -> DashboardInstanceCallbacksNotificationsGetOutput:
    """
    Get callback notification by ID
    Retrieves details for a specific callback by its ID.

    :param instance_id: str
    :param notification_id: str
    :return: DashboardInstanceCallbacksNotificationsGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "callbacks-notifications", notification_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceCallbacksNotificationsGetOutput.from_dict
    )
