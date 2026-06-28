from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerProfileGroupsListOutput, ConsumerProfileGroupsListOutput, mapConsumerProfileGroupsListQuery, ConsumerProfileGroupsListQuery

class MetorialConsumerProfileGroupsEndpoint(BaseMetorialEndpoint):
    """Inspect the authenticated consumer session and profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> ConsumerProfileGroupsListOutput:
        """
    List consumer profile groups
    Returns the effective groups for the authenticated consumer profile.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: ConsumerProfileGroupsListOutput
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
            path=['consumer', 'profile', 'groups'],
            query=query_dict
        )
        return self._post(request).transform(mapConsumerProfileGroupsListOutput.from_dict)