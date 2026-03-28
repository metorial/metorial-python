from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsServiceAccountsCredentialsListOutput, DashboardOrganizationsServiceAccountsCredentialsListOutput, mapDashboardOrganizationsServiceAccountsCredentialsListQuery, DashboardOrganizationsServiceAccountsCredentialsListQuery, mapDashboardOrganizationsServiceAccountsCredentialsGetOutput, DashboardOrganizationsServiceAccountsCredentialsGetOutput

class MetorialDashboardOrganizationsServiceAccountsCredentialsEndpoint(BaseMetorialEndpoint):
    """Create and manage service accounts for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, organization_id: str, service_account_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> DashboardOrganizationsServiceAccountsCredentialsListOutput:
        """
    List service account credentials
    Returns a paginated list of credentials for a service account.

    :param organization_id: str
    :param service_account_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: DashboardOrganizationsServiceAccountsCredentialsListOutput
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
            path=['dashboard', 'organizations', organization_id, 'service-accounts', service_account_id, 'credentials'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardOrganizationsServiceAccountsCredentialsListOutput.from_dict)

    def get(self, organization_id: str, service_account_id: str, service_account_credential_id: str) -> DashboardOrganizationsServiceAccountsCredentialsGetOutput:
        """
    Get service account credential
    Retrieves a specific credential for a service account.

    :param organization_id: str
    :param service_account_id: str
    :param service_account_credential_id: str
    :return: DashboardOrganizationsServiceAccountsCredentialsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'organizations', organization_id, 'service-accounts', service_account_id, 'credentials', service_account_credential_id]
        )
        return self._get(request).transform(mapDashboardOrganizationsServiceAccountsCredentialsGetOutput.from_dict)