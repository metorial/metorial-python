from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersSpecificationsListOutput, DashboardInstanceProvidersSpecificationsListOutput, mapDashboardInstanceProvidersSpecificationsListQuery, DashboardInstanceProvidersSpecificationsListQuery, mapDashboardInstanceProvidersSpecificationsGetOutput, DashboardInstanceProvidersSpecificationsGetOutput

class MetorialManagementInstanceProvidersSpecificationsEndpoint(BaseMetorialEndpoint):
    """A specification defines what a provider version can do: its tools, auth methods, and required configuration fields."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, provider_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProvidersSpecificationsListOutput:
        """
    List provider specifications
    Returns a paginated list of provider specifications.

    :param instance_id: str
    :param provider_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProvidersSpecificationsListOutput
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
            path=['instances', instance_id, 'providers', provider_id, 'specifications'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersSpecificationsListOutput.from_dict)

    def get(self, instance_id: str, provider_id: str, provider_specification_id: str) -> DashboardInstanceProvidersSpecificationsGetOutput:
        """
    Get provider specification
    Retrieves a specific provider specification by ID.

    :param instance_id: str
    :param provider_id: str
    :param provider_specification_id: str
    :return: DashboardInstanceProvidersSpecificationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'providers', provider_id, 'specifications', provider_specification_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersSpecificationsGetOutput.from_dict)
