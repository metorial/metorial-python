from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardOrganizationsInstancesListOutput,
  DashboardOrganizationsInstancesListOutput,
  mapDashboardOrganizationsInstancesListQuery,
  DashboardOrganizationsInstancesListQuery,
  mapDashboardOrganizationsInstancesGetOutput,
  DashboardOrganizationsInstancesGetOutput,
  mapDashboardOrganizationsInstancesCreateOutput,
  DashboardOrganizationsInstancesCreateOutput,
  mapDashboardOrganizationsInstancesCreateBody,
  DashboardOrganizationsInstancesCreateBody,
  mapDashboardOrganizationsInstancesDeleteOutput,
  DashboardOrganizationsInstancesDeleteOutput,
  mapDashboardOrganizationsInstancesUpdateOutput,
  DashboardOrganizationsInstancesUpdateOutput,
  mapDashboardOrganizationsInstancesUpdateBody,
  DashboardOrganizationsInstancesUpdateBody,
)


class MetorialDashboardOrganizationsInstancesEndpoint(BaseMetorialEndpoint):
  """Read and write instance information"""

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
    order: Optional[str] = None,
    project_id: Optional[str] = None
  ) -> DashboardOrganizationsInstancesListOutput:
    """
    List organization instances
    List all organization instances

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param project_id: Optional[str] (optional)
    :return: DashboardOrganizationsInstancesListOutput
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
    if project_id is not None:
      query_dict["project_id"] = project_id

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "instances"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardOrganizationsInstancesListOutput.from_dict
    )

  def get(
    self, organization_id: str, instance_id: str
  ) -> DashboardOrganizationsInstancesGetOutput:
    """
    Get organization instance
    Get the information of a specific organization instance

    :param organization_id: str
    :param instance_id: str
    :return: DashboardOrganizationsInstancesGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "instances", instance_id]
    )
    return self._get(request).transform(
      mapDashboardOrganizationsInstancesGetOutput.from_dict
    )

  def create(
    self, organization_id: str, *, name: str, type: str, project_id: str
  ) -> DashboardOrganizationsInstancesCreateOutput:
    """
    Create organization instance
    Create a new organization instance

    :param organization_id: str
    :param name: str
    :param type: str
    :param project_id: str
    :return: DashboardOrganizationsInstancesCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name
    body_dict["type"] = type
    body_dict["project_id"] = project_id

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "instances"], body=body_dict
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInstancesCreateOutput.from_dict
    )

  def delete(
    self, organization_id: str, instance_id: str
  ) -> DashboardOrganizationsInstancesDeleteOutput:
    """
    Delete organization instance
    Remove an organization instance

    :param organization_id: str
    :param instance_id: str
    :return: DashboardOrganizationsInstancesDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "instances", instance_id]
    )
    return self._delete(request).transform(
      mapDashboardOrganizationsInstancesDeleteOutput.from_dict
    )

  def update(
    self, organization_id: str, instance_id: str, *, name: Optional[str] = None
  ) -> DashboardOrganizationsInstancesUpdateOutput:
    """
    Update organization instance
    Update the role of an organization instance

    :param organization_id: str
    :param instance_id: str
    :param name: Optional[str] (optional)
    :return: DashboardOrganizationsInstancesUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "instances", instance_id],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardOrganizationsInstancesUpdateOutput.from_dict
    )
