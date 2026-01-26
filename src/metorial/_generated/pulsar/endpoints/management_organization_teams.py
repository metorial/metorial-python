from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsTeamsPermissionsOutput,
  DashboardOrganizationsTeamsPermissionsOutput,
  mapDashboardOrganizationsTeamsListOutput,
  DashboardOrganizationsTeamsListOutput,
  mapDashboardOrganizationsTeamsListQuery,
  DashboardOrganizationsTeamsListQuery,
  mapDashboardOrganizationsTeamsGetOutput,
  DashboardOrganizationsTeamsGetOutput,
  mapDashboardOrganizationsTeamsUpdateOutput,
  DashboardOrganizationsTeamsUpdateOutput,
  mapDashboardOrganizationsTeamsUpdateBody,
  DashboardOrganizationsTeamsUpdateBody,
  mapDashboardOrganizationsTeamsCreateOutput,
  DashboardOrganizationsTeamsCreateOutput,
  mapDashboardOrganizationsTeamsCreateBody,
  DashboardOrganizationsTeamsCreateBody,
)


class MetorialManagementOrganizationTeamsEndpoint(BaseMetorialEndpoint):
  """Read and write team information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def permissions(self) -> DashboardOrganizationsTeamsPermissionsOutput:
    """
    Get team
    Get the information of a specific team


    :return: DashboardOrganizationsTeamsPermissionsOutput
    """
    request = MetorialRequest(path=["organization", "team-role-permissions"])
    return self._get(request).transform(
      mapDashboardOrganizationsTeamsPermissionsOutput.from_dict
    )

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardOrganizationsTeamsListOutput:
    """
    List organization teams
    List all organization teams

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsTeamsListOutput
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

    request = MetorialRequest(path=["organization", "teams"], query=query_dict)
    return self._get(request).transform(
      mapDashboardOrganizationsTeamsListOutput.from_dict
    )

  def get(self, team_id: str) -> DashboardOrganizationsTeamsGetOutput:
    """
    Get team
    Get the information of a specific team

    :param team_id: str
    :return: DashboardOrganizationsTeamsGetOutput
    """
    request = MetorialRequest(path=["organization", "teams", team_id])
    return self._get(request).transform(
      mapDashboardOrganizationsTeamsGetOutput.from_dict
    )

  def update(
    self, team_id: str, *, name: Optional[str] = None, description: Optional[str] = None
  ) -> DashboardOrganizationsTeamsUpdateOutput:
    """
    Update team
    Update the role of an team

    :param team_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: DashboardOrganizationsTeamsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description

    request = MetorialRequest(path=["organization", "teams", team_id], body=body_dict)
    return self._post(request).transform(
      mapDashboardOrganizationsTeamsUpdateOutput.from_dict
    )

  def create(
    self, *, name: str, description: Optional[str] = None
  ) -> DashboardOrganizationsTeamsCreateOutput:
    """
    Create organization team
    Create a new organization team

    :param name: str
    :param description: Optional[str] (optional)
    :return: DashboardOrganizationsTeamsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description

    request = MetorialRequest(path=["organization", "teams"], body=body_dict)
    return self._post(request).transform(
      mapDashboardOrganizationsTeamsCreateOutput.from_dict
    )
