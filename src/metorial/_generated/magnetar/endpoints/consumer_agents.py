from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerAgentsListOutput, ConsumerAgentsListOutput, mapConsumerAgentsListQuery, ConsumerAgentsListQuery, mapConsumerAgentsGetOutput, ConsumerAgentsGetOutput

class MetorialConsumerAgentsEndpoint(BaseMetorialEndpoint):
    """Inspect runtime clients, connections, operations, and credentials for the authenticated consumer profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None) -> ConsumerAgentsListOutput:
        """
    List consumer runtime clients
    Returns MCP clients observed in Magic MCP sessions accessible to the authenticated profile.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :return: ConsumerAgentsListOutput
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

        request = MetorialRequest(
            path=['consumer', 'agents'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerAgentsListOutput.from_dict)

    def get(self, agent_id: str) -> ConsumerAgentsGetOutput:
        """
    Get consumer runtime client
    Retrieves one MCP client observed in an accessible Magic MCP session.

    :param agent_id: str
    :return: ConsumerAgentsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'agents', agent_id]
        )
        return self._get(request).transform(mapConsumerAgentsGetOutput.from_dict)