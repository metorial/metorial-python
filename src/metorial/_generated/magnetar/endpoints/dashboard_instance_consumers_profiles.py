from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceConsumersProfilesListOutput, DashboardInstanceConsumersProfilesListOutput, mapDashboardInstanceConsumersProfilesListQuery, DashboardInstanceConsumersProfilesListQuery, mapDashboardInstanceConsumersProfilesGetOutput, DashboardInstanceConsumersProfilesGetOutput

class MetorialDashboardInstanceConsumersProfilesEndpoint(BaseMetorialEndpoint):
    """Manage instance consumers independently from portals and inspect the profiles linked to each consumer."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, consumer_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceConsumersProfilesListOutput:
        """
    List consumer profiles
    Returns a paginated list of profiles for a consumer in an instance.

    :param instance_id: str
    :param consumer_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceConsumersProfilesListOutput
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

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumers', consumer_id, 'profiles'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceConsumersProfilesListOutput.from_dict)

    def get(self, instance_id: str, consumer_id: str, consumer_profile_id: str) -> DashboardInstanceConsumersProfilesGetOutput:
        """
    Get consumer profile
    Retrieves a consumer profile by ID for a consumer.

    :param instance_id: str
    :param consumer_id: str
    :param consumer_profile_id: str
    :return: DashboardInstanceConsumersProfilesGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'consumers', consumer_id, 'profiles', consumer_profile_id]
        )
        return self._get(request).transform(mapDashboardInstanceConsumersProfilesGetOutput.from_dict)