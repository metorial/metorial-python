from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsMembersPoliciesCreateOutput, DashboardOrganizationsMembersPoliciesCreateOutput, mapDashboardOrganizationsMembersPoliciesCreateBody, DashboardOrganizationsMembersPoliciesCreateBody, mapDashboardOrganizationsMembersPoliciesDeleteOutput, DashboardOrganizationsMembersPoliciesDeleteOutput

class MetorialManagementOrganizationMembersPoliciesEndpoint(BaseMetorialEndpoint):
    """Read and write organization member information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, member_id: str, *, access_policy_id: str) -> DashboardOrganizationsMembersPoliciesCreateOutput:
        """
    Assign policy to organization member
    Assign an access policy to an organization member

    :param member_id: str
    :param access_policy_id: str
    :return: DashboardOrganizationsMembersPoliciesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["access_policy_id"] = access_policy_id

        request = MetorialRequest(
            path=['organization', 'members', member_id, 'policies'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsMembersPoliciesCreateOutput.from_dict)

    def delete(self, member_id: str, access_policy_id: str) -> DashboardOrganizationsMembersPoliciesDeleteOutput:
        """
    Remove policy from organization member
    Remove an access policy from an organization member

    :param member_id: str
    :param access_policy_id: str
    :return: DashboardOrganizationsMembersPoliciesDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'members', member_id, 'policies', access_policy_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsMembersPoliciesDeleteOutput.from_dict)