from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsListOutput, DashboardInstanceSessionsListOutput, mapDashboardInstanceSessionsListQuery, DashboardInstanceSessionsListQuery, mapDashboardInstanceSessionsGetOutput, DashboardInstanceSessionsGetOutput, mapDashboardInstanceSessionsCreateOutput, DashboardInstanceSessionsCreateOutput, mapDashboardInstanceSessionsCreateBody, DashboardInstanceSessionsCreateBody, mapDashboardInstanceSessionsUpdateOutput, DashboardInstanceSessionsUpdateOutput, mapDashboardInstanceSessionsUpdateBody, DashboardInstanceSessionsUpdateBody

class MetorialDashboardInstanceSessionsEndpoint(BaseMetorialEndpoint):
    """Sessions are connections to providers that allow clients to interact with MCP servers. Each session can include one or more provider deployments."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, session_template_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsListOutput:
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
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
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
        if id is not None:
            query_dict["id"] = id
        if session_template_id is not None:
            query_dict["session_template_id"] = session_template_id
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sessions'],
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
            path=['dashboard', 'instances', instance_id, 'sessions', session_id]
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
            path=['dashboard', 'instances', instance_id, 'sessions'],
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
            path=['dashboard', 'instances', instance_id, 'sessions', session_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionsUpdateOutput.from_dict)