from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersDeploymentsListOutput,
  DashboardInstanceCustomServersDeploymentsListOutput,
  mapDashboardInstanceCustomServersDeploymentsListQuery,
  DashboardInstanceCustomServersDeploymentsListQuery,
  mapDashboardInstanceCustomServersDeploymentsGetOutput,
  DashboardInstanceCustomServersDeploymentsGetOutput,
)


class MetorialDashboardInstanceCustomServersDeploymentsEndpoint(BaseMetorialEndpoint):
  """Manager custom server deployments"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instanceId: str,
    customServerId: str,
    query: DashboardInstanceCustomServersDeploymentsListQuery = None,
  ) -> DashboardInstanceCustomServersDeploymentsListOutput:
    """
    List custom server deployments
    List all custom server deployments

    :param instanceId: str
    :param customServerId: str
    :param query: DashboardInstanceCustomServersDeploymentsListQuery
    :return: DashboardInstanceCustomServersDeploymentsListOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "deployments",
      ],
      query=mapDashboardInstanceCustomServersDeploymentsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersDeploymentsListOutput.from_dict
    )

  def get(
    self, instanceId: str, customServerId: str, customServerDeploymentId: str
  ) -> DashboardInstanceCustomServersDeploymentsGetOutput:
    """
    Get custom server deployment
    Get information for a specific custom server deployment

    :param instanceId: str
    :param customServerId: str
    :param customServerDeploymentId: str
    :return: DashboardInstanceCustomServersDeploymentsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instanceId,
        "custom-servers",
        customServerId,
        "deployments",
        customServerDeploymentId,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersDeploymentsGetOutput.from_dict
    )
