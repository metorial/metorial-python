from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapManagementOrganizationGetOutput,
  ManagementOrganizationGetOutput,
  mapManagementOrganizationUpdateOutput,
  ManagementOrganizationUpdateOutput,
  mapManagementOrganizationUpdateBody,
  ManagementOrganizationUpdateBody,
)


class MetorialManagementOrganizationEndpoint(BaseMetorialEndpoint):
  """Read and write organization information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(self) -> ManagementOrganizationGetOutput:
    """
    Get organization
    Get the current organization information


    :return: ManagementOrganizationGetOutput
    """
    request = MetorialRequest(path=["organization"])
    return self._get(request).transform(mapManagementOrganizationGetOutput.from_dict)

  def update(self, *, name: Optional[str] = None) -> ManagementOrganizationUpdateOutput:
    """
    Update organization
    Update the current organization information

    :param name: Optional[str] (optional)
    :return: ManagementOrganizationUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name

    request = MetorialRequest(path=["organization"], body=body_dict)
    return self._patch(request).transform(
      mapManagementOrganizationUpdateOutput.from_dict
    )
