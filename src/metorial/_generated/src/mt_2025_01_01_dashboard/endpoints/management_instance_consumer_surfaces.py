from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceConsumerSurfacesListOutput, DashboardInstanceConsumerSurfacesListOutput, mapDashboardInstanceConsumerSurfacesListQuery, DashboardInstanceConsumerSurfacesListQuery, mapDashboardInstanceConsumerSurfacesGetOutput, DashboardInstanceConsumerSurfacesGetOutput

class MetorialManagementInstanceConsumerSurfacesEndpoint(BaseMetorialEndpoint):
    """List and retrieve consumer surfaces for an instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceConsumerSurfacesListOutput:
        """
    List consumer surfaces
    Returns a paginated list of consumer surfaces for an instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceConsumerSurfacesListOutput
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
            path=['instances', instance_id, 'consumer-surfaces'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceConsumerSurfacesListOutput.from_dict)

    def get(self, instance_id: str, consumer_surface_id: str) -> DashboardInstanceConsumerSurfacesGetOutput:
        """
    Get consumer surface
    Retrieves a consumer surface by ID.

    :param instance_id: str
    :param consumer_surface_id: str
    :return: DashboardInstanceConsumerSurfacesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'consumer-surfaces', consumer_surface_id]
        )
        return self._get(request).transform(mapDashboardInstanceConsumerSurfacesGetOutput.from_dict)