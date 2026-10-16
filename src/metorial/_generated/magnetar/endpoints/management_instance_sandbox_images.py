from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxImagesListOutput, DashboardInstanceSandboxImagesListOutput, mapDashboardInstanceSandboxImagesListQuery, DashboardInstanceSandboxImagesListQuery, mapDashboardInstanceSandboxImagesGetOutput, DashboardInstanceSandboxImagesGetOutput, mapDashboardInstanceSandboxImagesCreateOutput, DashboardInstanceSandboxImagesCreateOutput, mapDashboardInstanceSandboxImagesCreateBody, DashboardInstanceSandboxImagesCreateBody, mapDashboardInstanceSandboxImagesUpdateOutput, DashboardInstanceSandboxImagesUpdateOutput, mapDashboardInstanceSandboxImagesUpdateBody, DashboardInstanceSandboxImagesUpdateBody, mapDashboardInstanceSandboxImagesDeleteOutput, DashboardInstanceSandboxImagesDeleteOutput

class MetorialManagementInstanceSandboxImagesEndpoint(BaseMetorialEndpoint):
    """Images machines boot from. Metorial provides global images, and you can build your own from a Dockerfile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, owner: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstanceSandboxImagesListOutput:
        """
    List sandbox images
    Returns a paginated list of the images you can create machines from.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param owner: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceSandboxImagesListOutput
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
        if owner is not None:
            query_dict["owner"] = owner
        if status is not None:
            query_dict["status"] = status
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'images'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImagesListOutput.from_dict)

    def get(self, instance_id: str, image_id: str) -> DashboardInstanceSandboxImagesGetOutput:
        """
    Get sandbox image
    Retrieves an image by ID.

    :param instance_id: str
    :param image_id: str
    :return: DashboardInstanceSandboxImagesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'images', image_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImagesGetOutput.from_dict)

    def create(self, instance_id: str, *, name: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSandboxImagesCreateOutput:
        """
    Create sandbox image
    Creates an empty image. Build a version of it to make it available to machines.

    :param instance_id: str
    :param name: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSandboxImagesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'images'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxImagesCreateOutput.from_dict)

    def update(self, instance_id: str, image_id: str, *, name: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSandboxImagesUpdateOutput:
        """
    Update sandbox image
    Updates the name and metadata of one of your images.

    :param instance_id: str
    :param image_id: str
    :param name: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSandboxImagesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'images', image_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSandboxImagesUpdateOutput.from_dict)

    def delete(self, instance_id: str, image_id: str) -> DashboardInstanceSandboxImagesDeleteOutput:
        """
    Delete sandbox image
    Deletes one of your images and cancels its running builds.

    :param instance_id: str
    :param image_id: str
    :return: DashboardInstanceSandboxImagesDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'images', image_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSandboxImagesDeleteOutput.from_dict)