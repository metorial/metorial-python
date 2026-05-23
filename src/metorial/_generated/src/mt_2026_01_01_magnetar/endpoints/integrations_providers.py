from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationsProvidersListOutput, DashboardInstanceIntegrationsProvidersListOutput, mapDashboardInstanceIntegrationsProvidersListQuery, DashboardInstanceIntegrationsProvidersListQuery, mapDashboardInstanceIntegrationsProvidersGetOutput, DashboardInstanceIntegrationsProvidersGetOutput, mapDashboardInstanceIntegrationsProvidersCreateOutput, DashboardInstanceIntegrationsProvidersCreateOutput, mapDashboardInstanceIntegrationsProvidersCreateBody, DashboardInstanceIntegrationsProvidersCreateBody, mapDashboardInstanceIntegrationsProvidersUpdateOutput, DashboardInstanceIntegrationsProvidersUpdateOutput, mapDashboardInstanceIntegrationsProvidersUpdateBody, DashboardInstanceIntegrationsProvidersUpdateBody, mapDashboardInstanceIntegrationsProvidersDeleteOutput, DashboardInstanceIntegrationsProvidersDeleteOutput

class MetorialIntegrationsProvidersEndpoint(BaseMetorialEndpoint):
    """Integration providers define the shared provider-level contract for a given integration."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_auth_method_id: Optional[Union[str, List[str]]] = None, provider_auth_credentials_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsProvidersListOutput:
        """
    List integration providers
    Returns a paginated list of integration providers.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_method_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_credentials_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsProvidersListOutput
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
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_auth_credentials_id is not None:
            query_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['integration-providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsProvidersListOutput.from_dict)

    def get(self, integration_provider_id: str) -> DashboardInstanceIntegrationsProvidersGetOutput:
        """
    Get integration provider
    Retrieves a specific integration provider.

    :param integration_provider_id: str
    :return: DashboardInstanceIntegrationsProvidersGetOutput
    """
        request = MetorialRequest(
            path=['integration-providers', integration_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsProvidersGetOutput.from_dict)

    def create(self, *, integration_id: str, provider_id: str, provider_deployment_id: str, provider_auth_method_id: Optional[str] = None, provider_auth_credentials_id: Optional[str] = None, provider_config_id: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceIntegrationsProvidersCreateOutput:
        """
    Create integration provider
    Creates a new integration provider.

    :param integration_id: str
    :param provider_id: str
    :param provider_deployment_id: str
    :param provider_auth_method_id: Optional[str] (optional)
    :param provider_auth_credentials_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceIntegrationsProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["integration_id"] = integration_id
        body_dict["provider_id"] = provider_id
        body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_method_id is not None:
            body_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_auth_credentials_id is not None:
            body_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['integration-providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsProvidersCreateOutput.from_dict)

    def update(self, integration_provider_id: str, *, provider_deployment_id: Optional[str] = None, provider_auth_method_id: Optional[str] = None, provider_auth_credentials_id: Optional[str] = None, provider_config_id: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceIntegrationsProvidersUpdateOutput:
        """
    Update integration provider
    Updates a specific integration provider.

    :param integration_provider_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_auth_method_id: Optional[str] (optional)
    :param provider_auth_credentials_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceIntegrationsProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_method_id is not None:
            body_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_auth_credentials_id is not None:
            body_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['integration-providers', integration_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIntegrationsProvidersUpdateOutput.from_dict)

    def delete(self, integration_provider_id: str) -> DashboardInstanceIntegrationsProvidersDeleteOutput:
        """
    Delete integration provider
    Archives a specific integration provider.

    :param integration_provider_id: str
    :return: DashboardInstanceIntegrationsProvidersDeleteOutput
    """
        request = MetorialRequest(
            path=['integration-providers', integration_provider_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIntegrationsProvidersDeleteOutput.from_dict)