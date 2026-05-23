from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsListOutput, DashboardInstanceSkillsListOutput, mapDashboardInstanceSkillsListQuery, DashboardInstanceSkillsListQuery, mapDashboardInstanceSkillsGetOutput, DashboardInstanceSkillsGetOutput, mapDashboardInstanceSkillsCreateOutput, DashboardInstanceSkillsCreateOutput, mapDashboardInstanceSkillsCreateBody, DashboardInstanceSkillsCreateBody, mapDashboardInstanceSkillsUpdateOutput, DashboardInstanceSkillsUpdateOutput, mapDashboardInstanceSkillsUpdateBody, DashboardInstanceSkillsUpdateBody, mapDashboardInstanceSkillsDeleteOutput, DashboardInstanceSkillsDeleteOutput, mapDashboardInstanceSkillsForkOutput, DashboardInstanceSkillsForkOutput, mapDashboardInstanceSkillsForkBody, DashboardInstanceSkillsForkBody, mapDashboardInstanceSkillsPublishConsumerSkillOutput, DashboardInstanceSkillsPublishConsumerSkillOutput, mapDashboardInstanceSkillsDuplicateOutput, DashboardInstanceSkillsDuplicateOutput, mapDashboardInstanceSkillsDuplicateBody, DashboardInstanceSkillsDuplicateBody

class MetorialSkillsEndpoint(BaseMetorialEndpoint):
    """Skills group provider and integration capabilities into reusable, owned compositions."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, skill_group_id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsListOutput:
        """
    List skills
    Returns a paginated list of skills.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param skill_group_id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsListOutput
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
        if id is not None:
            query_dict["id"] = id
        if skill_group_id is not None:
            query_dict["skill_group_id"] = skill_group_id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['skills'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsListOutput.from_dict)

    def get(self, skill_id: str) -> DashboardInstanceSkillsGetOutput:
        """
    Get skill
    Retrieves a specific skill.

    :param skill_id: str
    :return: DashboardInstanceSkillsGetOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsGetOutput.from_dict)

    def create(self, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, client_name: Optional[str] = None, client_description: Optional[str] = None, license: Optional[str] = None, compatibility: Optional[str] = None, client_metadata: Optional[Dict[str, Any]] = None, image_file_id: Optional[str] = None, template_id: Optional[str] = None) -> DashboardInstanceSkillsCreateOutput:
        """
    Create skill
    Creates a new skill.

    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param client_name: Optional[str] (optional)
    :param client_description: Optional[str] (optional)
    :param license: Optional[str] (optional)
    :param compatibility: Optional[str] (optional)
    :param client_metadata: Optional[Dict[str, Any]] (optional)
    :param image_file_id: Optional[str] (optional)
    :param template_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if client_name is not None:
            body_dict["client_name"] = client_name
        if client_description is not None:
            body_dict["client_description"] = client_description
        if license is not None:
            body_dict["license"] = license
        if compatibility is not None:
            body_dict["compatibility"] = compatibility
        if client_metadata is not None:
            body_dict["client_metadata"] = client_metadata
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id
        if template_id is not None:
            body_dict["template_id"] = template_id

        request = MetorialRequest(
            path=['skills'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsCreateOutput.from_dict)

    def update(self, skill_id: str, *, name: Optional[str] = None, description: Optional[str] = None, client_name: Optional[str] = None, client_description: Optional[str] = None, license: Optional[str] = None, compatibility: Optional[str] = None, client_metadata: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None, image_file_id: Optional[str] = None) -> DashboardInstanceSkillsUpdateOutput:
        """
    Update skill
    Updates a specific skill.

    :param skill_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param client_name: Optional[str] (optional)
    :param client_description: Optional[str] (optional)
    :param license: Optional[str] (optional)
    :param compatibility: Optional[str] (optional)
    :param client_metadata: Optional[Dict[str, Any]] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param image_file_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if client_name is not None:
            body_dict["client_name"] = client_name
        if client_description is not None:
            body_dict["client_description"] = client_description
        if license is not None:
            body_dict["license"] = license
        if compatibility is not None:
            body_dict["compatibility"] = compatibility
        if client_metadata is not None:
            body_dict["client_metadata"] = client_metadata
        if metadata is not None:
            body_dict["metadata"] = metadata
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id

        request = MetorialRequest(
            path=['skills', skill_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsUpdateOutput.from_dict)

    def delete(self, skill_id: str) -> DashboardInstanceSkillsDeleteOutput:
        """
    Delete skill
    Archives a specific skill.

    :param skill_id: str
    :return: DashboardInstanceSkillsDeleteOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsDeleteOutput.from_dict)

    def fork(self, skill_id: str, *, name: str, description: Optional[str] = None, client_name: Optional[str] = None, client_description: Optional[str] = None, license: Optional[str] = None, compatibility: Optional[str] = None, client_metadata: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None, image_file_id: Optional[str] = None) -> DashboardInstanceSkillsForkOutput:
        """
    Fork skill
    Forks a skill for the current consumer. Non-consumer callers duplicate the skill instead.

    :param skill_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param client_name: Optional[str] (optional)
    :param client_description: Optional[str] (optional)
    :param license: Optional[str] (optional)
    :param compatibility: Optional[str] (optional)
    :param client_metadata: Optional[Dict[str, Any]] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param image_file_id: Optional[str] (optional)
    :return: DashboardInstanceSkillsForkOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if client_name is not None:
            body_dict["client_name"] = client_name
        if client_description is not None:
            body_dict["client_description"] = client_description
        if license is not None:
            body_dict["license"] = license
        if compatibility is not None:
            body_dict["compatibility"] = compatibility
        if client_metadata is not None:
            body_dict["client_metadata"] = client_metadata
        if metadata is not None:
            body_dict["metadata"] = metadata
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id

        request = MetorialRequest(
            path=['skills', skill_id, 'fork'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsForkOutput.from_dict)

    def publish_consumer_skill(self, skill_id: str) -> DashboardInstanceSkillsPublishConsumerSkillOutput:
        """
    Publish consumer skill
    Publishes a consumer-owned skill to the consumer groups they belong to.

    :param skill_id: str
    :return: DashboardInstanceSkillsPublishConsumerSkillOutput
    """
        request = MetorialRequest(
            path=['skills', skill_id, 'publish']
        )
        return self._post(request).transform(mapDashboardInstanceSkillsPublishConsumerSkillOutput.from_dict)

    def duplicate(self, skill_id: str, *, name: str, description: Optional[str] = None, client_name: Optional[str] = None, client_description: Optional[str] = None, license: Optional[str] = None, compatibility: Optional[str] = None, client_metadata: Optional[Dict[str, Any]] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceSkillsDuplicateOutput:
        """
    Duplicate skill
    Duplicates a skill.

    :param skill_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param client_name: Optional[str] (optional)
    :param client_description: Optional[str] (optional)
    :param license: Optional[str] (optional)
    :param compatibility: Optional[str] (optional)
    :param client_metadata: Optional[Dict[str, Any]] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceSkillsDuplicateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if client_name is not None:
            body_dict["client_name"] = client_name
        if client_description is not None:
            body_dict["client_description"] = client_description
        if license is not None:
            body_dict["license"] = license
        if compatibility is not None:
            body_dict["compatibility"] = compatibility
        if client_metadata is not None:
            body_dict["client_metadata"] = client_metadata
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['skills', skill_id, 'duplicate'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsDuplicateOutput.from_dict)