from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceAssistantsListOutput, DashboardInstanceAssistantsListOutput, mapDashboardInstanceAssistantsListQuery, DashboardInstanceAssistantsListQuery, mapDashboardInstanceAssistantsGetOutput, DashboardInstanceAssistantsGetOutput

class MetorialDashboardInstanceAssistantsEndpoint(BaseMetorialEndpoint):
    """Assistant and conversation endpoints"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceAssistantsListOutput:
        """
    List assistants
    List assistants available in an instance.

    :param instance_id: str
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
            path=['dashboard', 'instances', instance_id, 'assistants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceAssistantsListOutput.from_dict)

    def get(self, instance_id: str, assistant_id: str) -> DashboardInstanceAssistantsGetOutput:
        """
    Get assistant
    Get an assistant available in an instance.

    :param instance_id: str
    :param assistant_id: str
    :return: DashboardInstanceAssistantsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'assistants', assistant_id]
        )
        return self._get(request).transform(mapDashboardInstanceAssistantsGetOutput.from_dict)