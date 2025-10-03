from typing import Any, Dict, List, Optional, Union
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
    self,
    organization_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardOrganizationsMembersListOutput:
    """
    List organization members
    List all organization members

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsMembersListOutput
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

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "members"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardOrganizationsMembersListOutput.from_dict
    )

  def get(
    self, organization_id: str, member_id: str
  ) -> DashboardOrganizationsMembersGetOutput:
    """
    Get organization member
    Get the information of a specific organization member

    :param organization_id: str
    :param member_id: str
    :return: DashboardOrganizationsMembersGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "members", member_id]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsMembersGetOutput.from_dict
    )

  def delete(
    self, organization_id: str, member_id: str
  ) -> DashboardOrganizationsMembersDeleteOutput:
    """
    Delete organization member
    Remove an organization member

    :param organization_id: str
    :param member_id: str
    :return: DashboardOrganizationsMembersDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "members", member_id]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsMembersDeleteOutput.from_dict
    )

  def update(
    self, organization_id: str, member_id: str, *, role: str
  ) -> DashboardOrganizationsMembersUpdateOutput:
    """
    Update organization member
    Update the role of an organization member

    :param organization_id: str
    :param member_id: str
    :param role: str
    :return: DashboardOrganizationsMembersUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["role"] = role

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "members", member_id],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsMembersUpdateOutput.from_dict
    )
