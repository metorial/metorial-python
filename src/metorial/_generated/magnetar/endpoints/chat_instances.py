from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceChatInstancesListOutput, DashboardInstanceChatInstancesListOutput, mapDashboardInstanceChatInstancesListQuery, DashboardInstanceChatInstancesListQuery, mapDashboardInstanceChatInstancesGetOutput, DashboardInstanceChatInstancesGetOutput, mapDashboardInstanceChatInstancesCreateOutput, DashboardInstanceChatInstancesCreateOutput, mapDashboardInstanceChatInstancesCreateBody, DashboardInstanceChatInstancesCreateBody, mapDashboardInstanceChatInstancesUpdateOutput, DashboardInstanceChatInstancesUpdateOutput, mapDashboardInstanceChatInstancesUpdateBody, DashboardInstanceChatInstancesUpdateBody, mapDashboardInstanceChatInstancesDeleteOutput, DashboardInstanceChatInstancesDeleteOutput, mapDashboardInstanceChatInstancesSyncOutput, DashboardInstanceChatInstancesSyncOutput

class MetorialChatInstancesEndpoint(BaseMetorialEndpoint):
    """Chat instances materialize a chat connection for a specific runtime configuration."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, chat_connection_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatInstancesListOutput:
        """
    List chat instances
    Returns a paginated list of chat instances.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param chat_connection_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceChatInstancesListOutput
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
        if chat_connection_id is not None:
            query_dict["chat_connection_id"] = chat_connection_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['chat', 'instances'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceChatInstancesListOutput.from_dict)

    def get(self, chat_instance_id: str) -> DashboardInstanceChatInstancesGetOutput:
        """
    Get chat instance
    Retrieves a specific chat instance.

    :param chat_instance_id: str
    :return: DashboardInstanceChatInstancesGetOutput
    """
        request = MetorialRequest(
            path=['chat', 'instances', chat_instance_id]
        )
        return self._get(request).transform(mapDashboardInstanceChatInstancesGetOutput.from_dict)

    def create(self, *, chat_connection_id: str, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, private_metadata: Optional[Dict[str, Any]] = None, identity_actor_id: Optional[str] = None, identity_id: Optional[str] = None) -> DashboardInstanceChatInstancesCreateOutput:
        """
    Create chat instance
    Creates a new chat instance for a chat connection.

    :param chat_connection_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param private_metadata: Optional[Dict[str, Any]] (optional)
    :param identity_actor_id: Optional[str] (optional)
    :param identity_id: Optional[str] (optional)
    :return: DashboardInstanceChatInstancesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["chat_connection_id"] = chat_connection_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if private_metadata is not None:
            body_dict["private_metadata"] = private_metadata
        if identity_actor_id is not None:
            body_dict["identity_actor_id"] = identity_actor_id
        if identity_id is not None:
            body_dict["identity_id"] = identity_id

        request = MetorialRequest(
            path=['chat', 'instances'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceChatInstancesCreateOutput.from_dict)

    def update(self, chat_instance_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, private_metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceChatInstancesUpdateOutput:
        """
    Update chat instance
    Updates a specific chat instance.

    :param chat_instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param private_metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceChatInstancesUpdateOutput
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
            path=['chat', 'instances', chat_instance_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceChatInstancesUpdateOutput.from_dict)

    def delete(self, chat_instance_id: str) -> DashboardInstanceChatInstancesDeleteOutput:
        """
    Delete chat instance
    Archives a specific chat instance.

    :param chat_instance_id: str
    :return: DashboardInstanceChatInstancesDeleteOutput
    """
        request = MetorialRequest(
            path=['chat', 'instances', chat_instance_id]
        )
        return self._delete(request).transform(mapDashboardInstanceChatInstancesDeleteOutput.from_dict)

    def sync(self, chat_instance_id: str) -> DashboardInstanceChatInstancesSyncOutput:
        """
    Sync chat instance
    Triggers a sync of the workspaces available on this chat instance.

    :param chat_instance_id: str
    :return: DashboardInstanceChatInstancesSyncOutput
    """
        request = MetorialRequest(
            path=['chat', 'instances', chat_instance_id, 'sync']
        )
        return self._post(request).transform(mapDashboardInstanceChatInstancesSyncOutput.from_dict)