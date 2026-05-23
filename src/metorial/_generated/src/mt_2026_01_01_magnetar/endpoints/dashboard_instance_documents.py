from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsListOutput, DashboardInstanceDocumentsListOutput, mapDashboardInstanceDocumentsListQuery, DashboardInstanceDocumentsListQuery, mapDashboardInstanceDocumentsCreateOutput, DashboardInstanceDocumentsCreateOutput, mapDashboardInstanceDocumentsCreateBody, DashboardInstanceDocumentsCreateBody, mapDashboardInstanceDocumentsGetOutput, DashboardInstanceDocumentsGetOutput, mapDashboardInstanceDocumentsUpdateOutput, DashboardInstanceDocumentsUpdateOutput, mapDashboardInstanceDocumentsUpdateBody, DashboardInstanceDocumentsUpdateBody, mapDashboardInstanceDocumentsDeleteOutput, DashboardInstanceDocumentsDeleteOutput, mapDashboardInstanceDocumentsCloneOutput, DashboardInstanceDocumentsCloneOutput, mapDashboardInstanceDocumentsCloneBody, DashboardInstanceDocumentsCloneBody

class MetorialDashboardInstanceDocumentsEndpoint(BaseMetorialEndpoint):
    """Create and manage instance documents backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, file_id: Optional[Union[str, List[str]]] = None, store_id: Optional[Union[str, List[str]]] = None, parent_document_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceDocumentsListOutput:
        """
    List documents
    Returns a paginated list of documents owned by the instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param file_id: Optional[Union[str, List[str]]] (optional)
    :param store_id: Optional[Union[str, List[str]]] (optional)
    :param parent_document_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceDocumentsListOutput
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
        if file_id is not None:
            query_dict["file_id"] = file_id
        if store_id is not None:
            query_dict["store_id"] = store_id
        if parent_document_id is not None:
            query_dict["parent_document_id"] = parent_document_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsListOutput.from_dict)

    def create(self, instance_id: str, *, title: str, content: str) -> DashboardInstanceDocumentsCreateOutput:
        """
    Create document
    Creates a new document for the instance.

    :param instance_id: str
    :param title: str
    :param content: str
    :return: DashboardInstanceDocumentsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["title"] = title
        body_dict["content"] = content

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceDocumentsCreateOutput.from_dict)

    def get(self, instance_id: str, document_id: str) -> DashboardInstanceDocumentsGetOutput:
        """
    Get document by ID
    Retrieves a document by its ID.

    :param instance_id: str
    :param document_id: str
    :return: DashboardInstanceDocumentsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents', document_id]
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsGetOutput.from_dict)

    def update(self, instance_id: str, document_id: str, *, title: Optional[str] = None, content: Optional[str] = None) -> DashboardInstanceDocumentsUpdateOutput:
        """
    Update document by ID
    Updates a specific document.

    :param instance_id: str
    :param document_id: str
    :param title: Optional[str] (optional)
    :param content: Optional[str] (optional)
    :return: DashboardInstanceDocumentsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if title is not None:
            body_dict["title"] = title
        if content is not None:
            body_dict["content"] = content

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents', document_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceDocumentsUpdateOutput.from_dict)

    def delete(self, instance_id: str, document_id: str) -> DashboardInstanceDocumentsDeleteOutput:
        """
    Delete document by ID
    Deletes a specific document.

    :param instance_id: str
    :param document_id: str
    :return: DashboardInstanceDocumentsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents', document_id]
        )
        return self._delete(request).transform(mapDashboardInstanceDocumentsDeleteOutput.from_dict)

    def clone(self, instance_id: str, document_id: str, *, target_document_id: Optional[str] = None, title: Optional[str] = None) -> DashboardInstanceDocumentsCloneOutput:
        """
    Clone document by ID
    Clones a specific document.

    :param instance_id: str
    :param document_id: str
    :param target_document_id: Optional[str] (optional)
    :param title: Optional[str] (optional)
    :return: DashboardInstanceDocumentsCloneOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if target_document_id is not None:
            body_dict["target_document_id"] = target_document_id
        if title is not None:
            body_dict["title"] = title

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents', document_id, 'clone'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceDocumentsCloneOutput.from_dict)