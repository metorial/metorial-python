from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsConfigVaultsListOutput, DashboardInstanceProviderDeploymentsConfigVaultsListOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsListQuery, DashboardInstanceProviderDeploymentsConfigVaultsListQuery, mapDashboardInstanceProviderDeploymentsConfigVaultsGetOutput, DashboardInstanceProviderDeploymentsConfigVaultsGetOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsCreateOutput, DashboardInstanceProviderDeploymentsConfigVaultsCreateOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsCreateBody, DashboardInstanceProviderDeploymentsConfigVaultsCreateBody, mapDashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput, DashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsUpdateBody, DashboardInstanceProviderDeploymentsConfigVaultsUpdateBody, mapDashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput, DashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput

class MetorialDashboardInstanceProviderDeploymentsConfigVaultsEndpoint(BaseMetorialEndpoint):
    """A config vault is a saved, reusable set of configuration values. Use vaults to store credentials once and apply them to multiple deployments without re-entering."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_config_vault_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstanceProviderDeploymentsConfigVaultsListOutput:
        """
    List provider config vaults
    Returns a paginated list of provider config vaults.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_vault_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceProviderDeploymentsConfigVaultsListOutput
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
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_config_vault_id is not None:
            query_dict["provider_config_vault_id"] = provider_config_vault_id
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-config-vaults'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsListOutput.from_dict)

    def get(self, instance_id: str, provider_config_vault_id: str) -> DashboardInstanceProviderDeploymentsConfigVaultsGetOutput:
        """
    Get provider config vault
    Retrieves a specific provider config vault by ID.

    :param instance_id: str
    :param provider_config_vault_id: str
    :return: DashboardInstanceProviderDeploymentsConfigVaultsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-config-vaults', provider_config_vault_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsGetOutput.from_dict)

    def create(self, instance_id: str, *, provider_id: str, name: str, value: Dict[str, Any], provider_deployment_id: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsConfigVaultsCreateOutput:
        """
    Create provider config vault
    Creates a new provider config vault.

    :param instance_id: str
    :param provider_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param value: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsConfigVaultsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["value"] = value

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-config-vaults'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsCreateOutput.from_dict)

    def update(self, instance_id: str, provider_config_vault_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput:
        """
    Update provider config vault
    Updates a specific provider config vault.

    :param instance_id: str
    :param provider_config_vault_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput
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
            path=['dashboard', 'instances', instance_id, 'provider-config-vaults', provider_config_vault_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput.from_dict)

    def delete(self, instance_id: str, provider_config_vault_id: str) -> DashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput:
        """
    Delete provider config vault
    Permanently deletes a provider config vault.

    :param instance_id: str
    :param provider_config_vault_id: str
    :return: DashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'provider-config-vaults', provider_config_vault_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput.from_dict)