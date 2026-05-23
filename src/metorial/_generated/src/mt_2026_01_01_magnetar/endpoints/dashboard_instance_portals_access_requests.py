from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsAccessRequestsListOutput, DashboardInstancePortalsAccessRequestsListOutput, mapDashboardInstancePortalsAccessRequestsListQuery, DashboardInstancePortalsAccessRequestsListQuery, mapDashboardInstancePortalsAccessRequestsGetOutput, DashboardInstancePortalsAccessRequestsGetOutput, mapDashboardInstancePortalsAccessRequestsUpdateOutput, DashboardInstancePortalsAccessRequestsUpdateOutput, mapDashboardInstancePortalsAccessRequestsUpdateBody, DashboardInstancePortalsAccessRequestsUpdateBody

class MetorialDashboardInstancePortalsAccessRequestsEndpoint(BaseMetorialEndpoint):
    """Review and resolve access requests for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, consumer_profile_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstancePortalsAccessRequestsListOutput:
        """
    List portal access requests
    Returns a paginated list of access requests for a portal.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param consumer_profile_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstancePortalsAccessRequestsListOutput
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
        if consumer_profile_id is not None:
            query_dict["consumer_profile_id"] = consumer_profile_id
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'access-requests'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsAccessRequestsListOutput.from_dict)

    def get(self, instance_id: str, portal_id: str, access_request_id: str) -> DashboardInstancePortalsAccessRequestsGetOutput:
        """
    Get portal access request
    Retrieves a access request by ID.

    :param instance_id: str
    :param portal_id: str
    :param access_request_id: str
    :return: DashboardInstancePortalsAccessRequestsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'access-requests', access_request_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsAccessRequestsGetOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, access_request_id: str, *, status: str, resolution_message: Optional[str] = None, consumer_group_id: Optional[str] = None) -> DashboardInstancePortalsAccessRequestsUpdateOutput:
        """
    Review portal access request
    Approves or rejects a access request.

    :param instance_id: str
    :param portal_id: str
    :param access_request_id: str
    :param status: str
    :param resolution_message: Optional[str] (optional)
    :param consumer_group_id: Optional[str] (optional)
    :return: DashboardInstancePortalsAccessRequestsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["status"] = status
        if resolution_message is not None:
            body_dict["resolution_message"] = resolution_message
        if consumer_group_id is not None:
            body_dict["consumer_group_id"] = consumer_group_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'access-requests', access_request_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsAccessRequestsUpdateOutput.from_dict)