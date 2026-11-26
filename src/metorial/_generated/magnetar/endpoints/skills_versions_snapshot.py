from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsVersionsSnapshotGetOutput, DashboardInstanceSkillsVersionsSnapshotGetOutput

class MetorialSkillsVersionsSnapshotEndpoint(BaseMetorialEndpoint):
    """A skill version is a snapshot of a skill at a point in time."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, skill_id: str, skill_version_id: str) -> DashboardInstanceSkillsVersionsSnapshotGetOutput:
        """
    Get skill version snapshot
    Retrieves the content snapshot for a skill version.

    :param skill_id: str
    :param skill_version_id: str
    :return: DashboardInstanceSkillsVersionsSnapshotGetOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id, 'versions', skill_version_id, 'snapshot']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsVersionsSnapshotGetOutput.from_dict)