from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerToolCallsListOutput, ConsumerToolCallsListOutput, mapConsumerToolCallsListQuery, ConsumerToolCallsListQuery, mapConsumerToolCallsGetOutput, ConsumerToolCallsGetOutput

class MetorialConsumerToolCallsEndpoint(BaseMetorialEndpoint):
    """Inspect runtime clients, connections, operations, and credentials for the authenticated consumer profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, agent_id: Optional[str] = None, tool_id: Optional[str] = None, provider_ids: Optional[Union[str, List[str]]] = None, connection_id: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None) -> ConsumerToolCallsListOutput:
        """
    List consumer tool calls
    Returns read-only tool-call activity for identities owned by the authenticated profile actor.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param agent_id: Optional[str] (optional)
    :param tool_id: Optional[str] (optional)
    :param provider_ids: Optional[Union[str, List[str]]] (optional)
    :param connection_id: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: ConsumerToolCallsListOutput
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
        if agent_id is not None:
            query_dict["agent_id"] = agent_id
        if tool_id is not None:
            query_dict["tool_id"] = tool_id
        if provider_ids is not None:
            query_dict["provider_ids"] = provider_ids
        if connection_id is not None:
            query_dict["connection_id"] = connection_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['consumer', 'tool-calls'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerToolCallsListOutput.from_dict)

    def get(self, tool_call_id: str) -> ConsumerToolCallsGetOutput:
        """
    Get consumer tool call
    Retrieves one tool call belonging to an identity owned by the authenticated profile actor.

    :param tool_call_id: str
    :return: ConsumerToolCallsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'tool-calls', tool_call_id]
        )
        return self._get(request).transform(mapConsumerToolCallsGetOutput.from_dict)