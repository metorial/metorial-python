from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAssistantsListOutput, DashboardInstanceAssistantsListOutput, mapDashboardInstanceAssistantsListQuery, DashboardInstanceAssistantsListQuery, mapDashboardInstanceAssistantsGetOutput, DashboardInstanceAssistantsGetOutput

class MetorialAssistantsEndpoint(BaseMetorialEndpoint):
    """Assistant and conversation endpoints"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceAssistantsListOutput:
        """
    List assistants
    List assistants available in an instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceAssistantsListOutput
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
            path=['assistants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAssistantsListOutput.from_dict)

    def get(self, assistant_id: str) -> DashboardInstanceAssistantsGetOutput:
        """
    Get assistant
    Get an assistant available in an instance.

    :param assistant_id: str
    :return: DashboardInstanceAssistantsGetOutput
    """
        request = MetorialRequest(
            path=['assistants', assistant_id]
        )
        return self._get(request).transform(mapDashboardInstanceAssistantsGetOutput.from_dict)