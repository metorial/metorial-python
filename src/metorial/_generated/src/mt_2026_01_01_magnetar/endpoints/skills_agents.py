from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsAgentsCreateOutput, DashboardInstanceSkillsAgentsCreateOutput, mapDashboardInstanceSkillsAgentsCreateBody, DashboardInstanceSkillsAgentsCreateBody, mapDashboardInstanceSkillsAgentsListOutput, DashboardInstanceSkillsAgentsListOutput, mapDashboardInstanceSkillsAgentsListQuery, DashboardInstanceSkillsAgentsListQuery, mapDashboardInstanceSkillsAgentsGetOutput, DashboardInstanceSkillsAgentsGetOutput, mapDashboardInstanceSkillsAgentsUpdateOutput, DashboardInstanceSkillsAgentsUpdateOutput, mapDashboardInstanceSkillsAgentsUpdateBody, DashboardInstanceSkillsAgentsUpdateBody, mapDashboardInstanceSkillsAgentsDeleteOutput, DashboardInstanceSkillsAgentsDeleteOutput

class MetorialSkillsAgentsEndpoint(BaseMetorialEndpoint):
    """Manage sub-agents attached to a skill."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, skill_id: str, *, name: str, description: Optional[str] = None, content: Optional[str] = None) -> DashboardInstanceSkillsAgentsCreateOutput:
        """
    Create skill agent
    Creates a new agent document in the skill agents directory.

    :param skill_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param content: Optional[str] (optional)
    :return: DashboardInstanceSkillsAgentsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if content is not None:
            body_dict["content"] = content

        request = MetorialRequest(
            path=['skills', skill_id, 'agents'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsAgentsCreateOutput.from_dict)

    def list(self, skill_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, include_archived: Optional[bool] = None) -> DashboardInstanceSkillsAgentsListOutput:
        """
    List skill agents
    Returns a paginated list of agents for a specific skill.

    :param skill_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param include_archived: Optional[bool] (optional)
    :return: DashboardInstanceSkillsAgentsListOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if limit is not None:
            query_dict["limit"] = limit
        if after is not None:
            query_dict["after"] = after
        if before is not None:
            query_dict["before"] = before
        if cursor is not None:
            query_dict["cursor"] = cursor
        if order is not None:
            query_dict["order"] = order
        if include_archived is not None:
            query_dict["include_archived"] = include_archived

        request = MetorialRequest(
            path=['skills', skill_id, 'agents'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsAgentsListOutput.from_dict)

    def get(self, skill_id: str, skill_agent_id: str) -> DashboardInstanceSkillsAgentsGetOutput:
        """
    Get skill agent by ID
    Retrieves a specific agent within a skill.

    :param skill_id: str
    :param skill_agent_id: str
    :return: DashboardInstanceSkillsAgentsGetOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id, 'agents', skill_agent_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsAgentsGetOutput.from_dict)

    def update(self, skill_id: str, skill_agent_id: str, *, name: Optional[str] = None, description: Optional[str] = None) -> DashboardInstanceSkillsAgentsUpdateOutput:
        """
    Update skill agent
    Updates the name or description for a specific skill agent.

    :param skill_id: str
    :param skill_agent_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :return: DashboardInstanceSkillsAgentsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description

        request = MetorialRequest(
            path=['skills', skill_id, 'agents', skill_agent_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsAgentsUpdateOutput.from_dict)

    def delete(self, skill_id: str, skill_agent_id: str) -> DashboardInstanceSkillsAgentsDeleteOutput:
        """
    Delete skill agent
    Archives a specific skill agent and removes its linked store item.

    :param skill_id: str
    :param skill_agent_id: str
    :return: DashboardInstanceSkillsAgentsDeleteOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id, 'agents', skill_agent_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsAgentsDeleteOutput.from_dict)