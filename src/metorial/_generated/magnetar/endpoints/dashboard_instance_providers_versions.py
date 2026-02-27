from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersVersionsListOutput, DashboardInstanceProvidersVersionsListOutput, mapDashboardInstanceProvidersVersionsListQuery, DashboardInstanceProvidersVersionsListQuery, mapDashboardInstanceProvidersVersionsGetOutput, DashboardInstanceProvidersVersionsGetOutput

class MetorialDashboardInstanceProvidersVersionsEndpoint(BaseMetorialEndpoint):
    """A version is a specific release of a provider (e.g., v1.2.0). Each version has its own tools, auth methods, and config schema. Deployments are pinned to a version for security reasons."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, provider_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProvidersVersionsListOutput:
        """
    List provider versions
    Returns a paginated list of provider versions.

    :param instance_id: str
    :param provider_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProvidersVersionsListOutput
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

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'providers', provider_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersVersionsListOutput.from_dict)

    def get(self, instance_id: str, provider_id: str, provider_version_id: str) -> DashboardInstanceProvidersVersionsGetOutput:
        """
    Get provider version
    Retrieves a specific provider version by ID.

    :param instance_id: str
    :param provider_id: str
    :param provider_version_id: str
    :return: DashboardInstanceProvidersVersionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'providers', provider_id, 'versions', provider_version_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersVersionsGetOutput.from_dict)
