from typing import Optional, Dict, Any, List, Union
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


class MetorialManagementOrganizationInvitesEndpoint(BaseMetorialEndpoint):
  """Read and write organization invite information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self, query: DashboardOrganizationsInvitesListQuery = None
  ) -> DashboardOrganizationsInvitesListOutput:
    """
    List organization invites
    List all organization invites

    :param query: DashboardOrganizationsInvitesListQuery
    :return: DashboardOrganizationsInvitesListOutput
    """
    request = MetorialRequest(
      path=["organization", "invites"],
      query=mapDashboardOrganizationsInvitesListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardOrganizationsInvitesListOutput.from_dict
    )

  def get(self, inviteId: str) -> DashboardOrganizationsInvitesGetOutput:
    """
    Get organization invite
    Get the information of a specific organization invite

    :param inviteId: str
    :return: DashboardOrganizationsInvitesGetOutput
    """
    request = MetorialRequest(path=["organization", "invites", inviteId])
    return self._get(request).transform(
      mapDashboardOrganizationsInvitesGetOutput.from_dict
    )

  def create(self) -> DashboardOrganizationsInvitesCreateOutput:
    """
    Create organization invite
    Create a new organization invite


    :return: DashboardOrganizationsInvitesCreateOutput
    """
    {}

    request = MetorialRequest(
      path=["organization", "invites"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInvitesCreateOutput.from_dict
    )

  def ensure_link(self) -> DashboardOrganizationsInvitesEnsureLinkOutput:
    """
    Ensure organization invite link
    Ensure the invite link for the organization


    :return: DashboardOrganizationsInvitesEnsureLinkOutput
    """
    request = MetorialRequest(path=["organization", "invites", "ensure"])
    return self._post(request).transform(
      mapDashboardOrganizationsInvitesEnsureLinkOutput.from_dict
    )

  def delete(self, inviteId: str) -> DashboardOrganizationsInvitesDeleteOutput:
    """
    Delete organization invite
    Remove an organization invite

    :param inviteId: str
    :return: DashboardOrganizationsInvitesDeleteOutput
    """
    request = MetorialRequest(path=["organization", "invites", inviteId])
    return self._delete(request).transform(
      mapDashboardOrganizationsInvitesDeleteOutput.from_dict
    )

  def update(
    self, inviteId: str, *, role: Optional[str] = None
  ) -> DashboardOrganizationsInvitesUpdateOutput:
    """
    Update organization invite
    Update the role of an organization invite

    :param inviteId: str
    :param role: str (optional)
    :return: DashboardOrganizationsInvitesUpdateOutput
    """
    _params = {"role": role}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["organization", "invites", inviteId],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInvitesUpdateOutput.from_dict
    )
