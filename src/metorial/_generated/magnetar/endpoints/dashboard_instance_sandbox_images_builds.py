from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxImagesBuildsListOutput, DashboardInstanceSandboxImagesBuildsListOutput, mapDashboardInstanceSandboxImagesBuildsListQuery, DashboardInstanceSandboxImagesBuildsListQuery, mapDashboardInstanceSandboxImagesBuildsCreateOutput, DashboardInstanceSandboxImagesBuildsCreateOutput, mapDashboardInstanceSandboxImagesBuildsCreateBody, DashboardInstanceSandboxImagesBuildsCreateBody

class MetorialDashboardInstanceSandboxImagesBuildsEndpoint(BaseMetorialEndpoint):
    """Images machines boot from. Metorial provides global images, and you can build your own from a Dockerfile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, image_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, image_version_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxImagesBuildsListOutput:
        """
    List image builds
    Returns a paginated list of the builds of an image.

    :param instance_id: str
    :param image_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param image_version_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxImagesBuildsListOutput
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
        if image_version_id is not None:
            query_dict["image_version_id"] = image_version_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'images', image_id, 'builds'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImagesBuildsListOutput.from_dict)

    def create(self, instance_id: str, image_id: str, *, file_id: str, dockerfile_path: Optional[str] = None, context_path: Optional[str] = None, target: Optional[str] = None, build_args: Optional[Dict[str, str]] = None, timeout_seconds: Optional[float] = None, disk_size_bytes: Optional[float] = None) -> DashboardInstanceSandboxImagesBuildsCreateOutput:
        """
    Build image
    Builds a new version of an image from a Dockerfile. Upload the build context as a file with the sandbox_image_build_context purpose first.

    :param instance_id: str
    :param image_id: str
    :param file_id: str
    :param dockerfile_path: Optional[str] (optional)
    :param context_path: Optional[str] (optional)
    :param target: Optional[str] (optional)
    :param build_args: Optional[Dict[str, str]] (optional)
    :param timeout_seconds: Optional[float] (optional)
    :param disk_size_bytes: Optional[float] (optional)
    :return: DashboardInstanceSandboxImagesBuildsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["file_id"] = file_id
        if dockerfile_path is not None:
            body_dict["dockerfile_path"] = dockerfile_path
        if context_path is not None:
            body_dict["context_path"] = context_path
        if target is not None:
            body_dict["target"] = target
        if build_args is not None:
            body_dict["build_args"] = build_args
        if timeout_seconds is not None:
            body_dict["timeout_seconds"] = timeout_seconds
        if disk_size_bytes is not None:
            body_dict["disk_size_bytes"] = disk_size_bytes

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'images', image_id, 'builds'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxImagesBuildsCreateOutput.from_dict)