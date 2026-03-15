from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderGroupsListOutput, DashboardInstanceProviderGroupsListOutput, mapDashboardInstanceProviderGroupsListQuery, DashboardInstanceProviderGroupsListQuery, mapDashboardInstanceProviderGroupsGetOutput, DashboardInstanceProviderGroupsGetOutput, mapDashboardInstanceProviderGroupsCreateOutput, DashboardInstanceProviderGroupsCreateOutput, mapDashboardInstanceProviderGroupsCreateBody, DashboardInstanceProviderGroupsCreateBody, mapDashboardInstanceProviderGroupsUpdateOutput, DashboardInstanceProviderGroupsUpdateOutput, mapDashboardInstanceProviderGroupsUpdateBody, DashboardInstanceProviderGroupsUpdateBody, mapDashboardInstanceProviderGroupsAddListingOutput, DashboardInstanceProviderGroupsAddListingOutput, mapDashboardInstanceProviderGroupsAddListingBody, DashboardInstanceProviderGroupsAddListingBody, mapDashboardInstanceProviderGroupsRemoveListingOutput, DashboardInstanceProviderGroupsRemoveListingOutput

class MetorialManagementInstanceProviderGroupsEndpoint(BaseMetorialEndpoint):
    """A group is a user-defined custom folder for organizing providers in your instance like 'Sales Tools' or 'Engineering'."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_listing_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceProviderGroupsListOutput:
        """
    List provider groups
    Returns a paginated list of provider groups.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_listing_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceProviderGroupsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_listing_id is not None:
            query_dict["provider_listing_id"] = provider_listing_id

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderGroupsListOutput.from_dict)

    def get(self, instance_id: str, provider_group_id: str) -> DashboardInstanceProviderGroupsGetOutput:
        """
    Get provider group
    Retrieves a specific provider group by ID.

    :param instance_id: str
    :param provider_group_id: str
    :return: DashboardInstanceProviderGroupsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-groups', provider_group_id]
        )
        return self._get(request).transform(mapDashboardInstanceProviderGroupsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None) -> DashboardInstanceProviderGroupsCreateOutput:
        """
    Create provider group
    Creates a new custom provider group.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :return: DashboardInstanceProviderGroupsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderGroupsCreateOutput.from_dict)

    def update(self, instance_id: str, provider_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None) -> DashboardInstanceProviderGroupsUpdateOutput:
        """
    Update provider group
    Updates an existing provider group.

    :param instance_id: str
    :param provider_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: DashboardInstanceProviderGroupsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-groups', provider_group_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceProviderGroupsUpdateOutput.from_dict)

    def add_listing(self, instance_id: str, provider_group_id: str, *, provider_listing_id: str) -> DashboardInstanceProviderGroupsAddListingOutput:
        """
    Add listing to group
    Adds a provider listing to a group.

    :param instance_id: str
    :param provider_group_id: str
    :param provider_listing_id: str
    :return: DashboardInstanceProviderGroupsAddListingOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["provider_listing_id"] = provider_listing_id

        request = MetorialRequest(
            path=['instances', instance_id, 'provider-groups', provider_group_id, 'listings'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderGroupsAddListingOutput.from_dict)

    def remove_listing(self, instance_id: str, provider_group_id: str, provider_listing_id: str) -> DashboardInstanceProviderGroupsRemoveListingOutput:
        """
    Remove listing from group
    Removes a provider listing from a group.

    :param instance_id: str
    :param provider_group_id: str
    :param provider_listing_id: str
    :return: DashboardInstanceProviderGroupsRemoveListingOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'provider-groups', provider_group_id, 'listings', provider_listing_id]
        )
        return self._delete(request).transform(mapDashboardInstanceProviderGroupsRemoveListingOutput.from_dict)