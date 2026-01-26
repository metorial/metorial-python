from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import (
  BaseMetorialEndpoint,
  MetorialEndpointManager,
  MetorialRequest,
)
from ..resources import (
  mapDashboardInstanceServerConfigVaultsListOutput,
  DashboardInstanceServerConfigVaultsListOutput,
  mapDashboardInstanceServerConfigVaultsListQuery,
  DashboardInstanceServerConfigVaultsListQuery,
  mapDashboardInstanceServerConfigVaultsGetOutput,
  DashboardInstanceServerConfigVaultsGetOutput,
  mapDashboardInstanceServerConfigVaultsCreateOutput,
  DashboardInstanceServerConfigVaultsCreateOutput,
  mapDashboardInstanceServerConfigVaultsCreateBody,
  DashboardInstanceServerConfigVaultsCreateBody,
  mapDashboardInstanceServerConfigVaultsUpdateOutput,
  DashboardInstanceServerConfigVaultsUpdateOutput,
  mapDashboardInstanceServerConfigVaultsUpdateBody,
  DashboardInstanceServerConfigVaultsUpdateBody,
)


class MetorialDashboardInstanceServerConfigVaultsEndpoint(BaseMetorialEndpoint):
  """Store reusable configuration data for MCP servers in a secure vault."""

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
    order: Optional[str] = None
  ) -> DashboardInstanceServerConfigVaultsListOutput:
    """
    List server runs
    List all server runs

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceServerConfigVaultsListOutput
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

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "server-config-vault"],
      query=query_dict,
    )
    return self._get(request).transform(
      mapDashboardInstanceServerConfigVaultsListOutput.from_dict
    )

  def get(
    self, instance_id: str, server_config_vault_id: str
  ) -> DashboardInstanceServerConfigVaultsGetOutput:
    """
    Get server run
    Get the information of a specific server run

    :param instance_id: str
    :param server_config_vault_id: str
    :return: DashboardInstanceServerConfigVaultsGetOutput
    """
    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instance_id,
        "server-config-vault",
        server_config_vault_id,
      ]
    )
    return self._get(request).transform(
      mapDashboardInstanceServerConfigVaultsGetOutput.from_dict
    )

  def create(
    self,
    instance_id: str,
    *,
    name: str,
    config: Dict[str, Any],
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceServerConfigVaultsCreateOutput:
    """
    Create server config vault
    Create a new server config vault

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param config: Dict[str, Any]
    :return: DashboardInstanceServerConfigVaultsCreateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata
    body_dict["config"] = config

    request = MetorialRequest(
      path=["dashboard", "instances", instance_id, "server-config-vault"],
      body=body_dict,
    )
    return self._post(request).transform(
      mapDashboardInstanceServerConfigVaultsCreateOutput.from_dict
    )

  def update(
    self,
    instance_id: str,
    server_config_vault_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None
  ) -> DashboardInstanceServerConfigVaultsUpdateOutput:
    """
    Update server config vault
    Update an existing server config vault

    :param instance_id: str
    :param server_config_vault_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceServerConfigVaultsUpdateOutput
    """
    # Build body parameters from keyword arguments
    body_dict = {}
    if name is not None:
      body_dict["name"] = name
    if description is not None:
      body_dict["description"] = description
    if metadata is not None:
      body_dict["metadata"] = metadata

    request = MetorialRequest(
      path=[
        "dashboard",
        "instances",
        instance_id,
        "server-config-vault",
        server_config_vault_id,
      ],
      body=body_dict,
    )
    return self._patch(request).transform(
      mapDashboardInstanceServerConfigVaultsUpdateOutput.from_dict
    )
