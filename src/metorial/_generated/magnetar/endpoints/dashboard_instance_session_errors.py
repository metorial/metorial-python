from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionErrorsListOutput, DashboardInstanceSessionErrorsListOutput, mapDashboardInstanceSessionErrorsListQuery, DashboardInstanceSessionErrorsListQuery

class MetorialDashboardInstanceSessionErrorsEndpoint(BaseMetorialEndpoint):
    """Session errors track errors that occurred during a session. This read-only resource provides visibility into issues that happened during provider execution."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[str] = None, session_id: Optional[Union[str, List[str]]] = None, session_error_group_id: Optional[Union[str, List[str]]] = None, provider_run_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionErrorsListOutput:
        """
    List all session errors
    Returns a paginated list of errors across all sessions.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[str] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param session_error_group_id: Optional[Union[str, List[str]]] (optional)
    :param provider_run_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionErrorsListOutput
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
        if type is not None:
            query_dict["type"] = type
        if session_id is not None:
            query_dict["session_id"] = session_id
        if session_error_group_id is not None:
            query_dict["session_error_group_id"] = session_error_group_id
        if provider_run_id is not None:
            query_dict["provider_run_id"] = provider_run_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'session-errors'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionErrorsListOutput.from_dict)
