from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceProviderOauthConnectionsListOutput,
  DashboardInstanceProviderOauthConnectionsListOutput,
  mapDashboardInstanceProviderOauthConnectionsListQuery,
  DashboardInstanceProviderOauthConnectionsListQuery,
  mapDashboardInstanceProviderOauthConnectionsCreateOutput,
  DashboardInstanceProviderOauthConnectionsCreateOutput,
  mapDashboardInstanceProviderOauthConnectionsCreateBody,
  DashboardInstanceProviderOauthConnectionsCreateBody,
  mapDashboardInstanceProviderOauthConnectionsGetOutput,
  DashboardInstanceProviderOauthConnectionsGetOutput,
  mapDashboardInstanceProviderOauthConnectionsUpdateOutput,
  DashboardInstanceProviderOauthConnectionsUpdateOutput,
  mapDashboardInstanceProviderOauthConnectionsUpdateBody,
  DashboardInstanceProviderOauthConnectionsUpdateBody,
  mapDashboardInstanceProviderOauthConnectionsDeleteOutput,
  DashboardInstanceProviderOauthConnectionsDeleteOutput,
)


class MetorialProviderOauthConnectionsEndpoint(BaseMetorialEndpoint):
  """Manage provider OAuth connection information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardInstanceProviderOauthConnectionsListOutput:
    """
    List provider OAuth connections
    List all provider OAuth connections

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderOauthConnectionsListOutput
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

    request = MetorialRequest(path=["provider-oauth", "connections"], query=query_dict)
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsListOutput.from_dict
    )

  def create(
    self,
    *,
    config: Dict[str, Any],
    client_id: str,
    client_secret: str,
    scopes: List[str],
    name: Optional[str] = None,
    description: Optional[str] = None,
    discovery_url: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceProviderOauthConnectionsCreateOutput:
    """
    Create provider OAuth connection
    Create a new provider OAuth connection

    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param discovery_url: Optional[str] (optional)
    :param config: Dict[str, Any]
    :param client_id: str
    :param client_secret: str
    :param scopes: List[str]
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderOauthConnectionsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if discovery_url is not None:
      body_dict["discovery_url"] = discovery_url
    body_dict["config"] = config
    body_dict["client_id"] = client_id
    body_dict["client_secret"] = client_secret
    body_dict["scopes"] = scopes
    if metadata is not None:
      body_dict["metadata"] = metadata

    request = MetorialRequest(path=["provider-oauth", "connections"], body=body_dict)
    return self._post(request).transform(
      mapDashboardInstanceProviderOauthConnectionsCreateOutput.from_dict
    )

  def get(
    self, connection_id: str
  ) -> DashboardInstanceProviderOauthConnectionsGetOutput:
    """
    Get provider OAuth connection
    Get information for a specific provider OAuth connection

    :param connection_id: str
    :return: DashboardInstanceProviderOauthConnectionsGetOutput
    """
    request = MetorialRequest(path=["provider-oauth", "connections", connection_id])
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsGetOutput.from_dict
    )

  def update(
    self,
    connection_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    scopes: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceProviderOauthConnectionsUpdateOutput:
    """
    Update provider OAuth connection
    Update a provider OAuth connection

    :param connection_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param config: Optional[Dict[str, Any]] (optional)
    :param client_id: Optional[str] (optional)
    :param client_secret: Optional[str] (optional)
    :param scopes: Optional[List[str]] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderOauthConnectionsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if config is not None:
      body_dict["config"] = config
    if client_id is not None:
      body_dict["client_id"] = client_id
    if client_secret is not None:
      body_dict["client_secret"] = client_secret
    if scopes is not None:
      body_dict["scopes"] = scopes
    if metadata is not None:
      body_dict["metadata"] = metadata

    request = MetorialRequest(
      path=["provider-oauth", "connections", connection_id], body=body_dict
    )
    return self._patch(request).transform(
      mapDashboardInstanceProviderOauthConnectionsUpdateOutput.from_dict
    )

  def delete(
    self, connection_id: str
  ) -> DashboardInstanceProviderOauthConnectionsDeleteOutput:
    """
    Delete provider OAuth connection
    Delete a provider OAuth connection

    :param connection_id: str
    :return: DashboardInstanceProviderOauthConnectionsDeleteOutput
    """
    request = MetorialRequest(path=["provider-oauth", "connections", connection_id])
    return self._delete(request).transform(
      mapDashboardInstanceProviderOauthConnectionsDeleteOutput.from_dict
    )
