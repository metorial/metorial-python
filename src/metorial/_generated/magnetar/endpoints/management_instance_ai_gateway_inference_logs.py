from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayInferenceLogsListOutput, DashboardInstanceAiGatewayInferenceLogsListOutput, mapDashboardInstanceAiGatewayInferenceLogsListQuery, DashboardInstanceAiGatewayInferenceLogsListQuery, mapDashboardInstanceAiGatewayInferenceLogsGetOutput, DashboardInstanceAiGatewayInferenceLogsGetOutput, mapDashboardInstanceAiGatewayInferenceLogsGetQuery, DashboardInstanceAiGatewayInferenceLogsGetQuery

class MetorialManagementInstanceAiGatewayInferenceLogsEndpoint(BaseMetorialEndpoint):
    """A record of every request made through the AI gateway: the model and provider used, tokens, cost, timing and errors. Kept for the configured log retention."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, token_id: Optional[str] = None, consumer_id: Optional[str] = None, model: Optional[str] = None, virtual_model_id: Optional[str] = None, status: Optional[str] = None) -> DashboardInstanceAiGatewayInferenceLogsListOutput:
        """
    List AI gateway inference logs
    Returns inference logs, newest first, without request and response content. Pages only go towards older logs: pass the after cursor of the previous page. before cursors are rejected.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param token_id: Optional[str] (optional)
    :param consumer_id: Optional[str] (optional)
    :param model: Optional[str] (optional)
    :param virtual_model_id: Optional[str] (optional)
    :param status: Optional[str] (optional)
    :return: DashboardInstanceAiGatewayInferenceLogsListOutput
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
        if token_id is not None:
            query_dict["token_id"] = token_id
        if consumer_id is not None:
            query_dict["consumer_id"] = consumer_id
        if model is not None:
            query_dict["model"] = model
        if virtual_model_id is not None:
            query_dict["virtual_model_id"] = virtual_model_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'inference-logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayInferenceLogsListOutput.from_dict)

    def get(self, instance_id: str, inference_log_id: str, *, include_content: Optional[bool] = None) -> DashboardInstanceAiGatewayInferenceLogsGetOutput:
        """
    Get AI gateway inference log
    Retrieves an inference log by ID. Request and response content is only returned when include_content is set.

    :param instance_id: str
    :param inference_log_id: str
    :param include_content: Optional[bool] (optional)
    :return: DashboardInstanceAiGatewayInferenceLogsGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if include_content is not None:
            query_dict["include_content"] = include_content

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'inference-logs', inference_log_id],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayInferenceLogsGetOutput.from_dict)