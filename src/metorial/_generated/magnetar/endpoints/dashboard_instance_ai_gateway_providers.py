from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayProvidersListOutput, DashboardInstanceAiGatewayProvidersListOutput, mapDashboardInstanceAiGatewayProvidersListQuery, DashboardInstanceAiGatewayProvidersListQuery

class MetorialDashboardInstanceAiGatewayProvidersEndpoint(BaseMetorialEndpoint):
    """The providers that serve models in the AI gateway catalog, e.g. OpenAI, Amazon Bedrock or OpenRouter."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceAiGatewayProvidersListOutput:
        """
    List AI gateway providers
    Returns a paginated list of the providers in the catalog, including whether you can connect your own account for each.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayProvidersListOutput
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
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayProvidersListOutput.from_dict)