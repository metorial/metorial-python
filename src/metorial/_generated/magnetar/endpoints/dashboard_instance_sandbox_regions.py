from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxRegionsListOutput, DashboardInstanceSandboxRegionsListOutput, mapDashboardInstanceSandboxRegionsListQuery, DashboardInstanceSandboxRegionsListQuery, mapDashboardInstanceSandboxRegionsGetOutput, DashboardInstanceSandboxRegionsGetOutput

class MetorialDashboardInstanceSandboxRegionsEndpoint(BaseMetorialEndpoint):
    """Regions in which sandbox machines, disks, and images are available."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSandboxRegionsListOutput:
        """
    List sandbox regions
    Returns a paginated list of regions sandboxes can run in.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSandboxRegionsListOutput
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
            path=['dashboard', 'instances', instance_id, 'sandbox', 'regions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxRegionsListOutput.from_dict)

    def get(self, instance_id: str, region_id: str) -> DashboardInstanceSandboxRegionsGetOutput:
        """
    Get sandbox region
    Retrieves a sandbox region by its identifier.

    :param instance_id: str
    :param region_id: str
    :return: DashboardInstanceSandboxRegionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'regions', region_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxRegionsGetOutput.from_dict)