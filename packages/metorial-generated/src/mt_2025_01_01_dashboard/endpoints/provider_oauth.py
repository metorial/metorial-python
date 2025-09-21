from typing import Optional, Dict, Any, List, Union
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
    self, organizationId: str, *, discovery_url: Optional[str] = None
  ) -> ProviderOauthDiscoverOutput:
    """
    Discover OAuth Configuration
    Discover OAuth configuration from a discovery URL

    :param organizationId: str
    :param discovery_url: str (optional)
    :return: ProviderOauthDiscoverOutput
    """
    _params = {"discovery_url": discovery_url}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "provider-oauth-discovery"],
      body=body,
    )
    return self._post(request).transform(mapProviderOauthDiscoverOutput.from_dict)
