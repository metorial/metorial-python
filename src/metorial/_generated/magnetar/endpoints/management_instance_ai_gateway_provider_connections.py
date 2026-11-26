from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAiGatewayProviderConnectionsListOutput, DashboardInstanceAiGatewayProviderConnectionsListOutput, mapDashboardInstanceAiGatewayProviderConnectionsListQuery, DashboardInstanceAiGatewayProviderConnectionsListQuery, mapDashboardInstanceAiGatewayProviderConnectionsGetOutput, DashboardInstanceAiGatewayProviderConnectionsGetOutput, mapDashboardInstanceAiGatewayProviderConnectionsCreateOutput, DashboardInstanceAiGatewayProviderConnectionsCreateOutput, mapDashboardInstanceAiGatewayProviderConnectionsCreateBody, DashboardInstanceAiGatewayProviderConnectionsCreateBody, mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutput, DashboardInstanceAiGatewayProviderConnectionsUpdateOutput, mapDashboardInstanceAiGatewayProviderConnectionsUpdateBody, DashboardInstanceAiGatewayProviderConnectionsUpdateBody, mapDashboardInstanceAiGatewayProviderConnectionsDeleteOutput, DashboardInstanceAiGatewayProviderConnectionsDeleteOutput, mapDashboardInstanceAiGatewayProviderConnectionsCheckOutput, DashboardInstanceAiGatewayProviderConnectionsCheckOutput, mapDashboardInstanceAiGatewayProviderConnectionsEnableOutput, DashboardInstanceAiGatewayProviderConnectionsEnableOutput, mapDashboardInstanceAiGatewayProviderConnectionsDisableOutput, DashboardInstanceAiGatewayProviderConnectionsDisableOutput

class MetorialManagementInstanceAiGatewayProviderConnectionsEndpoint(BaseMetorialEndpoint):
    """Your own credentials for an upstream provider such as OpenAI or Anthropic. The gateway routes requests through them, so the provider bills you directly."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, provider: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceAiGatewayProviderConnectionsListOutput:
        """
    List AI gateway provider connections
    Returns a paginated list of provider connections. Deleted connections are not included.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceAiGatewayProviderConnectionsListOutput
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
        if provider is not None:
            query_dict["provider"] = provider
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsListOutput.from_dict)

    def get(self, instance_id: str, connection_id: str) -> DashboardInstanceAiGatewayProviderConnectionsGetOutput:
        """
    Get AI gateway provider connection
    Retrieves a provider connection by ID. The credentials are never returned.

    :param instance_id: str
    :param connection_id: str
    :return: DashboardInstanceAiGatewayProviderConnectionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections', connection_id]
        )
        return self._get(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsGetOutput.from_dict)

    def create(self, instance_id: str, *, provider: str, name: str, credentials: Dict[str, str], description: Optional[str] = None, priority: Optional[float] = None, config: Optional[Dict[str, Union[str, float, bool]]] = None, features: Optional[Dict[str, Any]] = None, pricing_override: Optional[Dict[str, Any]] = None) -> DashboardInstanceAiGatewayProviderConnectionsCreateOutput:
        """
    Create AI gateway provider connection
    Connects a provider with your own credentials. The credentials are checked with the provider first, and the request fails if the provider rejects them.

    :param instance_id: str
    :param provider: str
    :param name: str
    :param description: Optional[str] (optional)
    :param priority: Optional[float] (optional)
    :param credentials: Dict[str, str]
    :param config: Optional[Dict[str, Union[str, float, bool]]] (optional)
    :param features: Optional[Dict[str, Any]] (optional)
    :param pricing_override: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceAiGatewayProviderConnectionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider"] = provider
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if priority is not None:
            body_dict["priority"] = priority
        body_dict["credentials"] = credentials
        if config is not None:
            body_dict["config"] = config
        if features is not None:
            body_dict["features"] = features
        if pricing_override is not None:
            body_dict["pricing_override"] = pricing_override

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsCreateOutput.from_dict)

    def update(self, instance_id: str, connection_id: str, *, name: Optional[str] = None, description: Optional[str] = None, priority: Optional[float] = None, credentials: Optional[Dict[str, str]] = None, config: Optional[Dict[str, Union[str, float, bool]]] = None, features: Optional[Dict[str, Any]] = None, pricing_override: Optional[Dict[str, Any]] = None) -> DashboardInstanceAiGatewayProviderConnectionsUpdateOutput:
        """
    Update AI gateway provider connection
    Updates a provider connection. New credentials or config are checked with the provider first, and the request fails if the provider rejects them.

    :param instance_id: str
    :param connection_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param priority: Optional[float] (optional)
    :param credentials: Optional[Dict[str, str]] (optional)
    :param config: Optional[Dict[str, Union[str, float, bool]]] (optional)
    :param features: Optional[Dict[str, Any]] (optional)
    :param pricing_override: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceAiGatewayProviderConnectionsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if priority is not None:
            body_dict["priority"] = priority
        if credentials is not None:
            body_dict["credentials"] = credentials
        if config is not None:
            body_dict["config"] = config
        if features is not None:
            body_dict["features"] = features
        if pricing_override is not None:
            body_dict["pricing_override"] = pricing_override

        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections', connection_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutput.from_dict)

    def delete(self, instance_id: str, connection_id: str) -> DashboardInstanceAiGatewayProviderConnectionsDeleteOutput:
        """
    Delete AI gateway provider connection
    Deletes a provider connection. Requests are no longer routed through it and its credentials are discarded.

    :param instance_id: str
    :param connection_id: str
    :return: DashboardInstanceAiGatewayProviderConnectionsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections', connection_id]
        )
        return self._delete(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsDeleteOutput.from_dict)

    def check(self, instance_id: str, connection_id: str) -> DashboardInstanceAiGatewayProviderConnectionsCheckOutput:
        """
    Check AI gateway provider connection
    Checks the credentials with the provider now and updates the status. Disabled connections cannot be checked.

    :param instance_id: str
    :param connection_id: str
    :return: DashboardInstanceAiGatewayProviderConnectionsCheckOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections', connection_id, 'check']
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsCheckOutput.from_dict)

    def enable(self, instance_id: str, connection_id: str) -> DashboardInstanceAiGatewayProviderConnectionsEnableOutput:
        """
    Enable AI gateway provider connection
    Turns a disabled connection back on and checks its credentials with the provider.

    :param instance_id: str
    :param connection_id: str
    :return: DashboardInstanceAiGatewayProviderConnectionsEnableOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections', connection_id, 'enable']
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsEnableOutput.from_dict)

    def disable(self, instance_id: str, connection_id: str) -> DashboardInstanceAiGatewayProviderConnectionsDisableOutput:
        """
    Disable AI gateway provider connection
    Turns a connection off without deleting it. Requests are not routed through it and its credentials are not checked until it is enabled again.

    :param instance_id: str
    :param connection_id: str
    :return: DashboardInstanceAiGatewayProviderConnectionsDisableOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'ai-gateway', 'provider-connections', connection_id, 'disable']
        )
        return self._post(request).transform(mapDashboardInstanceAiGatewayProviderConnectionsDisableOutput.from_dict)