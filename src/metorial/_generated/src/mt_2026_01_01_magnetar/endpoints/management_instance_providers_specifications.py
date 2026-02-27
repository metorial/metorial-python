from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProvidersSpecificationsListOutput, DashboardInstanceProvidersSpecificationsListOutput, mapDashboardInstanceProvidersSpecificationsListQuery, DashboardInstanceProvidersSpecificationsListQuery, mapDashboardInstanceProvidersSpecificationsGetOutput, DashboardInstanceProvidersSpecificationsGetOutput

class MetorialManagementInstanceProvidersSpecificationsEndpoint(BaseMetorialEndpoint):
    """A specification defines what a provider version can do: its tools, auth methods, and required configuration fields."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_version_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProvidersSpecificationsListOutput:
        """
    List provider specifications
    Returns a paginated list of provider specifications.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_version_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
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
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_version_id is not None:
            query_dict["provider_version_id"] = provider_version_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-specifications'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProvidersSpecificationsListOutput.from_dict)

    def get(self, instance_id: str, provider_specification_id: str) -> DashboardInstanceProvidersSpecificationsGetOutput:
        """
    Get provider specification
    Retrieves a specific provider specification by ID.

    :param instance_id: str
    :param provider_specification_id: str
    :return: DashboardInstanceProvidersSpecificationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-specifications', provider_specification_id]
        )
        return self._get(request).transform(mapDashboardInstanceProvidersSpecificationsGetOutput.from_dict)
