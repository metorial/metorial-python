from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthCredentialsListOutput, DashboardInstanceProviderDeploymentsAuthCredentialsListOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsListQuery, DashboardInstanceProviderDeploymentsAuthCredentialsListQuery, mapDashboardInstanceProviderDeploymentsAuthCredentialsGetOutput, DashboardInstanceProviderDeploymentsAuthCredentialsGetOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput, DashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsCreateBody, DashboardInstanceProviderDeploymentsAuthCredentialsCreateBody, mapDashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput, DashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput, mapDashboardInstanceProviderDeploymentsAuthCredentialsUpdateBody, DashboardInstanceProviderDeploymentsAuthCredentialsUpdateBody, mapDashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput, DashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput

class MetorialDashboardInstanceProviderDeploymentsAuthCredentialsEndpoint(BaseMetorialEndpoint):
    """Auth credentials store your OAuth app registration (client ID, client secret, and scopes). These are the app-level credentials you get from a service like GitHub or Slack."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderDeploymentsAuthCredentialsListOutput:
        """
    List provider auth credentials
    Returns a paginated list of provider auth credentials.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
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

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-credentials'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsListOutput.from_dict)

    def get(self, instance_id: str, provider_auth_credentials_id: str) -> DashboardInstanceProviderDeploymentsAuthCredentialsGetOutput:
        """
    Get provider auth credentials
    Retrieves specific provider auth credentials by ID.

    :param instance_id: str
    :param provider_auth_credentials_id: str
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-credentials', provider_auth_credentials_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsGetOutput.from_dict)

    def create(self, instance_id: str, *, provider_id: str, name: str, config: Dict[str, Any], description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput:
        """
    Create provider auth credentials
    Creates new provider auth credentials.

    :param instance_id: str
    :param provider_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param config: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_id"] = provider_id
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["config"] = config

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-credentials'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsCreateOutput.from_dict)

    def update(self, instance_id: str, provider_auth_credentials_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput:
        """
    Update provider auth credentials
    Updates specific provider auth credentials.

    :param instance_id: str
    :param provider_auth_credentials_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
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

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-credentials', provider_auth_credentials_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsUpdateOutput.from_dict)

    def delete(self, instance_id: str, provider_auth_credentials_id: str) -> DashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput:
        """
    Delete provider auth credentials
    Permanently deletes provider auth credentials.

    :param instance_id: str
    :param provider_auth_credentials_id: str
    :return: DashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-auth-credentials', provider_auth_credentials_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsAuthCredentialsDeleteOutput.from_dict)
