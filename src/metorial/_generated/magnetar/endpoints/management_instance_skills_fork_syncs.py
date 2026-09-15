from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsForkSyncsCreateOutput, DashboardInstanceSkillsForkSyncsCreateOutput, mapDashboardInstanceSkillsForkSyncsCreateBody, DashboardInstanceSkillsForkSyncsCreateBody, mapDashboardInstanceSkillsForkSyncsGetOutput, DashboardInstanceSkillsForkSyncsGetOutput

class MetorialManagementInstanceSkillsForkSyncsEndpoint(BaseMetorialEndpoint):
    """Synchronize changes from an upstream skill into a fork."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, instance_id: str, *, skill_id: str) -> DashboardInstanceSkillsForkSyncsCreateOutput:
        """
    Create skill fork sync
    Queues synchronization of upstream changes into a forked skill.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsForkSyncsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["skill_id"] = skill_id

        request = MetorialRequest(
            path=['instances', instance_id, 'skill-fork-syncs'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsForkSyncsCreateOutput.from_dict)

    def get(self, instance_id: str, skill_fork_sync_id: str) -> DashboardInstanceSkillsForkSyncsGetOutput:
        """
    Get skill fork sync
    Retrieves the state of a fork synchronization.

    :param instance_id: str
    :param skill_fork_sync_id: str
    :return: DashboardInstanceSkillsForkSyncsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skill-fork-syncs', skill_fork_sync_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsForkSyncsGetOutput.from_dict)