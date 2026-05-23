from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsTemplatesListOutput, DashboardInstanceSkillsTemplatesListOutput, mapDashboardInstanceSkillsTemplatesListQuery, DashboardInstanceSkillsTemplatesListQuery, mapDashboardInstanceSkillsTemplatesGetOutput, DashboardInstanceSkillsTemplatesGetOutput, mapDashboardInstanceSkillsTemplatesCreateOutput, DashboardInstanceSkillsTemplatesCreateOutput, mapDashboardInstanceSkillsTemplatesCreateBody, DashboardInstanceSkillsTemplatesCreateBody, mapDashboardInstanceSkillsTemplatesUpdateOutput, DashboardInstanceSkillsTemplatesUpdateOutput, mapDashboardInstanceSkillsTemplatesUpdateBody, DashboardInstanceSkillsTemplatesUpdateBody, mapDashboardInstanceSkillsTemplatesDeleteOutput, DashboardInstanceSkillsTemplatesDeleteOutput

class MetorialSkillsTemplatesEndpoint(BaseMetorialEndpoint):
    """Skill templates define reusable starting points for skills."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, owner: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsTemplatesListOutput:
        """
    List skill templates
    Returns a paginated list of skill templates.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param owner: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsTemplatesListOutput
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
        if search is not None:
            query_dict["search"] = search
        if status is not None:
            query_dict["status"] = status
        if owner is not None:
            query_dict["owner"] = owner
        if id is not None:
            query_dict["id"] = id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['skill-template'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsTemplatesListOutput.from_dict)

    def get(self, skill_template_id: str) -> DashboardInstanceSkillsTemplatesGetOutput:
        """
    Get skill template
    Retrieves a specific skill template.

    :param skill_template_id: str
    :return: DashboardInstanceSkillsTemplatesGetOutput
    """
        request = MetorialRequest(
            path=['skill-template', skill_template_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsTemplatesGetOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, from_skill_id: Optional[str] = None) -> DashboardInstanceSkillsTemplatesCreateOutput:
        """
    Create skill template
    Creates a skill template.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param from_skill_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsTemplatesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if from_skill_id is not None:
            body_dict["from_skill_Id"] = from_skill_id

        request = MetorialRequest(
            path=['skill-template'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsTemplatesCreateOutput.from_dict)

    def update(self, skill_template_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsTemplatesUpdateOutput:
        """
    Update skill template
    Updates a skill template.

    :param skill_template_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsTemplatesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['skill-template', skill_template_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsTemplatesUpdateOutput.from_dict)

    def delete(self, skill_template_id: str) -> DashboardInstanceSkillsTemplatesDeleteOutput:
        """
    Delete skill template
    Archives a skill template.

    :param skill_template_id: str
    :return: DashboardInstanceSkillsTemplatesDeleteOutput
    """
        request = MetorialRequest(
            path=['skill-template', skill_template_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsTemplatesDeleteOutput.from_dict)