from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersEnvironmentsListOutput, DashboardInstanceCustomProvidersEnvironmentsListOutput, mapDashboardInstanceCustomProvidersEnvironmentsListQuery, DashboardInstanceCustomProvidersEnvironmentsListQuery, mapDashboardInstanceCustomProvidersEnvironmentsGetOutput, DashboardInstanceCustomProvidersEnvironmentsGetOutput

class MetorialCustomProvidersEnvironmentsEndpoint(BaseMetorialEndpoint):
    """Environments represent deployment targets for custom provider versions (e.g., staging, production)."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, custom_provider_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, ids: Optional[Union[str, List[str]]] = None, custom_provider_version_ids: Optional[Union[str, List[str]]] = None) -> DashboardInstanceCustomProvidersEnvironmentsListOutput:
        """
    List custom provider environments
    Returns a paginated list of environments for a custom provider.

    :param custom_provider_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param ids: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_version_ids: Optional[Union[str, List[str]]] (optional)
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
        if ids is not None:
            query_dict["ids"] = ids
        if custom_provider_version_ids is not None:
            query_dict["custom_provider_version_ids"] = custom_provider_version_ids

        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'environments'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersEnvironmentsListOutput.from_dict)

    def get(self, custom_provider_id: str, custom_provider_environment_id: str) -> DashboardInstanceCustomProvidersEnvironmentsGetOutput:
        """
    Get custom provider environment
    Retrieves a specific environment.

    :param custom_provider_id: str
    :param custom_provider_environment_id: str
    :return: DashboardInstanceCustomProvidersEnvironmentsGetOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'environments', custom_provider_environment_id]
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersEnvironmentsGetOutput.from_dict)
