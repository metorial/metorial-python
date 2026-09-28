from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsEventsListOutput, DashboardOrganizationsEventsListOutput, mapDashboardOrganizationsEventsListQuery, DashboardOrganizationsEventsListQuery, mapDashboardOrganizationsEventsGetOutput, DashboardOrganizationsEventsGetOutput

class MetorialManagementOrganizationEventsEndpoint(BaseMetorialEndpoint):
    """Events are the record of everything Metorial delivers to your event destinations — normal resource events, callback occurrences, chat connection events, and manual pings."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, instance_id: Optional[str] = None, event_type: Optional[Union[str, List[str]]] = None, source: Optional[Union[str, List[str]]] = None, callback_id: Optional[Union[str, List[str]]] = None, callback_trigger_key: Optional[Union[str, List[str]]] = None, chat_connection_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardOrganizationsEventsListOutput:
        """
    List events
    List events recorded for the organization

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param instance_id: Optional[str] (optional)
    :param event_type: Optional[Union[str, List[str]]] (optional)
    :param source: Optional[Union[str, List[str]]] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :param callback_trigger_key: Optional[Union[str, List[str]]] (optional)
    :param chat_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardOrganizationsEventsListOutput
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
        if instance_id is not None:
            query_dict["instance_id"] = instance_id
        if event_type is not None:
            query_dict["event_type"] = event_type
        if source is not None:
            query_dict["source"] = source
        if callback_id is not None:
            query_dict["callback_id"] = callback_id
        if callback_trigger_key is not None:
            query_dict["callback_trigger_key"] = callback_trigger_key
        if chat_connection_id is not None:
            query_dict["chat_connection_id"] = chat_connection_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['organization', 'events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsEventsListOutput.from_dict)

    def get(self, event_id: str) -> DashboardOrganizationsEventsGetOutput:
        """
    Get event
    Get a specific event recorded for the organization

    :param event_id: str
    :return: DashboardOrganizationsEventsGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'events', event_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsEventsGetOutput.from_dict)