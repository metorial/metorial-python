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
    self, instanceId: str, query: DashboardInstanceProviderOauthSessionsListQuery = None
  ) -> DashboardInstanceProviderOauthSessionsListOutput:
    """
    List provider OAuth sessions
    List all provider OAuth sessions

    :param instanceId: str
    :param query: DashboardInstanceProviderOauthSessionsListQuery
    :return: DashboardInstanceProviderOauthSessionsListOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "provider-oauth", "sessions"],
      query=mapDashboardInstanceProviderOauthSessionsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthSessionsListOutput.from_dict
    )

  def create(
    self, instanceId: str, body: DashboardInstanceProviderOauthSessionsCreateBody
  ) -> DashboardInstanceProviderOauthSessionsCreateOutput:
    """
    Create provider OAuth session
    Create a new provider OAuth session

    :param instanceId: str
    :param body: DashboardInstanceProviderOauthSessionsCreateBody
    :return: DashboardInstanceProviderOauthSessionsCreateOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "provider-oauth", "sessions"],
      body=mapDashboardInstanceProviderOauthSessionsCreateBody.to_dict(body),
    )
    return self._post(request).transform(
      mapDashboardInstanceProviderOauthSessionsCreateOutput.from_dict
    )

  def get(
    self, instanceId: str, oauthSessionId: str
  ) -> DashboardInstanceProviderOauthSessionsGetOutput:
    """
    Get provider OAuth session
    Get information for a specific provider OAuth session

    :param instanceId: str
    :param oauthSessionId: str
    :return: DashboardInstanceProviderOauthSessionsGetOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "provider-oauth", "sessions", oauthSessionId]
    )
    return self._get(request).transform(
      mapDashboardInstanceProviderOauthSessionsGetOutput.from_dict
    )

  def delete(
    self, instanceId: str, oauthSessionId: str
  ) -> DashboardInstanceProviderOauthSessionsDeleteOutput:
    """
    Delete provider OAuth session
    Delete a provider OAuth session

    :param instanceId: str
    :param oauthSessionId: str
    :return: DashboardInstanceProviderOauthSessionsDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "provider-oauth", "sessions", oauthSessionId]
    )
    return self._delete(request).transform(
      mapDashboardInstanceProviderOauthSessionsDeleteOutput.from_dict
    )
