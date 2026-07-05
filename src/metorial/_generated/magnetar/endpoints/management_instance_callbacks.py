from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbacksListOutput, DashboardInstanceCallbacksListOutput, mapDashboardInstanceCallbacksListQuery, DashboardInstanceCallbacksListQuery, mapDashboardInstanceCallbacksGetOutput, DashboardInstanceCallbacksGetOutput, mapDashboardInstanceCallbacksCreateOutput, DashboardInstanceCallbacksCreateOutput, mapDashboardInstanceCallbacksCreateBody, DashboardInstanceCallbacksCreateBody, mapDashboardInstanceCallbacksUpdateOutput, DashboardInstanceCallbacksUpdateOutput, mapDashboardInstanceCallbacksUpdateBody, DashboardInstanceCallbacksUpdateBody, mapDashboardInstanceCallbacksDeleteOutput, DashboardInstanceCallbacksDeleteOutput

class MetorialManagementInstanceCallbacksEndpoint(BaseMetorialEndpoint):
    """Manage webhook-style callbacks backed by subspace trigger receivers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbacksListOutput:
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
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
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
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if status is not None:
            query_dict["status"] = status
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksListOutput.from_dict)

    def get(self, instance_id: str, callback_id: str) -> DashboardInstanceCallbacksGetOutput:
        """
    Get callback
    Retrieves a specific callback by ID.

    :param instance_id: str
    :param callback_id: str
    :return: DashboardInstanceCallbacksGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksGetOutput.from_dict)

    def create(self, instance_id: str, *, provider_deployment_id: str, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, poll_interval_seconds_override: Optional[float] = None, destination_ids: Optional[List[str]] = None, triggers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceCallbacksCreateOutput:
        """
    Create callback
    Creates a new callback definition.

    :param instance_id: str
    :param provider_deployment_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param poll_interval_seconds_override: Optional[float] (optional)
    :param destination_ids: Optional[List[str]] (optional)
    :param triggers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceCallbacksCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_deployment_id"] = provider_deployment_id
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if poll_interval_seconds_override is not None:
            body_dict["poll_interval_seconds_override"] = poll_interval_seconds_override
        if destination_ids is not None:
            body_dict["destination_ids"] = destination_ids
        if triggers is not None:
            body_dict["triggers"] = triggers

        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCallbacksCreateOutput.from_dict)

    def update(self, instance_id: str, callback_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, poll_interval_seconds_override: Optional[float] = None, destination_ids: Optional[List[str]] = None, triggers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceCallbacksUpdateOutput:
        """
    Update callback
    Updates a callback definition.

    :param instance_id: str
    :param callback_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param poll_interval_seconds_override: Optional[float] (optional)
    :param destination_ids: Optional[List[str]] (optional)
    :param triggers: Optional[List[Dict[str, Any]]] (optional)
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
        if poll_interval_seconds_override is not None:
            body_dict["poll_interval_seconds_override"] = poll_interval_seconds_override
        if destination_ids is not None:
            body_dict["destination_ids"] = destination_ids
        if triggers is not None:
            body_dict["triggers"] = triggers

        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceCallbacksUpdateOutput.from_dict)

    def delete(self, instance_id: str, callback_id: str) -> DashboardInstanceCallbacksDeleteOutput:
        """
    Delete callback
    Archives a callback definition.

    :param instance_id: str
    :param callback_id: str
    :return: DashboardInstanceCallbacksDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'callbacks', callback_id]
        )
        return self._delete(request).transform(mapDashboardInstanceCallbacksDeleteOutput.from_dict)