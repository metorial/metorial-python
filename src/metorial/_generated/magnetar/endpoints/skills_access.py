from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsAccessGetOutput, DashboardInstanceSkillsAccessGetOutput

class MetorialSkillsAccessEndpoint(BaseMetorialEndpoint):
    """Skill access is the record of who can view or edit a skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, skill_id: str) -> DashboardInstanceSkillsAccessGetOutput:
        """
    Get skill access
    Returns the access grants for a skill.

    :param skill_id: str
    :return: DashboardInstanceSkillsAccessGetOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id, 'access']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsAccessGetOutput.from_dict)