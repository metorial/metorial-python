from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayRoutingPreviewOutput, DashboardInstanceAiGatewayRoutingPreviewOutput, mapDashboardInstanceAiGatewayRoutingPreviewBody, DashboardInstanceAiGatewayRoutingPreviewBody

class MetorialManagementInstanceAiGatewayRoutingEndpoint(BaseMetorialEndpoint):
    """Shows how the AI gateway routes requests for a model on this instance, without sending one."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def preview(self, instance_id: str, *, model: str, required_features: Optional[List[str]] = None) -> DashboardInstanceAiGatewayRoutingPreviewOutput:
        """
    Preview AI gateway routing
    Returns the providers a request for the model would be sent to, in the order they are tried, with their pricing. Tokens' allowed models are not applied.

    :param instance_id: str
    :param model: str
    :param required_features: Optional[List[str]] (optional)
    :return: DashboardInstanceAiGatewayRoutingPreviewOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["model"] = model
        if required_features is not None:
            body_dict["required_features"] = required_features

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'routing', 'preview'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayRoutingPreviewOutput.from_dict)