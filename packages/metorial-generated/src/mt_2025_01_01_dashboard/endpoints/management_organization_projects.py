from typing import Any, Dict, List, Optional, Union
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


class MetorialManagementOrganizationProjectsEndpoint(BaseMetorialEndpoint):
  """Read and write project information"""

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
  ) -> DashboardOrganizationsProjectsListOutput:
    """
    List organization projects
    List all organization projects

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsProjectsListOutput
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

    request = MetorialRequest(path=["organization", "projects"], query=query_dict)
    return self._get(request).transform(
      mapDashboardOrganizationsProjectsListOutput.from_dict
    )

  def get(self, project_id: str) -> DashboardOrganizationsProjectsGetOutput:
    """
    Get organization project
    Get the information of a specific organization project

    :param project_id: str
    :return: DashboardOrganizationsProjectsGetOutput
    """
    request = MetorialRequest(path=["organization", "projects", project_id])
    return self._get(request).transform(
      mapDashboardOrganizationsProjectsGetOutput.from_dict
    )

  def create(self, *, name: str) -> DashboardOrganizationsProjectsCreateOutput:
    """
    Create organization project
    Create a new organization project

    :param name: str
    :return: DashboardOrganizationsProjectsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name

    request = MetorialRequest(path=["organization", "projects"], body=body_dict)
    return self._post(request).transform(
      mapDashboardOrganizationsProjectsCreateOutput.from_dict
    )

  def delete(self, project_id: str) -> DashboardOrganizationsProjectsDeleteOutput:
    """
    Delete organization project
    Remove an organization project

    :param project_id: str
    :return: DashboardOrganizationsProjectsDeleteOutput
    """
    request = MetorialRequest(path=["organization", "projects", project_id])
    return self._delete(request).transform(
      mapDashboardOrganizationsProjectsDeleteOutput.from_dict
    )

  def update(
    self, project_id: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsProjectsUpdateOutput:
    """
    Update organization project
    Update the role of an organization project

    :param project_id: str
    :param name: Optional[str] (optional)
    :return: DashboardOrganizationsProjectsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name

    request = MetorialRequest(
      path=["organization", "projects", project_id], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardOrganizationsProjectsUpdateOutput.from_dict
    )
