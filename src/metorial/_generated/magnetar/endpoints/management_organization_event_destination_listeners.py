from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsEventDestinationListenersListOutput, DashboardOrganizationsEventDestinationListenersListOutput, mapDashboardOrganizationsEventDestinationListenersListQuery, DashboardOrganizationsEventDestinationListenersListQuery, mapDashboardOrganizationsEventDestinationListenersGetOutput, DashboardOrganizationsEventDestinationListenersGetOutput, mapDashboardOrganizationsEventDestinationListenersCreateOutput, DashboardOrganizationsEventDestinationListenersCreateOutput, mapDashboardOrganizationsEventDestinationListenersCreateBody, DashboardOrganizationsEventDestinationListenersCreateBody, mapDashboardOrganizationsEventDestinationListenersUpdateOutput, DashboardOrganizationsEventDestinationListenersUpdateOutput, mapDashboardOrganizationsEventDestinationListenersUpdateBody, DashboardOrganizationsEventDestinationListenersUpdateBody, mapDashboardOrganizationsEventDestinationListenersDeleteOutput, DashboardOrganizationsEventDestinationListenersDeleteOutput

class MetorialManagementOrganizationEventDestinationListenersEndpoint(BaseMetorialEndpoint):
    """Event destination listeners subscribe an event destination to events for a specific instance — generic resource events, a callback's trigger events, or a chat connection's events."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, event_destination_id: Optional[Union[str, List[str]]] = None, instance_id: Optional[Union[str, List[str]]] = None, callback_id: Optional[Union[str, List[str]]] = None, chat_connection_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsEventDestinationListenersListOutput:
        """
    List event destination listeners
    Returns a paginated list of event destination listeners for the organization.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param event_destination_id: Optional[Union[str, List[str]]] (optional)
    :param instance_id: Optional[Union[str, List[str]]] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :param chat_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsEventDestinationListenersListOutput
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
        if event_destination_id is not None:
            query_dict["event_destination_id"] = event_destination_id
        if instance_id is not None:
            query_dict["instance_id"] = instance_id
        if callback_id is not None:
            query_dict["callback_id"] = callback_id
        if chat_connection_id is not None:
            query_dict["chat_connection_id"] = chat_connection_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['organization', 'event-destination-listeners'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDestinationListenersListOutput.from_dict)

    def get(self, event_destination_listener_id: str) -> DashboardOrganizationsEventDestinationListenersGetOutput:
        """
    Get event destination listener
    Retrieves a specific event destination listener by ID.

    :param event_destination_listener_id: str
    :return: DashboardOrganizationsEventDestinationListenersGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'event-destination-listeners', event_destination_listener_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDestinationListenersGetOutput.from_dict)

    def create(self) -> DashboardOrganizationsEventDestinationListenersCreateOutput:
        """
    Create event destination listener
    Subscribes an event destination to events for this instance — generic resource events, a callback's trigger events, or a chat connection's events.


    :return: DashboardOrganizationsEventDestinationListenersCreateOutput
    """
        request = MetorialRequest(
            path=['organization', 'event-destination-listeners']
        )
        return self._post(request).transform(mapDashboardOrganizationsEventDestinationListenersCreateOutput.from_dict)

    def update(self, event_destination_listener_id: str, *, event_types: Optional[List[str]] = None, triggers: Optional[List[str]] = None) -> DashboardOrganizationsEventDestinationListenersUpdateOutput:
        """
    Update event destination listener
    Updates the event types or callback triggers an event destination listener subscribes to.

    :param event_destination_listener_id: str
    :param event_types: Optional[List[str]] (optional)
    :param triggers: Optional[List[str]] (optional)
    :return: DashboardOrganizationsEventDestinationListenersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if event_types is not None:
            body_dict["event_types"] = event_types
        if triggers is not None:
            body_dict["triggers"] = triggers

        request = MetorialRequest(
            path=['organization', 'event-destination-listeners', event_destination_listener_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsEventDestinationListenersUpdateOutput.from_dict)

    def delete(self, event_destination_listener_id: str) -> DashboardOrganizationsEventDestinationListenersDeleteOutput:
        """
    Delete event destination listener
    Removes an event destination listener.

    :param event_destination_listener_id: str
    :return: DashboardOrganizationsEventDestinationListenersDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'event-destination-listeners', event_destination_listener_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsEventDestinationListenersDeleteOutput.from_dict)