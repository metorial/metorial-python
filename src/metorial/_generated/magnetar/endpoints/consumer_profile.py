from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerProfileGetOutput, ConsumerProfileGetOutput

class MetorialConsumerProfileEndpoint(BaseMetorialEndpoint):
    """Inspect the authenticated consumer session and profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> ConsumerProfileGetOutput:
        """
    Get consumer profile
    Returns the authenticated consumer profile.


    :return: ConsumerProfileGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'profile']
        )
        return self._post(request).transform(mapConsumerProfileGetOutput.from_dict)