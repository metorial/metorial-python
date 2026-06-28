from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceConsumersListOutput, DashboardInstanceConsumersListOutput, mapDashboardInstanceConsumersListQuery, DashboardInstanceConsumersListQuery, mapDashboardInstanceConsumersGetOutput, DashboardInstanceConsumersGetOutput, mapDashboardInstanceConsumersCreateOutput, DashboardInstanceConsumersCreateOutput, mapDashboardInstanceConsumersCreateBody, DashboardInstanceConsumersCreateBody, mapDashboardInstanceConsumersGetMemberConsumerOutput, DashboardInstanceConsumersGetMemberConsumerOutput, mapDashboardInstanceConsumersGetMemberConsumerBody, DashboardInstanceConsumersGetMemberConsumerBody, mapDashboardInstanceConsumersUpdateOutput, DashboardInstanceConsumersUpdateOutput, mapDashboardInstanceConsumersUpdateBody, DashboardInstanceConsumersUpdateBody

class MetorialDashboardInstanceConsumersEndpoint(BaseMetorialEndpoint):
    """Manage instance consumers independently from portals and inspect the profiles linked to each consumer."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, email: Optional[Union[str, List[str]]] = None, id: Optional[str] = None) -> DashboardInstanceConsumersListOutput:
        """
    List consumers
    Returns a paginated list of consumers for an instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param email: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[str] (optional)
    :return: DashboardInstanceConsumersListOutput
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
        if email is not None:
            query_dict["email"] = email
        if id is not None:
            query_dict["id"] = id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceConsumersListOutput.from_dict)

    def get(self, instance_id: str, consumer_id: str) -> DashboardInstanceConsumersGetOutput:
        """
    Get consumer
    Retrieves a consumer by ID.

    :param instance_id: str
    :param consumer_id: str
    :return: DashboardInstanceConsumersGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumers', consumer_id]
        )
        return self._get(request).transform(mapDashboardInstanceConsumersGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, email: str) -> DashboardInstanceConsumersCreateOutput:
        """
    Create consumer
    Creates or links a consumer for an instance.

    :param instance_id: str
    :param name: str
    :param email: str
    :return: DashboardInstanceConsumersCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        body_dict["email"] = email

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumers'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceConsumersCreateOutput.from_dict)

    def get_member_consumer(self, instance_id: str, *, surface_identifier: Optional[str] = None) -> DashboardInstanceConsumersGetMemberConsumerOutput:
        """
    Get member consumer
    Upserts and returns the consumer for the authenticated organization member.

    :param instance_id: str
    :param surface_identifier: Optional[str] (optional)
    :return: DashboardInstanceConsumersGetMemberConsumerOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if surface_identifier is not None:
            body_dict["surface_identifier"] = surface_identifier

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'get-member-consumer'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceConsumersGetMemberConsumerOutput.from_dict)

    def update(self, instance_id: str, consumer_id: str, *, name: Optional[str] = None, email: Optional[str] = None) -> DashboardInstanceConsumersUpdateOutput:
        """
    Update consumer
    Updates a consumer for an instance.

    :param instance_id: str
    :param consumer_id: str
    :param name: Optional[str] (optional)
    :param email: Optional[str] (optional)
    :return: DashboardInstanceConsumersUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if email is not None:
            body_dict["email"] = email

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumers', consumer_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceConsumersUpdateOutput.from_dict)