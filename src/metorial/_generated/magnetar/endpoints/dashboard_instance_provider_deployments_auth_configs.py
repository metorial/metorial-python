from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthConfigsListOutput, DashboardInstanceProviderDeploymentsAuthConfigsListOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsListQuery, DashboardInstanceProviderDeploymentsAuthConfigsListQuery, mapDashboardInstanceProviderDeploymentsAuthConfigsGetOutput, DashboardInstanceProviderDeploymentsAuthConfigsGetOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsCreateOutput, DashboardInstanceProviderDeploymentsAuthConfigsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsCreateBody, DashboardInstanceProviderDeploymentsAuthConfigsCreateBody, mapDashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput, DashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsUpdateBody, DashboardInstanceProviderDeploymentsAuthConfigsUpdateBody, mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput, DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput

class MetorialDashboardInstanceProviderDeploymentsAuthConfigsEndpoint(BaseMetorialEndpoint):
    """An auth config is a user's authenticated connection to a provider. Created when a user completes OAuth or manually enters an API token."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, available_for_use: Optional[bool] = None, available_for_provider_deployment_id: Optional[str] = None, provider_auth_credentials_id: Optional[Union[str, List[str]]] = None, provider_auth_method_id: Optional[Union[str, List[str]]] = None, actor_id: Optional[Union[str, List[str]]] = None, consumer_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, identity_credential_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsListOutput:
        """
    List provider auth configs
    Returns a paginated list of provider auth configs.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param available_for_use: Optional[bool] (optional)
    :param available_for_provider_deployment_id: Optional[str] (optional)
    :param provider_auth_credentials_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_method_id: Optional[Union[str, List[str]]] (optional)
    :param actor_id: Optional[Union[str, List[str]]] (optional)
    :param consumer_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param identity_credential_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthConfigsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if available_for_use is not None:
            query_dict["available_for_use"] = available_for_use
        if available_for_provider_deployment_id is not None:
            query_dict["available_for_provider_deployment_id"] = available_for_provider_deployment_id
        if provider_auth_credentials_id is not None:
            query_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id
        if actor_id is not None:
            query_dict["actor_id"] = actor_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if identity_credential_id is not None:
            query_dict["identity_credential_id"] = identity_credential_id
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-configs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsListOutput.from_dict)

    def get(self, instance_id: str, provider_auth_config_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsGetOutput:
        """
    Get provider auth config
    Retrieves a specific provider auth config by ID.

    :param instance_id: str
    :param provider_auth_config_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-configs', provider_auth_config_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsGetOutput.from_dict)

    def create(self, instance_id: str, *, provider_auth_method_id: str, value: Dict[str, Any], name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None, provider_deployment_id: Optional[str] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsCreateOutput:
        """
    Create provider auth config
    Creates a new provider auth config.

    :param instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :param provider_auth_method_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param value: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsAuthConfigsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters
        body_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        body_dict["value"] = value

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-configs'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsCreateOutput.from_dict)

    def update(self, instance_id: str, provider_auth_config_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput:
        """
    Update provider auth config
    Updates a specific provider auth config.

    :param instance_id: str
    :param provider_auth_config_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-configs', provider_auth_config_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput.from_dict)

    def delete(self, instance_id: str, provider_auth_config_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput:
        """
    Delete provider auth config
    Permanently deletes a provider auth config.

    :param instance_id: str
    :param provider_auth_config_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-configs', provider_auth_config_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput.from_dict)