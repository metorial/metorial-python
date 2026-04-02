from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapApiKeysRotateOutput, ApiKeysRotateOutput, mapApiKeysRotateBody, ApiKeysRotateBody, mapApiKeysRevealOutput, ApiKeysRevealOutput

class MetorialApiKeysEndpoint(BaseMetorialEndpoint):
    """Read and write API key information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def rotate(self, organization_id: str, api_key_id: str, *, current_expires_at: Optional[datetime] = None) -> ApiKeysRotateOutput:
        """
    Rotate API key
    Rotate a specific API key

    :param organization_id: str
    :param api_key_id: str
    :param current_expires_at: Optional[datetime] (optional)
    :return: ApiKeysRotateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if current_expires_at is not None:
            body_dict["current_expires_at"] = current_expires_at

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id, 'rotate'],
            body=body_dict
        )
        return self._post(request).transform(mapApiKeysRotateOutput.from_dict)

    def reveal(self, organization_id: str, api_key_id: str) -> ApiKeysRevealOutput:
        """
    Reveal API key
    Reveal a specific API key

    :param organization_id: str
    :param api_key_id: str
    :return: ApiKeysRevealOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'api-keys', api_key_id, 'reveal']
        )
        return self._post(request).transform(mapApiKeysRevealOutput.from_dict)