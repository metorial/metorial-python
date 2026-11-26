from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsEditTokenGetOutput, DashboardInstanceDocumentsEditTokenGetOutput

class MetorialDocumentsEditTokenEndpoint(BaseMetorialEndpoint):
    """A document is rich text with comments, versions, and participants."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, document_id: str) -> DashboardInstanceDocumentsEditTokenGetOutput:
        """
    Get document edit token
    Returns a short-lived read or write token for establishing a live document session. Requires write scopes, even when the issued token only grants read access.

    :param document_id: str
    :return: DashboardInstanceDocumentsEditTokenGetOutput
    """
        request = MetorialRequest(
            path=['documents', document_id, 'edit-token']
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsEditTokenGetOutput.from_dict)