from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceProviderOauthSessionsListOutput,
  DashboardInstanceProviderOauthSessionsListOutput,
  mapDashboardInstanceProviderOauthSessionsListQuery,
  DashboardInstanceProviderOauthSessionsListQuery,
  mapDashboardInstanceProviderOauthSessionsCreateOutput,
  DashboardInstanceProviderOauthSessionsCreateOutput,
  mapDashboardInstanceProviderOauthSessionsCreateBody,
  DashboardInstanceProviderOauthSessionsCreateBody,
  mapDashboardInstanceProviderOauthSessionsGetOutput,
  DashboardInstanceProviderOauthSessionsGetOutput,
  mapDashboardInstanceProviderOauthSessionsDeleteOutput,
  DashboardInstanceProviderOauthSessionsDeleteOutput,
)


class MetorialManagementInstanceProviderOauthSessionsEndpoint(BaseMetorialEndpoint):
  """Manage provider OAuth session information"""

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
  ) -> DashboardInstanceProviderOauthSessionsListOutput:
    """
    List provider OAuth sessions
    List all provider OAuth sessions

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderOauthSessionsListOutput
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
      path=["instances", instance_id, "provider-oauth", "sessions"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthSessionsListOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    *,
    metadata: Optional[Dict[str, Any]] = None,
    redirect_uri: Optional[str] = None,
    server_deployment_id: str = None,
    connection_id: str = None
  ) -> DashboardInstanceProviderOauthSessionsCreateOutput:
    """
    Create provider OAuth session
    Create a new provider OAuth session

    :param instance_id: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param redirect_uri: Optional[str] (optional)
    :param server_deployment_id: str (optional)
    :param connection_id: str (optional)
    :return: DashboardInstanceProviderOauthSessionsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if metadata is not None:
      body_dict["metadata"] = metadata
    if redirect_uri is not None:
      body_dict["redirect_uri"] = redirect_uri
    if server_deployment_id is not None:
      body_dict["server_deployment_id"] = server_deployment_id
    if connection_id is not None:
      body_dict["connection_id"] = connection_id

    request = MetorialRequest(
      path=["instances", instance_id, "provider-oauth", "sessions"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardInstanceProviderOauthSessionsCreateOutput.from_dict
    )

  def get(
    self, instance_id: str, oauth_session_id: str
  ) -> DashboardInstanceProviderOauthSessionsGetOutput:
    """
    Get provider OAuth session
    Get information for a specific provider OAuth session

    :param instance_id: str
    :param oauth_session_id: str
    :return: DashboardInstanceProviderOauthSessionsGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "provider-oauth", "sessions", oauth_session_id]
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthSessionsGetOutput.from_dict
    )

  def delete(
    self, instance_id: str, oauth_session_id: str
  ) -> DashboardInstanceProviderOauthSessionsDeleteOutput:
    """
    Delete provider OAuth session
    Delete a provider OAuth session

    :param instance_id: str
    :param oauth_session_id: str
    :return: DashboardInstanceProviderOauthSessionsDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "provider-oauth", "sessions", oauth_session_id]
    )
    return self._delete(request).transform(
      mapDashboardInstanceProviderOauthSessionsDeleteOutput.from_dict
    )
