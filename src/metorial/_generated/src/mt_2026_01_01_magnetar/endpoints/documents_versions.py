from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsVersionsListOutput, DashboardInstanceDocumentsVersionsListOutput, mapDashboardInstanceDocumentsVersionsListQuery, DashboardInstanceDocumentsVersionsListQuery, mapDashboardInstanceDocumentsVersionsGetOutput, DashboardInstanceDocumentsVersionsGetOutput

class MetorialDocumentsVersionsEndpoint(BaseMetorialEndpoint):
    """Inspect document version history for an instance document."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, document_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, last_edited_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceDocumentsVersionsListOutput:
        """
    List document versions
    Returns a paginated list of versions for a specific document.

    :param document_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param last_edited_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceDocumentsVersionsListOutput
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
        if created_at is not None:
            query_dict["created_at"] = created_at
        if last_edited_at is not None:
            query_dict["last_edited_at"] = last_edited_at

        request = MetorialRequest(
            path=['documents', document_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsVersionsListOutput.from_dict)

    def get(self, document_id: str, document_version_id: str) -> DashboardInstanceDocumentsVersionsGetOutput:
        """
    Get document version by ID
    Retrieves a specific document version by its ID.

    :param document_id: str
    :param document_version_id: str
    :return: DashboardInstanceDocumentsVersionsGetOutput
    """
        request = MetorialRequest(
            path=['documents', document_id, 'versions', document_version_id]
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsVersionsGetOutput.from_dict)