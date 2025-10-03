from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceSecretsListOutput,
  DashboardInstanceSecretsListOutput,
  mapDashboardInstanceSecretsListQuery,
  DashboardInstanceSecretsListQuery,
  mapDashboardInstanceSecretsGetOutput,
  DashboardInstanceSecretsGetOutput,
)


class MetorialDashboardInstanceSecretsEndpoint(BaseMetorialEndpoint):
  """Secrets represent sensitive information securely stored by Metorial. Secrets are automatically created by Metorial, for example for server deployment configurations."""

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
    type: Optional[Union[str, List[str]]] = None,
    status: Optional[Union[str, List[str]]] = None
  ) -> DashboardInstanceSecretsListOutput:
    """
    List secrets
    Returns a paginated list of secrets for the instance, optionally filtered by type or status.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSecretsListOutput
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
    if type is not None:
      query_dict["type"] = type
    if status is not None:
      query_dict["status"] = status

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "secrets"], query=query_dict
    )
    return self._get(request).transform(mapDashboardInstanceSecretsListOutput.from_dict)

  def get(self, instance_id: str, secret_id: str) -> DashboardInstanceSecretsGetOutput:
    """
    Get secret by ID
    Retrieves detailed information about a specific secret by ID.

    :param instance_id: str
    :param secret_id: str
    :return: DashboardInstanceSecretsGetOutput
    """
    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "secrets", secret_id]
    )
    return self._get(request).transform(mapDashboardInstanceSecretsGetOutput.from_dict)
