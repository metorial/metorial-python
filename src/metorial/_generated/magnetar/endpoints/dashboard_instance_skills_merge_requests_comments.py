from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMergeRequestsCommentsListOutput, DashboardInstanceSkillsMergeRequestsCommentsListOutput, mapDashboardInstanceSkillsMergeRequestsCommentsListQuery, DashboardInstanceSkillsMergeRequestsCommentsListQuery, mapDashboardInstanceSkillsMergeRequestsCommentsCreateOutput, DashboardInstanceSkillsMergeRequestsCommentsCreateOutput, mapDashboardInstanceSkillsMergeRequestsCommentsCreateBody, DashboardInstanceSkillsMergeRequestsCommentsCreateBody, mapDashboardInstanceSkillsMergeRequestsCommentsGetOutput, DashboardInstanceSkillsMergeRequestsCommentsGetOutput, mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutput, DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput, mapDashboardInstanceSkillsMergeRequestsCommentsUpdateBody, DashboardInstanceSkillsMergeRequestsCommentsUpdateBody, mapDashboardInstanceSkillsMergeRequestsCommentsDeleteOutput, DashboardInstanceSkillsMergeRequestsCommentsDeleteOutput

class MetorialDashboardInstanceSkillsMergeRequestsCommentsEndpoint(BaseMetorialEndpoint):
    """Discuss skill merge requests and individual proposed changes."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, skill_merge_request_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, item_id: Optional[str] = None) -> DashboardInstanceSkillsMergeRequestsCommentsListOutput:
        """
    List skill merge request comments
    Lists comments on a skill merge request or one of its items.

    :param instance_id: str
    :param skill_merge_request_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param item_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsMergeRequestsCommentsListOutput
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
        if item_id is not None:
            query_dict["item_id"] = item_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'comments'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsCommentsListOutput.from_dict)

    def create(self, instance_id: str, skill_merge_request_id: str, *, body: str, item_id: Optional[str] = None, in_reply_to_comment_id: Optional[str] = None, path: Optional[str] = None) -> DashboardInstanceSkillsMergeRequestsCommentsCreateOutput:
        """
    Create skill merge request comment
    Adds a comment to a skill merge request or one of its items.

    :param instance_id: str
    :param skill_merge_request_id: str
    :param item_id: Optional[str] (optional)
    :param in_reply_to_comment_id: Optional[str] (optional)
    :param body: str
    :param path: Optional[str] (optional)
    :return: DashboardInstanceSkillsMergeRequestsCommentsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if item_id is not None:
            body_dict["item_id"] = item_id
        if in_reply_to_comment_id is not None:
            body_dict["in_reply_to_comment_id"] = in_reply_to_comment_id
        body_dict["body"] = body
        if path is not None:
            body_dict["path"] = path

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'comments'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsMergeRequestsCommentsCreateOutput.from_dict)

    def get(self, instance_id: str, skill_merge_request_id: str, comment_id: str) -> DashboardInstanceSkillsMergeRequestsCommentsGetOutput:
        """
    Get skill merge request comment
    Retrieves a comment on a skill merge request.

    :param instance_id: str
    :param skill_merge_request_id: str
    :param comment_id: str
    :return: DashboardInstanceSkillsMergeRequestsCommentsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'comments', comment_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsCommentsGetOutput.from_dict)

    def update(self, instance_id: str, skill_merge_request_id: str, comment_id: str, *, body: str) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput:
        """
    Update skill merge request comment
    Updates a comment authored by the current actor.

    :param instance_id: str
    :param skill_merge_request_id: str
    :param comment_id: str
    :param body: str
    :return: DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["body"] = body

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'comments', comment_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutput.from_dict)

    def delete(self, instance_id: str, skill_merge_request_id: str, comment_id: str) -> DashboardInstanceSkillsMergeRequestsCommentsDeleteOutput:
        """
    Delete skill merge request comment
    Deletes a comment authored by the current actor.

    :param instance_id: str
    :param skill_merge_request_id: str
    :param comment_id: str
    :return: DashboardInstanceSkillsMergeRequestsCommentsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skill-merge-requests', skill_merge_request_id, 'comments', comment_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsMergeRequestsCommentsDeleteOutput.from_dict)