from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersListOutput, DashboardInstanceProvidersListOutput, mapDashboardInstanceProvidersListQuery, DashboardInstanceProvidersListQuery, mapDashboardInstanceProvidersGetOutput, DashboardInstanceProvidersGetOutput, mapDashboardInstanceProvidersUpdateOutput, DashboardInstanceProvidersUpdateOutput, mapDashboardInstanceProvidersUpdateBody, DashboardInstanceProvidersUpdateBody

class MetorialManagementInstanceProvidersEndpoint(BaseMetorialEndpoint):
    """A provider is a read-only template for an MCP server integration (like GitHub or Slack). To use a provider, create a deployment from it."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, publisher_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProvidersListOutput:
        """
    List providers
    Returns a paginated list of providers.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param publisher_id: Optional[Union[str, List[str]]] (optional)
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
        if publisher_id is not None:
            query_dict["publisher_id"] = publisher_id

        request = MetorialRequest(
            path=['instances', instance_id, 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersListOutput.from_dict)

    def get(self, instance_id: str, provider_id: str) -> DashboardInstanceProvidersGetOutput:
        """
    Get provider
    Retrieves a specific provider by ID.

    :param instance_id: str
    :param provider_id: str
    :return: DashboardInstanceProvidersGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'providers', provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersGetOutput.from_dict)

    def update(self, instance_id: str, provider_id: str, *, name: Optional[str] = None, description: Optional[str] = None, slug: Optional[str] = None, image: Optional[str] = None, skills: Optional[List[str]] = None) -> DashboardInstanceProvidersUpdateOutput:
        """
    Update provider
    Updates a provider.

    :param instance_id: str
    :param provider_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param slug: Optional[str] (optional)
    :param image: Optional[str] (optional)
    :param skills: Optional[List[str]] (optional)
    :return: DashboardInstanceProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if slug is not None:
            body_dict["slug"] = slug
        if image is not None:
            body_dict["image"] = image
        if skills is not None:
            body_dict["skills"] = skills

        request = MetorialRequest(
            path=['instances', instance_id, 'providers', provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProvidersUpdateOutput.from_dict)
