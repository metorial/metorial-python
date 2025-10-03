from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsCreateOutput,
  DashboardOrganizationsCreateOutput,
  mapDashboardOrganizationsCreateBody,
  DashboardOrganizationsCreateBody,
  mapDashboardOrganizationsListOutput,
  DashboardOrganizationsListOutput,
  mapDashboardOrganizationsListQuery,
  DashboardOrganizationsListQuery,
  mapDashboardOrganizationsGetOutput,
  DashboardOrganizationsGetOutput,
  mapDashboardOrganizationsUpdateOutput,
  DashboardOrganizationsUpdateOutput,
  mapDashboardOrganizationsUpdateBody,
  DashboardOrganizationsUpdateBody,
  mapDashboardOrganizationsDeleteOutput,
  DashboardOrganizationsDeleteOutput,
  mapDashboardOrganizationsGetMembershipOutput,
  DashboardOrganizationsGetMembershipOutput,
)


class MetorialDashboardOrganizationsEndpoint(BaseMetorialEndpoint):
  """Read and write organization information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def create(self, *, name: str) -> DashboardOrganizationsCreateOutput:
    """
    Create organization
    Create a new organization

    :param name: str
    :return: DashboardOrganizationsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name

    request = MetorialRequest(path=["dashboard", "organizations"], body=body_dict)
    return self._post(request).transform(
      mapDashboardOrganizationsCreateOutput.from_dict
    )

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None
  ) -> DashboardOrganizationsListOutput:
    """
    List organizations
    List all organizations

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsListOutput
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

    request = MetorialRequest(path=["dashboard", "organizations"], query=query_dict)
    return self._get(request).transform(mapDashboardOrganizationsListOutput.from_dict)

  def get(self, organization_id: str) -> DashboardOrganizationsGetOutput:
    """
    Get organization
    Get the current organization information

    :param organization_id: str
    :return: DashboardOrganizationsGetOutput
    """
    request = MetorialRequest(path=["dashboard", "organizations", organization_id])
    return self._get(request).transform(mapDashboardOrganizationsGetOutput.from_dict)

  def update(
    self, organization_id: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsUpdateOutput:
    """
    Update organization
    Update the current organization information

    :param organization_id: str
    :param name: Optional[str] (optional)
    :return: DashboardOrganizationsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id], body=body_dict
    )
    return self._patch(request).transform(
      mapDashboardOrganizationsUpdateOutput.from_dict
    )

  def delete(self, organization_id: str) -> DashboardOrganizationsDeleteOutput:
    """
    Delete organization
    Delete the current organization

    :param organization_id: str
    :return: DashboardOrganizationsDeleteOutput
    """
    request = MetorialRequest(path=["dashboard", "organizations", organization_id])
    return self._delete(request).transform(
      mapDashboardOrganizationsDeleteOutput.from_dict
    )

  def get_membership(
    self, organization_id: str
  ) -> DashboardOrganizationsGetMembershipOutput:
    """
    Get organization
    Get the current organization information

    :param organization_id: str
    :return: DashboardOrganizationsGetMembershipOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "membership"]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsGetMembershipOutput.from_dict
    )
