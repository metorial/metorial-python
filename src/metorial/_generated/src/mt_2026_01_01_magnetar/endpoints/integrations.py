from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationsListOutput, DashboardInstanceIntegrationsListOutput, mapDashboardInstanceIntegrationsListQuery, DashboardInstanceIntegrationsListQuery, mapDashboardInstanceIntegrationsGetOutput, DashboardInstanceIntegrationsGetOutput, mapDashboardInstanceIntegrationsCreateOutput, DashboardInstanceIntegrationsCreateOutput, mapDashboardInstanceIntegrationsCreateBody, DashboardInstanceIntegrationsCreateBody, mapDashboardInstanceIntegrationsUpdateOutput, DashboardInstanceIntegrationsUpdateOutput, mapDashboardInstanceIntegrationsUpdateBody, DashboardInstanceIntegrationsUpdateBody, mapDashboardInstanceIntegrationsDeleteOutput, DashboardInstanceIntegrationsDeleteOutput

class MetorialIntegrationsEndpoint(BaseMetorialEndpoint):
    """Integrations define reusable provider contracts that can then be materialized into integration instances."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, integration_provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsListOutput:
        """
    List integrations
    Returns a paginated list of integrations.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param integration_provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if integration_provider_id is not None:
            query_dict["integration_provider_id"] = integration_provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['integrations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsListOutput.from_dict)

    def get(self, integration_id: str) -> DashboardInstanceIntegrationsGetOutput:
        """
    Get integration
    Retrieves a specific integration.

    :param integration_id: str
    :return: DashboardInstanceIntegrationsGetOutput
    """
        request = MetorialRequest(
            path=['integrations', integration_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsGetOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, use_integration_name_in_tool_names: Optional[bool] = None, can_attach_custom_tool_filters: Optional[bool] = None, can_attach_custom_provider_config: Optional[bool] = None, can_override_tool_filters: Optional[bool] = None) -> DashboardInstanceIntegrationsCreateOutput:
        """
    Create integration
    Creates a new integration.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param use_integration_name_in_tool_names: Optional[bool] (optional)
    :param can_attach_custom_tool_filters: Optional[bool] (optional)
    :param can_attach_custom_provider_config: Optional[bool] (optional)
    :param can_override_tool_filters: Optional[bool] (optional)
    :return: DashboardInstanceIntegrationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if use_integration_name_in_tool_names is not None:
            body_dict["use_integration_name_in_tool_names"] = use_integration_name_in_tool_names
        if can_attach_custom_tool_filters is not None:
            body_dict["can_attach_custom_tool_filters"] = can_attach_custom_tool_filters
        if can_attach_custom_provider_config is not None:
            body_dict["can_attach_custom_provider_config"] = can_attach_custom_provider_config
        if can_override_tool_filters is not None:
            body_dict["can_override_tool_filters"] = can_override_tool_filters

        request = MetorialRequest(
            path=['integrations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsCreateOutput.from_dict)

    def update(self, integration_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, use_integration_name_in_tool_names: Optional[bool] = None, can_attach_custom_tool_filters: Optional[bool] = None, can_attach_custom_provider_config: Optional[bool] = None, can_override_tool_filters: Optional[bool] = None) -> DashboardInstanceIntegrationsUpdateOutput:
        """
    Update integration
    Updates a specific integration.

    :param integration_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param use_integration_name_in_tool_names: Optional[bool] (optional)
    :param can_attach_custom_tool_filters: Optional[bool] (optional)
    :param can_attach_custom_provider_config: Optional[bool] (optional)
    :param can_override_tool_filters: Optional[bool] (optional)
    :return: DashboardInstanceIntegrationsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if use_integration_name_in_tool_names is not None:
            body_dict["use_integration_name_in_tool_names"] = use_integration_name_in_tool_names
        if can_attach_custom_tool_filters is not None:
            body_dict["can_attach_custom_tool_filters"] = can_attach_custom_tool_filters
        if can_attach_custom_provider_config is not None:
            body_dict["can_attach_custom_provider_config"] = can_attach_custom_provider_config
        if can_override_tool_filters is not None:
            body_dict["can_override_tool_filters"] = can_override_tool_filters

        request = MetorialRequest(
            path=['integrations', integration_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIntegrationsUpdateOutput.from_dict)

    def delete(self, integration_id: str) -> DashboardInstanceIntegrationsDeleteOutput:
        """
    Delete integration
    Archives a specific integration.

    :param integration_id: str
    :return: DashboardInstanceIntegrationsDeleteOutput
    """
        request = MetorialRequest(
            path=['integrations', integration_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIntegrationsDeleteOutput.from_dict)