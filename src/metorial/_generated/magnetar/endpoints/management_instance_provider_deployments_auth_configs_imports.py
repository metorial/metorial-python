from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsListQuery, DashboardInstanceProviderDeploymentsAuthConfigsImportsListQuery, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsCreateBody, DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateBody, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput

class MetorialManagementInstanceProviderDeploymentsAuthConfigsImportsEndpoint(BaseMetorialEndpoint):
    """An auth import lets you bring in existing OAuth tokens or credentials from another system, so users don't need to re-authenticate to use Metorial."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, provider_deployment_id: str, provider_auth_config_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput:
        """
    List provider auth imports
    Returns a paginated list of provider auth imports.

    :param instance_id: str
    :param provider_deployment_id: str
    :param provider_auth_config_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput
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
            path=['instances', instance_id, 'provider-deployments', provider_deployment_id, 'auth-configs', provider_auth_config_id, 'imports'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput.from_dict)

    def get(self, instance_id: str, provider_deployment_id: str, provider_auth_config_id: str, provider_auth_import_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput:
        """
    Get provider auth import
    Retrieves a specific provider auth import by ID.

    :param instance_id: str
    :param provider_deployment_id: str
    :param provider_auth_config_id: str
    :param provider_auth_import_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-deployments', provider_deployment_id, 'auth-configs', provider_auth_config_id, 'imports', provider_auth_import_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput.from_dict)

    def create(self, instance_id: str, provider_deployment_id: str, provider_auth_config_id: str, *, note: str, value: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None, provider_auth_method_id: Optional[str] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput:
        """
    Create provider auth import
    Imports authentication credentials for a provider.

    :param instance_id: str
    :param provider_deployment_id: str
    :param provider_auth_config_id: str
    :param note: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param provider_auth_method_id: Optional[str] (optional)
    :param value: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["note"] = note
        if metadata is not None:
            body_dict["metadata"] = metadata
        if provider_auth_method_id is not None:
            body_dict["providerAuthMethodId"] = provider_auth_method_id
        body_dict["value"] = value

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-deployments', provider_deployment_id, 'auth-configs', provider_auth_config_id, 'imports'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput.from_dict)

    def get_schema(self, instance_id: str, provider_deployment_id: str, provider_auth_config_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
        """
    Get auth import schema
    Retrieves the JSON Schema for importing authentication credentials.

    :param instance_id: str
    :param provider_deployment_id: str
    :param provider_auth_config_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-deployments', provider_deployment_id, 'auth-configs', provider_auth_config_id, 'imports', 'schema']
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput.from_dict)
