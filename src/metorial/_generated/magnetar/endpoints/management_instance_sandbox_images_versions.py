from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxImagesVersionsListOutput, DashboardInstanceSandboxImagesVersionsListOutput, mapDashboardInstanceSandboxImagesVersionsListQuery, DashboardInstanceSandboxImagesVersionsListQuery, mapDashboardInstanceSandboxImagesVersionsGetOutput, DashboardInstanceSandboxImagesVersionsGetOutput

class MetorialManagementInstanceSandboxImagesVersionsEndpoint(BaseMetorialEndpoint):
    """Images machines boot from. Metorial provides global images, and you can build your own from a Dockerfile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, image_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSandboxImagesVersionsListOutput:
        """
    List image versions
    Returns a paginated list of the versions of an image.

    :param instance_id: str
    :param image_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSandboxImagesVersionsListOutput
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
            path=['instances', instance_id, 'sandbox', 'images', image_id, 'versions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImagesVersionsListOutput.from_dict)

    def get(self, instance_id: str, image_id: str, version_id: str) -> DashboardInstanceSandboxImagesVersionsGetOutput:
        """
    Get image version
    Retrieves a version of an image.

    :param instance_id: str
    :param image_id: str
    :param version_id: str
    :return: DashboardInstanceSandboxImagesVersionsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'sandbox', 'images', image_id, 'versions', version_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImagesVersionsGetOutput.from_dict)