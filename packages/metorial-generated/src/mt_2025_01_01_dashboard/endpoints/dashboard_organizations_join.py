from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsJoinGetOutput,
  DashboardOrganizationsJoinGetOutput,
  mapDashboardOrganizationsJoinGetQuery,
  DashboardOrganizationsJoinGetQuery,
  mapDashboardOrganizationsJoinAcceptOutput,
  DashboardOrganizationsJoinAcceptOutput,
  mapDashboardOrganizationsJoinAcceptBody,
  DashboardOrganizationsJoinAcceptBody,
  mapDashboardOrganizationsJoinRejectOutput,
  DashboardOrganizationsJoinRejectOutput,
  mapDashboardOrganizationsJoinRejectBody,
  DashboardOrganizationsJoinRejectBody,
)


class MetorialDashboardOrganizationsJoinEndpoint(BaseMetorialEndpoint):
  """Read and write organization information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(self, *, invite_key: str) -> DashboardOrganizationsJoinGetOutput:
    """
    Join organization
    Join an organization

    :param invite_key: str
    :return: DashboardOrganizationsJoinGetOutput
    """
    # Build query parameters from keyword arguments
    query_dict = {}
    query_dict["inviteKey"] = invite_key

    request = MetorialRequest(
      path=["dashboard", "organization-join", "find"], query=query_dict
    )
    return self._get(request).transform(
      mapDashboardOrganizationsJoinGetOutput.from_dict
    )

  def accept(self, *, invite_key: str) -> DashboardOrganizationsJoinAcceptOutput:
    """
    Join organization
    Join an organization

    :param invite_key: str
    :return: DashboardOrganizationsJoinAcceptOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["invite_key"] = invite_key

    request = MetorialRequest(
      path=["dashboard", "organization-join", "accept"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardOrganizationsJoinAcceptOutput.from_dict
    )

  def reject(self, *, invite_key: str) -> DashboardOrganizationsJoinRejectOutput:
    """
    Reject organization invite
    Reject an organization invite

    :param invite_key: str
    :return: DashboardOrganizationsJoinRejectOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["invite_key"] = invite_key

    request = MetorialRequest(
      path=["dashboard", "organization-join", "reject"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardOrganizationsJoinRejectOutput.from_dict
    )
