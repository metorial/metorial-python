from typing import Optional, Dict, Any, List, Union
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

  def create(self, *, name: Optional[str] = None) -> DashboardOrganizationsCreateOutput:
    """
    Create organization
    Create a new organization

    :param name: str (optional)
    :return: DashboardOrganizationsCreateOutput
    """
    _params = {"name": name}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsCreateOutput.from_dict
    )

  def list(
    self, query: DashboardOrganizationsListQuery = None
  ) -> DashboardOrganizationsListOutput:
    """
    List organizations
    List all organizations

    :param query: DashboardOrganizationsListQuery
    :return: DashboardOrganizationsListOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations"],
      query=mapDashboardOrganizationsListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(mapDashboardOrganizationsListOutput.from_dict)

  def get(self, organizationId: str) -> DashboardOrganizationsGetOutput:
    """
    Get organization
    Get the current organization information

    :param organizationId: str
    :return: DashboardOrganizationsGetOutput
    """
    request = MetorialRequest(path=["dashboard", "organizations", organizationId])
    return self._get(request).transform(mapDashboardOrganizationsGetOutput.from_dict)

  def update(
    self, organizationId: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsUpdateOutput:
    """
    Update organization
    Update the current organization information

    :param organizationId: str
    :param name: str (optional)
    :return: DashboardOrganizationsUpdateOutput
    """
    _params = {"name": name}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId],
      body=body,
    )
    return self._patch(request).transform(
      mapDashboardOrganizationsUpdateOutput.from_dict
    )

  def delete(self, organizationId: str) -> DashboardOrganizationsDeleteOutput:
    """
    Delete organization
    Delete the current organization

    :param organizationId: str
    :return: DashboardOrganizationsDeleteOutput
    """
    request = MetorialRequest(path=["dashboard", "organizations", organizationId])
    return self._delete(request).transform(
      mapDashboardOrganizationsDeleteOutput.from_dict
    )

  def get_membership(
    self, organizationId: str
  ) -> DashboardOrganizationsGetMembershipOutput:
    """
    Get organization
    Get the current organization information

    :param organizationId: str
    :return: DashboardOrganizationsGetMembershipOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "membership"]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsGetMembershipOutput.from_dict
    )
