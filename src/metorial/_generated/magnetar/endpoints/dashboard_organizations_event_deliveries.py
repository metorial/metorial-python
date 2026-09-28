from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsEventDeliveriesListOutput, DashboardOrganizationsEventDeliveriesListOutput, mapDashboardOrganizationsEventDeliveriesListQuery, DashboardOrganizationsEventDeliveriesListQuery, mapDashboardOrganizationsEventDeliveriesGetOutput, DashboardOrganizationsEventDeliveriesGetOutput, mapDashboardOrganizationsEventDeliveriesRetryOutput, DashboardOrganizationsEventDeliveriesRetryOutput

class MetorialDashboardOrganizationsEventDeliveriesEndpoint(BaseMetorialEndpoint):
    """An event delivery is Metorial's record of sending one event to one event destination, including every attempt it took to get there."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, event_id: Optional[Union[str, List[str]]] = None, event_type: Optional[Union[str, List[str]]] = None, event_destination_id: Optional[Union[str, List[str]]] = None, instance_id: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsEventDeliveriesListOutput:
        """
    List event deliveries
    List event deliveries recorded for the organization

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param event_id: Optional[Union[str, List[str]]] (optional)
    :param event_type: Optional[Union[str, List[str]]] (optional)
    :param event_destination_id: Optional[Union[str, List[str]]] (optional)
    :param instance_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsEventDeliveriesListOutput
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
        if status is not None:
            query_dict["status"] = status
        if event_id is not None:
            query_dict["event_id"] = event_id
        if event_type is not None:
            query_dict["event_type"] = event_type
        if event_destination_id is not None:
            query_dict["event_destination_id"] = event_destination_id
        if instance_id is not None:
            query_dict["instance_id"] = instance_id

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-deliveries'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDeliveriesListOutput.from_dict)

    def get(self, organization_id: str, event_delivery_id: str) -> DashboardOrganizationsEventDeliveriesGetOutput:
        """
    Get event delivery
    Get a specific event delivery recorded for the organization

    :param organization_id: str
    :param event_delivery_id: str
    :return: DashboardOrganizationsEventDeliveriesGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-deliveries', event_delivery_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDeliveriesGetOutput.from_dict)

    def retry(self, organization_id: str, event_delivery_id: str) -> DashboardOrganizationsEventDeliveriesRetryOutput:
        """
    Retry event delivery
    Schedules another attempt for a delivery that has finished, whether it succeeded or gave up. The delivery is given a fresh attempt budget.

    :param organization_id: str
    :param event_delivery_id: str
    :return: DashboardOrganizationsEventDeliveriesRetryOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-deliveries', event_delivery_id, 'retry']
        )
        return self._post(request).transform(mapDashboardOrganizationsEventDeliveriesRetryOutput.from_dict)