from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceLinksListOutput, DashboardInstanceLinksListOutput, mapDashboardInstanceLinksGetOutput, DashboardInstanceLinksGetOutput, mapDashboardInstanceLinksCreateOutput, DashboardInstanceLinksCreateOutput, mapDashboardInstanceLinksCreateBody, DashboardInstanceLinksCreateBody, mapDashboardInstanceLinksUpdateOutput, DashboardInstanceLinksUpdateOutput, mapDashboardInstanceLinksUpdateBody, DashboardInstanceLinksUpdateBody, mapDashboardInstanceLinksDeleteOutput, DashboardInstanceLinksDeleteOutput

class MetorialManagementInstanceLinksEndpoint(BaseMetorialEndpoint):
    """Files are private by default. If you want to share a file, you can create a link for it. Links are public and do not require authentication to access, so be careful with what you share."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instanceId: str, fileId: str):
        """
    List file links
    Returns a list of links associated with a specific file.

    :param instanceId: str
    :param fileId: str
    :return: DashboardInstanceLinksListOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'files', fileId, 'links']
        )
        return self._get(request).transform(mapDashboardInstanceLinksListOutput.from_dict)

    def get(self, instanceId: str, fileId: str, linkId: str):
        """
    Get file link by ID
    Retrieves the details of a specific file link by its ID.

    :param instanceId: str
    :param fileId: str
    :param linkId: str
    :return: DashboardInstanceLinksGetOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'files', fileId, 'links', linkId]
        )
        return self._get(request).transform(mapDashboardInstanceLinksGetOutput.from_dict)

    def create(self, instanceId: str, fileId: str, body: DashboardInstanceLinksCreateBody):
        """
    Create file link
    Creates a new link for a specific file.

    :param instanceId: str
    :param fileId: str
    :param body: DashboardInstanceLinksCreateBody
    :return: DashboardInstanceLinksCreateOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'files', fileId, 'links'],
            body=mapDashboardInstanceLinksCreateBody.to_dict(body),
        )
        return self._post(request).transform(mapDashboardInstanceLinksCreateOutput.from_dict)

    def update(self, instanceId: str, fileId: str, linkId: str, body: DashboardInstanceLinksUpdateBody):
        """
    Update file link by ID
    Updates a file link’s properties, such as expiration.

    :param instanceId: str
    :param fileId: str
    :param linkId: str
    :param body: DashboardInstanceLinksUpdateBody
    :return: DashboardInstanceLinksUpdateOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'files', fileId, 'links', linkId],
            body=mapDashboardInstanceLinksUpdateBody.to_dict(body),
        )
        return self._patch(request).transform(mapDashboardInstanceLinksUpdateOutput.from_dict)

    def delete(self, instanceId: str, fileId: str, linkId: str):
        """
    Delete file link by ID
    Deletes a specific file link by its ID.

    :param instanceId: str
    :param fileId: str
    :param linkId: str
    :return: DashboardInstanceLinksDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instanceId, 'files', fileId, 'links', linkId]
        )
        return self._delete(request).transform(mapDashboardInstanceLinksDeleteOutput.from_dict)