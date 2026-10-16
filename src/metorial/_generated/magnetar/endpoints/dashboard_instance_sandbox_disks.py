from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxDisksListOutput, DashboardInstanceSandboxDisksListOutput, mapDashboardInstanceSandboxDisksListQuery, DashboardInstanceSandboxDisksListQuery, mapDashboardInstanceSandboxDisksGetOutput, DashboardInstanceSandboxDisksGetOutput, mapDashboardInstanceSandboxDisksCreateOutput, DashboardInstanceSandboxDisksCreateOutput, mapDashboardInstanceSandboxDisksCreateBody, DashboardInstanceSandboxDisksCreateBody, mapDashboardInstanceSandboxDisksUpdateOutput, DashboardInstanceSandboxDisksUpdateOutput, mapDashboardInstanceSandboxDisksUpdateBody, DashboardInstanceSandboxDisksUpdateBody, mapDashboardInstanceSandboxDisksDeleteOutput, DashboardInstanceSandboxDisksDeleteOutput, mapDashboardInstanceSandboxDisksCloneOutput, DashboardInstanceSandboxDisksCloneOutput, mapDashboardInstanceSandboxDisksCloneBody, DashboardInstanceSandboxDisksCloneBody, mapDashboardInstanceSandboxDisksResizeOutput, DashboardInstanceSandboxDisksResizeOutput, mapDashboardInstanceSandboxDisksResizeBody, DashboardInstanceSandboxDisksResizeBody

class MetorialDashboardInstanceSandboxDisksEndpoint(BaseMetorialEndpoint):
    """Persistent disks that can be mounted into machines. Every machine also has a root filesystem disk that is managed for it."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, machine_id: Optional[Union[str, List[str]]] = None, region: Optional[Union[str, List[str]]] = None, attached: Optional[bool] = None, search: Optional[str] = None) -> DashboardInstanceSandboxDisksListOutput:
        """
    List sandbox disks
    Returns a paginated list of disks.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param machine_id: Optional[Union[str, List[str]]] (optional)
    :param region: Optional[Union[str, List[str]]] (optional)
    :param attached: Optional[bool] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceSandboxDisksListOutput
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
        if id is not None:
            query_dict["id"] = id
        if type is not None:
            query_dict["type"] = type
        if machine_id is not None:
            query_dict["machine_id"] = machine_id
        if region is not None:
            query_dict["region"] = region
        if attached is not None:
            query_dict["attached"] = attached
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxDisksListOutput.from_dict)

    def get(self, instance_id: str, disk_id: str) -> DashboardInstanceSandboxDisksGetOutput:
        """
    Get sandbox disk
    Retrieves a disk by ID.

    :param instance_id: str
    :param disk_id: str
    :return: DashboardInstanceSandboxDisksGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks', disk_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxDisksGetOutput.from_dict)

    def create(self, instance_id: str, *, region: str, metadata: Optional[Dict[str, Any]] = None, name: Optional[str] = None, size_bytes: Optional[float] = None) -> DashboardInstanceSandboxDisksCreateOutput:
        """
    Create sandbox disk
    Creates an empty disk.

    :param instance_id: str
    :param region: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param name: Optional[str] (optional)
    :param size_bytes: Optional[float] (optional)
    :return: DashboardInstanceSandboxDisksCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["region"] = region
        if metadata is not None:
            body_dict["metadata"] = metadata
        if name is not None:
            body_dict["name"] = name
        if size_bytes is not None:
            body_dict["size_bytes"] = size_bytes

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxDisksCreateOutput.from_dict)

    def update(self, instance_id: str, disk_id: str, *, metadata: Optional[Dict[str, Any]] = None, name: Optional[str] = None) -> DashboardInstanceSandboxDisksUpdateOutput:
        """
    Update sandbox disk
    Updates a disk name and metadata. Only metadata can be updated for root filesystem disks.

    :param instance_id: str
    :param disk_id: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param name: Optional[str] (optional)
    :return: DashboardInstanceSandboxDisksUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if metadata is not None:
            body_dict["metadata"] = metadata
        if name is not None:
            body_dict["name"] = name

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks', disk_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSandboxDisksUpdateOutput.from_dict)

    def delete(self, instance_id: str, disk_id: str) -> DashboardInstanceSandboxDisksDeleteOutput:
        """
    Delete sandbox disk
    Deletes a disk. Root filesystem disks cannot be deleted; they are removed with their machine.

    :param instance_id: str
    :param disk_id: str
    :return: DashboardInstanceSandboxDisksDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks', disk_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSandboxDisksDeleteOutput.from_dict)

    def clone(self, instance_id: str, disk_id: str, *, metadata: Optional[Dict[str, Any]] = None, name: Optional[str] = None) -> DashboardInstanceSandboxDisksCloneOutput:
        """
    Clone sandbox disk
    Creates a copy of a disk in the same region.

    :param instance_id: str
    :param disk_id: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param name: Optional[str] (optional)
    :return: DashboardInstanceSandboxDisksCloneOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if metadata is not None:
            body_dict["metadata"] = metadata
        if name is not None:
            body_dict["name"] = name

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks', disk_id, 'clone'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxDisksCloneOutput.from_dict)

    def resize(self, instance_id: str, disk_id: str, *, size_bytes: float) -> DashboardInstanceSandboxDisksResizeOutput:
        """
    Resize sandbox disk
    Starts growing a disk to a larger size.

    :param instance_id: str
    :param disk_id: str
    :param size_bytes: float
    :return: DashboardInstanceSandboxDisksResizeOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["size_bytes"] = size_bytes

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'disks', disk_id, 'resize'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxDisksResizeOutput.from_dict)