from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthCredentialsListOutput, DashboardInstanceProviderDeploymentsAuthCredentialsListOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsListQuery, DashboardInstanceProviderDeploymentsAuthCredentialsListQuery, mapDashboardInstanceProviderDeploymentsAuthCredentialsGetOutput, DashboardInstanceProviderDeploymentsAuthCredentialsGetOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput, DashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsCreateBody, DashboardInstanceProviderDeploymentsAuthCredentialsCreateBody, mapDashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput, DashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsUpdateBody, DashboardInstanceProviderDeploymentsAuthCredentialsUpdateBody, mapDashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput, DashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput

class MetorialProviderDeploymentsAuthCredentialsEndpoint(BaseMetorialEndpoint):
    """Auth credentials store your OAuth app registration (client ID, client secret, and scopes). These are the app-level credentials you get from a service like GitHub or Slack."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_auth_method_id: Optional[Union[str, List[str]]] = None, origin: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthCredentialsListOutput:
        """
    List provider auth credentials
    Returns a paginated list of provider auth credentials.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_method_id: Optional[Union[str, List[str]]] (optional)
    :param origin: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsListOutput
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
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id
        if origin is not None:
            query_dict["origin"] = origin
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['provider-auth-credentials'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsListOutput.from_dict)

    def get(self, provider_auth_credentials_id: str) -> DashboardInstanceProviderDeploymentsAuthCredentialsGetOutput:
        """
    Get provider auth credentials
    Retrieves specific provider auth credentials by ID.

    :param provider_auth_credentials_id: str
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsGetOutput
    """
        request = MetorialRequest(
            path=['provider-auth-credentials', provider_auth_credentials_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsGetOutput.from_dict)

    def create(self, *, provider_id: str, config: Dict[str, Any], name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput:
        """
    Create provider auth credentials
    Creates new provider auth credentials.

    :param provider_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param config: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_id"] = provider_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["config"] = config

        request = MetorialRequest(
            path=['provider-auth-credentials'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput.from_dict)

    def update(self, provider_auth_credentials_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, client_id: Optional[str] = None, client_secret: Optional[str] = None, scopes: Optional[List[str]] = None) -> DashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput:
        """
    Update provider auth credentials
    Updates specific provider auth credentials.

    :param provider_auth_credentials_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param client_id: Optional[str] (optional)
    :param client_secret: Optional[str] (optional)
    :param scopes: Optional[List[str]] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if client_id is not None:
            body_dict["client_id"] = client_id
        if client_secret is not None:
            body_dict["client_secret"] = client_secret
        if scopes is not None:
            body_dict["scopes"] = scopes

        request = MetorialRequest(
            path=['provider-auth-credentials', provider_auth_credentials_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput.from_dict)

    def delete(self, provider_auth_credentials_id: str) -> DashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput:
        """
    Delete provider auth credentials
    Permanently deletes provider auth credentials.

    :param provider_auth_credentials_id: str
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput
    """
        request = MetorialRequest(
            path=['provider-auth-credentials', provider_auth_credentials_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput.from_dict)