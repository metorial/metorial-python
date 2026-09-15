from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsEditTokenGetOutput, DashboardInstanceDocumentsEditTokenGetOutput

class MetorialDocumentsEditTokenEndpoint(BaseMetorialEndpoint):
    """Create and manage instance documents backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, document_id: str) -> DashboardInstanceDocumentsEditTokenGetOutput:
        """
    Get document edit token
    Returns a short-lived read or write token for establishing a live document session.

    :param document_id: str
    :return: DashboardInstanceDocumentsEditTokenGetOutput
    """
        request = MetorialRequest(
            path=['documents', document_id, 'edit-token']
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsEditTokenGetOutput.from_dict)