from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsVersionsSnapshotGetOutput, DashboardInstanceSkillsVersionsSnapshotGetOutput

class MetorialDashboardInstanceSkillsVersionsSnapshotEndpoint(BaseMetorialEndpoint):
    """Inspect version history and snapshots for a skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, skill_id: str, skill_version_id: str) -> DashboardInstanceSkillsVersionsSnapshotGetOutput:
        """
    Get skill version snapshot
    Retrieves the store-backed snapshot for a specific skill version.

    :param instance_id: str
    :param skill_id: str
    :param skill_version_id: str
    :return: DashboardInstanceSkillsVersionsSnapshotGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'versions', skill_version_id, 'snapshot']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsVersionsSnapshotGetOutput.from_dict)