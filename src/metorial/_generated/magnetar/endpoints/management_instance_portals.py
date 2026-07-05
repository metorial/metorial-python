from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsListOutput, DashboardInstancePortalsListOutput, mapDashboardInstancePortalsListQuery, DashboardInstancePortalsListQuery, mapDashboardInstancePortalsGetOutput, DashboardInstancePortalsGetOutput, mapDashboardInstancePortalsCreateOutput, DashboardInstancePortalsCreateOutput, mapDashboardInstancePortalsCreateBody, DashboardInstancePortalsCreateBody, mapDashboardInstancePortalsUpdateOutput, DashboardInstancePortalsUpdateOutput, mapDashboardInstancePortalsUpdateBody, DashboardInstancePortalsUpdateBody, mapDashboardInstancePortalsDeleteOutput, DashboardInstancePortalsDeleteOutput

class MetorialManagementInstancePortalsEndpoint(BaseMetorialEndpoint):
    """Use Portals to create custom branded MCP server marketplaces for your organization."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None) -> DashboardInstancePortalsListOutput:
        """
    List portals
    Returns a paginated list of portals.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstancePortalsListOutput
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
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['instances', instance_id, 'portals'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsListOutput.from_dict)

    def get(self, instance_id: str, portal_id: str) -> DashboardInstancePortalsGetOutput:
        """
    Get portal
    Retrieves details for a specific portal.

    :param instance_id: str
    :param portal_id: str
    :return: DashboardInstancePortalsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, allowed_redirect_url_filters: Optional[List[Dict[str, Any]]] = None, session_expiry_time_in_seconds: Optional[float] = None, allow_consumer_skill_authoring: Optional[bool] = None, allow_consumer_skill_publishing: Optional[bool] = None) -> DashboardInstancePortalsCreateOutput:
        """
    Create portal
    Creates a new portal for the instance.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param allowed_redirect_url_filters: Optional[List[Dict[str, Any]]] (optional)
    :param session_expiry_time_in_seconds: Optional[float] (optional)
    :param allow_consumer_skill_authoring: Optional[bool] (optional)
    :param allow_consumer_skill_publishing: Optional[bool] (optional)
    :return: DashboardInstancePortalsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if allowed_redirect_url_filters is not None:
            body_dict["allowed_redirect_url_filters"] = allowed_redirect_url_filters
        if session_expiry_time_in_seconds is not None:
            body_dict["session_expiry_time_in_seconds"] = session_expiry_time_in_seconds
        if allow_consumer_skill_authoring is not None:
            body_dict["allow_consumer_skill_authoring"] = allow_consumer_skill_authoring
        if allow_consumer_skill_publishing is not None:
            body_dict["allow_consumer_skill_publishing"] = allow_consumer_skill_publishing

        request = MetorialRequest(
            path=['instances', instance_id, 'portals'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsCreateOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, *, name: Optional[str] = None, description: Optional[str] = None, allowed_redirect_url_filters: Optional[List[Dict[str, Any]]] = None, session_expiry_time_in_seconds: Optional[float] = None, allow_consumer_skill_authoring: Optional[bool] = None, allow_consumer_skill_publishing: Optional[bool] = None, skill_configuration: Optional[Dict[str, Any]] = None) -> DashboardInstancePortalsUpdateOutput:
        """
    Update portal
    Updates an existing portal for the instance.

    :param instance_id: str
    :param portal_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param allowed_redirect_url_filters: Optional[List[Dict[str, Any]]] (optional)
    :param session_expiry_time_in_seconds: Optional[float] (optional)
    :param allow_consumer_skill_authoring: Optional[bool] (optional)
    :param allow_consumer_skill_publishing: Optional[bool] (optional)
    :param skill_configuration: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstancePortalsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if allowed_redirect_url_filters is not None:
            body_dict["allowed_redirect_url_filters"] = allowed_redirect_url_filters
        if session_expiry_time_in_seconds is not None:
            body_dict["session_expiry_time_in_seconds"] = session_expiry_time_in_seconds
        if allow_consumer_skill_authoring is not None:
            body_dict["allow_consumer_skill_authoring"] = allow_consumer_skill_authoring
        if allow_consumer_skill_publishing is not None:
            body_dict["allow_consumer_skill_publishing"] = allow_consumer_skill_publishing
        if skill_configuration is not None:
            body_dict["skill_configuration"] = skill_configuration

        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsUpdateOutput.from_dict)

    def delete(self, instance_id: str, portal_id: str) -> DashboardInstancePortalsDeleteOutput:
        """
    Delete portal
    Archives a portal.

    :param instance_id: str
    :param portal_id: str
    :return: DashboardInstancePortalsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'portals', portal_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsDeleteOutput.from_dict)