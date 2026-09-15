from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbackInstancesListOutput, DashboardInstanceCallbackInstancesListOutput, mapDashboardInstanceCallbackInstancesListQuery, DashboardInstanceCallbackInstancesListQuery, mapDashboardInstanceCallbackInstancesGetOutput, DashboardInstanceCallbackInstancesGetOutput

class MetorialCallbackInstancesEndpoint(BaseMetorialEndpoint):
    """A callback instance is a callback as it applies to one integration instance provider. Metorial reconciles one for every matching integration instance, so these are read-only."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, callback_id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, integration_instance_id: Optional[Union[str, List[str]]] = None, integration_instance_provider_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbackInstancesListOutput:
        """
    List callback instances
    Returns a paginated list of callback instances.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param callback_id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param integration_instance_id: Optional[Union[str, List[str]]] (optional)
    :param integration_instance_provider_id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCallbackInstancesListOutput
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
        if callback_id is not None:
            query_dict["callback_id"] = callback_id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if integration_instance_id is not None:
            query_dict["integration_instance_id"] = integration_instance_id
        if integration_instance_provider_id is not None:
            query_dict["integration_instance_provider_id"] = integration_instance_provider_id
        if status is not None:
            query_dict["status"] = status
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['callback-instances'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbackInstancesListOutput.from_dict)

    def get(self, callback_instance_id: str) -> DashboardInstanceCallbackInstancesGetOutput:
        """
    Get callback instance
    Retrieves a specific callback instance by ID.

    :param callback_instance_id: str
    :return: DashboardInstanceCallbackInstancesGetOutput
    """
        request = MetorialRequest(
            path=['callback-instances', callback_instance_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbackInstancesGetOutput.from_dict)