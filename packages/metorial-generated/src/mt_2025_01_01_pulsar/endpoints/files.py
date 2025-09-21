from typing import Optional, Dict, Any, List, Union
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
    self, query: DashboardInstanceFilesListQuery = None
  ) -> DashboardInstanceFilesListOutput:
    """
    List instance files
    Returns a paginated list of files owned by the instance.

    :param query: DashboardInstanceFilesListQuery
    :return: DashboardInstanceFilesListOutput
    """
    request = MetorialRequest(
      path=["files"],
      query=mapDashboardInstanceFilesListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(mapDashboardInstanceFilesListOutput.from_dict)

  def get(self, fileId: str) -> DashboardInstanceFilesGetOutput:
    """
    Get file by ID
    Retrieves details for a specific file by its ID.

    :param fileId: str
    :return: DashboardInstanceFilesGetOutput
    """
    request = MetorialRequest(path=["files", fileId])
    return self._get(request).transform(mapDashboardInstanceFilesGetOutput.from_dict)

  def update(
    self, fileId: str, *, title: Optional[str] = None
  ) -> DashboardInstanceFilesUpdateOutput:
    """
    Update file by ID
    Updates editable fields of a specific file by its ID.

    :param fileId: str
    :param title: str (optional)
    :return: DashboardInstanceFilesUpdateOutput
    """
    _params = {"title": title}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["files", fileId],
      body=body,
    )
    return self._patch(request).transform(
      mapDashboardInstanceFilesUpdateOutput.from_dict
    )

  def delete(self, fileId: str) -> DashboardInstanceFilesDeleteOutput:
    """
    Delete file by ID
    Deletes a specific file by its ID.

    :param fileId: str
    :return: DashboardInstanceFilesDeleteOutput
    """
    request = MetorialRequest(path=["files", fileId])
    return self._delete(request).transform(
      mapDashboardInstanceFilesDeleteOutput.from_dict
    )
