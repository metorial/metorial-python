from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceCallbacksDestinationsListOutput, DashboardInstanceCallbacksDestinationsListOutput, mapDashboardInstanceCallbacksDestinationsListQuery, DashboardInstanceCallbacksDestinationsListQuery, mapDashboardInstanceCallbacksDestinationsGetOutput, DashboardInstanceCallbacksDestinationsGetOutput, mapDashboardInstanceCallbacksDestinationsCreateOutput, DashboardInstanceCallbacksDestinationsCreateOutput, mapDashboardInstanceCallbacksDestinationsCreateBody, DashboardInstanceCallbacksDestinationsCreateBody, mapDashboardInstanceCallbacksDestinationsUpdateOutput, DashboardInstanceCallbacksDestinationsUpdateOutput, mapDashboardInstanceCallbacksDestinationsUpdateBody, DashboardInstanceCallbacksDestinationsUpdateBody, mapDashboardInstanceCallbacksDestinationsDeleteOutput, DashboardInstanceCallbacksDestinationsDeleteOutput

class MetorialManagementInstanceCallbacksDestinationsEndpoint(BaseMetorialEndpoint):
    """Manage callback webhook destinations."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbacksDestinationsListOutput:
        """
    List callback destinations
    Returns a paginated list of callback destinations.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceCallbacksDestinationsListOutput
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
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'callback-destinations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksDestinationsListOutput.from_dict)

    def get(self, instance_id: str, callback_destination_id: str) -> DashboardInstanceCallbacksDestinationsGetOutput:
        """
    Get callback destination
    Retrieves a specific callback destination.

    :param instance_id: str
    :param callback_destination_id: str
    :return: DashboardInstanceCallbacksDestinationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'callback-destinations', callback_destination_id]
        )
        return self._get(request).transform(mapDashboardInstanceCallbacksDestinationsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, url: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceCallbacksDestinationsCreateOutput:
        """
    Create callback destination
    Creates a new callback destination.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param url: str
    :return: DashboardInstanceCallbacksDestinationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["url"] = url

        request = MetorialRequest(
            path=['instances', instance_id, 'callback-destinations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceCallbacksDestinationsCreateOutput.from_dict)

    def update(self, instance_id: str, callback_destination_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, url: Optional[str] = None) -> DashboardInstanceCallbacksDestinationsUpdateOutput:
        """
    Update callback destination
    Updates a callback destination.

    :param instance_id: str
    :param callback_destination_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param url: Optional[str] (optional)
    :return: DashboardInstanceCallbacksDestinationsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if url is not None:
            body_dict["url"] = url

        request = MetorialRequest(
            path=['instances', instance_id, 'callback-destinations', callback_destination_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceCallbacksDestinationsUpdateOutput.from_dict)

    def delete(self, instance_id: str, callback_destination_id: str) -> DashboardInstanceCallbacksDestinationsDeleteOutput:
        """
    Delete callback destination
    Archives a callback destination.

    :param instance_id: str
    :param callback_destination_id: str
    :return: DashboardInstanceCallbacksDestinationsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'callback-destinations', callback_destination_id]
        )
        return self._delete(request).transform(mapDashboardInstanceCallbacksDestinationsDeleteOutput.from_dict)