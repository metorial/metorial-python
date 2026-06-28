from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsAuthConfigsExportsListOutput, DashboardInstanceProviderDeploymentsAuthConfigsExportsListOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsExportsListQuery, DashboardInstanceProviderDeploymentsAuthConfigsExportsListQuery, mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput, DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsExportsCreateOutput, DashboardInstanceProviderDeploymentsAuthConfigsExportsCreateOutput, mapDashboardInstanceProviderDeploymentsAuthConfigsExportsCreateBody, DashboardInstanceProviderDeploymentsAuthConfigsExportsCreateBody

class MetorialProviderDeploymentsAuthConfigsExportsEndpoint(BaseMetorialEndpoint):
    """An auth export lets you extract OAuth tokens or credentials from Metorial to use in other systems, avoiding duplicate authentication flows."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_auth_credentials_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsListOutput:
        """
    List provider auth exports
    Returns a paginated list of provider auth exports.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_credentials_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthConfigsExportsListOutput
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
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['provider-auth-config-exports'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsExportsListOutput.from_dict)

    def get(self, provider_auth_export_id: str) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput:
        """
    Get provider auth export
    Retrieves a specific provider auth export by ID.

    :param provider_auth_export_id: str
    :return: DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput
    """
        request = MetorialRequest(
            path=['provider-auth-config-exports', provider_auth_export_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput.from_dict)

    def create(self, *, provider_auth_config_id: str, note: str, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsCreateOutput:
        """
    Create provider auth export
    Exports authentication credentials from a provider.

    :param provider_auth_config_id: str
    :param note: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProviderDeploymentsAuthConfigsExportsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_auth_config_id"] = provider_auth_config_id
        body_dict["note"] = note
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['provider-auth-config-exports'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsAuthConfigsExportsCreateOutput.from_dict)