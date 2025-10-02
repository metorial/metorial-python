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

  def get(self, organizationId: str) -> OrganizationsProfileGetOutput:
    """
    Get own profile
    Get the profile for the current organization

    :param organizationId: str
    :return: OrganizationsProfileGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "profile"]
    )
    return self._get(request).transform(mapOrganizationsProfileGetOutput.from_dict)

  def update(
    self, organizationId: str, body: OrganizationsProfileUpdateBody
  ) -> OrganizationsProfileUpdateOutput:
    """
    Update own profile
    Update the profile for the current organization

    :param organizationId: str
    :param body: OrganizationsProfileUpdateBody
    :return: OrganizationsProfileUpdateOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "profile"],
      body=mapOrganizationsProfileUpdateBody.to_dict(body),
    )
    return self._patch(request).transform(mapOrganizationsProfileUpdateOutput.from_dict)
