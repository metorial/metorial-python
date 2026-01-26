from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardScmInstallationsListOutput,
  DashboardScmInstallationsListOutput,
  mapDashboardScmInstallationsListQuery,
  DashboardScmInstallationsListQuery,
  mapDashboardScmInstallationsGetOutput,
  DashboardScmInstallationsGetOutput,
  mapDashboardScmInstallationsCreateOutput,
  DashboardScmInstallationsCreateOutput,
  mapDashboardScmInstallationsCreateBody,
  DashboardScmInstallationsCreateBody,
)


class MetorialDashboardScmInstallationsEndpoint(BaseMetorialEndpoint):
  """Read and write SCM repository information"""

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
  ) -> DashboardScmInstallationsListOutput:
    """
    List SCM Installations
    List SCM installations for the organization

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardScmInstallationsListOutput
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
      path=["dashboard", "organizations", organization_id, "scm", "installations"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardScmInstallationsListOutput.from_dict
    )

  def get(
    self, organization_id: str, installation_id: str
  ) -> DashboardScmInstallationsGetOutput:
    """
    Get SCM Installation
    Get a single SCM installation for the organization

    :param organization_id: str
    :param installation_id: str
    :return: DashboardScmInstallationsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "scm",
        "installations",
        installation_id,
      ]
    )
    return self._get(request).transform(mapDashboardScmInstallationsGetOutput.from_dict)

  def create(
    self, organization_id: str, *, provider: str, redirect_url: str
  ) -> DashboardScmInstallationsCreateOutput:
    """
    Install SCM Integration
    Install an SCM integration for the organization

    :param organization_id: str
    :param provider: str
    :param redirect_url: str
    :return: DashboardScmInstallationsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["provider"] = provider
    body_dict["redirect_url"] = redirect_url

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "scm", "installations"],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardScmInstallationsCreateOutput.from_dict
    )
