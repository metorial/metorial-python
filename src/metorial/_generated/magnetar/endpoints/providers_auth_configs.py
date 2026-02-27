from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersAuthConfigsListOutput, DashboardInstanceProvidersAuthConfigsListOutput, mapDashboardInstanceProvidersAuthConfigsListQuery, DashboardInstanceProvidersAuthConfigsListQuery

class MetorialProvidersAuthConfigsEndpoint(BaseMetorialEndpoint):
    """List auth configs scoped to a provider, optionally filtered by deployment."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_auth_method_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProvidersAuthConfigsListOutput:
        """
    List provider auth configs
    Returns a paginated list of auth configs, optionally filtered by provider and deployment IDs.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_method_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProvidersAuthConfigsListOutput
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
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id

        request = MetorialRequest(
            path=['providers', 'auth-configs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersAuthConfigsListOutput.from_dict)
