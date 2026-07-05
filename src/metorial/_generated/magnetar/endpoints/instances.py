from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapInstancesGetOutput, InstancesGetOutput, mapInstancesListOutput, InstancesListOutput

class MetorialInstancesEndpoint(BaseMetorialEndpoint):
    """Endpoints for listing and retrieving instances. An instance is an isolated environment within a Metorial project. Instances are created via the dashboard (since API keys are scoped to instances). Common setups include production, staging, and development instances."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str) -> InstancesGetOutput:
        """
    Get instance details
    Retrieves metadata and configuration details for a specific instance.

    :param instance_id: str
    :return: InstancesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id]
        )
        return self._get(request).transform(mapInstancesGetOutput.from_dict)

    def list(self) -> InstancesListOutput:
        """
    List instances
    Lists all instances within the organization that the authenticated actor has access to.


    :return: InstancesListOutput
    """
        request = MetorialRequest(
            path=['instances']
        )
        return self._get(request).transform(mapInstancesListOutput.from_dict)