from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsConsumerInvitesListOutput, DashboardInstancePortalsConsumerInvitesListOutput, mapDashboardInstancePortalsConsumerInvitesListQuery, DashboardInstancePortalsConsumerInvitesListQuery, mapDashboardInstancePortalsConsumerInvitesCreateOutput, DashboardInstancePortalsConsumerInvitesCreateOutput, mapDashboardInstancePortalsConsumerInvitesCreateBody, DashboardInstancePortalsConsumerInvitesCreateBody, mapDashboardInstancePortalsConsumerInvitesGetOutput, DashboardInstancePortalsConsumerInvitesGetOutput

class MetorialManagementInstancePortalsConsumerInvitesEndpoint(BaseMetorialEndpoint):
    """List and inspect consumer invites for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstancePortalsConsumerInvitesListOutput:
        """
    List portal consumer invites
    Returns a paginated list of invites for a portal.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstancePortalsConsumerInvitesListOutput
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
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'invites'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerInvitesListOutput.from_dict)

    def create(self, instance_id: str, portal_id: str, *, name: str, email: str, message: Optional[str] = None) -> DashboardInstancePortalsConsumerInvitesCreateOutput:
        """
    Create portal consumer invite
    Invites a consumer to a portal.

    :param instance_id: str
    :param portal_id: str
    :param name: str
    :param email: str
    :param message: Optional[str] (optional)
    :return: DashboardInstancePortalsConsumerInvitesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        body_dict["email"] = email
        if message is not None:
            body_dict["message"] = message

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'invites'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsConsumerInvitesCreateOutput.from_dict)

    def get(self, instance_id: str, portal_id: str, consumer_invite_id: str) -> DashboardInstancePortalsConsumerInvitesGetOutput:
        """
    Get portal consumer invite
    Retrieves a portal consumer invite by ID.

    :param instance_id: str
    :param portal_id: str
    :param consumer_invite_id: str
    :return: DashboardInstancePortalsConsumerInvitesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'invites', consumer_invite_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerInvitesGetOutput.from_dict)