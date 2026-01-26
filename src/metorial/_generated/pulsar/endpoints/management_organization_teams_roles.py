from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsTeamsRolesListOutput,
  DashboardOrganizationsTeamsRolesListOutput,
  mapDashboardOrganizationsTeamsRolesListQuery,
  DashboardOrganizationsTeamsRolesListQuery,
  mapDashboardOrganizationsTeamsRolesGetOutput,
  DashboardOrganizationsTeamsRolesGetOutput,
  mapDashboardOrganizationsTeamsRolesUpdateOutput,
  DashboardOrganizationsTeamsRolesUpdateOutput,
  mapDashboardOrganizationsTeamsRolesUpdateBody,
  DashboardOrganizationsTeamsRolesUpdateBody,
  mapDashboardOrganizationsTeamsRolesCreateOutput,
  DashboardOrganizationsTeamsRolesCreateOutput,
  mapDashboardOrganizationsTeamsRolesCreateBody,
  DashboardOrganizationsTeamsRolesCreateBody,
)


class MetorialManagementOrganizationTeamsRolesEndpoint(BaseMetorialEndpoint):
  """Read and write team information"""

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
  ) -> DashboardOrganizationsTeamsRolesListOutput:
    """
    List organization teams
    List all organization teams

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsTeamsRolesListOutput
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

    request = MetorialRequest(path=["organization", "team-roles"], query=query_dict)
    return self._get(request).transform(
      mapDashboardOrganizationsTeamsRolesListOutput.from_dict
    )

  def get(self, team_role_id: str) -> DashboardOrganizationsTeamsRolesGetOutput:
    """
    Get team
    Get the information of a specific team

    :param team_role_id: str
    :return: DashboardOrganizationsTeamsRolesGetOutput
    """
    request = MetorialRequest(path=["organization", "team-roles", team_role_id])
    return self._get(request).transform(
      mapDashboardOrganizationsTeamsRolesGetOutput.from_dict
    )

  def update(
    self,
    team_role_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    permissions: Optional[List[str]] = None
  ) -> DashboardOrganizationsTeamsRolesUpdateOutput:
    """
    Update team
    Update the role of an team

    :param team_role_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param permissions: Optional[List[str]] (optional)
    :return: DashboardOrganizationsTeamsRolesUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if permissions is not None:
      body_dict["permissions"] = permissions

    request = MetorialRequest(
      path=["organization", "team-roles", team_role_id], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardOrganizationsTeamsRolesUpdateOutput.from_dict
    )

  def create(
    self,
    *,
    name: str,
    description: Optional[str] = None,
    permissions: Optional[List[str]] = None
  ) -> DashboardOrganizationsTeamsRolesCreateOutput:
    """
    Create organization team
    Create a new organization team

    :param name: str
    :param description: Optional[str] (optional)
    :param permissions: Optional[List[str]] (optional)
    :return: DashboardOrganizationsTeamsRolesCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if permissions is not None:
      body_dict["permissions"] = permissions

    request = MetorialRequest(path=["organization", "team-roles"], body=body_dict)
    return self._post(request).transform(
      mapDashboardOrganizationsTeamsRolesCreateOutput.from_dict
    )
