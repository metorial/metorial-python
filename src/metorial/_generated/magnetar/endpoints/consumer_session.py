from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerSessionGetOutput, ConsumerSessionGetOutput, mapConsumerSessionLogoutOutput, ConsumerSessionLogoutOutput

class MetorialConsumerSessionEndpoint(BaseMetorialEndpoint):
    """Inspect the authenticated consumer session and profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> ConsumerSessionGetOutput:
        """
    Get consumer session
    Returns the authenticated consumer session.


    :return: ConsumerSessionGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'session']
        )
        return self._post(request).transform(mapConsumerSessionGetOutput.from_dict)

    def logout(self) -> ConsumerSessionLogoutOutput:
        """
    Logout consumer session
    Revokes the authenticated consumer session.


    :return: ConsumerSessionLogoutOutput
    """
        request = MetorialRequest(
            path=['consumer', 'session', 'logout']
        )
        return self._post(request).transform(mapConsumerSessionLogoutOutput.from_dict)