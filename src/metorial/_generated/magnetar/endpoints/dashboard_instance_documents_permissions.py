from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsPermissionsGetOutput, DashboardInstanceDocumentsPermissionsGetOutput

class MetorialDashboardInstanceDocumentsPermissionsEndpoint(BaseMetorialEndpoint):
    """A document is rich text with comments, versions, and participants."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, document_id: str) -> DashboardInstanceDocumentsPermissionsGetOutput:
        """
    Get document permissions
    Returns what the caller can do with a document.

    :param instance_id: str
    :param document_id: str
    :return: DashboardInstanceDocumentsPermissionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents', document_id, 'permissions']
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsPermissionsGetOutput.from_dict)