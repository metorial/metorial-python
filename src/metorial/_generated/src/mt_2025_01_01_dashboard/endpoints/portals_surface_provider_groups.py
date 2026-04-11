from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstancePortalsSurfaceProviderGroupsListOutput, DashboardInstancePortalsSurfaceProviderGroupsListOutput, mapDashboardInstancePortalsSurfaceProviderGroupsListQuery, DashboardInstancePortalsSurfaceProviderGroupsListQuery, mapDashboardInstancePortalsSurfaceProviderGroupsGetOutput, DashboardInstancePortalsSurfaceProviderGroupsGetOutput, mapDashboardInstancePortalsSurfaceProviderGroupsCreateOutput, DashboardInstancePortalsSurfaceProviderGroupsCreateOutput, mapDashboardInstancePortalsSurfaceProviderGroupsCreateBody, DashboardInstancePortalsSurfaceProviderGroupsCreateBody, mapDashboardInstancePortalsSurfaceProviderGroupsUpdateOutput, DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput, mapDashboardInstancePortalsSurfaceProviderGroupsUpdateBody, DashboardInstancePortalsSurfaceProviderGroupsUpdateBody, mapDashboardInstancePortalsSurfaceProviderGroupsDeleteOutput, DashboardInstancePortalsSurfaceProviderGroupsDeleteOutput, mapDashboardInstancePortalsSurfaceProviderGroupsAddListingOutput, DashboardInstancePortalsSurfaceProviderGroupsAddListingOutput, mapDashboardInstancePortalsSurfaceProviderGroupsAddListingBody, DashboardInstancePortalsSurfaceProviderGroupsAddListingBody, mapDashboardInstancePortalsSurfaceProviderGroupsRemoveListingOutput, DashboardInstancePortalsSurfaceProviderGroupsRemoveListingOutput

class MetorialPortalsSurfaceProviderGroupsEndpoint(BaseMetorialEndpoint):
    """Manage the provider groups linked to a portal consumer surface for organizing providers."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, portal_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstancePortalsSurfaceProviderGroupsListOutput:
        """
    List portal surface provider groups
    Returns a paginated list of provider groups linked to the portal consumer surface.

    :param portal_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstancePortalsSurfaceProviderGroupsListOutput
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
            path=['portals', portal_id, 'surface-provider-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsListOutput.from_dict)

    def get(self, portal_id: str, consumer_surface_provider_group_id: str) -> DashboardInstancePortalsSurfaceProviderGroupsGetOutput:
        """
    Get portal surface provider group
    Retrieves a portal surface provider group by ID.

    :param portal_id: str
    :param consumer_surface_provider_group_id: str
    :return: DashboardInstancePortalsSurfaceProviderGroupsGetOutput
    """
        request = MetorialRequest(
            path=['portals', portal_id, 'surface-provider-groups', consumer_surface_provider_group_id]
        )
        return self._get(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsGetOutput.from_dict)

    def create(self, portal_id: str, *, name: str, description: Optional[str] = None) -> DashboardInstancePortalsSurfaceProviderGroupsCreateOutput:
        """
    Create portal surface provider group
    Creates a new provider group linked to the portal consumer surface.

    :param portal_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :return: DashboardInstancePortalsSurfaceProviderGroupsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['portals', portal_id, 'surface-provider-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsCreateOutput.from_dict)

    def update(self, portal_id: str, consumer_surface_provider_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, index: Optional[float] = None) -> DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput:
        """
    Update portal surface provider group
    Updates a provider group linked to the portal consumer surface.

    :param portal_id: str
    :param consumer_surface_provider_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param index: Optional[float] (optional)
    :return: DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if index is not None:
            body_dict["index"] = index

        request = MetorialRequest(
            path=['portals', portal_id, 'surface-provider-groups', consumer_surface_provider_group_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsUpdateOutput.from_dict)

    def delete(self, portal_id: str, consumer_surface_provider_group_id: str) -> DashboardInstancePortalsSurfaceProviderGroupsDeleteOutput:
        """
    Delete portal surface provider group
    Deletes a provider group linked to the portal consumer surface.

    :param portal_id: str
    :param consumer_surface_provider_group_id: str
    :return: DashboardInstancePortalsSurfaceProviderGroupsDeleteOutput
    """
        request = MetorialRequest(
            path=['portals', portal_id, 'surface-provider-groups', consumer_surface_provider_group_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsDeleteOutput.from_dict)

    def add_listing(self, portal_id: str, consumer_surface_provider_group_id: str, *, consumer_access_listing_id: str) -> DashboardInstancePortalsSurfaceProviderGroupsAddListingOutput:
        """
    Add listing to surface provider group
    Adds a consumer access listing to the surface provider group.

    :param portal_id: str
    :param consumer_surface_provider_group_id: str
    :param consumer_access_listing_id: str
    :return: DashboardInstancePortalsSurfaceProviderGroupsAddListingOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["consumer_access_listing_id"] = consumer_access_listing_id

        request = MetorialRequest(
            path=['portals', portal_id, 'surface-provider-groups', consumer_surface_provider_group_id, 'listings'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsAddListingOutput.from_dict)

    def remove_listing(self, portal_id: str, consumer_surface_provider_group_id: str, consumer_access_listing_id: str) -> DashboardInstancePortalsSurfaceProviderGroupsRemoveListingOutput:
        """
    Remove listing from surface provider group
    Removes a consumer access listing from the surface provider group.

    :param portal_id: str
    :param consumer_surface_provider_group_id: str
    :param consumer_access_listing_id: str
    :return: DashboardInstancePortalsSurfaceProviderGroupsRemoveListingOutput
    """
        request = MetorialRequest(
            path=['portals', portal_id, 'surface-provider-groups', consumer_surface_provider_group_id, 'listings', consumer_access_listing_id]
        )
        return self._delete(request).transform(mapDashboardInstancePortalsSurfaceProviderGroupsRemoveListingOutput.from_dict)