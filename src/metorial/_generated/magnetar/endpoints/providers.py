from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersListOutput, DashboardInstanceProvidersListOutput, mapDashboardInstanceProvidersListQuery, DashboardInstanceProvidersListQuery, mapDashboardInstanceProvidersGetOutput, DashboardInstanceProvidersGetOutput

class MetorialProvidersEndpoint(BaseMetorialEndpoint):
    """A provider is a read-only template for an MCP server integration (like GitHub or Slack). To use a provider, create a deployment from it."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProvidersListOutput:
        """
    List providers
    Returns a paginated list of providers.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProvidersListOutput
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

        request = MetorialRequest(
            path=['providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersListOutput.from_dict)

    def get(self, provider_id: str) -> DashboardInstanceProvidersGetOutput:
        """
    Get provider
    Retrieves a specific provider by ID.

    :param provider_id: str
    :return: DashboardInstanceProvidersGetOutput
    """
        request = MetorialRequest(
            path=['providers', provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersGetOutput.from_dict)