from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersVersionsListOutput,
  DashboardInstanceCustomServersVersionsListOutput,
  mapDashboardInstanceCustomServersVersionsListQuery,
  DashboardInstanceCustomServersVersionsListQuery,
  mapDashboardInstanceCustomServersVersionsCreateOutput,
  DashboardInstanceCustomServersVersionsCreateOutput,
  mapDashboardInstanceCustomServersVersionsCreateBody,
  DashboardInstanceCustomServersVersionsCreateBody,
  mapDashboardInstanceCustomServersVersionsGetOutput,
  DashboardInstanceCustomServersVersionsGetOutput,
)


class MetorialCustomServersVersionsEndpoint(BaseMetorialEndpoint):
  """Manager custom server versions"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    customServerId: str,
    query: DashboardInstanceCustomServersVersionsListQuery = None,
  ) -> DashboardInstanceCustomServersVersionsListOutput:
    """
    List custom server versions
    List all custom server versions

    :param customServerId: str
    :param query: DashboardInstanceCustomServersVersionsListQuery
    :return: DashboardInstanceCustomServersVersionsListOutput
    """
    request = MetorialRequest(
      path=["custom-servers", customServerId, "versions"],
      query=mapDashboardInstanceCustomServersVersionsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersVersionsListOutput.from_dict
    )

  def create(
    self, customServerId: str, body: DashboardInstanceCustomServersVersionsCreateBody
  ) -> DashboardInstanceCustomServersVersionsCreateOutput:
    """
    Create custom server version
    Create a new custom server version

    :param customServerId: str
    :param body: DashboardInstanceCustomServersVersionsCreateBody
    :return: DashboardInstanceCustomServersVersionsCreateOutput
    """
    request = MetorialRequest(
      path=["custom-servers", customServerId, "versions"],
      body=mapDashboardInstanceCustomServersVersionsCreateBody.to_dict(body),
    )
    return self._post(request).transform(
      mapDashboardInstanceCustomServersVersionsCreateOutput.from_dict
    )

  def get(
    self, customServerId: str, customServerVersionId: str
  ) -> DashboardInstanceCustomServersVersionsGetOutput:
    """
    Get custom server version
    Get information for a specific custom server version

    :param customServerId: str
    :param customServerVersionId: str
    :return: DashboardInstanceCustomServersVersionsGetOutput
    """
    request = MetorialRequest(
      path=["custom-servers", customServerId, "versions", customServerVersionId]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersVersionsGetOutput.from_dict
    )
