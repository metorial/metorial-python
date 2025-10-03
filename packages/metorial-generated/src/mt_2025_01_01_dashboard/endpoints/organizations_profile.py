from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapOrganizationsProfileGetOutput,
  OrganizationsProfileGetOutput,
  mapOrganizationsProfileUpdateOutput,
  OrganizationsProfileUpdateOutput,
  mapOrganizationsProfileUpdateBody,
  OrganizationsProfileUpdateBody,
)


class MetorialOrganizationsProfileEndpoint(BaseMetorialEndpoint):
  """Get and manage profile information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def get(self, organization_id: str) -> OrganizationsProfileGetOutput:
    """
    Get own profile
    Get the profile for the current organization

    :param organization_id: str
    :return: OrganizationsProfileGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "profile"]
    )
    return self._get(request).transform(mapOrganizationsProfileGetOutput.from_dict)

  def update(
    self,
    organization_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None
  ) -> OrganizationsProfileUpdateOutput:
    """
    Update own profile
    Update the profile for the current organization

    :param organization_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: OrganizationsProfileUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description

    request = MetorialRequest(
      path=["dashboard", "organizations", organization_id, "profile"], body=body_dict
    )
    return self._patch(request).transform(mapOrganizationsProfileUpdateOutput.from_dict)
