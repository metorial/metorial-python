from typing import Optional, Dict, Any, List, Union
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

    :param name: str (optional)
    :return: ManagementOrganizationUpdateOutput
    """
    _params = {"name": name}
    body = {k: v for k, v in _params.items() if v is not None}

    if not body:
      raise ValueError("No fields to update. At least one parameter must be provided.")

    request = MetorialRequest(
      path=["organization"],
      body=body,
    )
    return self._patch(request).transform(
      mapManagementOrganizationUpdateOutput.from_dict
    )
