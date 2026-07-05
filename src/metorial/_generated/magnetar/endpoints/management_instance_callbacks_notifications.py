from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbacksNotificationsListOutput, DashboardInstanceCallbacksNotificationsListOutput, mapDashboardInstanceCallbacksNotificationsListQuery, DashboardInstanceCallbacksNotificationsListQuery, mapDashboardInstanceCallbacksNotificationsGetOutput, DashboardInstanceCallbacksNotificationsGetOutput

class MetorialManagementInstanceCallbacksNotificationsEndpoint(BaseMetorialEndpoint):
    """Read callback notification deliveries."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, callback_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, destination_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceCallbacksNotificationsListOutput:
        """
    List callback notifications
    Returns a paginated list of callback notifications.

    :param instance_id: str
    :param callback_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param destination_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceCallbacksNotificationsListOutput
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
        if destination_id is not None:
            query_dict["destination_id"] = destination_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id, 'notifications'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksNotificationsListOutput.from_dict)

    def get(self, instance_id: str, callback_id: str, callback_notification_id: str) -> DashboardInstanceCallbacksNotificationsGetOutput:
        """
    Get callback notification
    Retrieves a specific callback notification.

    :param instance_id: str
    :param callback_id: str
    :param callback_notification_id: str
    :return: DashboardInstanceCallbacksNotificationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id, 'notifications', callback_notification_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksNotificationsGetOutput.from_dict)