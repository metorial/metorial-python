from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionTemplatesProvidersListOutput, DashboardInstanceSessionTemplatesProvidersListOutput, mapDashboardInstanceSessionTemplatesProvidersListQuery, DashboardInstanceSessionTemplatesProvidersListQuery, mapDashboardInstanceSessionTemplatesProvidersGetOutput, DashboardInstanceSessionTemplatesProvidersGetOutput, mapDashboardInstanceSessionTemplatesProvidersCreateOutput, DashboardInstanceSessionTemplatesProvidersCreateOutput, mapDashboardInstanceSessionTemplatesProvidersCreateBody, DashboardInstanceSessionTemplatesProvidersCreateBody, mapDashboardInstanceSessionTemplatesProvidersUpdateOutput, DashboardInstanceSessionTemplatesProvidersUpdateOutput, mapDashboardInstanceSessionTemplatesProvidersUpdateBody, DashboardInstanceSessionTemplatesProvidersUpdateBody, mapDashboardInstanceSessionTemplatesProvidersDeleteOutput, DashboardInstanceSessionTemplatesProvidersDeleteOutput

class MetorialSessionTemplatesProvidersEndpoint(BaseMetorialEndpoint):
    """Session template providers define which providers should be included when a session is created from a template."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, session_template_id: Optional[Union[str, List[str]]] = None, session_template_template_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionTemplatesProvidersListOutput:
        """
    List session template providers
    Returns a paginated list of providers configured for a session template.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param session_template_template_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
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
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if session_template_id is not None:
            query_dict["session_template_id"] = session_template_id
        if session_template_template_id is not None:
            query_dict["session_template_template_id"] = session_template_template_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id

        request = MetorialRequest(
            path=['session-template-providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionTemplatesProvidersListOutput.from_dict)

    def get(self, session_template_provider_id: str) -> DashboardInstanceSessionTemplatesProvidersGetOutput:
        """
    Get session template provider
    Retrieves a specific provider configuration from a session template.

    :param session_template_provider_id: str
    :return: DashboardInstanceSessionTemplatesProvidersGetOutput
    """
        request = MetorialRequest(
            path=['session-template-providers', session_template_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionTemplatesProvidersGetOutput.from_dict)

    def create(self, *, session_template_id: str, provider_deployment_id: Optional[str] = None, provider_config_id: Optional[str] = None, provider_config_vault_id: Optional[str] = None, provider_auth_config_id: Optional[str] = None, tool_filters: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionTemplatesProvidersCreateOutput:
        """
    Create session template provider
    Adds a new provider configuration to a session template.

    :param session_template_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param provider_config_vault_id: Optional[str] (optional)
    :param provider_auth_config_id: Optional[str] (optional)
    :param tool_filters: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionTemplatesProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["session_template_id"] = session_template_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if provider_config_vault_id is not None:
            body_dict["provider_config_vault_id"] = provider_config_vault_id
        if provider_auth_config_id is not None:
            body_dict["provider_auth_config_id"] = provider_auth_config_id
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['session-template-providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSessionTemplatesProvidersCreateOutput.from_dict)

    def update(self, session_template_provider_id: str, *, tool_filters: Optional[Dict[str, Any]] = None) -> DashboardInstanceSessionTemplatesProvidersUpdateOutput:
        """
    Update session template provider
    Updates a provider configuration in a session template.

    :param session_template_provider_id: str
    :param tool_filters: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSessionTemplatesProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['session-template-providers', session_template_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSessionTemplatesProvidersUpdateOutput.from_dict)

    def delete(self, session_template_provider_id: str) -> DashboardInstanceSessionTemplatesProvidersDeleteOutput:
        """
    Delete session template provider
    Removes a provider configuration from a session template.

    :param session_template_provider_id: str
    :return: DashboardInstanceSessionTemplatesProvidersDeleteOutput
    """
        request = MetorialRequest(
            path=['session-template-providers', session_template_provider_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSessionTemplatesProvidersDeleteOutput.from_dict)