from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapTokenGetOutput, TokenGetOutput

class MetorialTokenEndpoint(BaseMetorialEndpoint):
    """Endpoint for retrieving metadata about the token used for authentication. This is useful for clients to understand the type and capabilities of the token they are using, especially since Metorial supports multiple token types with different permission models."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self) -> TokenGetOutput:
        """
    Get token details
    Retrieves metadata and configuration details for a specific token.


    :return: TokenGetOutput
    """
        request = MetorialRequest(
            path=['token']
        )
        return self._get(request).transform(mapTokenGetOutput.from_dict)