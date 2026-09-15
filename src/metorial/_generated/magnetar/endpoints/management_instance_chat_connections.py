from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatConnectionsListOutput, DashboardInstanceChatConnectionsListOutput, mapDashboardInstanceChatConnectionsListQuery, DashboardInstanceChatConnectionsListQuery, mapDashboardInstanceChatConnectionsGetOutput, DashboardInstanceChatConnectionsGetOutput, mapDashboardInstanceChatConnectionsCreateOutput, DashboardInstanceChatConnectionsCreateOutput, mapDashboardInstanceChatConnectionsCreateBody, DashboardInstanceChatConnectionsCreateBody, mapDashboardInstanceChatConnectionsUpdateOutput, DashboardInstanceChatConnectionsUpdateOutput, mapDashboardInstanceChatConnectionsUpdateBody, DashboardInstanceChatConnectionsUpdateBody, mapDashboardInstanceChatConnectionsDeleteOutput, DashboardInstanceChatConnectionsDeleteOutput

class MetorialManagementInstanceChatConnectionsEndpoint(BaseMetorialEndpoint):
    """Chat connections link a chat provider, such as Slack or Microsoft Teams, to your instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatConnectionsListOutput:
        """
    List chat connections
    Returns a paginated list of chat connections.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceChatConnectionsListOutput
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
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'connections'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatConnectionsListOutput.from_dict)

    def get(self, instance_id: str, chat_connection_id: str) -> DashboardInstanceChatConnectionsGetOutput:
        """
    Get chat connection
    Retrieves a specific chat connection.

    :param instance_id: str
    :param chat_connection_id: str
    :return: DashboardInstanceChatConnectionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'connections', chat_connection_id]
        )
        return self._get(request).transform(mapDashboardInstanceChatConnectionsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, provider: Dict[str, Any], description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, private_metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatConnectionsCreateOutput:
        """
    Create chat connection
    Creates a new chat connection, together with the single provider it is linked to.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param private_metadata: Optional[Dict[str, Any]] (optional)
    :param provider: Dict[str, Any]
    :return: DashboardInstanceChatConnectionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if private_metadata is not None:
            body_dict["private_metadata"] = private_metadata
        body_dict["provider"] = provider

        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'connections'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatConnectionsCreateOutput.from_dict)

    def update(self, instance_id: str, chat_connection_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, private_metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatConnectionsUpdateOutput:
        """
    Update chat connection
    Updates a specific chat connection.

    :param instance_id: str
    :param chat_connection_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param private_metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceChatConnectionsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if private_metadata is not None:
            body_dict["private_metadata"] = private_metadata

        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'connections', chat_connection_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceChatConnectionsUpdateOutput.from_dict)

    def delete(self, instance_id: str, chat_connection_id: str) -> DashboardInstanceChatConnectionsDeleteOutput:
        """
    Delete chat connection
    Archives a specific chat connection.

    :param instance_id: str
    :param chat_connection_id: str
    :return: DashboardInstanceChatConnectionsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'chat', 'connections', chat_connection_id]
        )
        return self._delete(request).transform(mapDashboardInstanceChatConnectionsDeleteOutput.from_dict)