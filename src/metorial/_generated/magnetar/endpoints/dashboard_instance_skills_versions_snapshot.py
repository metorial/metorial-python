from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsVersionsSnapshotGetOutput, DashboardInstanceSkillsVersionsSnapshotGetOutput

class MetorialDashboardInstanceSkillsVersionsSnapshotEndpoint(BaseMetorialEndpoint):
    """A skill version is a snapshot of a skill at a point in time."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, skill_id: str, skill_version_id: str) -> DashboardInstanceSkillsVersionsSnapshotGetOutput:
        """
    Get skill version snapshot
    Retrieves the content snapshot for a skill version.

    :param instance_id: str
    :param skill_id: str
    :param skill_version_id: str
    :return: DashboardInstanceSkillsVersionsSnapshotGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'versions', skill_version_id, 'snapshot']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsVersionsSnapshotGetOutput.from_dict)