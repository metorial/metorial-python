from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutput,
  DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput,
  mapDashboardInstanceProviderOauthConnectionsAuthenticationsListQuery,
  DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery,
  mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput,
  DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput,
)


class MetorialDashboardInstanceProviderOauthConnectionsAuthenticationsEndpoint(
  BaseMetorialEndpoint
):
  """Manage provider OAuth connection authentication information"""

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
  ) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput:
    """
    List provider OAuth connection authentications
    List provider OAuth connection authentications for a specific connection

    :param instance_id: str
    :param connection_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput
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
        "dashboard",
        "instances",
        instance_id,
        "provider-oauth",
        "connections",
        connection_id,
        "authentications",
      ],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutput.from_dict
    )

  def get(
    self, instance_id: str, connection_id: str, authentication_id: str
  ) -> DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput:
    """
    Get provider OAuth connection authentication
    Get the information of a specific provider OAuth connection authentication

    :param instance_id: str
    :param connection_id: str
    :param authentication_id: str
    :return: DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instance_id,
        "provider-oauth",
        "connections",
        connection_id,
        "authentications",
        authentication_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput.from_dict
    )
