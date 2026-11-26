from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProtoGuardSuppressionsListOutput, DashboardInstanceProtoGuardSuppressionsListOutput, mapDashboardInstanceProtoGuardSuppressionsListQuery, DashboardInstanceProtoGuardSuppressionsListQuery, mapDashboardInstanceProtoGuardSuppressionsGetOutput, DashboardInstanceProtoGuardSuppressionsGetOutput, mapDashboardInstanceProtoGuardSuppressionsCreateOutput, DashboardInstanceProtoGuardSuppressionsCreateOutput, mapDashboardInstanceProtoGuardSuppressionsCreateBody, DashboardInstanceProtoGuardSuppressionsCreateBody, mapDashboardInstanceProtoGuardSuppressionsArchiveOutput, DashboardInstanceProtoGuardSuppressionsArchiveOutput

class MetorialProtoGuardSuppressionsEndpoint(BaseMetorialEndpoint):
    """A ProtoGuard suppression is a rule that hides known-benign findings. Matching findings no longer raise alerts."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, filter_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProtoGuardSuppressionsListOutput:
        """
    List ProtoGuard suppressions
    Returns a paginated list of ProtoGuard suppressions in the instance.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param filter_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProtoGuardSuppressionsListOutput
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
        if filter_id is not None:
            query_dict["filter_id"] = filter_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id

        request = MetorialRequest(
            path=['protoguard-suppressions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProtoGuardSuppressionsListOutput.from_dict)

    def get(self, suppression_id: str) -> DashboardInstanceProtoGuardSuppressionsGetOutput:
        """
    Get ProtoGuard suppression
    Retrieves a ProtoGuard suppression.

    :param suppression_id: str
    :return: DashboardInstanceProtoGuardSuppressionsGetOutput
    """
        request = MetorialRequest(
            path=['protoguard-suppressions', suppression_id]
        )
        return self._get(request).transform(mapDashboardInstanceProtoGuardSuppressionsGetOutput.from_dict)

    def create(self, *, filter_id: str, provider_id: Optional[str] = None, tool_key: Optional[str] = None, content_hash: Optional[str] = None, reason: Optional[str] = None, expires_at: Optional[datetime] = None) -> DashboardInstanceProtoGuardSuppressionsCreateOutput:
        """
    Create ProtoGuard suppression
    Suppresses future findings of a filter, optionally narrowed to a provider, tool, or specific matched content.

    :param filter_id: str
    :param provider_id: Optional[str] (optional)
    :param tool_key: Optional[str] (optional)
    :param content_hash: Optional[str] (optional)
    :param reason: Optional[str] (optional)
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardInstanceProtoGuardSuppressionsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["filter_id"] = filter_id
        if provider_id is not None:
            body_dict["provider_id"] = provider_id
        if tool_key is not None:
            body_dict["tool_key"] = tool_key
        if content_hash is not None:
            body_dict["content_hash"] = content_hash
        if reason is not None:
            body_dict["reason"] = reason
        if expires_at is not None:
            body_dict["expires_at"] = expires_at

        request = MetorialRequest(
            path=['protoguard-suppressions'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProtoGuardSuppressionsCreateOutput.from_dict)

    def archive(self, suppression_id: str) -> DashboardInstanceProtoGuardSuppressionsArchiveOutput:
        """
    Archive ProtoGuard suppression
    Archives a ProtoGuard suppression so matching findings alert again.

    :param suppression_id: str
    :return: DashboardInstanceProtoGuardSuppressionsArchiveOutput
    """
        request = MetorialRequest(
            path=['protoguard-suppressions', suppression_id, 'archive']
        )
        return self._post(request).transform(mapDashboardInstanceProtoGuardSuppressionsArchiveOutput.from_dict)