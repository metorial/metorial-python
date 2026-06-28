from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProtoGuardAlertsListOutput, DashboardInstanceProtoGuardAlertsListOutput, mapDashboardInstanceProtoGuardAlertsListQuery, DashboardInstanceProtoGuardAlertsListQuery, mapDashboardInstanceProtoGuardAlertsGetOutput, DashboardInstanceProtoGuardAlertsGetOutput

class MetorialProtoGuardAlertsEndpoint(BaseMetorialEndpoint):
    """ProtoGuard alerts describe prompt-injection detections."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, run_id: Optional[Union[str, List[str]]] = None, filter_id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, session_message_id: Optional[Union[str, List[str]]] = None, session_connection_id: Optional[Union[str, List[str]]] = None, provider_run_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceProtoGuardAlertsListOutput:
        """
    List ProtoGuard alerts
    Returns a paginated list of ProtoGuard alerts for this instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param run_id: Optional[Union[str, List[str]]] (optional)
    :param filter_id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_message_id: Optional[Union[str, List[str]]] (optional)
    :param session_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_run_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceProtoGuardAlertsListOutput
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
        if run_id is not None:
            query_dict["run_id"] = run_id
        if filter_id is not None:
            query_dict["filter_id"] = filter_id
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

        request = MetorialRequest(
            path=['protoguard-alerts'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProtoGuardAlertsListOutput.from_dict)

    def get(self, proto_guard_alert_id: str) -> DashboardInstanceProtoGuardAlertsGetOutput:
        """
    Get ProtoGuard alert
    Retrieves a ProtoGuard alert by ID.

    :param proto_guard_alert_id: str
    :return: DashboardInstanceProtoGuardAlertsGetOutput
    """
        request = MetorialRequest(
            path=['protoguard-alerts', proto_guard_alert_id]
        )
        return self._get(request).transform(mapDashboardInstanceProtoGuardAlertsGetOutput.from_dict)