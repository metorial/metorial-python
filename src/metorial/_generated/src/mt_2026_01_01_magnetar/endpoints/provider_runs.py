from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderRunsListOutput, DashboardInstanceProviderRunsListOutput, mapDashboardInstanceProviderRunsListQuery, DashboardInstanceProviderRunsListQuery, mapDashboardInstanceProviderRunsGetOutput, DashboardInstanceProviderRunsGetOutput, mapDashboardInstanceProviderRunsGetLogsOutput, DashboardInstanceProviderRunsGetLogsOutput

class MetorialProviderRunsEndpoint(BaseMetorialEndpoint):
    """Provider runs track the execution of provider operations within a session. This read-only resource provides visibility into provider activity."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, session_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None, session_connection_id: Optional[Union[str, List[str]]] = None, provider_version_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderRunsListOutput:
        """
    List all provider runs
    Returns a paginated list of provider runs across all sessions.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param session_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :param session_connection_id: Optional[Union[str, List[str]]] (optional)
    :param provider_version_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProviderRunsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if session_id is not None:
            query_dict["session_id"] = session_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id
        if session_connection_id is not None:
            query_dict["session_connection_id"] = session_connection_id
        if provider_version_id is not None:
            query_dict["provider_version_id"] = provider_version_id

        request = MetorialRequest(
            path=['provider-runs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderRunsListOutput.from_dict)

    def get(self, provider_run_id: str) -> DashboardInstanceProviderRunsGetOutput:
        """
    Get provider run
    Retrieves a specific provider run by ID.

    :param provider_run_id: str
    :return: DashboardInstanceProviderRunsGetOutput
    """
        request = MetorialRequest(
            path=['provider-runs', provider_run_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderRunsGetOutput.from_dict)

    def get_logs(self, provider_run_id: str) -> DashboardInstanceProviderRunsGetLogsOutput:
        """
    Get provider run logs
    Retrieves the logs for a specific provider run.

    :param provider_run_id: str
    :return: DashboardInstanceProviderRunsGetLogsOutput
    """
        request = MetorialRequest(
            path=['provider-runs', provider_run_id, 'logs']
        )
        return self._get(request).transform(mapDashboardInstanceProviderRunsGetLogsOutput.from_dict)