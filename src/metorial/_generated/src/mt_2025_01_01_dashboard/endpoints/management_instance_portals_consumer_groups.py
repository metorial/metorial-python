from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsConsumerGroupsListOutput, DashboardInstancePortalsConsumerGroupsListOutput, mapDashboardInstancePortalsConsumerGroupsListQuery, DashboardInstancePortalsConsumerGroupsListQuery, mapDashboardInstancePortalsConsumerGroupsGetOutput, DashboardInstancePortalsConsumerGroupsGetOutput, mapDashboardInstancePortalsConsumerGroupsCreateOutput, DashboardInstancePortalsConsumerGroupsCreateOutput, mapDashboardInstancePortalsConsumerGroupsCreateBody, DashboardInstancePortalsConsumerGroupsCreateBody, mapDashboardInstancePortalsConsumerGroupsUpdateOutput, DashboardInstancePortalsConsumerGroupsUpdateOutput, mapDashboardInstancePortalsConsumerGroupsUpdateBody, DashboardInstancePortalsConsumerGroupsUpdateBody, mapDashboardInstancePortalsConsumerGroupsDeleteOutput, DashboardInstancePortalsConsumerGroupsDeleteOutput

class MetorialManagementInstancePortalsConsumerGroupsEndpoint(BaseMetorialEndpoint):
    """Manage the consumer groups that drive portal visibility and access rules."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstancePortalsConsumerGroupsListOutput:
        """
    List portal consumer groups
    Returns a paginated list of consumer groups for a portal.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstancePortalsConsumerGroupsListOutput
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
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'consumer-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerGroupsListOutput.from_dict)

    def get(self, instance_id: str, portal_id: str, consumer_group_id: str) -> DashboardInstancePortalsConsumerGroupsGetOutput:
        """
    Get portal consumer group
    Retrieves a portal consumer group by ID.

    :param instance_id: str
    :param portal_id: str
    :param consumer_group_id: str
    :return: DashboardInstancePortalsConsumerGroupsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'consumer-groups', consumer_group_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerGroupsGetOutput.from_dict)

    def create(self, instance_id: str, portal_id: str, *, name: str, description: Optional[str] = None, sso_group_ids: Optional[List[str]] = None, is_default: Optional[bool] = None) -> DashboardInstancePortalsConsumerGroupsCreateOutput:
        """
    Create portal consumer group
    Creates a new consumer group for the portal.

    :param instance_id: str
    :param portal_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param sso_group_ids: Optional[List[str]] (optional)
    :param is_default: Optional[bool] (optional)
    :return: DashboardInstancePortalsConsumerGroupsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if sso_group_ids is not None:
            body_dict["sso_group_ids"] = sso_group_ids
        if is_default is not None:
            body_dict["is_default"] = is_default

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'consumer-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsConsumerGroupsCreateOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, consumer_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, sso_group_ids: Optional[List[str]] = None, is_default: Optional[bool] = None) -> DashboardInstancePortalsConsumerGroupsUpdateOutput:
        """
    Update portal consumer group
    Updates a consumer group for the portal.

    :param instance_id: str
    :param portal_id: str
    :param consumer_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param sso_group_ids: Optional[List[str]] (optional)
    :param is_default: Optional[bool] (optional)
    :return: DashboardInstancePortalsConsumerGroupsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if sso_group_ids is not None:
            body_dict["sso_group_ids"] = sso_group_ids
        if is_default is not None:
            body_dict["is_default"] = is_default

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'consumer-groups', consumer_group_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsConsumerGroupsUpdateOutput.from_dict)

    def delete(self, instance_id: str, portal_id: str, consumer_group_id: str) -> DashboardInstancePortalsConsumerGroupsDeleteOutput:
        """
    Delete portal consumer group
    Archives a consumer group for the portal.

    :param instance_id: str
    :param portal_id: str
    :param consumer_group_id: str
    :return: DashboardInstancePortalsConsumerGroupsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id, 'consumer-groups', consumer_group_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsConsumerGroupsDeleteOutput.from_dict)