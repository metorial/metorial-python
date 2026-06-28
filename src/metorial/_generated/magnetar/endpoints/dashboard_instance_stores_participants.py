from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceStoresParticipantsListOutput, DashboardInstanceStoresParticipantsListOutput, mapDashboardInstanceStoresParticipantsListQuery, DashboardInstanceStoresParticipantsListQuery, mapDashboardInstanceStoresParticipantsGetOutput, DashboardInstanceStoresParticipantsGetOutput

class MetorialDashboardInstanceStoresParticipantsEndpoint(BaseMetorialEndpoint):
    """Inspect participants assigned to an instance store."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, store_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceStoresParticipantsListOutput:
        """
    List store participants
    Returns a paginated list of participants for a specific store.

    :param instance_id: str
    :param store_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceStoresParticipantsListOutput
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
            path=['dashboard', 'instances', instance_id, 'stores', store_id, 'participants'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceStoresParticipantsListOutput.from_dict)

    def get(self, instance_id: str, store_id: str, store_participant_id: str) -> DashboardInstanceStoresParticipantsGetOutput:
        """
    Get store participant by ID
    Retrieves a specific participant within a store.

    :param instance_id: str
    :param store_id: str
    :param store_participant_id: str
    :return: DashboardInstanceStoresParticipantsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'stores', store_id, 'participants', store_participant_id]
        )
        return self._get(request).transform(mapDashboardInstanceStoresParticipantsGetOutput.from_dict)