from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsAccessGetOutput, DashboardInstanceSkillsAccessGetOutput

class MetorialManagementInstanceSkillsAccessEndpoint(BaseMetorialEndpoint):
    """Inspect who has been granted access to an instance skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsAccessGetOutput:
        """
    Get skill access
    Returns the access grants of a specific skill.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsAccessGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'access']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsAccessGetOutput.from_dict)