from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerConsumerInternalOauthClientsGetOutput, ConsumerConsumerInternalOauthClientsGetOutput

class MetorialConsumerConsumerInternalOauthClientsEndpoint(BaseMetorialEndpoint):
    """Browse and configure portal providers from the consumer side."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, portal_auth_client_id: str) -> ConsumerConsumerInternalOauthClientsGetOutput:
        """
    Get portal OAuth client
    Returns one portal OAuth client visible to the current portal consumer.

    :param portal_auth_client_id: str
    :return: ConsumerConsumerInternalOauthClientsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'portal-oauth-clients', portal_auth_client_id]
        )
        return self._get(request).transform(mapConsumerConsumerInternalOauthClientsGetOutput.from_dict)