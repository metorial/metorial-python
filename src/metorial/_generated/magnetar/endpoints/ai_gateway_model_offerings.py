from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayModelOfferingsListOutput, DashboardInstanceAiGatewayModelOfferingsListOutput, mapDashboardInstanceAiGatewayModelOfferingsListQuery, DashboardInstanceAiGatewayModelOfferingsListQuery

class MetorialAiGatewayModelOfferingsEndpoint(BaseMetorialEndpoint):
    """How each provider serves a model: its id for the model, pricing, limits and capabilities."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, model_id: Optional[str] = None, provider: Optional[str] = None) -> DashboardInstanceAiGatewayModelOfferingsListOutput:
        """
    List AI gateway model offerings
    Returns a paginated list of the offerings in the catalog that are not retired.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param model_id: Optional[str] (optional)
    :param provider: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayModelOfferingsListOutput
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
        if model_id is not None:
            query_dict["model_id"] = model_id
        if provider is not None:
            query_dict["provider"] = provider

        request = MetorialRequest(
            path=['ai-gateway', 'model-offerings'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayModelOfferingsListOutput.from_dict)