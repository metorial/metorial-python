from typing import Optional, Dict, Any, List, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServersDeploymentsListOutput,
  DashboardInstanceServersDeploymentsListOutput,
  mapDashboardInstanceServersDeploymentsListQuery,
  DashboardInstanceServersDeploymentsListQuery,
  mapDashboardInstanceServersDeploymentsGetOutput,
  DashboardInstanceServersDeploymentsGetOutput,
  mapDashboardInstanceServersDeploymentsCreateOutput,
  DashboardInstanceServersDeploymentsCreateOutput,
  mapDashboardInstanceServersDeploymentsCreateBody,
  DashboardInstanceServersDeploymentsCreateBody,
  mapDashboardInstanceServersDeploymentsUpdateOutput,
  DashboardInstanceServersDeploymentsUpdateOutput,
  mapDashboardInstanceServersDeploymentsUpdateBody,
  DashboardInstanceServersDeploymentsUpdateBody,
  mapDashboardInstanceServersDeploymentsDeleteOutput,
  DashboardInstanceServersDeploymentsDeleteOutput,
)


class MetorialManagementInstanceServersDeploymentsEndpoint(BaseMetorialEndpoint):
  """A server deployment represents a specific instance of an MCP server that can be connected to. It contains configuration for the MCP server, such as API keys for the underlying MCP server."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, instanceId: str, query: DashboardInstanceServersDeploymentsListQuery = None
  ) -> DashboardInstanceServersDeploymentsListOutput:
    """
    List server deployments
    Retrieve a list of server deployments within the instance. Supports filtering by status, server, variant, and session.

    :param instanceId: str
    :param query: DashboardInstanceServersDeploymentsListQuery
    :return: DashboardInstanceServersDeploymentsListOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "server-deployments"],
      query=mapDashboardInstanceServersDeploymentsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardInstanceServersDeploymentsListOutput.from_dict
    )

  def get(
    self, instanceId: str, serverDeploymentId: str
  ) -> DashboardInstanceServersDeploymentsGetOutput:
    """
    Get server deployment
    Fetch detailed information about a specific server deployment.

    :param instanceId: str
    :param serverDeploymentId: str
    :return: DashboardInstanceServersDeploymentsGetOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "server-deployments", serverDeploymentId]
    )
    return self._get(request).transform(
      mapDashboardInstanceServersDeploymentsGetOutput.from_dict
    )

  def create(self, instanceId: str) -> DashboardInstanceServersDeploymentsCreateOutput:
    """
    Create server deployment
    Create a new server deployment using an existing or newly defined server implementation.

    :param instanceId: str
    :return: DashboardInstanceServersDeploymentsCreateOutput
    """
    {}

    request = MetorialRequest(
      path=["instances", instanceId, "server-deployments"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardInstanceServersDeploymentsCreateOutput.from_dict
    )

  def update(
    self,
    instanceId: str,
    serverDeploymentId: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    config: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceServersDeploymentsUpdateOutput:
    """
    Update server deployment
    Update metadata, configuration, or other properties of a server deployment.

    :param instanceId: str
    :param serverDeploymentId: str
    :param name: str (optional)
    :param description: str (optional)
    :param metadata: Dict[str, Any] (optional)
    :param config: Dict[str, Any] (optional)
    :return: DashboardInstanceServersDeploymentsUpdateOutput
    """
    _params = {
      "name": name,
      "description": description,
      "metadata": metadata,
      "config": config,
    }
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["instances", instanceId, "server-deployments", serverDeploymentId],
      body=body,
    )
    return self._patch(request).transform(
      mapDashboardInstanceServersDeploymentsUpdateOutput.from_dict
    )

  def delete(
    self, instanceId: str, serverDeploymentId: str
  ) -> DashboardInstanceServersDeploymentsDeleteOutput:
    """
    Delete server deployment
    Delete a server deployment from the instance.

    :param instanceId: str
    :param serverDeploymentId: str
    :return: DashboardInstanceServersDeploymentsDeleteOutput
    """
    request = MetorialRequest(
      path=["instances", instanceId, "server-deployments", serverDeploymentId]
    )
    return self._delete(request).transform(
      mapDashboardInstanceServersDeploymentsDeleteOutput.from_dict
    )
