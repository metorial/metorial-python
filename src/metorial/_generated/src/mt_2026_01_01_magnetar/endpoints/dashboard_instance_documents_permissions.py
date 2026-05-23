from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsPermissionsGetOutput, DashboardInstanceDocumentsPermissionsGetOutput

class MetorialDashboardInstanceDocumentsPermissionsEndpoint(BaseMetorialEndpoint):
    """Create and manage instance documents backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, document_id: str) -> DashboardInstanceDocumentsPermissionsGetOutput:
        """
    Get document permissions
    Returns the effective Cargo permissions for the current actor on a specific document.

    :param instance_id: str
    :param document_id: str
    :return: DashboardInstanceDocumentsPermissionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'documents', document_id, 'permissions']
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsPermissionsGetOutput.from_dict)