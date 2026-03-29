from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsOauthAppsListOutput, DashboardOrganizationsOauthAppsListOutput, mapDashboardOrganizationsOauthAppsListQuery, DashboardOrganizationsOauthAppsListQuery, mapDashboardOrganizationsOauthAppsGetOutput, DashboardOrganizationsOauthAppsGetOutput, mapDashboardOrganizationsOauthAppsCreateOutput, DashboardOrganizationsOauthAppsCreateOutput, mapDashboardOrganizationsOauthAppsCreateBody, DashboardOrganizationsOauthAppsCreateBody, mapDashboardOrganizationsOauthAppsUpdateOutput, DashboardOrganizationsOauthAppsUpdateOutput, mapDashboardOrganizationsOauthAppsUpdateBody, DashboardOrganizationsOauthAppsUpdateBody, mapDashboardOrganizationsOauthAppsDeleteOutput, DashboardOrganizationsOauthAppsDeleteOutput

class MetorialManagementOrganizationOauthAppsEndpoint(BaseMetorialEndpoint):
    """Create and manage OAuth applications for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsOauthAppsListOutput:
        """
    List organization OAuth applications
    Returns a paginated list of OAuth applications owned by the organization.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsOauthAppsListOutput
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
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['organization', 'oauth', 'apps'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthAppsListOutput.from_dict)

    def get(self, oauth_application_id: str) -> DashboardOrganizationsOauthAppsGetOutput:
        """
    Get organization OAuth application
    Retrieves a specific OAuth application owned by the organization.

    :param oauth_application_id: str
    :return: DashboardOrganizationsOauthAppsGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'apps', oauth_application_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsOauthAppsGetOutput.from_dict)

    def create(self, *, access_level: str, name: str, scopes: List[str], allow_token_exchange_without_client_secret: Optional[bool] = None, description: Optional[str] = None, website_url: Optional[str] = None, privacy_policy_url: Optional[str] = None, terms_of_service_url: Optional[str] = None, redirect_uris: Optional[List[str]] = None) -> DashboardOrganizationsOauthAppsCreateOutput:
        """
    Create organization OAuth application
    Creates a new OAuth application that belongs to the organization.

    :param access_level: str
    :param allow_token_exchange_without_client_secret: Optional[bool] (optional)
    :param name: str
    :param description: Optional[str] (optional)
    :param website_url: Optional[str] (optional)
    :param privacy_policy_url: Optional[str] (optional)
    :param terms_of_service_url: Optional[str] (optional)
    :param redirect_uris: Optional[List[str]] (optional)
    :param scopes: List[str]
    :return: DashboardOrganizationsOauthAppsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["access_level"] = access_level
        if allow_token_exchange_without_client_secret is not None:
            body_dict["allow_token_exchange_without_client_secret"] = allow_token_exchange_without_client_secret
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if website_url is not None:
            body_dict["website_url"] = website_url
        if privacy_policy_url is not None:
            body_dict["privacy_policy_url"] = privacy_policy_url
        if terms_of_service_url is not None:
            body_dict["terms_of_service_url"] = terms_of_service_url
        if redirect_uris is not None:
            body_dict["redirect_uris"] = redirect_uris
        body_dict["scopes"] = scopes

        request = MetorialRequest(
            path=['organization', 'oauth', 'apps'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsOauthAppsCreateOutput.from_dict)

    def update(self, oauth_application_id: str, *, access_level: Optional[str] = None, allow_token_exchange_without_client_secret: Optional[bool] = None, name: Optional[str] = None, description: Optional[str] = None, website_url: Optional[str] = None, privacy_policy_url: Optional[str] = None, terms_of_service_url: Optional[str] = None, redirect_uris: Optional[List[str]] = None, scopes: Optional[List[str]] = None) -> DashboardOrganizationsOauthAppsUpdateOutput:
        """
    Update organization OAuth application
    Updates an existing OAuth application owned by the organization.

    :param oauth_application_id: str
    :param access_level: Optional[str] (optional)
    :param allow_token_exchange_without_client_secret: Optional[bool] (optional)
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param website_url: Optional[str] (optional)
    :param privacy_policy_url: Optional[str] (optional)
    :param terms_of_service_url: Optional[str] (optional)
    :param redirect_uris: Optional[List[str]] (optional)
    :param scopes: Optional[List[str]] (optional)
    :return: DashboardOrganizationsOauthAppsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if access_level is not None:
            body_dict["access_level"] = access_level
        if allow_token_exchange_without_client_secret is not None:
            body_dict["allow_token_exchange_without_client_secret"] = allow_token_exchange_without_client_secret
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if website_url is not None:
            body_dict["website_url"] = website_url
        if privacy_policy_url is not None:
            body_dict["privacy_policy_url"] = privacy_policy_url
        if terms_of_service_url is not None:
            body_dict["terms_of_service_url"] = terms_of_service_url
        if redirect_uris is not None:
            body_dict["redirect_uris"] = redirect_uris
        if scopes is not None:
            body_dict["scopes"] = scopes

        request = MetorialRequest(
            path=['organization', 'oauth', 'apps', oauth_application_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsOauthAppsUpdateOutput.from_dict)

    def delete(self, oauth_application_id: str) -> DashboardOrganizationsOauthAppsDeleteOutput:
        """
    Delete organization OAuth application
    Archives an OAuth application owned by the organization.

    :param oauth_application_id: str
    :return: DashboardOrganizationsOauthAppsDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'oauth', 'apps', oauth_application_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsOauthAppsDeleteOutput.from_dict)