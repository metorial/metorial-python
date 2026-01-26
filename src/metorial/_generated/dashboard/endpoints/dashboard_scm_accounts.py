from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardScmAccountsPreviewOutput,
  DashboardScmAccountsPreviewOutput,
  mapDashboardScmAccountsPreviewQuery,
  DashboardScmAccountsPreviewQuery,
)


class MetorialDashboardScmAccountsEndpoint(BaseMetorialEndpoint):
  """Read and write SCM repository information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def preview(
    self, organization_id: str, *, installation_id: str
  ) -> DashboardScmAccountsPreviewOutput:
    """
    List SCM Repositories
    List SCM accounts for all organizations the user is a member of

    :param organization_id: str
    :param installation_id: str
    :return: DashboardScmAccountsPreviewOutput
    """
    # Build query parameters from keyword arguments
    query_dict = {}
    query_dict["installation_id"] = installation_id

    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "scm",
        "accounts",
        "preview",
      ],
      query=query_dict,
    )
    return self._get(request).transform(mapDashboardScmAccountsPreviewOutput.from_dict)
