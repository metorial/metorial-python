from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbacksListOutput, DashboardInstanceCallbacksListOutput, mapDashboardInstanceCallbacksListQuery, DashboardInstanceCallbacksListQuery, mapDashboardInstanceCallbacksCreateOutput, DashboardInstanceCallbacksCreateOutput, mapDashboardInstanceCallbacksCreateBody, DashboardInstanceCallbacksCreateBody, mapDashboardInstanceCallbacksGetOutput, DashboardInstanceCallbacksGetOutput, mapDashboardInstanceCallbacksUpdateOutput, DashboardInstanceCallbacksUpdateOutput, mapDashboardInstanceCallbacksUpdateBody, DashboardInstanceCallbacksUpdateBody, mapDashboardInstanceCallbacksDeleteOutput, DashboardInstanceCallbacksDeleteOutput

class MetorialDashboardInstanceCallbacksEndpoint(BaseMetorialEndpoint):
    """A callback is what receives provider events for an integration provider. Creating one enables callbacks on the integration provider, and Metorial then registers the callback against every matching integration instance. Setting `callbacks.status` on the integration provider itself does the same thing."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, integration_provider_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbacksListOutput:
        """
    List callbacks
    Returns a paginated list of callbacks.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param integration_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCallbacksListOutput
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
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if integration_provider_id is not None:
            query_dict["integration_provider_id"] = integration_provider_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callbacks'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksListOutput.from_dict)

    def create(self, instance_id: str, *, integration_id: str, integration_provider_id: str, name: Optional[str] = None, description: Optional[str] = None) -> DashboardInstanceCallbacksCreateOutput:
        """
    Create callback
    Enables callbacks for an integration provider and returns the callback it created. Only providers whose type reports `triggers.status` as `enabled` support this. Callback instances are then registered for every matching integration instance in the background.

    :param instance_id: str
    :param integration_id: str
    :param integration_provider_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: DashboardInstanceCallbacksCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["integration_id"] = integration_id
        body_dict["integration_provider_id"] = integration_provider_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callbacks'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCallbacksCreateOutput.from_dict)

    def get(self, instance_id: str, callback_id: str) -> DashboardInstanceCallbacksGetOutput:
        """
    Get callback
    Retrieves a specific callback by ID.

    :param instance_id: str
    :param callback_id: str
    :return: DashboardInstanceCallbacksGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callbacks', callback_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksGetOutput.from_dict)

    def update(self, instance_id: str, callback_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbacksUpdateOutput:
        """
    Update callback
    Updates the name, description or metadata of a callback. Everything else about a callback is derived from its integration provider - set `callbacks.status` to `disabled` there to tear it down.

    :param instance_id: str
    :param callback_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCallbacksUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callbacks', callback_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceCallbacksUpdateOutput.from_dict)

    def delete(self, instance_id: str, callback_id: str) -> DashboardInstanceCallbacksDeleteOutput:
        """
    Delete callback
    Disables callbacks on the underlying integration provider, tearing down this callback and every callback instance registered for it.

    :param instance_id: str
    :param callback_id: str
    :return: DashboardInstanceCallbacksDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'callbacks', callback_id]
        )
        return self._delete(request).transform(mapDashboardInstanceCallbacksDeleteOutput.from_dict)