from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationsInstancesProvidersListOutput, DashboardInstanceIntegrationsInstancesProvidersListOutput, mapDashboardInstanceIntegrationsInstancesProvidersListQuery, DashboardInstanceIntegrationsInstancesProvidersListQuery, mapDashboardInstanceIntegrationsInstancesProvidersGetOutput, DashboardInstanceIntegrationsInstancesProvidersGetOutput, mapDashboardInstanceIntegrationsInstancesProvidersSetOutput, DashboardInstanceIntegrationsInstancesProvidersSetOutput, mapDashboardInstanceIntegrationsInstancesProvidersSetBody, DashboardInstanceIntegrationsInstancesProvidersSetBody

class MetorialManagementInstanceIntegrationsInstancesProvidersEndpoint(BaseMetorialEndpoint):
    """Integration instance providers resolve the effective per-instance provider materialization for an integration."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, integration_instance_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, integration_provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, session_template_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstancesProvidersListOutput:
        """
    List integration instance providers
    Returns a paginated list of integration instance providers.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param integration_instance_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param integration_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstancesProvidersListOutput
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
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if integration_instance_id is not None:
            query_dict["integration_instance_id"] = integration_instance_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if integration_provider_id is not None:
            query_dict["integration_provider_id"] = integration_provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if session_template_id is not None:
            query_dict["session_template_id"] = session_template_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instance-providers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsInstancesProvidersListOutput.from_dict)

    def get(self, instance_id: str, integration_instance_provider_id: str) -> DashboardInstanceIntegrationsInstancesProvidersGetOutput:
        """
    Get integration instance provider
    Retrieves a specific integration instance provider.

    :param instance_id: str
    :param integration_instance_provider_id: str
    :return: DashboardInstanceIntegrationsInstancesProvidersGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instance-providers', integration_instance_provider_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsInstancesProvidersGetOutput.from_dict)

    def set(self, instance_id: str, integration_instance_id: str, provider_id: str, *, provider_deployment_id: Optional[str] = None, provider_config_id: Optional[str] = None, provider_auth_config_id: Optional[str] = None, tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] = None, is_override_tool_filter: Optional[bool] = None) -> DashboardInstanceIntegrationsInstancesProvidersSetOutput:
        """
    Set integration instance provider
    Creates or updates the effective integration instance provider materialization.

    :param instance_id: str
    :param integration_instance_id: str
    :param provider_id: str
    :param provider_deployment_id: Optional[str] (optional)
    :param provider_config_id: Optional[str] (optional)
    :param provider_auth_config_id: Optional[str] (optional)
    :param tool_filters: Optional[Union[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]], List[Union[Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]]]] (optional)
    :param is_override_tool_filter: Optional[bool] (optional)
    :return: DashboardInstanceIntegrationsInstancesProvidersSetOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if provider_deployment_id is not None:
            body_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            body_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            body_dict["provider_auth_config_id"] = provider_auth_config_id
        if tool_filters is not None:
            body_dict["tool_filters"] = tool_filters
        if is_override_tool_filter is not None:
            body_dict["is_override_tool_filter"] = is_override_tool_filter

        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instances', integration_instance_id, 'providers', provider_id],
            body=body_dict
        )
        return self._put(request).transform(mapDashboardInstanceIntegrationsInstancesProvidersSetOutput.from_dict)