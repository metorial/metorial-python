from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceConversationsListOutput, DashboardInstanceConversationsListOutput, mapDashboardInstanceConversationsListQuery, DashboardInstanceConversationsListQuery, mapDashboardInstanceConversationsCreateOutput, DashboardInstanceConversationsCreateOutput, mapDashboardInstanceConversationsCreateBody, DashboardInstanceConversationsCreateBody, mapDashboardInstanceConversationsGetOutput, DashboardInstanceConversationsGetOutput, mapDashboardInstanceConversationsUpdateOutput, DashboardInstanceConversationsUpdateOutput, mapDashboardInstanceConversationsUpdateBody, DashboardInstanceConversationsUpdateBody

class MetorialConversationsEndpoint(BaseMetorialEndpoint):
    """Assistant and conversation endpoints"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, assistant_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceConversationsListOutput:
        """
    List assistant conversations
    List assistant conversations in an instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param assistant_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceConversationsListOutput
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
        if assistant_id is not None:
            query_dict["assistant_id"] = assistant_id

        request = MetorialRequest(
            path=['conversations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceConversationsListOutput.from_dict)

    def create(self, *, assistant_id: str, title: Optional[str] = None, input: Optional[Dict[str, Any]] = None) -> DashboardInstanceConversationsCreateOutput:
        """
    Create assistant conversation
    Create a new assistant conversation in an instance.

    :param assistant_id: str
    :param title: Optional[str] (optional)
    :param input: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceConversationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["assistant_id"] = assistant_id
        if title is not None:
            body_dict["title"] = title
        if input is not None:
            body_dict["input"] = input

        request = MetorialRequest(
            path=['conversations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceConversationsCreateOutput.from_dict)

    def get(self, assistant_conversation_id: str) -> DashboardInstanceConversationsGetOutput:
        """
    Get assistant conversation
    Get a specific assistant conversation.

    :param assistant_conversation_id: str
    :return: DashboardInstanceConversationsGetOutput
    """
        request = MetorialRequest(
            path=['conversations', assistant_conversation_id]
        )
        return self._get(request).transform(mapDashboardInstanceConversationsGetOutput.from_dict)

    def update(self, assistant_conversation_id: str, *, title: Optional[str] = None) -> DashboardInstanceConversationsUpdateOutput:
        """
    Update assistant conversation
    Update a specific assistant conversation.

    :param assistant_conversation_id: str
    :param title: Optional[str] (optional)
    :return: DashboardInstanceConversationsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if title is not None:
            body_dict["title"] = title

        request = MetorialRequest(
            path=['conversations', assistant_conversation_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceConversationsUpdateOutput.from_dict)