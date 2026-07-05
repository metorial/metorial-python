from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceStoresListOutput, DashboardInstanceStoresListOutput, mapDashboardInstanceStoresListQuery, DashboardInstanceStoresListQuery, mapDashboardInstanceStoresCreateOutput, DashboardInstanceStoresCreateOutput, mapDashboardInstanceStoresCreateBody, DashboardInstanceStoresCreateBody, mapDashboardInstanceStoresGetOutput, DashboardInstanceStoresGetOutput, mapDashboardInstanceStoresUpdateOutput, DashboardInstanceStoresUpdateOutput, mapDashboardInstanceStoresUpdateBody, DashboardInstanceStoresUpdateBody, mapDashboardInstanceStoresDeleteOutput, DashboardInstanceStoresDeleteOutput

class MetorialManagementInstanceStoresEndpoint(BaseMetorialEndpoint):
    """Create and manage instance stores backed by Cargo."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceStoresListOutput:
        """
    List stores
    Returns a paginated list of stores owned by the instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceStoresListOutput
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
            path=['instances', instance_id, 'stores'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceStoresListOutput.from_dict)

    def create(self, instance_id: str, *, name: str, access: Optional[str] = None, template_id: Optional[str] = None, parent_id: Optional[str] = None) -> DashboardInstanceStoresCreateOutput:
        """
    Create store
    Creates a new store for the instance.

    :param instance_id: str
    :param name: str
    :param access: Optional[str] (optional)
    :param template_id: Optional[str] (optional)
    :param parent_id: Optional[str] (optional)
    :return: DashboardInstanceStoresCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if access is not None:
            body_dict["access"] = access
        if template_id is not None:
            body_dict["template_id"] = template_id
        if parent_id is not None:
            body_dict["parent_id"] = parent_id

        request = MetorialRequest(
            path=['instances', instance_id, 'stores'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceStoresCreateOutput.from_dict)

    def get(self, instance_id: str, store_id: str) -> DashboardInstanceStoresGetOutput:
        """
    Get store by ID
    Retrieves a store by its ID.

    :param instance_id: str
    :param store_id: str
    :return: DashboardInstanceStoresGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'stores', store_id]
        )
        return self._get(request).transform(mapDashboardInstanceStoresGetOutput.from_dict)

    def update(self, instance_id: str, store_id: str, *, name: Optional[str] = None, access: Optional[str] = None) -> DashboardInstanceStoresUpdateOutput:
        """
    Update store by ID
    Updates a specific store.

    :param instance_id: str
    :param store_id: str
    :param name: Optional[str] (optional)
    :param access: Optional[str] (optional)
    :return: DashboardInstanceStoresUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if access is not None:
            body_dict["access"] = access

        request = MetorialRequest(
            path=['instances', instance_id, 'stores', store_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceStoresUpdateOutput.from_dict)

    def delete(self, instance_id: str, store_id: str) -> DashboardInstanceStoresDeleteOutput:
        """
    Delete store by ID
    Deletes a specific store.

    :param instance_id: str
    :param store_id: str
    :return: DashboardInstanceStoresDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'stores', store_id]
        )
        return self._delete(request).transform(mapDashboardInstanceStoresDeleteOutput.from_dict)