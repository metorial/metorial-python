from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersTriggersListOutput, DashboardInstanceProvidersTriggersListOutput, mapDashboardInstanceProvidersTriggersListQuery, DashboardInstanceProvidersTriggersListQuery, mapDashboardInstanceProvidersTriggersGetOutput, DashboardInstanceProvidersTriggersGetOutput

class MetorialDashboardInstanceProvidersTriggersEndpoint(BaseMetorialEndpoint):
    """A provider trigger describes an event source a provider can emit for callbacks. Use triggers to discover which callback subscriptions a provider version supports."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, provider_version_id: str, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProvidersTriggersListOutput:
        """
    List provider triggers
    Returns a paginated list of provider triggers for a specific provider version.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_version_id: str
    :return: DashboardInstanceProvidersTriggersListOutput
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
        query_dict["provider_version_id"] = provider_version_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-triggers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersTriggersListOutput.from_dict)

    def get(self, instance_id: str, provider_trigger_id: str) -> DashboardInstanceProvidersTriggersGetOutput:
        """
    Get provider trigger
    Retrieves a specific provider trigger by ID.

    :param instance_id: str
    :param provider_trigger_id: str
    :return: DashboardInstanceProvidersTriggersGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-triggers', provider_trigger_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersTriggersGetOutput.from_dict)