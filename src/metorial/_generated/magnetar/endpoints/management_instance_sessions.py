from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsListOutput, DashboardInstanceSessionsListOutput, mapDashboardInstanceSessionsListQuery, DashboardInstanceSessionsListQuery, mapDashboardInstanceSessionsGetOutput, DashboardInstanceSessionsGetOutput, mapDashboardInstanceSessionsCreateOutput, DashboardInstanceSessionsCreateOutput, mapDashboardInstanceSessionsCreateBody, DashboardInstanceSessionsCreateBody, mapDashboardInstanceSessionsUpdateOutput, DashboardInstanceSessionsUpdateOutput, mapDashboardInstanceSessionsUpdateBody, DashboardInstanceSessionsUpdateBody, mapDashboardInstanceSessionsDeleteOutput, DashboardInstanceSessionsDeleteOutput

class MetorialManagementInstanceSessionsEndpoint(BaseMetorialEndpoint):
    """Sessions are connections to providers that allow clients to interact with MCP servers. Each session can include one or more provider deployments."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionsListOutput:
        """
    List sessions
    Returns a paginated list of sessions.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsListOutput
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
        if status is not None:
            query_dict["status"] = status
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id

        request = MetorialRequest(
            path=['instances', instance_id, 'sessions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsListOutput.from_dict)

    def get(self, instance_id: str, session_id: str) -> DashboardInstanceSessionsGetOutput:
        """
    Get session
    Retrieves a specific session by ID.

    :param instance_id: str
    :param session_id: str
    :return: DashboardInstanceSessionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsGetOutput.from_dict)

    def create(self, instance_id: str, *, providers: List[Dict[str, Any]], name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsCreateOutput:
        """
    Create session
    Creates a new session with provider deployments.

    :param instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param providers: List[Dict[str, Any]]
    :return: DashboardInstanceSessionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["providers"] = providers

        request = MetorialRequest(
            path=['instances', instance_id, 'sessions'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSessionsCreateOutput.from_dict)

    def update(self, instance_id: str, session_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsUpdateOutput:
        """
    Update session
    Updates a session.

    :param instance_id: str
    :param session_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionsUpdateOutput.from_dict)

    def delete(self, instance_id: str, session_id: str) -> DashboardInstanceSessionsDeleteOutput:
        """
    Delete session
    Deletes a session.

    :param instance_id: str
    :param session_id: str
    :return: DashboardInstanceSessionsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSessionsDeleteOutput.from_dict)
