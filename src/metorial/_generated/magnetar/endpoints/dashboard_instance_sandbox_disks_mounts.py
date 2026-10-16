from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxDisksMountsListOutput, DashboardInstanceSandboxDisksMountsListOutput, mapDashboardInstanceSandboxDisksMountsListQuery, DashboardInstanceSandboxDisksMountsListQuery

class MetorialDashboardInstanceSandboxDisksMountsEndpoint(BaseMetorialEndpoint):
    """Persistent disks that can be mounted into machines. Every machine also has a root filesystem disk that is managed for it."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, disk_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSandboxDisksMountsListOutput:
        """
    List disk mounts
    Returns a paginated list of the times a disk was mounted into a machine.

    :param instance_id: str
    :param disk_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSandboxDisksMountsListOutput
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
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks', disk_id, 'mounts'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxDisksMountsListOutput.from_dict)