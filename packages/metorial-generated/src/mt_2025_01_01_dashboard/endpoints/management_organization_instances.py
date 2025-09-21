from typing import Optional, Dict, Any, List, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsInstancesListOutput,
  DashboardOrganizationsInstancesListOutput,
  mapDashboardOrganizationsInstancesListQuery,
  DashboardOrganizationsInstancesListQuery,
  mapDashboardOrganizationsInstancesGetOutput,
  DashboardOrganizationsInstancesGetOutput,
  mapDashboardOrganizationsInstancesCreateOutput,
  DashboardOrganizationsInstancesCreateOutput,
  mapDashboardOrganizationsInstancesCreateBody,
  DashboardOrganizationsInstancesCreateBody,
  mapDashboardOrganizationsInstancesDeleteOutput,
  DashboardOrganizationsInstancesDeleteOutput,
  mapDashboardOrganizationsInstancesUpdateOutput,
  DashboardOrganizationsInstancesUpdateOutput,
  mapDashboardOrganizationsInstancesUpdateBody,
  DashboardOrganizationsInstancesUpdateBody,
)


class MetorialManagementOrganizationInstancesEndpoint(BaseMetorialEndpoint):
  """Read and write instance information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, query: DashboardOrganizationsInstancesListQuery = None
  ) -> DashboardOrganizationsInstancesListOutput:
    """
    List organization instances
    List all organization instances

    :param query: DashboardOrganizationsInstancesListQuery
    :return: DashboardOrganizationsInstancesListOutput
    """
    request = MetorialRequest(
      path=["organization", "instances"],
      query=mapDashboardOrganizationsInstancesListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardOrganizationsInstancesListOutput.from_dict
    )

  def get(self, instanceId: str) -> DashboardOrganizationsInstancesGetOutput:
    """
    Get organization instance
    Get the information of a specific organization instance

    :param instanceId: str
    :return: DashboardOrganizationsInstancesGetOutput
    """
    request = MetorialRequest(path=["organization", "instances", instanceId])
    return self._get(request).transform(
      mapDashboardOrganizationsInstancesGetOutput.from_dict
    )

  def create(
    self,
    *,
    name: Optional[str] = None,
    type: Optional[str] = None,
    project_id: Optional[str] = None
  ) -> DashboardOrganizationsInstancesCreateOutput:
    """
    Create organization instance
    Create a new organization instance

    :param name: str (optional)
    :param type: str (optional)
    :param project_id: str (optional)
    :return: DashboardOrganizationsInstancesCreateOutput
    """
    _params = {"name": name, "type": type, "project_id": project_id}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["organization", "instances"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInstancesCreateOutput.from_dict
    )

  def delete(self, instanceId: str) -> DashboardOrganizationsInstancesDeleteOutput:
    """
    Delete organization instance
    Remove an organization instance

    :param instanceId: str
    :return: DashboardOrganizationsInstancesDeleteOutput
    """
    request = MetorialRequest(path=["organization", "instances", instanceId])
    return self._delete(request).transform(
      mapDashboardOrganizationsInstancesDeleteOutput.from_dict
    )

  def update(
    self, instanceId: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsInstancesUpdateOutput:
    """
    Update organization instance
    Update the role of an organization instance

    :param instanceId: str
    :param name: str (optional)
    :return: DashboardOrganizationsInstancesUpdateOutput
    """
    _params = {"name": name}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["organization", "instances", instanceId],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInstancesUpdateOutput.from_dict
    )
