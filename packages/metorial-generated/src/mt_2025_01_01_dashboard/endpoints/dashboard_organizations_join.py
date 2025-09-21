from typing import Optional, Dict, Any, List, Union
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

  def get(
    self, query: DashboardOrganizationsJoinGetQuery = None
  ) -> DashboardOrganizationsJoinGetOutput:
    """
    Join organization
    Join an organization

    :param query: DashboardOrganizationsJoinGetQuery
    :return: DashboardOrganizationsJoinGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organization-join", "find"],
      query=mapDashboardOrganizationsJoinGetQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapDashboardOrganizationsJoinGetOutput.from_dict
    )

  def accept(
    self, *, invite_key: Optional[str] = None
  ) -> DashboardOrganizationsJoinAcceptOutput:
    """
    Join organization
    Join an organization

    :param invite_key: str (optional)
    :return: DashboardOrganizationsJoinAcceptOutput
    """
    _params = {"invite_key": invite_key}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organization-join", "accept"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsJoinAcceptOutput.from_dict
    )

  def reject(
    self, *, invite_key: Optional[str] = None
  ) -> DashboardOrganizationsJoinRejectOutput:
    """
    Reject organization invite
    Reject an organization invite

    :param invite_key: str (optional)
    :return: DashboardOrganizationsJoinRejectOutput
    """
    _params = {"invite_key": invite_key}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organization-join", "reject"],
      body=body,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsJoinRejectOutput.from_dict
    )
