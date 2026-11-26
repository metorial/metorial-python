from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapTokenGetOutput, TokenGetOutput

class MetorialTokenEndpoint(BaseMetorialEndpoint):
    """A token is the credential a request authenticates with. This resource describes the calling token’s type and scope."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> TokenGetOutput:
        """
    Get token
    Retrieves metadata about the calling token.


    :return: TokenGetOutput
    """
        request = MetorialRequest(
            path=['token']
        )
        return self._get(request).transform(mapTokenGetOutput.from_dict)