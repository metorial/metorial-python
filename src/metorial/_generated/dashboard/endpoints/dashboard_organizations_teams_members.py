from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsTeamsMembersCreateOutput,
  DashboardOrganizationsTeamsMembersCreateOutput,
  mapDashboardOrganizationsTeamsMembersCreateBody,
  DashboardOrganizationsTeamsMembersCreateBody,
  mapDashboardOrganizationsTeamsMembersDeleteOutput,
  DashboardOrganizationsTeamsMembersDeleteOutput,
)


class MetorialDashboardOrganizationsTeamsMembersEndpoint(BaseMetorialEndpoint):
  """Read and write team information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def create(
    self, organization_id: str, team_id: str, *, actor_id: str
  ) -> DashboardOrganizationsTeamsMembersCreateOutput:
    """
    Assign member to team
    Assign an organization member to a team

    :param organization_id: str
    :param team_id: str
    :param actor_id: str
    :return: DashboardOrganizationsTeamsMembersCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["actor_id"] = actor_id

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "teams", team_id, "members"],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsTeamsMembersCreateOutput.from_dict
    )

  def delete(
    self, organization_id: str, team_id: str, actor_id: str
  ) -> DashboardOrganizationsTeamsMembersDeleteOutput:
    """
    Remove member from team
    Remove an organization member from a team

    :param organization_id: str
    :param team_id: str
    :param actor_id: str
    :return: DashboardOrganizationsTeamsMembersDeleteOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "teams",
        team_id,
        "members",
        actor_id,
      ]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsTeamsMembersDeleteOutput.from_dict
    )
