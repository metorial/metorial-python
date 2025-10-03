from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceProviderOauthConnectionsEventsListOutput,
  DashboardInstanceProviderOauthConnectionsEventsListOutput,
  mapDashboardInstanceProviderOauthConnectionsEventsListQuery,
  DashboardInstanceProviderOauthConnectionsEventsListQuery,
  mapDashboardInstanceProviderOauthConnectionsEventsGetOutput,
  DashboardInstanceProviderOauthConnectionsEventsGetOutput,
)


class MetorialManagementInstanceProviderOauthConnectionsEventsEndpoint(
  BaseMetorialEndpoint
):
  """Manage provider OAuth connection event information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    connection_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardInstanceProviderOauthConnectionsEventsListOutput:
    """
    List provider OAuth connection events
    List provider OAuth connection events for a specific connection

    :param instance_id: str
    :param connection_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderOauthConnectionsEventsListOutput
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
      path=[
        "instances",
        instance_id,
        "provider-oauth",
        "connections",
        connection_id,
        "events",
      ],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsEventsListOutput.from_dict
    )

  def get(
    self, instance_id: str, connection_id: str, event_id: str
  ) -> DashboardInstanceProviderOauthConnectionsEventsGetOutput:
    """
    Get provider OAuth connection event
    Get the information of a specific provider OAuth connection event

    :param instance_id: str
    :param connection_id: str
    :param event_id: str
    :return: DashboardInstanceProviderOauthConnectionsEventsGetOutput
    """
    request = MetorialRequest(
      path=[
        "instances",
        instance_id,
        "provider-oauth",
        "connections",
        connection_id,
        "events",
        event_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsEventsGetOutput.from_dict
    )
