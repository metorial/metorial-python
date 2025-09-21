from typing import Optional, Dict, Any, List, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsMembersListOutput,
  DashboardOrganizationsMembersListOutput,
  mapDashboardOrganizationsMembersListQuery,
  DashboardOrganizationsMembersListQuery,
  mapDashboardOrganizationsMembersGetOutput,
  DashboardOrganizationsMembersGetOutput,
  mapDashboardOrganizationsMembersDeleteOutput,
  DashboardOrganizationsMembersDeleteOutput,
  mapDashboardOrganizationsMembersUpdateOutput,
  DashboardOrganizationsMembersUpdateOutput,
  mapDashboardOrganizationsMembersUpdateBody,
  DashboardOrganizationsMembersUpdateBody,
)


class MetorialDashboardOrganizationsMembersEndpoint(BaseMetorialEndpoint):
  """Read and write organization member information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, organizationId: str, query: DashboardOrganizationsMembersListQuery = None
  ) -> DashboardOrganizationsMembersListOutput:
    """
    List organization members
    List all organization members

    :param organizationId: str
    :param query: DashboardOrganizationsMembersListQuery
    :return: DashboardOrganizationsMembersListOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "members"],
      query=mapDashboardOrganizationsMembersListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardOrganizationsMembersListOutput.from_dict
    )

  def get(
    self, organizationId: str, memberId: str
  ) -> DashboardOrganizationsMembersGetOutput:
    """
    Get organization member
    Get the information of a specific organization member

    :param organizationId: str
    :param memberId: str
    :return: DashboardOrganizationsMembersGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "members", memberId]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsMembersGetOutput.from_dict
    )

  def delete(
    self, organizationId: str, memberId: str
  ) -> DashboardOrganizationsMembersDeleteOutput:
    """
    Delete organization member
    Remove an organization member

    :param organizationId: str
    :param memberId: str
    :return: DashboardOrganizationsMembersDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "members", memberId]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsMembersDeleteOutput.from_dict
    )

  def update(
    self, organizationId: str, memberId: str, *, role: Optional[str] = None
  ) -> DashboardOrganizationsMembersUpdateOutput:
    """
    Update organization member
    Update the role of an organization member

    :param organizationId: str
    :param memberId: str
    :param role: str (optional)
    :return: DashboardOrganizationsMembersUpdateOutput
    """
    _params = {"role": role}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "members", memberId],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsMembersUpdateOutput.from_dict
    )
