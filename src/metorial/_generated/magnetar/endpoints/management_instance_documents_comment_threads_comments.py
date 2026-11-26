from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutput, DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput, mapDashboardInstanceDocumentsCommentThreadsCommentsCreateBody, DashboardInstanceDocumentsCommentThreadsCommentsCreateBody, mapDashboardInstanceDocumentsCommentThreadsCommentsUpdateOutput, DashboardInstanceDocumentsCommentThreadsCommentsUpdateOutput, mapDashboardInstanceDocumentsCommentThreadsCommentsUpdateBody, DashboardInstanceDocumentsCommentThreadsCommentsUpdateBody, mapDashboardInstanceDocumentsCommentThreadsCommentsDeleteOutput, DashboardInstanceDocumentsCommentThreadsCommentsDeleteOutput

class MetorialManagementInstanceDocumentsCommentThreadsCommentsEndpoint(BaseMetorialEndpoint):
    """A document comment is a message in a document comment thread."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, instance_id: str, document_id: str, document_comment_thread_id: str, *, body: str) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput:
        """
    Create document comment
    Creates a comment in a document comment thread.

    :param instance_id: str
    :param document_id: str
    :param document_comment_thread_id: str
    :param body: str
    :return: DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["body"] = body

        request = MetorialRequest(
            path=['instances', instance_id, 'documents', document_id, 'comment-threads', document_comment_thread_id, 'comments'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutput.from_dict)

    def update(self, instance_id: str, document_id: str, document_comment_thread_id: str, document_comment_id: str, *, body: str) -> DashboardInstanceDocumentsCommentThreadsCommentsUpdateOutput:
        """
    Update document comment
    Edits a comment. Only the comment author can edit it.

    :param instance_id: str
    :param document_id: str
    :param document_comment_thread_id: str
    :param document_comment_id: str
    :param body: str
    :return: DashboardInstanceDocumentsCommentThreadsCommentsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["body"] = body

        request = MetorialRequest(
            path=['instances', instance_id, 'documents', document_id, 'comment-threads', document_comment_thread_id, 'comments', document_comment_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceDocumentsCommentThreadsCommentsUpdateOutput.from_dict)

    def delete(self, instance_id: str, document_id: str, document_comment_thread_id: str, document_comment_id: str) -> DashboardInstanceDocumentsCommentThreadsCommentsDeleteOutput:
        """
    Delete document comment
    Deletes a comment. Only the comment author can delete it.

    :param instance_id: str
    :param document_id: str
    :param document_comment_thread_id: str
    :param document_comment_id: str
    :return: DashboardInstanceDocumentsCommentThreadsCommentsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'documents', document_id, 'comment-threads', document_comment_thread_id, 'comments', document_comment_id]
        )
        return self._delete(request).transform(mapDashboardInstanceDocumentsCommentThreadsCommentsDeleteOutput.from_dict)