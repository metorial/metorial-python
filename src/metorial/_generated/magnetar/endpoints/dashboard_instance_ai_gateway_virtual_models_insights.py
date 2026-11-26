from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutput, DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput, mapDashboardInstanceAiGatewayVirtualModelsInsightsGetQuery, DashboardInstanceAiGatewayVirtualModelsInsightsGetQuery

class MetorialDashboardInstanceAiGatewayVirtualModelsInsightsEndpoint(BaseMetorialEndpoint):
    """Virtual models are model names that pick a real model for every request, using rules, optional signals answered by a decision model, a default, and stickiness. Every change to the definition creates a new version."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, virtual_model_id: str, *, days: Optional[float] = None, baseline_model: Optional[str] = None) -> DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput:
        """
    Get AI gateway virtual model insights
    Summarizes how the virtual model routed requests over the last days: requests, failures, cost and latency per rule and model, decision model usage, and optionally the savings compared with sending everything to one model.

    :param instance_id: str
    :param virtual_model_id: str
    :param days: Optional[float] (optional)
    :param baseline_model: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if days is not None:
            query_dict["days"] = days
        if baseline_model is not None:
            query_dict["baseline_model"] = baseline_model

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'virtual-models', virtual_model_id, 'insights'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutput.from_dict)