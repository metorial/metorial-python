from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsListQuery, DashboardInstanceProviderDeploymentsAuthConfigsImportsListQuery, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsCreateBody, DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateBody, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput, DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery, DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaQuery

class MetorialProviderDeploymentsAuthConfigsImportsEndpoint(BaseMetorialEndpoint):
    """An auth import lets you bring in existing OAuth tokens or credentials from another system, so users don't need to re-authenticate to use Metorial."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_auth_credentials_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput:
        """
    List provider auth imports
    Returns a paginated list of provider auth imports.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_credentials_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
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
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_auth_credentials_id is not None:
            query_dict["provider_auth_credentials_id"] = provider_auth_credentials_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['provider-auth-config-imports'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsListOutput.from_dict)

    def get(self, provider_auth_import_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput:
        """
    Get provider auth import
    Retrieves a specific provider auth import by ID.

    :param provider_auth_import_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput
    """
        request = MetorialRequest(
            path=['provider-auth-config-imports', provider_auth_import_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetOutput.from_dict)

    def create(self, *, note: str, value: Dict[str, Any], provider_id: Optional[str] = None, provider_deployment_id: Optional[str] = None, provider_auth_config_id: Optional[str] = None, provider_auth_method_id: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput:
        """
    Create provider auth import
    Imports authentication credentials for a provider.

    :param provider_id: Optional[str] (optional)
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_auth_config_id: Optional[str] (optional)
    :param provider_auth_method_id: Optional[str] (optional)
    :param note: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param value: Dict[str, Any]
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if provider_id is not None:
            body_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_config_id is not None:
            body_dict["provider_auth_config_id"] = provider_auth_config_id
        if provider_auth_method_id is not None:
            body_dict["provider_auth_method_id"] = provider_auth_method_id
        body_dict["note"] = note
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["value"] = value

        request = MetorialRequest(
            path=['provider-auth-config-imports'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsCreateOutput.from_dict)

    def get_schema(self, *, provider_id: Optional[str] = None, provider_deployment_id: Optional[str] = None, provider_auth_config_id: Optional[str] = None, provider_auth_method_id: Optional[str] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
        """
    Get auth import schema
    Retrieves the JSON Schema for importing authentication credentials.

    :param provider_id: Optional[str] (optional)
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_auth_config_id: Optional[str] (optional)
    :param provider_auth_method_id: Optional[str] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if provider_auth_method_id is not None:
            query_dict["provider_auth_method_id"] = provider_auth_method_id

        request = MetorialRequest(
            path=['provider-auth-config-imports', 'schema'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput.from_dict)