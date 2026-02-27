from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCustomProvidersDeploymentsListOutput, DashboardInstanceCustomProvidersDeploymentsListOutput, mapDashboardInstanceCustomProvidersDeploymentsListQuery, DashboardInstanceCustomProvidersDeploymentsListQuery, mapDashboardInstanceCustomProvidersDeploymentsGetOutput, DashboardInstanceCustomProvidersDeploymentsGetOutput, mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutput, DashboardInstanceCustomProvidersDeploymentsGetLogsOutput

class MetorialCustomProvidersDeploymentsEndpoint(BaseMetorialEndpoint):
    """Deployments track the build and deployment process of custom provider versions. View deployment status and logs."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, custom_provider_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, ids: Optional[Union[str, List[str]]] = None, custom_provider_version_ids: Optional[Union[str, List[str]]] = None) -> DashboardInstanceCustomProvidersDeploymentsListOutput:
        """
    List custom provider deployments
    Returns a paginated list of deployments for a custom provider.

    :param custom_provider_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param ids: Optional[Union[str, List[str]]] (optional)
    :param custom_provider_version_ids: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCustomProvidersDeploymentsListOutput
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
        if ids is not None:
            query_dict["ids"] = ids
        if custom_provider_version_ids is not None:
            query_dict["custom_provider_version_ids"] = custom_provider_version_ids

        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'deployments'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersDeploymentsListOutput.from_dict)

    def get(self, custom_provider_id: str, custom_provider_deployment_id: str) -> DashboardInstanceCustomProvidersDeploymentsGetOutput:
        """
    Get custom provider deployment
    Retrieves a specific deployment.

    :param custom_provider_id: str
    :param custom_provider_deployment_id: str
    :return: DashboardInstanceCustomProvidersDeploymentsGetOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'deployments', custom_provider_deployment_id]
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersDeploymentsGetOutput.from_dict)

    def get_logs(self, custom_provider_id: str, custom_provider_deployment_id: str) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutput:
        """
    Get deployment logs
    Retrieves the build and deployment logs for a deployment.

    :param custom_provider_id: str
    :param custom_provider_deployment_id: str
    :return: DashboardInstanceCustomProvidersDeploymentsGetLogsOutput
    """
        request = MetorialRequest(
            path=['custom-providers', custom_provider_id, 'deployments', custom_provider_deployment_id, 'logs']
        )
        return self._get(request).transform(mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutput.from_dict)
