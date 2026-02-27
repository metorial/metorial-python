from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsProvidersListOutput, DashboardInstanceSessionsProvidersListOutput, mapDashboardInstanceSessionsProvidersListQuery, DashboardInstanceSessionsProvidersListQuery, mapDashboardInstanceSessionsProvidersGetOutput, DashboardInstanceSessionsProvidersGetOutput, mapDashboardInstanceSessionsProvidersCreateOutput, DashboardInstanceSessionsProvidersCreateOutput, mapDashboardInstanceSessionsProvidersCreateBody, DashboardInstanceSessionsProvidersCreateBody, mapDashboardInstanceSessionsProvidersUpdateOutput, DashboardInstanceSessionsProvidersUpdateOutput, mapDashboardInstanceSessionsProvidersUpdateBody, DashboardInstanceSessionsProvidersUpdateBody, mapDashboardInstanceSessionsProvidersDeleteOutput, DashboardInstanceSessionsProvidersDeleteOutput

class MetorialSessionsProvidersEndpoint(BaseMetorialEndpoint):
    """Session providers represent the providers that are actively connected to a session. Each session can have multiple providers, and providers can be added or removed during the session lifecycle."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_template_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionsProvidersListOutput:
        """
    List session providers
    Returns a paginated list of providers connected to a session.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
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
        if id is not None:
            query_dict["id"] = id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if session_template_id is not None:
            query_dict["session_template_id"] = session_template_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['session-providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProvidersListOutput.from_dict)

    def get(self, session_provider_id: str) -> DashboardInstanceSessionsProvidersGetOutput:
        """
    Get session provider
    Retrieves a specific provider connected to a session.

    :param session_provider_id: str
    :return: DashboardInstanceSessionsProvidersGetOutput
    """
        request = MetorialRequest(
            path=['session-providers', session_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProvidersGetOutput.from_dict)

    def create(self, *, session_id: str, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceSessionsProvidersCreateOutput:
        """
    Create session provider
    Adds a new provider to an active session.

    :param session_id: str
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceSessionsProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["session_id"] = session_id
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['session-providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSessionsProvidersCreateOutput.from_dict)

    def update(self, session_provider_id: str, *, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceSessionsProvidersUpdateOutput:
        """
    Update session provider
    Updates a provider connected to a session.

    :param session_provider_id: str
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceSessionsProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['session-providers', session_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionsProvidersUpdateOutput.from_dict)

    def delete(self, session_provider_id: str) -> DashboardInstanceSessionsProvidersDeleteOutput:
        """
    Delete session provider
    Removes a provider from a session.

    :param session_provider_id: str
    :return: DashboardInstanceSessionsProvidersDeleteOutput
    """
        request = MetorialRequest(
            path=['session-providers', session_provider_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSessionsProvidersDeleteOutput.from_dict)
