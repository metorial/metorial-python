from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceLinksListOutput,
  DashboardInstanceLinksListOutput,
  mapDashboardInstanceLinksGetOutput,
  DashboardInstanceLinksGetOutput,
  mapDashboardInstanceLinksCreateOutput,
  DashboardInstanceLinksCreateOutput,
  mapDashboardInstanceLinksCreateBody,
  DashboardInstanceLinksCreateBody,
  mapDashboardInstanceLinksUpdateOutput,
  DashboardInstanceLinksUpdateOutput,
  mapDashboardInstanceLinksUpdateBody,
  DashboardInstanceLinksUpdateBody,
  mapDashboardInstanceLinksDeleteOutput,
  DashboardInstanceLinksDeleteOutput,
)


class MetorialDashboardInstanceLinksEndpoint(BaseMetorialEndpoint):
  """Files are private by default. If you want to share a file, you can create a link for it. Links are public and do not require authentication to access, so be careful with what you share."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(self, instance_id: str, file_id: str) -> DashboardInstanceLinksListOutput:
    """
    List file links
    Returns a list of links associated with a specific file.

    :param instance_id: str
    :param file_id: str
    :return: DashboardInstanceLinksListOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "files", file_id, "links"]
    )
    return self._get(request).transform(mapDashboardInstanceLinksListOutput.from_dict)

  def get(
    self, instance_id: str, file_id: str, link_id: str
  ) -> DashboardInstanceLinksGetOutput:
    """
    Get file link by ID
    Retrieves the details of a specific file link by its ID.

    :param instance_id: str
    :param file_id: str
    :param link_id: str
    :return: DashboardInstanceLinksGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "files", file_id, "links", link_id]
    )
    return self._get(request).transform(mapDashboardInstanceLinksGetOutput.from_dict)

  def create(
    self, instance_id: str, file_id: str, *, expires_at: Optional[datetime] = None
  ) -> DashboardInstanceLinksCreateOutput:
    """
    Create file link
    Creates a new link for a specific file.

    :param instance_id: str
    :param file_id: str
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardInstanceLinksCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if expires_at is not None:
      body_dict["expires_at"] = expires_at

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "files", file_id, "links"],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardInstanceLinksCreateOutput.from_dict
    )

  def update(
    self,
    instance_id: str,
    file_id: str,
    link_id: str,
    *,
    expires_at: Optional[datetime] = None
  ) -> DashboardInstanceLinksUpdateOutput:
    """
    Update file link by ID
    Updates a file link’s properties, such as expiration.

    :param instance_id: str
    :param file_id: str
    :param link_id: str
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardInstanceLinksUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if expires_at is not None:
      body_dict["expires_at"] = expires_at

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "files", file_id, "links", link_id],
      body=body_dict,
    )
    return self._patch(request).transform(
      mapDashboardInstanceLinksUpdateOutput.from_dict
    )

  def delete(
    self, instance_id: str, file_id: str, link_id: str
  ) -> DashboardInstanceLinksDeleteOutput:
    """
    Delete file link by ID
    Deletes a specific file link by its ID.

    :param instance_id: str
    :param file_id: str
    :param link_id: str
    :return: DashboardInstanceLinksDeleteOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "files", file_id, "links", link_id]
    )
    return self._delete(request).transform(
      mapDashboardInstanceLinksDeleteOutput.from_dict
    )
