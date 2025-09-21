from typing import Optional, Dict, Any, List, Union
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
    self, query: DashboardInstanceProviderOauthConnectionsListQuery = None
  ) -> DashboardInstanceProviderOauthConnectionsListOutput:
    """
    List provider OAuth connections
    List all provider OAuth connections

    :param query: DashboardInstanceProviderOauthConnectionsListQuery
    :return: DashboardInstanceProviderOauthConnectionsListOutput
    """
    request = MetorialRequest(
      path=["provider-oauth", "connections"],
      query=mapDashboardInstanceProviderOauthConnectionsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsListOutput.from_dict
    )

  def create(
    self,
    *,
    template_id: Optional[str] = None,
    name: Optional[str] = None,
    discovery_url: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    scopes: Optional[List[str]] = None
  ) -> DashboardInstanceProviderOauthConnectionsCreateOutput:
    """
    Create provider OAuth connection
    Create a new provider OAuth connection

    :param template_id: str (optional)
    :param name: str (optional)
    :param discovery_url: str (optional)
    :param config: Dict[str, Any] (optional)
    :param client_id: str (optional)
    :param client_secret: str (optional)
    :param scopes: List[str] (optional)
    :return: DashboardInstanceProviderOauthConnectionsCreateOutput
    """
    _params = {
      "template_id": template_id,
      "name": name,
      "discovery_url": discovery_url,
      "config": config,
      "client_id": client_id,
      "client_secret": client_secret,
      "scopes": scopes,
    }
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["provider-oauth", "connections"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardInstanceProviderOauthConnectionsCreateOutput.from_dict
    )

  def get(
    self, connectionId: str
  ) -> DashboardInstanceProviderOauthConnectionsGetOutput:
    """
    Get provider OAuth connection
    Get information for a specific provider OAuth connection

    :param connectionId: str
    :return: DashboardInstanceProviderOauthConnectionsGetOutput
    """
    request = MetorialRequest(path=["provider-oauth", "connections", connectionId])
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthConnectionsGetOutput.from_dict
    )

  def update(
    self,
    connectionId: str,
    *,
    name: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    scopes: Optional[List[str]] = None
  ) -> DashboardInstanceProviderOauthConnectionsUpdateOutput:
    """
    Update provider OAuth connection
    Update a provider OAuth connection

    :param connectionId: str
    :param name: str (optional)
    :param config: Dict[str, Any] (optional)
    :param client_id: str (optional)
    :param client_secret: str (optional)
    :param scopes: List[str] (optional)
    :return: DashboardInstanceProviderOauthConnectionsUpdateOutput
    """
    _params = {
      "name": name,
      "config": config,
      "client_id": client_id,
      "client_secret": client_secret,
      "scopes": scopes,
    }
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["provider-oauth", "connections", connectionId],
      body=body,
    )
    return self._patch(request).transform(
      mapDashboardInstanceProviderOauthConnectionsUpdateOutput.from_dict
    )

  def delete(
    self, connectionId: str
  ) -> DashboardInstanceProviderOauthConnectionsDeleteOutput:
    """
    Delete provider OAuth connection
    Delete a provider OAuth connection

    :param connectionId: str
    :return: DashboardInstanceProviderOauthConnectionsDeleteOutput
    """
    request = MetorialRequest(path=["provider-oauth", "connections", connectionId])
    return self._delete(request).transform(
      mapDashboardInstanceProviderOauthConnectionsDeleteOutput.from_dict
    )
