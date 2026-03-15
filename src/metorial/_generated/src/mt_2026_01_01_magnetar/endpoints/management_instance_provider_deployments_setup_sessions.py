from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsSetupSessionsListOutput, DashboardInstanceProviderDeploymentsSetupSessionsListOutput, mapDashboardInstanceProviderDeploymentsSetupSessionsListQuery, DashboardInstanceProviderDeploymentsSetupSessionsListQuery, mapDashboardInstanceProviderDeploymentsSetupSessionsGetOutput, DashboardInstanceProviderDeploymentsSetupSessionsGetOutput, mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutput, DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput, mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBody, DashboardInstanceProviderDeploymentsSetupSessionsCreateBody, mapDashboardInstanceProviderDeploymentsSetupSessionsUpdateOutput, DashboardInstanceProviderDeploymentsSetupSessionsUpdateOutput, mapDashboardInstanceProviderDeploymentsSetupSessionsUpdateBody, DashboardInstanceProviderDeploymentsSetupSessionsUpdateBody, mapDashboardInstanceProviderDeploymentsSetupSessionsDeleteOutput, DashboardInstanceProviderDeploymentsSetupSessionsDeleteOutput

class MetorialManagementInstanceProviderDeploymentsSetupSessionsEndpoint(BaseMetorialEndpoint):
    """A setup session tracks an in-progress OAuth flow, storing state during the redirect. On success, it creates an auth config with the user's access token."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_auth_method_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, provider_auth_credentials_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderDeploymentsSetupSessionsListOutput:
        """
    List provider setup sessions
    Returns a paginated list of provider setup sessions.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_method_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_credentials_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProviderDeploymentsSetupSessionsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if provider_auth_credentials_id is not None:
            query_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-setup-sessions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsListOutput.from_dict)

    def get(self, instance_id: str, provider_setup_session_id: str) -> DashboardInstanceProviderDeploymentsSetupSessionsGetOutput:
        """
    Get provider setup session
    Retrieves a specific provider setup session by ID.

    :param instance_id: str
    :param provider_setup_session_id: str
    :return: DashboardInstanceProviderDeploymentsSetupSessionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-setup-sessions', provider_setup_session_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsGetOutput.from_dict)

    def create(self, instance_id: str, *, provider_id: str, provider_deployment_id: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, provider_auth_method_id: Optional[str] = None, provider_auth_credentials_id: Optional[str] = None, redirect_url: Optional[str] = None) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput:
        """
    Create provider setup session
    Creates a new provider setup session for OAuth authentication.

    :param instance_id: str
    :param provider_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_auth_method_id: Optional[str] (optional)
    :param provider_auth_credentials_id: Optional[str] (optional)
    :param redirect_url: Optional[str] (optional)
    :return: DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if provider_auth_method_id is not None:
            body_dict["provider_auth_method_id"] = provider_auth_method_id
        if provider_auth_credentials_id is not None:
            body_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if redirect_url is not None:
            body_dict["redirect_url"] = redirect_url

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-setup-sessions'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutput.from_dict)

    def update(self, instance_id: str, provider_setup_session_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsSetupSessionsUpdateOutput:
        """
    Update provider setup session
    Updates a specific provider setup session.

    :param instance_id: str
    :param provider_setup_session_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsSetupSessionsUpdateOutput
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
            path=['instances', instance_id, 'provider-setup-sessions', provider_setup_session_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsUpdateOutput.from_dict)

    def delete(self, instance_id: str, provider_setup_session_id: str) -> DashboardInstanceProviderDeploymentsSetupSessionsDeleteOutput:
        """
    Delete provider setup session
    Deletes a provider setup session.

    :param instance_id: str
    :param provider_setup_session_id: str
    :return: DashboardInstanceProviderDeploymentsSetupSessionsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-setup-sessions', provider_setup_session_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsDeleteOutput.from_dict)