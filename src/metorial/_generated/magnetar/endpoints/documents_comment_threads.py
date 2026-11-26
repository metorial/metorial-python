from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsCommentThreadsListOutput, DashboardInstanceDocumentsCommentThreadsListOutput, mapDashboardInstanceDocumentsCommentThreadsListQuery, DashboardInstanceDocumentsCommentThreadsListQuery, mapDashboardInstanceDocumentsCommentThreadsGetOutput, DashboardInstanceDocumentsCommentThreadsGetOutput, mapDashboardInstanceDocumentsCommentThreadsCreateOutput, DashboardInstanceDocumentsCommentThreadsCreateOutput, mapDashboardInstanceDocumentsCommentThreadsCreateBody, DashboardInstanceDocumentsCommentThreadsCreateBody, mapDashboardInstanceDocumentsCommentThreadsUpdateOutput, DashboardInstanceDocumentsCommentThreadsUpdateOutput, mapDashboardInstanceDocumentsCommentThreadsUpdateBody, DashboardInstanceDocumentsCommentThreadsUpdateBody, mapDashboardInstanceDocumentsCommentThreadsDeleteOutput, DashboardInstanceDocumentsCommentThreadsDeleteOutput

class MetorialDocumentsCommentThreadsEndpoint(BaseMetorialEndpoint):
    """A document comment thread is a discussion anchored to a text selection in a document."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, document_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, anchor_status: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceDocumentsCommentThreadsListOutput:
        """
    List document comment threads
    Returns a paginated list of comment threads in a document.

    :param document_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param anchor_status: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceDocumentsCommentThreadsListOutput
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
        if status is not None:
            query_dict["status"] = status
        if anchor_status is not None:
            query_dict["anchor_status"] = anchor_status
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['documents', document_id, 'comment-threads'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsCommentThreadsListOutput.from_dict)

    def get(self, document_id: str, document_comment_thread_id: str) -> DashboardInstanceDocumentsCommentThreadsGetOutput:
        """
    Get document comment thread
    Retrieves a document comment thread with its comments.

    :param document_id: str
    :param document_comment_thread_id: str
    :return: DashboardInstanceDocumentsCommentThreadsGetOutput
    """
        request = MetorialRequest(
            path=['documents', document_id, 'comment-threads', document_comment_thread_id]
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsCommentThreadsGetOutput.from_dict)

    def create(self, document_id: str, *, anchor: Dict[str, Any], body: str) -> DashboardInstanceDocumentsCommentThreadsCreateOutput:
        """
    Create document comment thread
    Starts a comment thread on a text selection. Anyone who can read the document can comment.

    :param document_id: str
    :param anchor: Dict[str, Any]
    :param body: str
    :return: DashboardInstanceDocumentsCommentThreadsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["anchor"] = anchor
        body_dict["body"] = body

        request = MetorialRequest(
            path=['documents', document_id, 'comment-threads'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceDocumentsCommentThreadsCreateOutput.from_dict)

    def update(self, document_id: str, document_comment_thread_id: str, *, status: Optional[str] = None) -> DashboardInstanceDocumentsCommentThreadsUpdateOutput:
        """
    Update document comment thread
    Resolves or reopens a comment thread. Allowed for the thread author and document editors.

    :param document_id: str
    :param document_comment_thread_id: str
    :param status: Optional[str] (optional)
    :return: DashboardInstanceDocumentsCommentThreadsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if status is not None:
            body_dict["status"] = status

        request = MetorialRequest(
            path=['documents', document_id, 'comment-threads', document_comment_thread_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceDocumentsCommentThreadsUpdateOutput.from_dict)

    def delete(self, document_id: str, document_comment_thread_id: str) -> DashboardInstanceDocumentsCommentThreadsDeleteOutput:
        """
    Delete document comment thread
    Deletes a comment thread and removes its highlight. Requires document write access.

    :param document_id: str
    :param document_comment_thread_id: str
    :return: DashboardInstanceDocumentsCommentThreadsDeleteOutput
    """
        request = MetorialRequest(
            path=['documents', document_id, 'comment-threads', document_comment_thread_id]
        )
        return self._delete(request).transform(mapDashboardInstanceDocumentsCommentThreadsDeleteOutput.from_dict)