from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersEnvironmentsListOutput, DashboardInstanceCustomProvidersEnvironmentsListOutput, mapDashboardInstanceCustomProvidersEnvironmentsListQuery, DashboardInstanceCustomProvidersEnvironmentsListQuery, mapDashboardInstanceCustomProvidersEnvironmentsGetOutput, DashboardInstanceCustomProvidersEnvironmentsGetOutput

class MetorialManagementInstanceCustomProvidersEnvironmentsEndpoint(BaseMetorialEndpoint):
    """Environments represent deployment targets for custom provider versions (e.g., staging, production)."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, custom_provider_version_id: Optional[Union[str, List[str]]] = None, custom_provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCustomProvidersEnvironmentsListOutput:
        """
    List custom provider environments
    Returns a paginated list of environments for a custom provider.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_version_id: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCustomProvidersEnvironmentsListOutput
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
        if custom_provider_version_id is not None:
            query_dict["custom_provider_version_id"] = custom_provider_version_id
        if custom_provider_id is not None:
            query_dict["custom_provider_id"] = custom_provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'custom-provider-environments'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersEnvironmentsListOutput.from_dict)

    def get(self, instance_id: str, custom_provider_environment_id: str) -> DashboardInstanceCustomProvidersEnvironmentsGetOutput:
        """
    Get custom provider environment
    Retrieves a specific environment.

    :param instance_id: str
    :param custom_provider_environment_id: str
    :return: DashboardInstanceCustomProvidersEnvironmentsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'custom-provider-environments', custom_provider_environment_id]
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersEnvironmentsGetOutput.from_dict)