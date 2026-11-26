from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutput, DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput, mapDashboardInstanceSkillsPluginsSkillGroupMatchesListQuery, DashboardInstanceSkillsPluginsSkillGroupMatchesListQuery

class MetorialSkillsPluginsSkillGroupMatchesEndpoint(BaseMetorialEndpoint):
    """A skill plugin is a set of skills distributed through a skill marketplace."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, skill_plugin_id: str, *, skill_group_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput:
        """
    List skill group matches
    Compares a skill plugin with skill groups and returns the skills attaching each group would add or remove. Without a filter, returns up to 5 groups that share the most skills with the plugin.

    :param skill_plugin_id: str
    :param skill_group_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSkillsPluginsSkillGroupMatchesListOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if skill_group_id is not None:
            query_dict["skill_group_id"] = skill_group_id

        request = MetorialRequest(
            path=['skill-plugins', skill_plugin_id, 'skill-group-matches'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsPluginsSkillGroupMatchesListOutput.from_dict)