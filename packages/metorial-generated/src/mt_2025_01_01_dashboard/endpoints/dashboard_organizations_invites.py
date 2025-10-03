from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsInvitesListOutput,
  DashboardOrganizationsInvitesListOutput,
  mapDashboardOrganizationsInvitesListQuery,
  DashboardOrganizationsInvitesListQuery,
  mapDashboardOrganizationsInvitesGetOutput,
  DashboardOrganizationsInvitesGetOutput,
  mapDashboardOrganizationsInvitesCreateOutput,
  DashboardOrganizationsInvitesCreateOutput,
  mapDashboardOrganizationsInvitesCreateBody,
  DashboardOrganizationsInvitesCreateBody,
  mapDashboardOrganizationsInvitesEnsureLinkOutput,
  DashboardOrganizationsInvitesEnsureLinkOutput,
  mapDashboardOrganizationsInvitesDeleteOutput,
  DashboardOrganizationsInvitesDeleteOutput,
  mapDashboardOrganizationsInvitesUpdateOutput,
  DashboardOrganizationsInvitesUpdateOutput,
  mapDashboardOrganizationsInvitesUpdateBody,
  DashboardOrganizationsInvitesUpdateBody,
)


class MetorialDashboardOrganizationsInvitesEndpoint(BaseMetorialEndpoint):
  """Read and write organization invite information"""

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
  ) -> DashboardOrganizationsInvitesListOutput:
    """
    List organization invites
    List all organization invites

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardOrganizationsInvitesListOutput
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
      path=["dashboard", "organizations", organization_id, "invites"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardOrganizationsInvitesListOutput.from_dict
    )

  def get(
    self, organization_id: str, invite_id: str
  ) -> DashboardOrganizationsInvitesGetOutput:
    """
    Get organization invite
    Get the information of a specific organization invite

    :param organization_id: str
    :param invite_id: str
    :return: DashboardOrganizationsInvitesGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "invites", invite_id]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsInvitesGetOutput.from_dict
    )

  def create(self, organization_id: str) -> DashboardOrganizationsInvitesCreateOutput:
    """
    Create organization invite
    Create a new organization invite

    :param organization_id: str
    :return: DashboardOrganizationsInvitesCreateOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "invites"]
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInvitesCreateOutput.from_dict
    )

  def ensure_link(
    self, organization_id: str
  ) -> DashboardOrganizationsInvitesEnsureLinkOutput:
    """
    Ensure organization invite link
    Ensure the invite link for the organization

    :param organization_id: str
    :return: DashboardOrganizationsInvitesEnsureLinkOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "invites", "ensure"]
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInvitesEnsureLinkOutput.from_dict
    )

  def delete(
    self, organization_id: str, invite_id: str
  ) -> DashboardOrganizationsInvitesDeleteOutput:
    """
    Delete organization invite
    Remove an organization invite

    :param organization_id: str
    :param invite_id: str
    :return: DashboardOrganizationsInvitesDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "invites", invite_id]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsInvitesDeleteOutput.from_dict
    )

  def update(
    self, organization_id: str, invite_id: str, *, role: str
  ) -> DashboardOrganizationsInvitesUpdateOutput:
    """
    Update organization invite
    Update the role of an organization invite

    :param organization_id: str
    :param invite_id: str
    :param role: str
    :return: DashboardOrganizationsInvitesUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["role"] = role

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "invites", invite_id],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInvitesUpdateOutput.from_dict
    )
