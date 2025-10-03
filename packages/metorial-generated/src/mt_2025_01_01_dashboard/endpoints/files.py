from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceFilesListOutput,
  DashboardInstanceFilesListOutput,
  mapDashboardInstanceFilesListQuery,
  DashboardInstanceFilesListQuery,
  mapDashboardInstanceFilesGetOutput,
  DashboardInstanceFilesGetOutput,
  mapDashboardInstanceFilesUpdateOutput,
  DashboardInstanceFilesUpdateOutput,
  mapDashboardInstanceFilesUpdateBody,
  DashboardInstanceFilesUpdateBody,
  mapDashboardInstanceFilesDeleteOutput,
  DashboardInstanceFilesDeleteOutput,
)


class MetorialFilesEndpoint(BaseMetorialEndpoint):
  """Represents files that you have uploaded to Metorial. Files can be linked to various resources based on their purpose. Metorial can also automatically extract files for you, for example for data exports."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    purpose: Optional[str] = None,
    organization_id: Optional[str] = None
  ) -> DashboardInstanceFilesListOutput:
    """
    List instance files
    Returns a paginated list of files owned by the instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param purpose: Optional[str] (optional)
    :param organization_id: Optional[str] (optional)
    :return: DashboardInstanceFilesListOutput
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
    if purpose is not None:
      query_dict["purpose"] = purpose
    if organization_id is not None:
      query_dict["organization_id"] = organization_id

    request = MetorialRequest(path=["files"], query=query_dict)
    return self._get(request).transform(mapDashboardInstanceFilesListOutput.from_dict)

  def get(self, file_id: str) -> DashboardInstanceFilesGetOutput:
    """
    Get file by ID
    Retrieves details for a specific file by its ID.

    :param file_id: str
    :return: DashboardInstanceFilesGetOutput
    """
    request = MetorialRequest(path=["files", file_id])
    return self._get(request).transform(mapDashboardInstanceFilesGetOutput.from_dict)

  def update(
    self, file_id: str, *, title: Optional[str] = None
  ) -> DashboardInstanceFilesUpdateOutput:
    """
    Update file by ID
    Updates editable fields of a specific file by its ID.

    :param file_id: str
    :param title: Optional[str] (optional)
    :return: DashboardInstanceFilesUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if title is not None:
      body_dict["title"] = title

    request = MetorialRequest(path=["files", file_id], body=body_dict)
    return self._patch(request).transform(
      mapDashboardInstanceFilesUpdateOutput.from_dict
    )

  def delete(self, file_id: str) -> DashboardInstanceFilesDeleteOutput:
    """
    Delete file by ID
    Deletes a specific file by its ID.

    :param file_id: str
    :return: DashboardInstanceFilesDeleteOutput
    """
    request = MetorialRequest(path=["files", file_id])
    return self._delete(request).transform(
      mapDashboardInstanceFilesDeleteOutput.from_dict
    )
