from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbacksEventsListOutput, DashboardInstanceCallbacksEventsListOutput, mapDashboardInstanceCallbacksEventsListQuery, DashboardInstanceCallbacksEventsListQuery, mapDashboardInstanceCallbacksEventsGetOutput, DashboardInstanceCallbacksEventsGetOutput

class MetorialManagementInstanceCallbacksEventsEndpoint(BaseMetorialEndpoint):
    """Read callback trigger events."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, callback_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, source_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceCallbacksEventsListOutput:
        """
    List callback events
    Returns a paginated list of callback events.

    :param instance_id: str
    :param callback_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param source_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCallbacksEventsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if type is not None:
            query_dict["type"] = type
        if source_id is not None:
            query_dict["source_id"] = source_id

        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id, 'events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksEventsListOutput.from_dict)

    def get(self, instance_id: str, callback_id: str, callback_event_id: str) -> DashboardInstanceCallbacksEventsGetOutput:
        """
    Get callback event
    Retrieves a specific callback event.

    :param instance_id: str
    :param callback_id: str
    :param callback_event_id: str
    :return: DashboardInstanceCallbacksEventsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id, 'events', callback_event_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksEventsGetOutput.from_dict)