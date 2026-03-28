from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsServiceAccountsPoliciesCreateOutput, DashboardOrganizationsServiceAccountsPoliciesCreateOutput, mapDashboardOrganizationsServiceAccountsPoliciesCreateBody, DashboardOrganizationsServiceAccountsPoliciesCreateBody, mapDashboardOrganizationsServiceAccountsPoliciesDeleteOutput, DashboardOrganizationsServiceAccountsPoliciesDeleteOutput

class MetorialManagementOrganizationServiceAccountsPoliciesEndpoint(BaseMetorialEndpoint):
    """Create and manage service accounts for an organization"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, service_account_id: str, *, access_policy_id: str) -> DashboardOrganizationsServiceAccountsPoliciesCreateOutput:
        """
    Assign service account policy
    Assign an access policy to a service account

    :param service_account_id: str
    :param access_policy_id: str
    :return: DashboardOrganizationsServiceAccountsPoliciesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["access_policy_id"] = access_policy_id

        request = MetorialRequest(
            path=['organization', 'service-accounts', service_account_id, 'policies'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsServiceAccountsPoliciesCreateOutput.from_dict)

    def delete(self, service_account_id: str, access_policy_id: str) -> DashboardOrganizationsServiceAccountsPoliciesDeleteOutput:
        """
    Remove service account policy
    Remove an access policy from a service account

    :param service_account_id: str
    :param access_policy_id: str
    :return: DashboardOrganizationsServiceAccountsPoliciesDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'service-accounts', service_account_id, 'policies', access_policy_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsServiceAccountsPoliciesDeleteOutput.from_dict)