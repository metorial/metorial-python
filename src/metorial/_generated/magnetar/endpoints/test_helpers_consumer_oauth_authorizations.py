from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapTestHelpersConsumerOauthAuthorizationsCreateOutput, TestHelpersConsumerOauthAuthorizationsCreateOutput, mapTestHelpersConsumerOauthAuthorizationsCreateBody, TestHelpersConsumerOauthAuthorizationsCreateBody

class MetorialTestHelpersConsumerOauthAuthorizationsEndpoint(BaseMetorialEndpoint):
    """Helpers for testing consumer OAuth flows."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, *, instance_id: str, url: str, consumer_profile_id: str, magic_mcp_endpoint_id: str) -> TestHelpersConsumerOauthAuthorizationsCreateOutput:
        """
    Create consumer OAuth test authorization
    Creates a single-use test authorization token for a consumer OAuth authorize URL.

    :param instance_id: str
    :param url: str
    :param consumer_profile_id: str
    :param magic_mcp_endpoint_id: str
    :return: TestHelpersConsumerOauthAuthorizationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["instance_id"] = instance_id
        body_dict["url"] = url
        body_dict["consumer_profile_id"] = consumer_profile_id
        body_dict["magic_mcp_endpoint_id"] = magic_mcp_endpoint_id

        request = MetorialRequest(
            path=['test-helpers', 'consumer-oauth-authorizations'],
            body=body_dict
        )
        return self._post(request).transform(mapTestHelpersConsumerOauthAuthorizationsCreateOutput.from_dict)