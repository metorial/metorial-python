from typing import Optional, Dict, Any, List, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsProjectsListOutput,
  DashboardOrganizationsProjectsListOutput,
  mapDashboardOrganizationsProjectsListQuery,
  DashboardOrganizationsProjectsListQuery,
  mapDashboardOrganizationsProjectsGetOutput,
  DashboardOrganizationsProjectsGetOutput,
  mapDashboardOrganizationsProjectsCreateOutput,
  DashboardOrganizationsProjectsCreateOutput,
  mapDashboardOrganizationsProjectsCreateBody,
  DashboardOrganizationsProjectsCreateBody,
  mapDashboardOrganizationsProjectsDeleteOutput,
  DashboardOrganizationsProjectsDeleteOutput,
  mapDashboardOrganizationsProjectsUpdateOutput,
  DashboardOrganizationsProjectsUpdateOutput,
  mapDashboardOrganizationsProjectsUpdateBody,
  DashboardOrganizationsProjectsUpdateBody,
)


class MetorialDashboardOrganizationsProjectsEndpoint(BaseMetorialEndpoint):
  """Read and write project information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, organizationId: str, query: DashboardOrganizationsProjectsListQuery = None
  ) -> DashboardOrganizationsProjectsListOutput:
    """
    List organization projects
    List all organization projects

    :param organizationId: str
    :param query: DashboardOrganizationsProjectsListQuery
    :return: DashboardOrganizationsProjectsListOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "projects"],
      query=mapDashboardOrganizationsProjectsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardOrganizationsProjectsListOutput.from_dict
    )

  def get(
    self, organizationId: str, projectId: str
  ) -> DashboardOrganizationsProjectsGetOutput:
    """
    Get organization project
    Get the information of a specific organization project

    :param organizationId: str
    :param projectId: str
    :return: DashboardOrganizationsProjectsGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "projects", projectId]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsProjectsGetOutput.from_dict
    )

  def create(
    self, organizationId: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsProjectsCreateOutput:
    """
    Create organization project
    Create a new organization project

    :param organizationId: str
    :param name: str (optional)
    :return: DashboardOrganizationsProjectsCreateOutput
    """
    _params = {"name": name}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "projects"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsProjectsCreateOutput.from_dict
    )

  def delete(
    self, organizationId: str, projectId: str
  ) -> DashboardOrganizationsProjectsDeleteOutput:
    """
    Delete organization project
    Remove an organization project

    :param organizationId: str
    :param projectId: str
    :return: DashboardOrganizationsProjectsDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "projects", projectId]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsProjectsDeleteOutput.from_dict
    )

  def update(
    self, organizationId: str, projectId: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsProjectsUpdateOutput:
    """
    Update organization project
    Update the role of an organization project

    :param organizationId: str
    :param projectId: str
    :param name: str (optional)
    :return: DashboardOrganizationsProjectsUpdateOutput
    """
    _params = {"name": name}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "projects", projectId],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsProjectsUpdateOutput.from_dict
    )
