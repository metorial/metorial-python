from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsSecurityReviewGetOutput, DashboardInstanceSkillsSecurityReviewGetOutput, mapDashboardInstanceSkillsSecurityReviewReassessOutput, DashboardInstanceSkillsSecurityReviewReassessOutput, mapDashboardInstanceSkillsSecurityReviewDismissOutput, DashboardInstanceSkillsSecurityReviewDismissOutput, mapDashboardInstanceSkillsSecurityReviewRestoreOutput, DashboardInstanceSkillsSecurityReviewRestoreOutput

class MetorialDashboardInstanceSkillsSecurityReviewEndpoint(BaseMetorialEndpoint):
    """A security review assesses what a skill makes an agent do and whether its files can be trusted. Everyone who can read a skill can read its review."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsSecurityReviewGetOutput:
        """
    Get skill security review
    Returns the security review of a skill's latest version. Requests a review if none exists yet.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsSecurityReviewGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'security-review']
        )
        return self._get(request).transform(mapDashboardInstanceSkillsSecurityReviewGetOutput.from_dict)

    def reassess(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsSecurityReviewReassessOutput:
        """
    Reassess skill security review
    Starts a new review of the skill. Pending edits are sealed into a new version first.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsSecurityReviewReassessOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'security-review', 'reassess']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsSecurityReviewReassessOutput.from_dict)

    def dismiss(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsSecurityReviewDismissOutput:
        """
    Dismiss skill security review
    Stops reviewing the skill. Its verdict becomes `dismissed` and no longer holds back the skill.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsSecurityReviewDismissOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'security-review', 'dismiss']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsSecurityReviewDismissOutput.from_dict)

    def restore(self, instance_id: str, skill_id: str) -> DashboardInstanceSkillsSecurityReviewRestoreOutput:
        """
    Restore skill security review
    Resumes reviewing a dismissed skill and starts a new review.

    :param instance_id: str
    :param skill_id: str
    :return: DashboardInstanceSkillsSecurityReviewRestoreOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'skills', skill_id, 'security-review', 'restore']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsSecurityReviewRestoreOutput.from_dict)