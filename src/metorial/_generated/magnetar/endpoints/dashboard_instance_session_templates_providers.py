from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionTemplatesProvidersListOutput, DashboardInstanceSessionTemplatesProvidersListOutput, mapDashboardInstanceSessionTemplatesProvidersListQuery, DashboardInstanceSessionTemplatesProvidersListQuery, mapDashboardInstanceSessionTemplatesProvidersGetOutput, DashboardInstanceSessionTemplatesProvidersGetOutput, mapDashboardInstanceSessionTemplatesProvidersCreateOutput, DashboardInstanceSessionTemplatesProvidersCreateOutput, mapDashboardInstanceSessionTemplatesProvidersCreateBody, DashboardInstanceSessionTemplatesProvidersCreateBody, mapDashboardInstanceSessionTemplatesProvidersUpdateOutput, DashboardInstanceSessionTemplatesProvidersUpdateOutput, mapDashboardInstanceSessionTemplatesProvidersUpdateBody, DashboardInstanceSessionTemplatesProvidersUpdateBody, mapDashboardInstanceSessionTemplatesProvidersDeleteOutput, DashboardInstanceSessionTemplatesProvidersDeleteOutput

class MetorialDashboardInstanceSessionTemplatesProvidersEndpoint(BaseMetorialEndpoint):
    """Session template providers define which providers should be included when a session is created from a template."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, session_template_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, provider_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionTemplatesProvidersListOutput:
        """
    List session template providers
    Returns a paginated list of providers configured for a session template.

    :param instance_id: str
    :param session_template_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionTemplatesProvidersListOutput
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

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'session-templates', session_template_id, 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionTemplatesProvidersListOutput.from_dict)

    def get(self, instance_id: str, session_template_id: str, session_template_provider_id: str) -> DashboardInstanceSessionTemplatesProvidersGetOutput:
        """
    Get session template provider
    Retrieves a specific provider configuration from a session template.

    :param instance_id: str
    :param session_template_id: str
    :param session_template_provider_id: str
    :return: DashboardInstanceSessionTemplatesProvidersGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'session-templates', session_template_id, 'providers', session_template_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionTemplatesProvidersGetOutput.from_dict)

    def create(self, instance_id: str, session_template_id: str, *, provider_deployment: Union[Dict[str, Any], Dict[str, Any], str], name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, provider_auth_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, tool_filters: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionTemplatesProvidersCreateOutput:
        """
    Create session template provider
    Adds a new provider configuration to a session template.

    :param instance_id: str
    :param session_template_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_deployment: Union[Dict[str, Any], Dict[str, Any], str]
    :param provider_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param provider_auth_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param tool_filters: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionTemplatesProvidersCreateOutput
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
            path=['dashboard', 'instances', instance_id, 'session-templates', session_template_id, 'providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSessionTemplatesProvidersCreateOutput.from_dict)

    def update(self, instance_id: str, session_template_id: str, session_template_provider_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_deployment: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, provider_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, provider_auth_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] = None, tool_filters: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionTemplatesProvidersUpdateOutput:
        """
    Update session template provider
    Updates a provider configuration in a session template.

    :param instance_id: str
    :param session_template_id: str
    :param session_template_provider_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_deployment: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param provider_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param provider_auth_config: Optional[Union[Dict[str, Any], Dict[str, Any], str]] (optional)
    :param tool_filters: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionTemplatesProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if provider_deployment is not None:
            body_dict["provider_deployment"] = provider_deployment
        if provider_config is not None:
            body_dict["provider_config"] = provider_config
        if provider_auth_config is not None:
            body_dict["provider_auth_config"] = provider_auth_config
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'session-templates', session_template_id, 'providers', session_template_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionTemplatesProvidersUpdateOutput.from_dict)

    def delete(self, instance_id: str, session_template_id: str, session_template_provider_id: str) -> DashboardInstanceSessionTemplatesProvidersDeleteOutput:
        """
    Delete session template provider
    Removes a provider configuration from a session template.

    :param instance_id: str
    :param session_template_id: str
    :param session_template_provider_id: str
    :return: DashboardInstanceSessionTemplatesProvidersDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'session-templates', session_template_id, 'providers', session_template_provider_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSessionTemplatesProvidersDeleteOutput.from_dict)
