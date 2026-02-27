from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthConfigsListOutput, DashboardInstanceProviderDeploymentsAuthConfigsListOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsListQuery, DashboardInstanceProviderDeploymentsAuthConfigsListQuery, mapDashboardInstanceProviderDeploymentsAuthConfigsGetOutput, DashboardInstanceProviderDeploymentsAuthConfigsGetOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsCreateOutput, DashboardInstanceProviderDeploymentsAuthConfigsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsCreateBody, DashboardInstanceProviderDeploymentsAuthConfigsCreateBody, mapDashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput, DashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsUpdateBody, DashboardInstanceProviderDeploymentsAuthConfigsUpdateBody, mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput, DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput

class MetorialProviderDeploymentsAuthConfigsEndpoint(BaseMetorialEndpoint):
    """An auth config is a user's authenticated connection to a provider. Created when a user completes OAuth or manually enters an API token."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_auth_credentials_id: Optional[Union[str, List[str]]] = None, provider_auth_method_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsListOutput:
        """
    List provider auth configs
    Returns a paginated list of provider auth configs.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_credentials_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_method_id: Optional[Union[str, List[str]]] (optional)
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
        if provider_auth_credentials_id is not None:
            query_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id

        request = MetorialRequest(
            path=['provider-auth-configs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsListOutput.from_dict)

    def get(self, provider_auth_config_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsGetOutput:
        """
    Get provider auth config
    Retrieves a specific provider auth config by ID.

    :param provider_auth_config_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsGetOutput
    """
        request = MetorialRequest(
            path=['provider-auth-configs', provider_auth_config_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsGetOutput.from_dict)

    def create(self, *, name: str, provider_auth_method_id: str, value: Dict[str, Any], description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_deployment_id: Optional[str] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsCreateOutput:
        """
    Create provider auth config
    Creates a new provider auth config.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_auth_method_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param value: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsAuthConfigsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        body_dict["value"] = value

        request = MetorialRequest(
            path=['provider-auth-configs'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsCreateOutput.from_dict)

    def update(self, provider_auth_config_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput:
        """
    Update provider auth config
    Updates a specific provider auth config.

    :param provider_auth_config_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
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

        request = MetorialRequest(
            path=['provider-auth-configs', provider_auth_config_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsUpdateOutput.from_dict)

    def delete(self, provider_auth_config_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput:
        """
    Delete provider auth config
    Permanently deletes a provider auth config.

    :param provider_auth_config_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput
    """
        request = MetorialRequest(
            path=['provider-auth-configs', provider_auth_config_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput.from_dict)
