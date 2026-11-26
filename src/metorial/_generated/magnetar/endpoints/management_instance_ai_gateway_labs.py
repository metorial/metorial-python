from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayLabsListOutput, DashboardInstanceAiGatewayLabsListOutput, mapDashboardInstanceAiGatewayLabsListQuery, DashboardInstanceAiGatewayLabsListQuery

class MetorialManagementInstanceAiGatewayLabsEndpoint(BaseMetorialEndpoint):
    """The labs that make the models in the AI gateway catalog, e.g. Anthropic or OpenAI."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceAiGatewayLabsListOutput:
        """
    List AI gateway labs
    Returns a paginated list of the labs in the catalog.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayLabsListOutput
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
            path=['instances', instance_id, 'ai-gateway', 'labs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayLabsListOutput.from_dict)