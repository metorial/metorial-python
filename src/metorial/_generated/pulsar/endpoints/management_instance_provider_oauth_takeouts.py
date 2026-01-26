from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceProviderOauthTakeoutsListOutput,
  DashboardInstanceProviderOauthTakeoutsListOutput,
  mapDashboardInstanceProviderOauthTakeoutsListQuery,
  DashboardInstanceProviderOauthTakeoutsListQuery,
  mapDashboardInstanceProviderOauthTakeoutsCreateOutput,
  DashboardInstanceProviderOauthTakeoutsCreateOutput,
  mapDashboardInstanceProviderOauthTakeoutsCreateBody,
  DashboardInstanceProviderOauthTakeoutsCreateBody,
  mapDashboardInstanceProviderOauthTakeoutsGetOutput,
  DashboardInstanceProviderOauthTakeoutsGetOutput,
)


class MetorialManagementInstanceProviderOauthTakeoutsEndpoint(BaseMetorialEndpoint):
  """Manage provider OAuth takeout information"""

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
  ) -> DashboardInstanceProviderOauthTakeoutsListOutput:
    """
    List provider OAuth takeouts
    List all provider OAuth takeouts

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderOauthTakeoutsListOutput
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
      path=["instances", instance_id, "provider-oauth", "takeouts"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthTakeoutsListOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    *,
    oauth_session_id: str,
    note: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceProviderOauthTakeoutsCreateOutput:
    """
    Create provider OAuth takeout
    Create a new provider OAuth takeout

    :param instance_id: str
    :param note: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param oauth_session_id: str
    :return: DashboardInstanceProviderOauthTakeoutsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if note is not None:
      body_dict["note"] = note
    if metadata is not None:
      body_dict["metadata"] = metadata
    body_dict["oauth_session_id"] = oauth_session_id

    request = MetorialRequest(
      path=["instances", instance_id, "provider-oauth", "takeouts"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardInstanceProviderOauthTakeoutsCreateOutput.from_dict
    )

  def get(
    self, instance_id: str, takeout_id: str
  ) -> DashboardInstanceProviderOauthTakeoutsGetOutput:
    """
    Get provider OAuth takeout
    Get information for a specific provider OAuth takeout

    :param instance_id: str
    :param takeout_id: str
    :return: DashboardInstanceProviderOauthTakeoutsGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "provider-oauth", "takeouts", takeout_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthTakeoutsGetOutput.from_dict
    )
