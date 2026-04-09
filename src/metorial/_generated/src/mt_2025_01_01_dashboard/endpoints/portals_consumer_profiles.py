from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsConsumerProfilesListOutput, DashboardInstancePortalsConsumerProfilesListOutput, mapDashboardInstancePortalsConsumerProfilesListQuery, DashboardInstancePortalsConsumerProfilesListQuery, mapDashboardInstancePortalsConsumerProfilesGetOutput, DashboardInstancePortalsConsumerProfilesGetOutput, mapDashboardInstancePortalsConsumerProfilesAssignGroupsOutput, DashboardInstancePortalsConsumerProfilesAssignGroupsOutput, mapDashboardInstancePortalsConsumerProfilesAssignGroupsBody, DashboardInstancePortalsConsumerProfilesAssignGroupsBody, mapDashboardInstancePortalsConsumerProfilesUnassignGroupsOutput, DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput, mapDashboardInstancePortalsConsumerProfilesUnassignGroupsBody, DashboardInstancePortalsConsumerProfilesUnassignGroupsBody

class MetorialPortalsConsumerProfilesEndpoint(BaseMetorialEndpoint):
    """Manage the consumers and effective group assignments for a portal."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, consumer_group_id: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstancePortalsConsumerProfilesListOutput:
        """
    List portal consumer profiles
    Returns a paginated list of consumer profiles for a portal.

    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param consumer_group_id: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstancePortalsConsumerProfilesListOutput
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
        if consumer_group_id is not None:
            query_dict["consumer_group_id"] = consumer_group_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['portals', portal_id, 'consumer-profile'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerProfilesListOutput.from_dict)

    def get(self, portal_id: str, consumer_profile_id: str) -> DashboardInstancePortalsConsumerProfilesGetOutput:
        """
    Get portal consumer profile
    Retrieves a portal consumer profile by ID.

    :param portal_id: str
    :param consumer_profile_id: str
    :return: DashboardInstancePortalsConsumerProfilesGetOutput
    """
        request = MetorialRequest(
            path=['portals', portal_id, 'consumer-profile', consumer_profile_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerProfilesGetOutput.from_dict)

    def assign_groups(self, portal_id: str, consumer_profile_id: str, *, group_ids: List[str]) -> DashboardInstancePortalsConsumerProfilesAssignGroupsOutput:
        """
    Assign portal consumer profile groups
    Assigns one or more groups to a portal consumer profile.

    :param portal_id: str
    :param consumer_profile_id: str
    :param group_ids: List[str]
    :return: DashboardInstancePortalsConsumerProfilesAssignGroupsOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["group_ids"] = group_ids

        request = MetorialRequest(
            path=['portals', portal_id, 'consumer-profile', consumer_profile_id, 'assign-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsConsumerProfilesAssignGroupsOutput.from_dict)

    def unassign_groups(self, portal_id: str, consumer_profile_id: str, *, group_ids: List[str]) -> DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput:
        """
    Unassign portal consumer profile groups
    Removes one or more groups from a portal consumer profile.

    :param portal_id: str
    :param consumer_profile_id: str
    :param group_ids: List[str]
    :return: DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["group_ids"] = group_ids

        request = MetorialRequest(
            path=['portals', portal_id, 'consumer-profile', consumer_profile_id, 'unassign-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsConsumerProfilesUnassignGroupsOutput.from_dict)