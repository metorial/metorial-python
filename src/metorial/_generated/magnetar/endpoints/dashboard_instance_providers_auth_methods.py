from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersAuthMethodsListOutput, DashboardInstanceProvidersAuthMethodsListOutput, mapDashboardInstanceProvidersAuthMethodsListQuery, DashboardInstanceProvidersAuthMethodsListQuery, mapDashboardInstanceProvidersAuthMethodsGetOutput, DashboardInstanceProvidersAuthMethodsGetOutput

class MetorialDashboardInstanceProvidersAuthMethodsEndpoint(BaseMetorialEndpoint):
    """An auth method defines one way to authenticate with a provider (OAuth, API token, or custom credentials). A provider version may support multiple auth methods."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, provider_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, provider_version_id: Optional[str] = None) -> DashboardInstanceProvidersAuthMethodsListOutput:
        """
    List provider auth methods
    Returns a paginated list of provider auth methods.

    :param instance_id: str
    :param provider_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_version_id: Optional[str] (optional)
    :return: DashboardInstanceProvidersAuthMethodsListOutput
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
        if provider_version_id is not None:
            query_dict["provider_version_id"] = provider_version_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'providers', provider_id, 'auth-methods'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersAuthMethodsListOutput.from_dict)

    def get(self, instance_id: str, provider_id: str, provider_auth_method_id: str) -> DashboardInstanceProvidersAuthMethodsGetOutput:
        """
    Get provider auth method
    Retrieves a specific provider auth method by ID.

    :param instance_id: str
    :param provider_id: str
    :param provider_auth_method_id: str
    :return: DashboardInstanceProvidersAuthMethodsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'providers', provider_id, 'auth-methods', provider_auth_method_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersAuthMethodsGetOutput.from_dict)
