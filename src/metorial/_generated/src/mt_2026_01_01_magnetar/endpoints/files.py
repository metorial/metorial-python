from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceFilesListOutput, DashboardInstanceFilesListOutput, mapDashboardInstanceFilesListQuery, DashboardInstanceFilesListQuery, mapDashboardInstanceFilesGetOutput, DashboardInstanceFilesGetOutput, mapDashboardInstanceFilesDeleteOutput, DashboardInstanceFilesDeleteOutput

class MetorialFilesEndpoint(BaseMetorialEndpoint):
    """Represents files that you have uploaded to Metorial. Files can be linked to various resources based on their purpose. Metorial can also automatically extract files for you, for example for data exports."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, purpose: Optional[Union[str, List[str]]] = None, store_id: Optional[Union[str, List[str]]] = None, document_id: Optional[Union[str, List[str]]] = None, file_link_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceFilesListOutput:
        """
    List instance files
    Returns a paginated list of files owned by the instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param purpose: Optional[Union[str, List[str]]] (optional)
    :param store_id: Optional[Union[str, List[str]]] (optional)
    :param document_id: Optional[Union[str, List[str]]] (optional)
    :param file_link_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
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
        if id is not None:
            query_dict["id"] = id
        if purpose is not None:
            query_dict["purpose"] = purpose
        if store_id is not None:
            query_dict["store_id"] = store_id
        if document_id is not None:
            query_dict["document_id"] = document_id
        if file_link_id is not None:
            query_dict["file_link_id"] = file_link_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['files'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceFilesListOutput.from_dict)

    def get(self, file_id: str) -> DashboardInstanceFilesGetOutput:
        """
    Get file by ID
    Retrieves details for a specific file by its ID.

    :param file_id: str
    :return: DashboardInstanceFilesGetOutput
    """
        request = MetorialRequest(
            path=['files', file_id]
        )
        return self._get(request).transform(mapDashboardInstanceFilesGetOutput.from_dict)

    def delete(self, file_id: str) -> DashboardInstanceFilesDeleteOutput:
        """
    Delete file by ID
    Deletes a specific file by its ID.

    :param file_id: str
    :return: DashboardInstanceFilesDeleteOutput
    """
        request = MetorialRequest(
            path=['files', file_id]
        )
        return self._delete(request).transform(mapDashboardInstanceFilesDeleteOutput.from_dict)