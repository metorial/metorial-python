from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayConfigGetOutput, DashboardInstanceAiGatewayConfigGetOutput, mapDashboardInstanceAiGatewayConfigUpdateOutput, DashboardInstanceAiGatewayConfigUpdateOutput, mapDashboardInstanceAiGatewayConfigUpdateBody, DashboardInstanceAiGatewayConfigUpdateBody

class MetorialAiGatewayConfigEndpoint(BaseMetorialEndpoint):
    """Settings, limits and log retention for every request made through the AI gateway in this instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> DashboardInstanceAiGatewayConfigGetOutput:
        """
    Get AI gateway configuration
    Retrieves the instance's AI gateway settings and limits, along with the limits and restrictions of your plan.


    :return: DashboardInstanceAiGatewayConfigGetOutput
    """
        request = MetorialRequest(
            path=['ai-gateway', 'config']
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayConfigGetOutput.from_dict)

    def update(self, *, log_retention_days: Optional[float] = None, settings: Optional[Dict[str, Any]] = None, limits: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceAiGatewayConfigUpdateOutput:
        """
    Update AI gateway configuration
    Updates the log retention, settings or limits. Fields you omit keep their current value.

    :param log_retention_days: Optional[float] (optional)
    :param settings: Optional[Dict[str, Any]] (optional)
    :param limits: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceAiGatewayConfigUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if log_retention_days is not None:
            body_dict["log_retention_days"] = log_retention_days
        if settings is not None:
            body_dict["settings"] = settings
        if limits is not None:
            body_dict["limits"] = limits

        request = MetorialRequest(
            path=['ai-gateway', 'config'],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceAiGatewayConfigUpdateOutput.from_dict)