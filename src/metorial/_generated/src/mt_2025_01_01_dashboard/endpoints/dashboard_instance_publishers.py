from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePublishersListOutput, DashboardInstancePublishersListOutput, mapDashboardInstancePublishersListQuery, DashboardInstancePublishersListQuery, mapDashboardInstancePublishersGetOutput, DashboardInstancePublishersGetOutput

class MetorialDashboardInstancePublishersEndpoint(BaseMetorialEndpoint):
    """A publisher is the organization or individual who created and maintains a provider."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstancePublishersListOutput:
        """
    List publishers
    Returns a paginated list of publishers.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstancePublishersListOutput
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
            path=['dashboard', 'instances', instance_id, 'publishers'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePublishersListOutput.from_dict)

    def get(self, instance_id: str, publisher_id: str) -> DashboardInstancePublishersGetOutput:
        """
    Get publisher
    Retrieves a specific publisher by ID.

    :param instance_id: str
    :param publisher_id: str
    :return: DashboardInstancePublishersGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'publishers', publisher_id]
        )
        return self._get(request).transform(mapDashboardInstancePublishersGetOutput.from_dict)