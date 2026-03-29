from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsTeamsPoliciesCreateOutput, DashboardOrganizationsTeamsPoliciesCreateOutput, mapDashboardOrganizationsTeamsPoliciesCreateBody, DashboardOrganizationsTeamsPoliciesCreateBody, mapDashboardOrganizationsTeamsPoliciesDeleteOutput, DashboardOrganizationsTeamsPoliciesDeleteOutput

class MetorialManagementOrganizationTeamsPoliciesEndpoint(BaseMetorialEndpoint):
    """Read and write team information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, team_id: str, *, access_policy_id: str) -> DashboardOrganizationsTeamsPoliciesCreateOutput:
        """
    Assign policy to team
    Assign an access policy to a team

    :param team_id: str
    :param access_policy_id: str
    :return: DashboardOrganizationsTeamsPoliciesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["access_policy_id"] = access_policy_id

        request = MetorialRequest(
            path=['organization', 'teams', team_id, 'policies'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardOrganizationsTeamsPoliciesCreateOutput.from_dict)

    def delete(self, team_id: str, access_policy_id: str) -> DashboardOrganizationsTeamsPoliciesDeleteOutput:
        """
    Remove policy from team
    Remove an access policy from a team

    :param team_id: str
    :param access_policy_id: str
    :return: DashboardOrganizationsTeamsPoliciesDeleteOutput
    """
        request = MetorialRequest(
            path=['organization', 'teams', team_id, 'policies', access_policy_id]
        )
        return self._delete(request).transform(mapDashboardOrganizationsTeamsPoliciesDeleteOutput.from_dict)