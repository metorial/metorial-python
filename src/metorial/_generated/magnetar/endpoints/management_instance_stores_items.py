from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceStoresItemsModifyOutput, DashboardInstanceStoresItemsModifyOutput, mapDashboardInstanceStoresItemsModifyBody, DashboardInstanceStoresItemsModifyBody, mapDashboardInstanceStoresItemsListOutput, DashboardInstanceStoresItemsListOutput, mapDashboardInstanceStoresItemsListQuery, DashboardInstanceStoresItemsListQuery, mapDashboardInstanceStoresItemsGetOutput, DashboardInstanceStoresItemsGetOutput

class MetorialManagementInstanceStoresItemsEndpoint(BaseMetorialEndpoint):
    """Create and manage instance stores backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def modify(self, instance_id: str, store_id: str, *, operations: List[Dict[str, Any]]) -> DashboardInstanceStoresItemsModifyOutput:
        """
    Modify store items
    Applies bulk item operations to a specific store.

    :param instance_id: str
    :param store_id: str
    :param operations: List[Dict[str, Any]]
    :return: DashboardInstanceStoresItemsModifyOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["operations"] = operations

        request = MetorialRequest(
            path=['instances', instance_id, 'stores', store_id, 'items'],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceStoresItemsModifyOutput.from_dict)

    def list(self, instance_id: str, store_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, file_id: Optional[Union[str, List[str]]] = None, document_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceStoresItemsListOutput:
        """
    List store items
    Returns a paginated list of items for a specific store.

    :param instance_id: str
    :param store_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param file_id: Optional[Union[str, List[str]]] (optional)
    :param document_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceStoresItemsListOutput
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
        if file_id is not None:
            query_dict["file_id"] = file_id
        if document_id is not None:
            query_dict["document_id"] = document_id
        if type is not None:
            query_dict["type"] = type
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'stores', store_id, 'items'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceStoresItemsListOutput.from_dict)

    def get(self, instance_id: str, store_id: str, item_id: str) -> DashboardInstanceStoresItemsGetOutput:
        """
    Get store item by ID
    Retrieves a specific item within a store.

    :param instance_id: str
    :param store_id: str
    :param item_id: str
    :return: DashboardInstanceStoresItemsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'stores', store_id, 'items', item_id]
        )
        return self._get(request).transform(mapDashboardInstanceStoresItemsGetOutput.from_dict)