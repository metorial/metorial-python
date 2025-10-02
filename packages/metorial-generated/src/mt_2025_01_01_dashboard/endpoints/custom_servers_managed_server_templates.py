from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapCustomServersManagedServerTemplatesListOutput,
  CustomServersManagedServerTemplatesListOutput,
  mapCustomServersManagedServerTemplatesListQuery,
  CustomServersManagedServerTemplatesListQuery,
  mapCustomServersManagedServerTemplatesGetOutput,
  CustomServersManagedServerTemplatesGetOutput,
)


class MetorialCustomServersManagedServerTemplatesEndpoint(BaseMetorialEndpoint):
  """Get managed server template information"""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    organizationId: str,
    query: CustomServersManagedServerTemplatesListQuery = None,
  ) -> CustomServersManagedServerTemplatesListOutput:
    """
    List oauth connection templates
    List all oauth connection templates

    :param organizationId: str
    :param query: CustomServersManagedServerTemplatesListQuery
    :return: CustomServersManagedServerTemplatesListOutput
    """
    request = MetorialRequest(
      path=["dashboard", "organizations", organizationId, "managed-server-templates"],
      query=mapCustomServersManagedServerTemplatesListQuery.to_dict(query)
      if query is not None
      else None,
    )
    return self._get(request).transform(
      mapCustomServersManagedServerTemplatesListOutput.from_dict
    )

  def get(
    self, organizationId: str, managedServerId: str
  ) -> CustomServersManagedServerTemplatesGetOutput:
    """
    Get oauth connection template
    Get the information of a specific oauth connection template

    :param organizationId: str
    :param managedServerId: str
    :return: CustomServersManagedServerTemplatesGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "organizations",
        organizationId,
        "managed-server-templates",
        managedServerId,
      ]
    )
    return self._get(request).transform(
      mapCustomServersManagedServerTemplatesGetOutput.from_dict
    )
