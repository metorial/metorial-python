from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxImageBuildsListOutput, DashboardInstanceSandboxImageBuildsListOutput, mapDashboardInstanceSandboxImageBuildsListQuery, DashboardInstanceSandboxImageBuildsListQuery, mapDashboardInstanceSandboxImageBuildsGetOutput, DashboardInstanceSandboxImageBuildsGetOutput, mapDashboardInstanceSandboxImageBuildsCancelOutput, DashboardInstanceSandboxImageBuildsCancelOutput, mapDashboardInstanceSandboxImageBuildsLogsOutput, DashboardInstanceSandboxImageBuildsLogsOutput, mapDashboardInstanceSandboxImageBuildsLogsQuery, DashboardInstanceSandboxImageBuildsLogsQuery

class MetorialSandboxImageBuildsEndpoint(BaseMetorialEndpoint):
    """Builds turn a Dockerfile and its context into an image version and replicate it to every region."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, image_id: Optional[Union[str, List[str]]] = None, image_version_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxImageBuildsListOutput:
        """
    List image builds
    Returns a paginated list of image builds across all images.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param image_id: Optional[Union[str, List[str]]] (optional)
    :param image_version_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxImageBuildsListOutput
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
        if image_id is not None:
            query_dict["image_id"] = image_id
        if image_version_id is not None:
            query_dict["image_version_id"] = image_version_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['sandbox', 'image-builds'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImageBuildsListOutput.from_dict)

    def get(self, build_id: str) -> DashboardInstanceSandboxImageBuildsGetOutput:
        """
    Get image build
    Retrieves an image build by ID.

    :param build_id: str
    :return: DashboardInstanceSandboxImageBuildsGetOutput
    """
        request = MetorialRequest(
            path=['sandbox', 'image-builds', build_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImageBuildsGetOutput.from_dict)

    def cancel(self, build_id: str) -> DashboardInstanceSandboxImageBuildsCancelOutput:
        """
    Cancel image build
    Cancels a build that is still running.

    :param build_id: str
    :return: DashboardInstanceSandboxImageBuildsCancelOutput
    """
        request = MetorialRequest(
            path=['sandbox', 'image-builds', build_id, 'cancel']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxImageBuildsCancelOutput.from_dict)

    def logs(self, build_id: str, *, direction: Optional[str] = None, cursor: Optional[float] = None, limit: Optional[float] = None) -> DashboardInstanceSandboxImageBuildsLogsOutput:
        """
    Get image build logs
    Returns a page of the build output.

    :param build_id: str
    :param direction: Optional[str] (optional)
    :param cursor: Optional[float] (optional)
    :param limit: Optional[float] (optional)
    :return: DashboardInstanceSandboxImageBuildsLogsOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if direction is not None:
            query_dict["direction"] = direction
        if cursor is not None:
            query_dict["cursor"] = cursor
        if limit is not None:
            query_dict["limit"] = limit

        request = MetorialRequest(
            path=['sandbox', 'image-builds', build_id, 'logs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxImageBuildsLogsOutput.from_dict)