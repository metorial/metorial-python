from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput, DashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput, mapDashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateBody, DashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateBody, mapDashboardInstanceProviderDeploymentsSetupSessionsEmailsListOutput, DashboardInstanceProviderDeploymentsSetupSessionsEmailsListOutput, mapDashboardInstanceProviderDeploymentsSetupSessionsEmailsListQuery, DashboardInstanceProviderDeploymentsSetupSessionsEmailsListQuery

class MetorialProviderDeploymentsSetupSessionsEmailsEndpoint(BaseMetorialEndpoint):
    """A setup session tracks an in-progress OAuth flow, storing state during the redirect. On success, it creates an auth config with the user's access token."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, provider_setup_session_id: str, *, emails: Optional[List[str]] = None, organization_member_ids: Optional[List[str]] = None) -> DashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput:
        """
    Email provider setup session link
    Queues the link of an admin setup session for delivery to up to 10 recipients in total, given as email addresses and/or organization member IDs. Recipients are deduplicated case-insensitively and processed in order; if a later recipient fails, earlier ones may already have been queued, and retrying the request within the same window does not email them again. A recipient already emailed this setup link in the current fixed 10-minute window is not emailed again; their earlier record is returned with `deduplicated` set to true. A setup link can be emailed to at most 50 different recipients within 24 hours, and the setup links of an instance to at most 200 different recipients combined; a request that would exceed either limit is rejected with `admin_setup_email_limit_reached` before any email is queued. Passing `organization_member_ids` also requires the `organization.member:read` scope, since the response contains the members' email addresses.

    :param provider_setup_session_id: str
    :param emails: Optional[List[str]] (optional)
    :param organization_member_ids: Optional[List[str]] (optional)
    :return: DashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if emails is not None:
            body_dict["emails"] = emails
        if organization_member_ids is not None:
            body_dict["organization_member_ids"] = organization_member_ids

        request = MetorialRequest(
            path=['provider-setup-sessions', provider_setup_session_id, 'emails'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput.from_dict)

    def list(self, provider_setup_session_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceProviderDeploymentsSetupSessionsEmailsListOutput:
        """
    List provider setup session emails
    Returns a paginated list of the emails queued for delivery with the link of a provider setup session. Emails addressed to organization members have `recipient_email` set to null unless the caller also has the `organization.member:read` scope.

    :param provider_setup_session_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceProviderDeploymentsSetupSessionsEmailsListOutput
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
            path=['provider-setup-sessions', provider_setup_session_id, 'emails'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceProviderDeploymentsSetupSessionsEmailsListOutput.from_dict)