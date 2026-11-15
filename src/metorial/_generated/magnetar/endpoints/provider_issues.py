from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderIssuesListOutput, DashboardInstanceProviderIssuesListOutput, mapDashboardInstanceProviderIssuesListQuery, DashboardInstanceProviderIssuesListQuery, mapDashboardInstanceProviderIssuesGetOutput, DashboardInstanceProviderIssuesGetOutput

class MetorialProviderIssuesEndpoint(BaseMetorialEndpoint):
    """Provider issues aggregate repeated provider errors, authentication failures and ProtoGuard warnings into one record per distinct problem."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, type: Optional[Union[str, List[str]]] = None, severity: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, last_seen_at: Optional[Dict[str, Any]] = None, created_at: Optional[Dict[str, Any]] = None, search: Optional[str] = None) -> DashboardInstanceProviderIssuesListOutput:
        """
    List provider issues
    Returns a paginated list of provider issues. Only issue types the caller has read access to are included.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param severity: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param last_seen_at: Optional[Dict[str, Any]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceProviderIssuesListOutput
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
        if severity is not None:
            query_dict["severity"] = severity
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if last_seen_at is not None:
            query_dict["last_seen_at"] = last_seen_at
        if created_at is not None:
            query_dict["created_at"] = created_at
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['provider-issues'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderIssuesListOutput.from_dict)

    def get(self, provider_issue_id: str) -> DashboardInstanceProviderIssuesGetOutput:
        """
    Get provider issue
    Retrieves a specific provider issue.

    :param provider_issue_id: str
    :return: DashboardInstanceProviderIssuesGetOutput
    """
        request = MetorialRequest(
            path=['provider-issues', provider_issue_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderIssuesGetOutput.from_dict)