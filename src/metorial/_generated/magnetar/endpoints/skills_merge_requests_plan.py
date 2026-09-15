from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMergeRequestsPlanGetOutput, DashboardInstanceSkillsMergeRequestsPlanGetOutput

class MetorialSkillsMergeRequestsPlanEndpoint(BaseMetorialEndpoint):
    """Review, resolve, and apply changes between skills."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, skill_merge_request_id: str) -> DashboardInstanceSkillsMergeRequestsPlanGetOutput:
        """
    Get skill merge plan
    Returns the proposed changes and conflicts for a skill merge request.

    :param skill_merge_request_id: str
    :return: DashboardInstanceSkillsMergeRequestsPlanGetOutput
    """
        request = MetorialRequest(
            path=['skill-merge-requests', skill_merge_request_id, 'plan']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMergeRequestsPlanGetOutput.from_dict)