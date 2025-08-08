from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapProviderOauthDiscoverOutput, ProviderOauthDiscoverOutput, mapProviderOauthDiscoverBody, ProviderOauthDiscoverBody

class MetorialProviderOauthEndpoint(BaseMetorialEndpoint):
    """Get OAuth connection template information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def discover(self, body: ProviderOauthDiscoverBody):
        """
    Discover OAuth Configuration
    Discover OAuth configuration from a discovery URL

    :param body: ProviderOauthDiscoverBody
    :return: ProviderOauthDiscoverOutput
    """
        request = MetorialRequest(
            path=['provider-oauth-discovery'],
            body=mapProviderOauthDiscoverBody.to_dict(body),
        )
        return self._post(request).transform(mapProviderOauthDiscoverOutput.from_dict)