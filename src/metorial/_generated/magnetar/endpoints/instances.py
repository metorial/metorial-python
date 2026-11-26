from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapInstancesGetOutput, InstancesGetOutput, mapInstancesListOutput, InstancesListOutput

class MetorialInstancesEndpoint(BaseMetorialEndpoint):
    """An instance is an isolated environment within a Metorial project. Only the instances you can access are listed."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str) -> InstancesGetOutput:
        """
    Get instance
    Retrieves an instance.

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
    Returns the instances in the organization that the caller can access.


    :return: InstancesListOutput
    """
        request = MetorialRequest(
            path=['instances']
        )
        return self._get(request).transform(mapInstancesListOutput.from_dict)