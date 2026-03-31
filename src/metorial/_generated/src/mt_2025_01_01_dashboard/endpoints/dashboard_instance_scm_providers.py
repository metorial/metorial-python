from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceScmProvidersListOutput, DashboardInstanceScmProvidersListOutput, mapDashboardInstanceScmProvidersListQuery, DashboardInstanceScmProvidersListQuery, mapDashboardInstanceScmProvidersGetOutput, DashboardInstanceScmProvidersGetOutput, mapDashboardInstanceScmProvidersCreateOutput, DashboardInstanceScmProvidersCreateOutput, mapDashboardInstanceScmProvidersCreateBody, DashboardInstanceScmProvidersCreateBody

class MetorialDashboardInstanceScmProvidersEndpoint(BaseMetorialEndpoint):
    """Manage SCM providers configured for an instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceScmProvidersListOutput:
        """
    List SCM providers
    Returns a paginated list of SCM providers.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceScmProvidersListOutput
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
            path=['dashboard', 'instances', instance_id, 'scm', 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceScmProvidersListOutput.from_dict)

    def get(self, instance_id: str, scm_provider_id: str) -> DashboardInstanceScmProvidersGetOutput:
        """
    Get SCM provider
    Retrieves a specific SCM provider by ID.

    :param instance_id: str
    :param scm_provider_id: str
    :return: DashboardInstanceScmProvidersGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'scm', 'providers', scm_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceScmProvidersGetOutput.from_dict)

    def create(self, instance_id: str, *, type: str) -> DashboardInstanceScmProvidersCreateOutput:
        """
    Create SCM provider
    Initiates a setup session for a self-hosted SCM provider.

    :param instance_id: str
    :param type: str
    :return: DashboardInstanceScmProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["type"] = type

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'scm', 'providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceScmProvidersCreateOutput.from_dict)