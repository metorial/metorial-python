from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersListOutput, DashboardInstanceCustomProvidersListOutput, mapDashboardInstanceCustomProvidersListQuery, DashboardInstanceCustomProvidersListQuery, mapDashboardInstanceCustomProvidersGetOutput, DashboardInstanceCustomProvidersGetOutput, mapDashboardInstanceCustomProvidersGetEnvOutput, DashboardInstanceCustomProvidersGetEnvOutput, mapDashboardInstanceCustomProvidersCreateOutput, DashboardInstanceCustomProvidersCreateOutput, mapDashboardInstanceCustomProvidersCreateBody, DashboardInstanceCustomProvidersCreateBody, mapDashboardInstanceCustomProvidersUpdateOutput, DashboardInstanceCustomProvidersUpdateOutput, mapDashboardInstanceCustomProvidersUpdateBody, DashboardInstanceCustomProvidersUpdateBody, mapDashboardInstanceCustomProvidersArchiveOutput, DashboardInstanceCustomProvidersArchiveOutput

class MetorialCustomProvidersEndpoint(BaseMetorialEndpoint):
    """Custom providers allow you to deploy your own MCP servers. Create providers from container images, remote URLs, or serverless functions."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCustomProvidersListOutput:
        """
    List custom providers
    Returns a paginated list of custom providers.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCustomProvidersListOutput
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
        if type is not None:
            query_dict["type"] = type
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['custom-providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersListOutput.from_dict)

    def get(self, custom_provider_id: str) -> DashboardInstanceCustomProvidersGetOutput:
        """
    Get custom provider
    Retrieves a specific custom provider by ID.

    :param custom_provider_id: str
    :return: DashboardInstanceCustomProvidersGetOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersGetOutput.from_dict)

    def get_env(self, custom_provider_id: str) -> DashboardInstanceCustomProvidersGetEnvOutput:
        """
    Get custom provider environment
    Retrieves the environment variables for a specific custom provider by ID.

    :param custom_provider_id: str
    :return: DashboardInstanceCustomProvidersGetEnvOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'env']
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersGetEnvOutput.from_dict)

    def create(self, *, name: str, from_: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, config: Optional[Dict[str, Any]] = None) -> DashboardInstanceCustomProvidersCreateOutput:
        """
    Create custom provider
    Creates a new custom provider.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param from_: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]
    :param config: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCustomProvidersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["from"] = from_
        if config is not None:
            body_dict["config"] = config

        request = MetorialRequest(
            path=['custom-providers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCustomProvidersCreateOutput.from_dict)

    def update(self, custom_provider_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, readme: Optional[str] = None) -> DashboardInstanceCustomProvidersUpdateOutput:
        """
    Update custom provider
    Updates a specific custom provider.

    :param custom_provider_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param readme: Optional[str] (optional)
    :return: DashboardInstanceCustomProvidersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if readme is not None:
            body_dict["readme"] = readme

        request = MetorialRequest(
            path=['custom-providers', custom_provider_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceCustomProvidersUpdateOutput.from_dict)

    def archive(self, custom_provider_id: str) -> DashboardInstanceCustomProvidersArchiveOutput:
        """
    Archive custom provider
    Archives a specific custom provider and disables new connections to it.

    :param custom_provider_id: str
    :return: DashboardInstanceCustomProvidersArchiveOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'archive']
        )
        return self._post(request).transform(mapDashboardInstanceCustomProvidersArchiveOutput.from_dict)