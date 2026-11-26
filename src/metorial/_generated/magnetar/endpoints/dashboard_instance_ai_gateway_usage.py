from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayUsageTimelineOutput, DashboardInstanceAiGatewayUsageTimelineOutput, mapDashboardInstanceAiGatewayUsageTimelineQuery, DashboardInstanceAiGatewayUsageTimelineQuery

class MetorialDashboardInstanceAiGatewayUsageEndpoint(BaseMetorialEndpoint):
    """Requests, tokens and cost of the AI gateway over time. Built from inference logs, so it covers the configured log retention."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def timeline(self, instance_id: str, *, from_: datetime, to: datetime, interval: Optional[str] = None, token_id: Optional[str] = None, consumer_id: Optional[str] = None, model: Optional[str] = None, virtual_model_id: Optional[str] = None) -> DashboardInstanceAiGatewayUsageTimelineOutput:
        """
    Get AI gateway usage timeline
    Returns usage in fixed-width buckets aligned to UTC, oldest first. A range can span at most 1500 buckets.

    :param instance_id: str
    :param from_: datetime
    :param to: datetime
    :param interval: Optional[str] (optional)
    :param token_id: Optional[str] (optional)
    :param consumer_id: Optional[str] (optional)
    :param model: Optional[str] (optional)
    :param virtual_model_id: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayUsageTimelineOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        query_dict["from"] = from_
        query_dict["to"] = to
        if interval is not None:
            query_dict["interval"] = interval
        if token_id is not None:
            query_dict["token_id"] = token_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if model is not None:
            query_dict["model"] = model
        if virtual_model_id is not None:
            query_dict["virtual_model_id"] = virtual_model_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'ai-gateway', 'usage', 'timeline'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayUsageTimelineOutput.from_dict)