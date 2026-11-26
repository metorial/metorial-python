from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayVirtualModelsVersionsListOutput, DashboardInstanceAiGatewayVirtualModelsVersionsListOutput, mapDashboardInstanceAiGatewayVirtualModelsVersionsListQuery, DashboardInstanceAiGatewayVirtualModelsVersionsListQuery, mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutput, DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput

class MetorialManagementInstanceAiGatewayVirtualModelsVersionsEndpoint(BaseMetorialEndpoint):
    """Every change to the definition of a virtual model is kept as a numbered version that can be rolled back to."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, virtual_model_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceAiGatewayVirtualModelsVersionsListOutput:
        """
    List AI gateway virtual model versions
    Returns a paginated list of the versions of a virtual model.

    :param instance_id: str
    :param virtual_model_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsVersionsListOutput
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
            path=['instances', instance_id, 'ai-gateway', 'virtual-models', virtual_model_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayVirtualModelsVersionsListOutput.from_dict)

    def get(self, instance_id: str, virtual_model_id: str, version_id: str) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput:
        """
    Get AI gateway virtual model version
    Retrieves a version of a virtual model by ID, with its definition.

    :param instance_id: str
    :param virtual_model_id: str
    :param version_id: str
    :return: DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'virtual-models', virtual_model_id, 'versions', version_id]
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutput.from_dict)