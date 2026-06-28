from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerConsumerInternalOauthAuthorizationsGetOutput, ConsumerConsumerInternalOauthAuthorizationsGetOutput, mapConsumerConsumerInternalOauthAuthorizationsAcceptOutput, ConsumerConsumerInternalOauthAuthorizationsAcceptOutput, mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput, ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput, mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody, ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody, mapConsumerConsumerInternalOauthAuthorizationsRejectOutput, ConsumerConsumerInternalOauthAuthorizationsRejectOutput

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

    def connect_magic_mcp_endpoint(self, portal_auth_attempt_id: str, *, magic_mcp_endpoint_id: str) -> ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput:
        """
    Connect portal OAuth authorization to magic MCP endpoint
    Links a pending portal OAuth authorization request to a consumer-owned magic MCP endpoint.

    :param portal_auth_attempt_id: str
    :param magic_mcp_endpoint_id: str
    :return: ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["magic_mcp_endpoint_id"] = magic_mcp_endpoint_id

        request = MetorialRequest(
            path=['consumer', 'portal-oauth-attempts', portal_auth_attempt_id, 'connect-magic-mcp-endpoint'],
            body=body_dict
        )
        return self._post(request).transform(mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput.from_dict)

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