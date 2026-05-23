from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsVersionsSnapshotGetOutput, DashboardInstanceSkillsVersionsSnapshotGetOutput

class MetorialSkillsVersionsSnapshotEndpoint(BaseMetorialEndpoint):
    """Inspect version history and snapshots for a skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, skill_id: str, skill_version_id: str) -> DashboardInstanceSkillsVersionsSnapshotGetOutput:
        """
    Get skill version snapshot
    Retrieves the store-backed snapshot for a specific skill version.

    :param skill_id: str
    :param skill_version_id: str
    :return: DashboardInstanceSkillsVersionsSnapshotGetOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id, 'versions', skill_version_id, 'snapshot']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsVersionsSnapshotGetOutput.from_dict)