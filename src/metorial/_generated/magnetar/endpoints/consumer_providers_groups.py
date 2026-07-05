from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerProvidersGroupsListOutput, ConsumerProvidersGroupsListOutput, mapConsumerProvidersGroupsListQuery, ConsumerProvidersGroupsListQuery

class MetorialConsumerProvidersGroupsEndpoint(BaseMetorialEndpoint):
    """Browse and configure portal providers from the consumer side."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> ConsumerProvidersGroupsListOutput:
        """
    List consumer provider groups
    Returns the ordered provider groups for the current consumer surface.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: ConsumerProvidersGroupsListOutput
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
            path=['consumer', 'providers', 'groups'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerProvidersGroupsListOutput.from_dict)