from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceFileLinksListOutput, DashboardInstanceFileLinksListOutput, mapDashboardInstanceFileLinksListQuery, DashboardInstanceFileLinksListQuery, mapDashboardInstanceFileLinksGetOutput, DashboardInstanceFileLinksGetOutput, mapDashboardInstanceFileLinksCreateOutput, DashboardInstanceFileLinksCreateOutput, mapDashboardInstanceFileLinksCreateBody, DashboardInstanceFileLinksCreateBody, mapDashboardInstanceFileLinksDeleteOutput, DashboardInstanceFileLinksDeleteOutput

class MetorialFileLinksEndpoint(BaseMetorialEndpoint):
    """Files are private by default. If you want to share a file, you can create a link for it. Links are public and do not require authentication to access, so be careful with what you share."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, file_id: Optional[str] = None) -> DashboardInstanceFileLinksListOutput:
        """
    List file links
    Returns a paginated list of file links owned by the instance organization.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param file_id: Optional[str] (optional)
    :return: DashboardInstanceFileLinksListOutput
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
        if file_id is not None:
            query_dict["file_id"] = file_id

        request = MetorialRequest(
            path=['file-links'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceFileLinksListOutput.from_dict)

    def get(self, link_id: str) -> DashboardInstanceFileLinksGetOutput:
        """
    Get file link by ID
    Retrieves the details of a specific file link by its ID.

    :param link_id: str
    :return: DashboardInstanceFileLinksGetOutput
    """
        request = MetorialRequest(
            path=['file-links', link_id]
        )
        return self._get(request).transform(mapDashboardInstanceFileLinksGetOutput.from_dict)

    def create(self, *, file_id: str, expires_at: Optional[datetime] = None) -> DashboardInstanceFileLinksCreateOutput:
        """
    Create file link
    Creates a new link for a specific file.

    :param file_id: str
    :param expires_at: Optional[datetime] (optional)
    :return: DashboardInstanceFileLinksCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["file_id"] = file_id
        if expires_at is not None:
            body_dict["expires_at"] = expires_at

        request = MetorialRequest(
            path=['file-links'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceFileLinksCreateOutput.from_dict)

    def delete(self, link_id: str) -> DashboardInstanceFileLinksDeleteOutput:
        """
    Delete file link by ID
    Deletes a specific file link by its ID.

    :param link_id: str
    :return: DashboardInstanceFileLinksDeleteOutput
    """
        request = MetorialRequest(
            path=['file-links', link_id]
        )
        return self._delete(request).transform(mapDashboardInstanceFileLinksDeleteOutput.from_dict)