from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceCustomServersListingGetOutput,
  DashboardInstanceCustomServersListingGetOutput,
  mapDashboardInstanceCustomServersListingUpdateOutput,
  DashboardInstanceCustomServersListingUpdateOutput,
  mapDashboardInstanceCustomServersListingUpdateBody,
  DashboardInstanceCustomServersListingUpdateBody,
)


class MetorialManagementInstanceCustomServersListingEndpoint(BaseMetorialEndpoint):
  """Manager custom servers"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(
    self, instance_id: str, custom_server_id: str
  ) -> DashboardInstanceCustomServersListingGetOutput:
    """
    Get custom server listing
    Get a custom server listing

    :param instance_id: str
    :param custom_server_id: str
    :return: DashboardInstanceCustomServersListingGetOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers", custom_server_id, "listing"]
    )
    return self._get(request).transform(
      mapDashboardInstanceCustomServersListingGetOutput.from_dict
    )

  def update(
    self, instance_id: str, custom_server_id: str
  ) -> DashboardInstanceCustomServersListingUpdateOutput:
    """
    Update custom server listing
    Update a custom server listing

    :param instance_id: str
    :param custom_server_id: str
    :return: DashboardInstanceCustomServersListingUpdateOutput
    """
    request = MetorialRequest(
      path=["instances", instance_id, "custom-servers", custom_server_id, "listing"]
    )
    return self._patch(request).transform(
      mapDashboardInstanceCustomServersListingUpdateOutput.from_dict
    )
