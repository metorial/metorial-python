from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsMcpAvailabilityGetOutput, DashboardInstanceSkillsMcpAvailabilityGetOutput

class MetorialManagementInstanceSkillsMcpAvailabilityEndpoint(BaseMetorialEndpoint):
    """Read and edit the files of a skill by path."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsMcpAvailabilityGetOutput:
        """
    Get skill MCP availability
    Returns whether apps connected over MCP can see the skill. Skills with too many files or too large a total size are left out of MCP connections and keep working everywhere else.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsMcpAvailabilityGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', skill_id, 'mcp-availability']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsMcpAvailabilityGetOutput.from_dict)