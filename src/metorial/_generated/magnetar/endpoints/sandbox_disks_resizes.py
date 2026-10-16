from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxDisksResizesListOutput, DashboardInstanceSandboxDisksResizesListOutput, mapDashboardInstanceSandboxDisksResizesListQuery, DashboardInstanceSandboxDisksResizesListQuery, mapDashboardInstanceSandboxDisksResizesGetOutput, DashboardInstanceSandboxDisksResizesGetOutput, mapDashboardInstanceSandboxDisksResizesRetryOutput, DashboardInstanceSandboxDisksResizesRetryOutput

class MetorialSandboxDisksResizesEndpoint(BaseMetorialEndpoint):
    """Resizing a disk briefly stops the machines it is mounted into. Each resize is tracked until it completes."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, disk_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxDisksResizesListOutput:
        """
    List disk resizes
    Returns a paginated list of the resizes of a disk.

    :param disk_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxDisksResizesListOutput
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

        request = MetorialRequest(
            path=['sandbox', 'disks', disk_id, 'resizes'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxDisksResizesListOutput.from_dict)

    def get(self, disk_id: str, resize_id: str) -> DashboardInstanceSandboxDisksResizesGetOutput:
        """
    Get disk resize
    Retrieves a resize of a disk.

    :param disk_id: str
    :param resize_id: str
    :return: DashboardInstanceSandboxDisksResizesGetOutput
    """
        request = MetorialRequest(
            path=['sandbox', 'disks', disk_id, 'resizes', resize_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxDisksResizesGetOutput.from_dict)

    def retry(self, disk_id: str, resize_id: str) -> DashboardInstanceSandboxDisksResizesRetryOutput:
        """
    Retry disk resize
    Retries a resize that failed.

    :param disk_id: str
    :param resize_id: str
    :return: DashboardInstanceSandboxDisksResizesRetryOutput
    """
        request = MetorialRequest(
            path=['sandbox', 'disks', disk_id, 'resizes', resize_id, 'retry']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxDisksResizesRetryOutput.from_dict)