from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsProvidersListOutput, DashboardInstanceSessionsProvidersListOutput, mapDashboardInstanceSessionsProvidersListQuery, DashboardInstanceSessionsProvidersListQuery, mapDashboardInstanceSessionsProvidersGetOutput, DashboardInstanceSessionsProvidersGetOutput, mapDashboardInstanceSessionsProvidersCreateOutput, DashboardInstanceSessionsProvidersCreateOutput, mapDashboardInstanceSessionsProvidersCreateBody, DashboardInstanceSessionsProvidersCreateBody, mapDashboardInstanceSessionsProvidersUpdateOutput, DashboardInstanceSessionsProvidersUpdateOutput, mapDashboardInstanceSessionsProvidersUpdateBody, DashboardInstanceSessionsProvidersUpdateBody, mapDashboardInstanceSessionsProvidersDeleteOutput, DashboardInstanceSessionsProvidersDeleteOutput

class MetorialManagementInstanceSessionsProvidersEndpoint(BaseMetorialEndpoint):
    """Session providers represent the providers that are actively connected to a session. Each session can have multiple providers, and providers can be added or removed during the session lifecycle."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, session_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, provider_id: Optional[Union[str, List[str]]] = None, status: Optional[str] = None) -> DashboardInstanceSessionsProvidersListOutput:
        """
    List session providers
    Returns a paginated list of providers connected to a session.

    :param instance_id: str
    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[str] (optional)
    :return: DashboardInstanceSessionsProvidersListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id, 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProvidersListOutput.from_dict)

    def get(self, instance_id: str, session_id: str, session_provider_id: str) -> DashboardInstanceSessionsProvidersGetOutput:
        """
    Get session provider
    Retrieves a specific provider connected to a session.

    :param instance_id: str
    :param session_id: str
    :param session_provider_id: str
    :return: DashboardInstanceSessionsProvidersGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id, 'providers', session_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProvidersGetOutput.from_dict)

    def create(self, instance_id: str, session_id: str, *, provider_deployment: Union[Dict[str, Any], Dict[str, Any], str], name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, provider_auth_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, tool_filters: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsProvidersCreateOutput:
        """
    Create session provider
    Adds a new provider to an active session.

    :param instance_id: str
    :param session_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_deployment: Union[Dict[str, Any], Dict[str, Any], str]
    :param provider_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param provider_auth_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param tool_filters: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionsProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["provider_deployment"] = provider_deployment
        if provider_config is not None:
            body_dict["provider_config"] = provider_config
        if provider_auth_config is not None:
            body_dict["provider_auth_config"] = provider_auth_config
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id, 'providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSessionsProvidersCreateOutput.from_dict)

    def update(self, instance_id: str, session_id: str, session_provider_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionsProvidersUpdateOutput:
        """
    Update session provider
    Updates a provider connected to a session.

    :param instance_id: str
    :param session_id: str
    :param session_provider_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionsProvidersUpdateOutput
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
            path=['instances', instance_id, 'sessions', session_id, 'providers', session_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionsProvidersUpdateOutput.from_dict)

    def delete(self, instance_id: str, session_id: str, session_provider_id: str) -> DashboardInstanceSessionsProvidersDeleteOutput:
        """
    Delete session provider
    Removes a provider from a session.

    :param instance_id: str
    :param session_id: str
    :param session_provider_id: str
    :return: DashboardInstanceSessionsProvidersDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sessions', session_id, 'providers', session_provider_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSessionsProvidersDeleteOutput.from_dict)
