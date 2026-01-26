from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCallbacksEventsListOutput,
  DashboardInstanceCallbacksEventsListOutput,
  mapDashboardInstanceCallbacksEventsListQuery,
  DashboardInstanceCallbacksEventsListQuery,
  mapDashboardInstanceCallbacksEventsGetOutput,
  DashboardInstanceCallbacksEventsGetOutput,
)


class MetorialCallbacksEventsEndpoint(BaseMetorialEndpoint):
  """Represents callbacks that you have uploaded to Metorial. Callbacks can be linked to various resources based on their purpose. Metorial can also automatically extract callbacks for you, for example for data exports."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    callback_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceCallbacksEventsListOutput:
    """
    List callback events
    Returns a paginated list of callback events for a specific callback.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCallbacksEventsListOutput
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

    request = MetorialRequest(path=["callbacks-events"], query=query_dict)
    return self._get(request).transform(
      mapDashboardInstanceCallbacksEventsListOutput.from_dict
    )

  def get(self, event_id: str) -> DashboardInstanceCallbacksEventsGetOutput:
    """
    Get callback event by ID
    Retrieves details for a specific callback by its ID.

    :param event_id: str
    :return: DashboardInstanceCallbacksEventsGetOutput
    """
    request = MetorialRequest(path=["callbacks-events", event_id])
    return self._get(request).transform(
      mapDashboardInstanceCallbacksEventsGetOutput.from_dict
    )
