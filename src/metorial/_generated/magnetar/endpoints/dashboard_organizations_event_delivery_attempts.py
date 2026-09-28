from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsEventDeliveryAttemptsListOutput, DashboardOrganizationsEventDeliveryAttemptsListOutput, mapDashboardOrganizationsEventDeliveryAttemptsListQuery, DashboardOrganizationsEventDeliveryAttemptsListQuery, mapDashboardOrganizationsEventDeliveryAttemptsGetOutput, DashboardOrganizationsEventDeliveryAttemptsGetOutput

class MetorialDashboardOrganizationsEventDeliveryAttemptsEndpoint(BaseMetorialEndpoint):
    """A delivery attempt is one request Metorial made to an event destination, with the request it sent and the response it got back."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, event_delivery_id: Optional[Union[str, List[str]]] = None, event_id: Optional[Union[str, List[str]]] = None, event_destination_id: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsEventDeliveryAttemptsListOutput:
        """
    List event delivery attempts
    List delivery attempts recorded for the organization

    :param organization_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param event_delivery_id: Optional[Union[str, List[str]]] (optional)
    :param event_id: Optional[Union[str, List[str]]] (optional)
    :param event_destination_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsEventDeliveryAttemptsListOutput
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
        if event_delivery_id is not None:
            query_dict["event_delivery_id"] = event_delivery_id
        if event_id is not None:
            query_dict["event_id"] = event_id
        if event_destination_id is not None:
            query_dict["event_destination_id"] = event_destination_id

        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-delivery-attempts'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDeliveryAttemptsListOutput.from_dict)

    def get(self, organization_id: str, event_delivery_attempt_id: str) -> DashboardOrganizationsEventDeliveryAttemptsGetOutput:
        """
    Get event delivery attempt
    Get a specific delivery attempt, including the request Metorial sent and the response the destination returned

    :param organization_id: str
    :param event_delivery_attempt_id: str
    :return: DashboardOrganizationsEventDeliveryAttemptsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'event-delivery-attempts', event_delivery_attempt_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsEventDeliveryAttemptsGetOutput.from_dict)