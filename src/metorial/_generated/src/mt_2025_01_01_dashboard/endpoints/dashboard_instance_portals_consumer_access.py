from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsConsumerAccessListOutput, DashboardInstancePortalsConsumerAccessListOutput, mapDashboardInstancePortalsConsumerAccessListQuery, DashboardInstancePortalsConsumerAccessListQuery, mapDashboardInstancePortalsConsumerAccessGetOutput, DashboardInstancePortalsConsumerAccessGetOutput, mapDashboardInstancePortalsConsumerAccessCreateOutput, DashboardInstancePortalsConsumerAccessCreateOutput, mapDashboardInstancePortalsConsumerAccessCreateBody, DashboardInstancePortalsConsumerAccessCreateBody, mapDashboardInstancePortalsConsumerAccessUpdateOutput, DashboardInstancePortalsConsumerAccessUpdateOutput, mapDashboardInstancePortalsConsumerAccessUpdateBody, DashboardInstancePortalsConsumerAccessUpdateBody, mapDashboardInstancePortalsConsumerAccessDeleteOutput, DashboardInstancePortalsConsumerAccessDeleteOutput

class MetorialDashboardInstancePortalsConsumerAccessEndpoint(BaseMetorialEndpoint):
    """Manage which consumer groups can access portal provider templates and MCP servers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, consumer_group_id: Optional[Union[str, List[str]]] = None, provider_template_id: Optional[Union[str, List[str]]] = None, magic_mcp_server_id: Optional[Union[str, List[str]]] = None, type: Optional[Union[str, List[str]]] = None) -> DashboardInstancePortalsConsumerAccessListOutput:
        """
    List portal consumer access
    Returns a paginated list of consumer access rules for a portal.

    :param instance_id: str
    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param consumer_group_id: Optional[Union[str, List[str]]] (optional)
    :param provider_template_id: Optional[Union[str, List[str]]] (optional)
    :param magic_mcp_server_id: Optional[Union[str, List[str]]] (optional)
    :param type: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstancePortalsConsumerAccessListOutput
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
        if consumer_group_id is not None:
            query_dict["consumer_group_id"] = consumer_group_id
        if provider_template_id is not None:
            query_dict["provider_template_id"] = provider_template_id
        if magic_mcp_server_id is not None:
            query_dict["magic_mcp_server_id"] = magic_mcp_server_id
        if type is not None:
            query_dict["type"] = type

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'consumer-access'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerAccessListOutput.from_dict)

    def get(self, instance_id: str, portal_id: str, consumer_access_id: str) -> DashboardInstancePortalsConsumerAccessGetOutput:
        """
    Get portal consumer access
    Retrieves a portal consumer access rule by ID.

    :param instance_id: str
    :param portal_id: str
    :param consumer_access_id: str
    :return: DashboardInstancePortalsConsumerAccessGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'consumer-access', consumer_access_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsConsumerAccessGetOutput.from_dict)

    def create(self, instance_id: str, portal_id: str, *, consumer_group_id: str, access: Union[Dict[str, Any], Dict[str, Any]], name: Optional[str] = None, description: Optional[str] = None, readme: Optional[str] = None) -> DashboardInstancePortalsConsumerAccessCreateOutput:
        """
    Create portal consumer access
    Creates a new consumer access rule for the portal.

    :param instance_id: str
    :param portal_id: str
    :param consumer_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param readme: Optional[str] (optional)
    :param access: Union[Dict[str, Any], Dict[str, Any]]
    :return: DashboardInstancePortalsConsumerAccessCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["consumer_group_id"] = consumer_group_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if readme is not None:
            body_dict["readme"] = readme
        body_dict["access"] = access

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'consumer-access'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsConsumerAccessCreateOutput.from_dict)

    def update(self, instance_id: str, portal_id: str, consumer_access_id: str, *, name: Optional[str] = None, description: Optional[str] = None, readme: Optional[str] = None) -> DashboardInstancePortalsConsumerAccessUpdateOutput:
        """
    Update portal consumer access
    Updates the shared listing fields for a portal consumer access rule.

    :param instance_id: str
    :param portal_id: str
    :param consumer_access_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param readme: Optional[str] (optional)
    :return: DashboardInstancePortalsConsumerAccessUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if readme is not None:
            body_dict["readme"] = readme

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'consumer-access', consumer_access_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsConsumerAccessUpdateOutput.from_dict)

    def delete(self, instance_id: str, portal_id: str, consumer_access_id: str) -> DashboardInstancePortalsConsumerAccessDeleteOutput:
        """
    Delete portal consumer access
    Deletes a consumer access rule from the portal.

    :param instance_id: str
    :param portal_id: str
    :param consumer_access_id: str
    :return: DashboardInstancePortalsConsumerAccessDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'portals', portal_id, 'consumer-access', consumer_access_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsConsumerAccessDeleteOutput.from_dict)