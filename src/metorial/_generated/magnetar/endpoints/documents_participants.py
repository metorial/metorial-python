from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceDocumentsParticipantsListOutput, DashboardInstanceDocumentsParticipantsListOutput, mapDashboardInstanceDocumentsParticipantsListQuery, DashboardInstanceDocumentsParticipantsListQuery, mapDashboardInstanceDocumentsParticipantsGetOutput, DashboardInstanceDocumentsParticipantsGetOutput

class MetorialDocumentsParticipantsEndpoint(BaseMetorialEndpoint):
    """Inspect document participants and their linked Metorial resources."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, document_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceDocumentsParticipantsListOutput:
        """
    List document participants
    Returns a paginated list of participants for a specific document.

    :param document_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceDocumentsParticipantsListOutput
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
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['documents', document_id, 'participants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsParticipantsListOutput.from_dict)

    def get(self, document_id: str, document_participant_id: str) -> DashboardInstanceDocumentsParticipantsGetOutput:
        """
    Get document participant by ID
    Retrieves a specific document participant by its ID.

    :param document_id: str
    :param document_participant_id: str
    :return: DashboardInstanceDocumentsParticipantsGetOutput
    """
        request = MetorialRequest(
            path=['documents', document_id, 'participants', document_participant_id]
        )
        return self._get(request).transform(mapDashboardInstanceDocumentsParticipantsGetOutput.from_dict)