from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardScmReposCreateOutput,
  DashboardScmReposCreateOutput,
  mapDashboardScmReposCreateBody,
  DashboardScmReposCreateBody,
  mapDashboardScmReposPreviewOutput,
  DashboardScmReposPreviewOutput,
  mapDashboardScmReposPreviewQuery,
  DashboardScmReposPreviewQuery,
)


class MetorialDashboardScmReposEndpoint(BaseMetorialEndpoint):
  """Read and write SCM repository information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def create(self, organization_id: str) -> DashboardScmReposCreateOutput:
    """
    Link SCM Repository
    Link an SCM repository to the organization

    :param organization_id: str
    :return: DashboardScmReposCreateOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "scm", "repos"]
    )
    return self._post(request).transform(mapDashboardScmReposCreateOutput.from_dict)

  def preview(
    self, organization_id: str, *, installation_id: str, external_account_id: str
  ) -> DashboardScmReposPreviewOutput:
    """
    List SCM Repositories
    List SCM repositories for all organizations the user is a member of

    :param organization_id: str
    :param installation_id: str
    :param external_account_id: str
    :return: DashboardScmReposPreviewOutput
    """
    # Build query parameters from keyword arguments
    query_dict = {}
    query_dict["installation_id"] = installation_id
    query_dict["external_account_id"] = external_account_id

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "scm", "repos", "preview"],
      query=query_dict,
    )
    return self._get(request).transform(mapDashboardScmReposPreviewOutput.from_dict)
