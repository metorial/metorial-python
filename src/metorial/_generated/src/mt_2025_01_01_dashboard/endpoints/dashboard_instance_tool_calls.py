from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceToolCallsListOutput, DashboardInstanceToolCallsListOutput, mapDashboardInstanceToolCallsListQuery, DashboardInstanceToolCallsListQuery, mapDashboardInstanceToolCallsGetOutput, DashboardInstanceToolCallsGetOutput, mapDashboardInstanceToolCallsCreateOutput, DashboardInstanceToolCallsCreateOutput, mapDashboardInstanceToolCallsCreateBody, DashboardInstanceToolCallsCreateBody

class MetorialDashboardInstanceToolCallsEndpoint(BaseMetorialEndpoint):
    """Tool calls represent individual tool invocations within a session. They track the input, output, and status of each tool execution."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, session_template_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, tool_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceToolCallsListOutput:
        """
    List all tool calls
    Returns a paginated list of tool calls across all sessions.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param tool_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceToolCallsListOutput
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
        if session_template_id is not None:
            query_dict["session_template_id"] = session_template_id
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if tool_id is not None:
            query_dict["tool_id"] = tool_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'tool-calls'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceToolCallsListOutput.from_dict)

    def get(self, instance_id: str, tool_call_id: str) -> DashboardInstanceToolCallsGetOutput:
        """
    Get tool call
    Retrieves a specific tool call by ID.

    :param instance_id: str
    :param tool_call_id: str
    :return: DashboardInstanceToolCallsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'tool-calls', tool_call_id]
        )
        return self._get(request).transform(mapDashboardInstanceToolCallsGetOutput.from_dict)

    def create(self, instance_id: str, *, tool_id: str, input: Dict[str, Any], session_id: str, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceToolCallsCreateOutput:
        """
    Create tool call
    Creates a new tool call in a session by invoking a specific tool.

    :param instance_id: str
    :param tool_id: str
    :param input: Dict[str, Any]
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param session_id: str
    :return: DashboardInstanceToolCallsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["tool_id"] = tool_id
        body_dict["input"] = input
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["session_id"] = session_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'tool-calls'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceToolCallsCreateOutput.from_dict)