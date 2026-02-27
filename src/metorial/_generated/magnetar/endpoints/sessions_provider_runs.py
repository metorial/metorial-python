from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSessionsProviderRunsListOutput, DashboardInstanceSessionsProviderRunsListOutput, mapDashboardInstanceSessionsProviderRunsListQuery, DashboardInstanceSessionsProviderRunsListQuery, mapDashboardInstanceSessionsProviderRunsGetOutput, DashboardInstanceSessionsProviderRunsGetOutput, mapDashboardInstanceSessionsProviderRunsGetLogsOutput, DashboardInstanceSessionsProviderRunsGetLogsOutput

class MetorialSessionsProviderRunsEndpoint(BaseMetorialEndpoint):
    """Provider runs track the execution of provider operations within a session. This read-only resource provides visibility into provider activity."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, session_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[str] = None, provider_id: Optional[Union[str, List[str]]] = None, session_provider_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSessionsProviderRunsListOutput:
        """
    List provider runs
    Returns a paginated list of provider runs for a session.

    :param session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[str] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param session_provider_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSessionsProviderRunsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if session_provider_id is not None:
            query_dict["session_provider_id"] = session_provider_id

        request = MetorialRequest(
            path=['sessions', session_id, 'provider-runs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProviderRunsListOutput.from_dict)

    def get(self, session_id: str, provider_run_id: str) -> DashboardInstanceSessionsProviderRunsGetOutput:
        """
    Get provider run
    Retrieves a specific provider run for a session.

    :param session_id: str
    :param provider_run_id: str
    :return: DashboardInstanceSessionsProviderRunsGetOutput
    """
        request = MetorialRequest(
            path=['sessions', session_id, 'provider-runs', provider_run_id]
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProviderRunsGetOutput.from_dict)

    def get_logs(self, session_id: str, provider_run_id: str) -> DashboardInstanceSessionsProviderRunsGetLogsOutput:
        """
    Get provider run logs
    Retrieves the logs for a specific provider run.

    :param session_id: str
    :param provider_run_id: str
    :return: DashboardInstanceSessionsProviderRunsGetLogsOutput
    """
        request = MetorialRequest(
            path=['sessions', session_id, 'provider-runs', provider_run_id, 'logs']
        )
        return self._get(request).transform(mapDashboardInstanceSessionsProviderRunsGetLogsOutput.from_dict)
