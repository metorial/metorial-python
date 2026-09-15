from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbackEventsListOutput, DashboardInstanceCallbackEventsListOutput, mapDashboardInstanceCallbackEventsListQuery, DashboardInstanceCallbackEventsListQuery, mapDashboardInstanceCallbackEventsGetOutput, DashboardInstanceCallbackEventsGetOutput

class MetorialDashboardInstanceCallbackEventsEndpoint(BaseMetorialEndpoint):
    """A callback event is recorded every time a provider trigger behind one of your callbacks fires. Listing returns the events themselves; fetch a single event to enrich it with the payload the provider produced, and the inbound webhook behind it, if any."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, callback_id: Optional[Union[str, List[str]]] = None, callback_instance_id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, integration_provider_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_trigger_key: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, source: Optional[Union[str, List[str]]] = None, occurred_at: Optional[Dict[str, Any]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbackEventsListOutput:
        """
    List callback events
    Returns a paginated list of callback events.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :param callback_instance_id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param integration_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_trigger_key: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param source: Optional[Union[str, List[str]]] (optional)
    :param occurred_at: Optional[Dict[str, Any]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCallbackEventsListOutput
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
        if callback_id is not None:
            query_dict["callback_id"] = callback_id
        if callback_instance_id is not None:
            query_dict["callback_instance_id"] = callback_instance_id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if integration_provider_id is not None:
            query_dict["integration_provider_id"] = integration_provider_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_trigger_key is not None:
            query_dict["provider_trigger_key"] = provider_trigger_key
        if status is not None:
            query_dict["status"] = status
        if source is not None:
            query_dict["source"] = source
        if occurred_at is not None:
            query_dict["occurred_at"] = occurred_at
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callback-events'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbackEventsListOutput.from_dict)

    def get(self, instance_id: str, callback_event_id: str) -> DashboardInstanceCallbackEventsGetOutput:
        """
    Get callback event
    Retrieves a specific callback event by ID, enriched with the payload the provider produced for it and, if it came from a webhook, the inbound request behind it.

    :param instance_id: str
    :param callback_event_id: str
    :return: DashboardInstanceCallbackEventsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callback-events', callback_event_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbackEventsGetOutput.from_dict)