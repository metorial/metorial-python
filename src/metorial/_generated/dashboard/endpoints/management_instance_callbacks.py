from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCallbacksListOutput,
  DashboardInstanceCallbacksListOutput,
  mapDashboardInstanceCallbacksListQuery,
  DashboardInstanceCallbacksListQuery,
  mapDashboardInstanceCallbacksGetOutput,
  DashboardInstanceCallbacksGetOutput,
)


class MetorialManagementInstanceCallbacksEndpoint(BaseMetorialEndpoint):
  """Callbacks allow you to receive webhooks from MCP servers on Metorial. Callbacks are automatically created when you create a callback-enabled server deployment."""

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
    order: Optional[str] = None
  ) -> DashboardInstanceCallbacksListOutput:
    """
    List callbacks
    Returns a paginated list of callbacks.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceCallbacksListOutput
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
      path=["instances", instance_id, "callbacks"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceCallbacksListOutput.from_dict
    )

  def get(
    self, instance_id: str, callback_id: str
  ) -> DashboardInstanceCallbacksGetOutput:
    """
    Get callback by ID
    Retrieves details for a specific callback by its ID.

    :param instance_id: str
    :param callback_id: str
    :return: DashboardInstanceCallbacksGetOutput
    """
    request = MetorialRequest(path=["instances", instance_id, "callbacks", callback_id])
    return self._get(request).transform(
      mapDashboardInstanceCallbacksGetOutput.from_dict
    )
