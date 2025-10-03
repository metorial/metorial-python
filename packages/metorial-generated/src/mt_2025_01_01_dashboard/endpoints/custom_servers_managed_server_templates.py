from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapCustomServersManagedServerTemplatesListOutput,
  CustomServersManagedServerTemplatesListOutput,
  mapCustomServersManagedServerTemplatesListQuery,
  CustomServersManagedServerTemplatesListQuery,
  mapCustomServersManagedServerTemplatesGetOutput,
  CustomServersManagedServerTemplatesGetOutput,
)


class MetorialCustomServersManagedServerTemplatesEndpoint(BaseMetorialEndpoint):
  """Get managed server template information"""

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
  ) -> CustomServersManagedServerTemplatesListOutput:
    """
    List oauth connection templates
    List all oauth connection templates

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: CustomServersManagedServerTemplatesListOutput
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
      path=["dashboard", "organizations", organization_id, "managed-server-templates"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapCustomServersManagedServerTemplatesListOutput.from_dict
    )

  def get(
    self, organization_id: str, managed_server_id: str
  ) -> CustomServersManagedServerTemplatesGetOutput:
    """
    Get oauth connection template
    Get the information of a specific oauth connection template

    :param organization_id: str
    :param managed_server_id: str
    :return: CustomServersManagedServerTemplatesGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organization_id,
        "managed-server-templates",
        managed_server_id,
      ]
    )
    return self._get(request).transform(
      mapCustomServersManagedServerTemplatesGetOutput.from_dict
    )
