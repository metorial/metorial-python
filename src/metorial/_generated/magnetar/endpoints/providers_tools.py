from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersToolsListOutput, DashboardInstanceProvidersToolsListOutput, mapDashboardInstanceProvidersToolsListQuery, DashboardInstanceProvidersToolsListQuery, mapDashboardInstanceProvidersToolsGetOutput, DashboardInstanceProvidersToolsGetOutput

class MetorialProvidersToolsEndpoint(BaseMetorialEndpoint):
    """A tool is a single action a provider can perform like 'search_issues' or 'send_message'. Tools are what AI agents call via MCP. By default, tools from the latest provider version are returned. Use the optional version filter to get tools for a specific version."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, provider_version_id: str, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProvidersToolsListOutput:
        """
    List provider tools
    Returns a paginated list of provider tools. By default returns tools from the latest version. Use optional filters to get tools for a specific version.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_version_id: str
    :return: DashboardInstanceProvidersToolsListOutput
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
            path=['providers-tools'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersToolsListOutput.from_dict)

    def get(self, provider_tool_id: str) -> DashboardInstanceProvidersToolsGetOutput:
        """
    Get provider tool
    Retrieves a specific provider tool by ID.

    :param provider_tool_id: str
    :return: DashboardInstanceProvidersToolsGetOutput
    """
        request = MetorialRequest(
            path=['providers-tools', provider_tool_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersToolsGetOutput.from_dict)