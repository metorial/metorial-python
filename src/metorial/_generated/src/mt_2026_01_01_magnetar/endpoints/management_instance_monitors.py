from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceMonitorsListOutput, DashboardInstanceMonitorsListOutput, mapDashboardInstanceMonitorsListQuery, DashboardInstanceMonitorsListQuery, mapDashboardInstanceMonitorsGetOutput, DashboardInstanceMonitorsGetOutput

class MetorialManagementInstanceMonitorsEndpoint(BaseMetorialEndpoint):
    """Monitors track automated observability checks for this instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, target: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, proto_guard_filter_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None, first_alert_at: Optional[Dict[str, Any]] = None, last_alert_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceMonitorsListOutput:
        """
    List monitors
    Returns a paginated list of monitors for this instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param target: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param proto_guard_filter_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :param first_alert_at: Optional[Dict[str, Any]] (optional)
    :param last_alert_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceMonitorsListOutput
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
        if target is not None:
            query_dict["target"] = target
        if status is not None:
            query_dict["status"] = status
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if proto_guard_filter_id is not None:
            query_dict["proto_guard_filter_id"] = proto_guard_filter_id
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at
        if first_alert_at is not None:
            query_dict["first_alert_at"] = first_alert_at
        if last_alert_at is not None:
            query_dict["last_alert_at"] = last_alert_at

        request = MetorialRequest(
            path=['instances', instance_id, 'monitors'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceMonitorsListOutput.from_dict)

    def get(self, instance_id: str, monitor_id: str) -> DashboardInstanceMonitorsGetOutput:
        """
    Get monitor
    Retrieves a monitor by ID.

    :param instance_id: str
    :param monitor_id: str
    :return: DashboardInstanceMonitorsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'monitors', monitor_id]
        )
        return self._get(request).transform(mapDashboardInstanceMonitorsGetOutput.from_dict)