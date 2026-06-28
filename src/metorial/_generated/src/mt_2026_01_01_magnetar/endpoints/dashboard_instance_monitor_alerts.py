from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMonitorAlertsListOutput, DashboardInstanceMonitorAlertsListOutput, mapDashboardInstanceMonitorAlertsListQuery, DashboardInstanceMonitorAlertsListQuery, mapDashboardInstanceMonitorAlertsGetOutput, DashboardInstanceMonitorAlertsGetOutput, mapDashboardInstanceMonitorAlertsViewedOutput, DashboardInstanceMonitorAlertsViewedOutput, mapDashboardInstanceMonitorAlertsResolveOutput, DashboardInstanceMonitorAlertsResolveOutput, mapDashboardInstanceMonitorAlertsUnresolveOutput, DashboardInstanceMonitorAlertsUnresolveOutput

class MetorialDashboardInstanceMonitorAlertsEndpoint(BaseMetorialEndpoint):
    """Monitor alerts represent detected prompt-injection or schema-change events."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, monitor_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, target: Optional[Union[str, List[str]]] = None, source: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, proto_guard_alert_id: Optional[Union[str, List[str]]] = None, proto_guard_run_id: Optional[Union[str, List[str]]] = None, proto_guard_filter_id: Optional[Union[str, List[str]]] = None, specification_change_notification_id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_message_id: Optional[Union[str, List[str]]] = None, session_connection_id: Optional[Union[str, List[str]]] = None, provider_run_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, resolved_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceMonitorAlertsListOutput:
        """
    List monitor alerts
    Returns a paginated list of monitor alerts for this instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param monitor_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param target: Optional[Union[str, List[str]]] (optional)
    :param source: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param proto_guard_alert_id: Optional[Union[str, List[str]]] (optional)
    :param proto_guard_run_id: Optional[Union[str, List[str]]] (optional)
    :param proto_guard_filter_id: Optional[Union[str, List[str]]] (optional)
    :param specification_change_notification_id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_message_id: Optional[Union[str, List[str]]] (optional)
    :param session_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_run_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param resolved_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMonitorAlertsListOutput
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
        if monitor_id is not None:
            query_dict["monitor_id"] = monitor_id
        if status is not None:
            query_dict["status"] = status
        if target is not None:
            query_dict["target"] = target
        if source is not None:
            query_dict["source"] = source
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if proto_guard_alert_id is not None:
            query_dict["proto_guard_alert_id"] = proto_guard_alert_id
        if proto_guard_run_id is not None:
            query_dict["proto_guard_run_id"] = proto_guard_run_id
        if proto_guard_filter_id is not None:
            query_dict["proto_guard_filter_id"] = proto_guard_filter_id
        if specification_change_notification_id is not None:
            query_dict["specification_change_notification_id"] = specification_change_notification_id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if session_message_id is not None:
            query_dict["session_message_id"] = session_message_id
        if session_connection_id is not None:
            query_dict["session_connection_id"] = session_connection_id
        if provider_run_id is not None:
            query_dict["provider_run_id"] = provider_run_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if resolved_at is not None:
            query_dict["resolved_at"] = resolved_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'monitor-alerts'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMonitorAlertsListOutput.from_dict)

    def get(self, instance_id: str, monitor_alert_id: str) -> DashboardInstanceMonitorAlertsGetOutput:
        """
    Get monitor alert
    Retrieves a monitor alert by ID.

    :param instance_id: str
    :param monitor_alert_id: str
    :return: DashboardInstanceMonitorAlertsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'monitor-alerts', monitor_alert_id]
        )
        return self._get(request).transform(mapDashboardInstanceMonitorAlertsGetOutput.from_dict)

    def viewed(self, instance_id: str, monitor_alert_id: str) -> DashboardInstanceMonitorAlertsViewedOutput:
        """
    Mark monitor alert viewed
    Marks a monitor alert as viewed by the current actor.

    :param instance_id: str
    :param monitor_alert_id: str
    :return: DashboardInstanceMonitorAlertsViewedOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'monitor-alerts', monitor_alert_id, 'viewed']
        )
        return self._post(request).transform(mapDashboardInstanceMonitorAlertsViewedOutput.from_dict)

    def resolve(self, instance_id: str, monitor_alert_id: str) -> DashboardInstanceMonitorAlertsResolveOutput:
        """
    Resolve monitor alert
    Marks a monitor alert as resolved.

    :param instance_id: str
    :param monitor_alert_id: str
    :return: DashboardInstanceMonitorAlertsResolveOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'monitor-alerts', monitor_alert_id, 'resolve']
        )
        return self._post(request).transform(mapDashboardInstanceMonitorAlertsResolveOutput.from_dict)

    def unresolve(self, instance_id: str, monitor_alert_id: str) -> DashboardInstanceMonitorAlertsUnresolveOutput:
        """
    Unresolve monitor alert
    Reopens a resolved monitor alert.

    :param instance_id: str
    :param monitor_alert_id: str
    :return: DashboardInstanceMonitorAlertsUnresolveOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'monitor-alerts', monitor_alert_id, 'unresolve']
        )
        return self._post(request).transform(mapDashboardInstanceMonitorAlertsUnresolveOutput.from_dict)