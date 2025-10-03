from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapProviderOauthDiscoverOutput,
  ProviderOauthDiscoverOutput,
  mapProviderOauthDiscoverBody,
  ProviderOauthDiscoverBody,
)


class MetorialProviderOauthEndpoint(BaseMetorialEndpoint):
  """Get OAuth connection template information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def discover(
    self, *, discovery_url: str, client_name: str
  ) -> ProviderOauthDiscoverOutput:
    """
    Discover OAuth Configuration
    Discover OAuth configuration from a discovery URL

    :param discovery_url: str
    :param client_name: str
    :return: ProviderOauthDiscoverOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["discovery_url"] = discovery_url
    body_dict["client_name"] = client_name

    request = MetorialRequest(path=["provider-oauth-discovery"], body=body_dict)
    return self._post(request).transform(mapProviderOauthDiscoverOutput.from_dict)
