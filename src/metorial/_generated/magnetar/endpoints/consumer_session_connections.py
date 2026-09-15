from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerSessionConnectionsListOutput, ConsumerSessionConnectionsListOutput, mapConsumerSessionConnectionsListQuery, ConsumerSessionConnectionsListQuery, mapConsumerSessionConnectionsGetOutput, ConsumerSessionConnectionsGetOutput

class MetorialConsumerSessionConnectionsEndpoint(BaseMetorialEndpoint):
    """Inspect runtime clients, connections, operations, and credentials for the authenticated consumer profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, connection_state: Optional[Union[str, List[str]]] = None, agent_id: Optional[str] = None, session_id: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None) -> ConsumerSessionConnectionsListOutput:
        """
    List consumer session connections
    Returns connections from Magic MCP sessions accessible to the authenticated profile.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param connection_state: Optional[Union[str, List[str]]] (optional)
    :param agent_id: Optional[str] (optional)
    :param session_id: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: ConsumerSessionConnectionsListOutput
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
        if connection_state is not None:
            query_dict["connection_state"] = connection_state
        if agent_id is not None:
            query_dict["agent_id"] = agent_id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['consumer', 'session-connections'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerSessionConnectionsListOutput.from_dict)

    def get(self, session_connection_id: str) -> ConsumerSessionConnectionsGetOutput:
        """
    Get consumer session connection
    Retrieves one connection from a Magic MCP session accessible to the authenticated profile.

    :param session_connection_id: str
    :return: ConsumerSessionConnectionsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'session-connections', session_connection_id]
        )
        return self._get(request).transform(mapConsumerSessionConnectionsGetOutput.from_dict)