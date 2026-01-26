from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsTeamsProjectsSetOutput,
  DashboardOrganizationsTeamsProjectsSetOutput,
  mapDashboardOrganizationsTeamsProjectsSetBody,
  DashboardOrganizationsTeamsProjectsSetBody,
  mapDashboardOrganizationsTeamsProjectsRemoveOutput,
  DashboardOrganizationsTeamsProjectsRemoveOutput,
)


class MetorialManagementOrganizationTeamsProjectsEndpoint(BaseMetorialEndpoint):
  """Read and write team information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def set(
    self, team_id: str, *, project_id: str, team_role_ids: List[str]
  ) -> DashboardOrganizationsTeamsProjectsSetOutput:
    """
    Set team projects
    Set the projects assigned to a team

    :param team_id: str
    :param project_id: str
    :param team_role_ids: List[str]
    :return: DashboardOrganizationsTeamsProjectsSetOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["project_id"] = project_id
    body_dict["team_role_ids"] = team_role_ids

    request = MetorialRequest(
      path=["organization", "teams", team_id, "projects"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardOrganizationsTeamsProjectsSetOutput.from_dict
    )

  def remove(
    self, team_id: str, project_id: str
  ) -> DashboardOrganizationsTeamsProjectsRemoveOutput:
    """
    Remove team project
    Remove a project from a team

    :param team_id: str
    :param project_id: str
    :return: DashboardOrganizationsTeamsProjectsRemoveOutput
    """
    request = MetorialRequest(
      path=["organization", "teams", team_id, "projects", project_id]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsTeamsProjectsRemoveOutput.from_dict
    )
