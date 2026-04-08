from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerConsumerInternalOauthAuthorizationsGetOutput, ConsumerConsumerInternalOauthAuthorizationsGetOutput, mapConsumerConsumerInternalOauthAuthorizationsAcceptOutput, ConsumerConsumerInternalOauthAuthorizationsAcceptOutput, mapConsumerConsumerInternalOauthAuthorizationsRejectOutput, ConsumerConsumerInternalOauthAuthorizationsRejectOutput

class MetorialConsumerConsumerInternalOauthAuthorizationsEndpoint(BaseMetorialEndpoint):
    """Browse and configure portal providers from the consumer side."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, portal_auth_attempt_id: str) -> ConsumerConsumerInternalOauthAuthorizationsGetOutput:
        """
    Get portal OAuth authorization
    Returns the current portal OAuth authorization request for the active consumer.

    :param portal_auth_attempt_id: str
    :return: ConsumerConsumerInternalOauthAuthorizationsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'portal-oauth-attempts', portal_auth_attempt_id]
        )
        return self._get(request).transform(mapConsumerConsumerInternalOauthAuthorizationsGetOutput.from_dict)

    def accept(self, portal_auth_attempt_id: str) -> ConsumerConsumerInternalOauthAuthorizationsAcceptOutput:
        """
    Accept portal OAuth authorization
    Approves a pending portal OAuth authorization request and returns the redirect URL.

    :param portal_auth_attempt_id: str
    :return: ConsumerConsumerInternalOauthAuthorizationsAcceptOutput
    """
        request = MetorialRequest(
            path=['consumer', 'portal-oauth-attempts', portal_auth_attempt_id, 'accept']
        )
        return self._post(request).transform(mapConsumerConsumerInternalOauthAuthorizationsAcceptOutput.from_dict)

    def reject(self, portal_auth_attempt_id: str) -> ConsumerConsumerInternalOauthAuthorizationsRejectOutput:
        """
    Reject portal OAuth authorization
    Rejects a pending portal OAuth authorization request and returns the redirect URL.

    :param portal_auth_attempt_id: str
    :return: ConsumerConsumerInternalOauthAuthorizationsRejectOutput
    """
        request = MetorialRequest(
            path=['consumer', 'portal-oauth-attempts', portal_auth_attempt_id, 'reject']
        )
        return self._post(request).transform(mapConsumerConsumerInternalOauthAuthorizationsRejectOutput.from_dict)