from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutput, DashboardInstanceAiGatewayVirtualModelTemplatesListOutput

class MetorialAiGatewayVirtualModelTemplatesEndpoint(BaseMetorialEndpoint):
    """Ready-made virtual model definitions for common routing setups. Pick the models they ask for to create a virtual model from one."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self) -> DashboardInstanceAiGatewayVirtualModelTemplatesListOutput:
        """
    List AI gateway virtual model templates
    Returns every template. The list is not paginated.


    :return: DashboardInstanceAiGatewayVirtualModelTemplatesListOutput
    """
        request = MetorialRequest(
            path=['ai-gateway', 'virtual-model-templates']
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutput.from_dict)