from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsConfigVaultsListOutput, DashboardInstanceProviderDeploymentsConfigVaultsListOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsListQuery, DashboardInstanceProviderDeploymentsConfigVaultsListQuery, mapDashboardInstanceProviderDeploymentsConfigVaultsGetOutput, DashboardInstanceProviderDeploymentsConfigVaultsGetOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsCreateOutput, DashboardInstanceProviderDeploymentsConfigVaultsCreateOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsCreateBody, DashboardInstanceProviderDeploymentsConfigVaultsCreateBody, mapDashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput, DashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput, mapDashboardInstanceProviderDeploymentsConfigVaultsUpdateBody, DashboardInstanceProviderDeploymentsConfigVaultsUpdateBody, mapDashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput, DashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput

class MetorialProviderDeploymentsConfigVaultsEndpoint(BaseMetorialEndpoint):
    """A config vault is a saved, reusable set of configuration values. Use vaults to store credentials once and apply them to multiple deployments without re-entering."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, provider_deployment_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProviderDeploymentsConfigVaultsListOutput:
        """
    List provider config vaults
    Returns a paginated list of provider config vaults.

    :param provider_deployment_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
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

        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id, 'config-vaults'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsListOutput.from_dict)

    def get(self, provider_deployment_id: str, provider_config_vault_id: str) -> DashboardInstanceProviderDeploymentsConfigVaultsGetOutput:
        """
    Get provider config vault
    Retrieves a specific provider config vault by ID.

    :param provider_deployment_id: str
    :param provider_config_vault_id: str
    :return: DashboardInstanceProviderDeploymentsConfigVaultsGetOutput
    """
        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id, 'config-vaults', provider_config_vault_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsGetOutput.from_dict)

    def create(self, provider_deployment_id: str, *, name: str, data: Dict[str, Any], description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsConfigVaultsCreateOutput:
        """
    Create provider config vault
    Creates a new provider config vault.

    :param provider_deployment_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param data: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsConfigVaultsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["data"] = data

        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id, 'config-vaults'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsCreateOutput.from_dict)

    def update(self, provider_deployment_id: str, provider_config_vault_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput:
        """
    Update provider config vault
    Updates a specific provider config vault.

    :param provider_deployment_id: str
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
            path=['provider-deployments', provider_deployment_id, 'config-vaults', provider_config_vault_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsUpdateOutput.from_dict)

    def delete(self, provider_deployment_id: str, provider_config_vault_id: str) -> DashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput:
        """
    Delete provider config vault
    Permanently deletes a provider config vault.

    :param provider_deployment_id: str
    :param provider_config_vault_id: str
    :return: DashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput
    """
        request = MetorialRequest(
            path=['provider-deployments', provider_deployment_id, 'config-vaults', provider_config_vault_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderDeploymentsConfigVaultsDeleteOutput.from_dict)
