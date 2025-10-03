from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardBootOutput,
  DashboardBootOutput,
  mapDashboardBootBody,
  DashboardBootBody,
)


class MetorialDashboardEndpoint(BaseMetorialEndpoint):
  """Boot user"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def boot(self) -> DashboardBootOutput:
    """
    Create organization
    Create a new organization


    :return: DashboardBootOutput
    """
    request = MetorialRequest(path=["dashboard", "boot"])
    return self._post(request).transform(mapDashboardBootOutput.from_dict)
