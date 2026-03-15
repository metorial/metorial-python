from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersVersionsListOutput, DashboardInstanceCustomProvidersVersionsListOutput, mapDashboardInstanceCustomProvidersVersionsListQuery, DashboardInstanceCustomProvidersVersionsListQuery, mapDashboardInstanceCustomProvidersVersionsGetOutput, DashboardInstanceCustomProvidersVersionsGetOutput, mapDashboardInstanceCustomProvidersVersionsCreateOutput, DashboardInstanceCustomProvidersVersionsCreateOutput, mapDashboardInstanceCustomProvidersVersionsCreateBody, DashboardInstanceCustomProvidersVersionsCreateBody

class MetorialDashboardInstanceCustomProvidersVersionsEndpoint(BaseMetorialEndpoint):
    """Versions represent different releases of a custom provider. Each version can be deployed to environments."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_version_id: Optional[Union[str, List[str]]] = None, custom_provider_id: Optional[Union[str, List[str]]] = None, custom_provider_deployment_id: Optional[Union[str, List[str]]] = None, custom_provider_environment_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceCustomProvidersVersionsListOutput:
        """
    List custom provider versions
    Returns a paginated list of versions for a custom provider.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_version_id: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_id: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_environment_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCustomProvidersVersionsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_version_id is not None:
            query_dict["provider_version_id"] = provider_version_id
        if custom_provider_id is not None:
            query_dict["custom_provider_id"] = custom_provider_id
        if custom_provider_deployment_id is not None:
            query_dict["custom_provider_deployment_id"] = custom_provider_deployment_id
        if custom_provider_environment_id is not None:
            query_dict["custom_provider_environment_id"] = custom_provider_environment_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'custom-provider-versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersVersionsListOutput.from_dict)

    def get(self, instance_id: str, custom_provider_version_id: str) -> DashboardInstanceCustomProvidersVersionsGetOutput:
        """
    Get custom provider version
    Retrieves a specific version of a custom provider.

    :param instance_id: str
    :param custom_provider_version_id: str
    :return: DashboardInstanceCustomProvidersVersionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'custom-provider-versions', custom_provider_version_id]
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersVersionsGetOutput.from_dict)

    def create(self, instance_id: str, *, custom_provider_id: str, from_: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], config: Optional[Dict[str, Any]] = None) -> DashboardInstanceCustomProvidersVersionsCreateOutput:
        """
    Create custom provider version
    Creates a new version for a custom provider.

    :param instance_id: str
    :param custom_provider_id: str
    :param from_: Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]
    :param config: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCustomProvidersVersionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["custom_provider_id"] = custom_provider_id
        body_dict["from"] = from_
        if config is not None:
            body_dict["config"] = config

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'custom-provider-versions'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCustomProvidersVersionsCreateOutput.from_dict)