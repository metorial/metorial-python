from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServersCapabilitiesListOutput,
  DashboardInstanceServersCapabilitiesListOutput,
  mapDashboardInstanceServersCapabilitiesListQuery,
  DashboardInstanceServersCapabilitiesListQuery,
)


class MetorialDashboardInstanceServersCapabilitiesEndpoint(BaseMetorialEndpoint):
  """Describes the capabilities, i.e., the tools, resources, and prompts, that certain servers support."""

  def __init__(self, config: MetorialEndpointManager):
    super().__init__(config)

  def list(
    self,
    instance_id: str,
    *,
    limit: Optional[float] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
    cursor: Optional[str] = None,
    order: Optional[str] = None,
    server_deployment_id: Optional[Union[str, List[str]]] = None,
    server_variant_id: Optional[Union[str, List[str]]] = None,
    server_id: Optional[Union[str, List[str]]] = None,
    server_version_id: Optional[Union[str, List[str]]] = None,
    server_implementation_id: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceServersCapabilitiesListOutput:
    """
    List server capabilities
    Returns a list of server capabilities, filterable by server attributes such as deployment, variant, or version.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param server_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param server_variant_id: Optional[Union[str, List[str]]] (optional)
    :param server_id: Optional[Union[str, List[str]]] (optional)
    :param server_version_id: Optional[Union[str, List[str]]] (optional)
    :param server_implementation_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceServersCapabilitiesListOutput
    """
    # Build query parameters from keyword arguments
    query_dict = {}
    if limit is not None:
      query_dict["limit"] = limit
    if after is not None:
      query_dict["after"] = after
    if before is not None:
      query_dict["before"] = before
    if cursor is not None:
      query_dict["cursor"] = cursor
    if order is not None:
      query_dict["order"] = order
    if server_deployment_id is not None:
      query_dict["server_deployment_id"] = server_deployment_id
    if server_variant_id is not None:
      query_dict["server_variant_id"] = server_variant_id
    if server_id is not None:
      query_dict["server_id"] = server_id
    if server_version_id is not None:
      query_dict["server_version_id"] = server_version_id
    if server_implementation_id is not None:
      query_dict["server_implementation_id"] = server_implementation_id

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "server-capabilities"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceServersCapabilitiesListOutput.from_dict
    )
