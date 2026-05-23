from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSkillsConfigurationsCreateOutput, DashboardInstanceSkillsConfigurationsCreateOutput, mapDashboardInstanceSkillsConfigurationsCreateBody, DashboardInstanceSkillsConfigurationsCreateBody, mapDashboardInstanceSkillsConfigurationsListOutput, DashboardInstanceSkillsConfigurationsListOutput, mapDashboardInstanceSkillsConfigurationsListQuery, DashboardInstanceSkillsConfigurationsListQuery, mapDashboardInstanceSkillsConfigurationsGetOutput, DashboardInstanceSkillsConfigurationsGetOutput, mapDashboardInstanceSkillsConfigurationsUpdateOutput, DashboardInstanceSkillsConfigurationsUpdateOutput, mapDashboardInstanceSkillsConfigurationsUpdateBody, DashboardInstanceSkillsConfigurationsUpdateBody, mapDashboardInstanceSkillsConfigurationsDeleteOutput, DashboardInstanceSkillsConfigurationsDeleteOutput

class MetorialManagementInstanceSkillsConfigurationsEndpoint(BaseMetorialEndpoint):
    """Manage configuration profiles for skill execution."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, instance_id: str, *, allow_scripts: Optional[bool] = None, allowed_file_extensions: Optional[List[str]] = None, allow_non_standard_directories: Optional[bool] = None) -> DashboardInstanceSkillsConfigurationsCreateOutput:
        """
    Create skill configuration
    Creates a new non-default skill configuration.

    :param instance_id: str
    :param allow_scripts: Optional[bool] (optional)
    :param allowed_file_extensions: Optional[List[str]] (optional)
    :param allow_non_standard_directories: Optional[bool] (optional)
    :return: DashboardInstanceSkillsConfigurationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if allow_scripts is not None:
            body_dict["allow_scripts"] = allow_scripts
        if allowed_file_extensions is not None:
            body_dict["allowed_file_extensions"] = allowed_file_extensions
        if allow_non_standard_directories is not None:
            body_dict["allow_non_standard_directories"] = allow_non_standard_directories

        request = MetorialRequest(
            path=['instances', instance_id, 'skills', 'configurations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSkillsConfigurationsCreateOutput.from_dict)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None) -> DashboardInstanceSkillsConfigurationsListOutput:
        """
    List skill configurations
    Returns a paginated list of visible skill configurations.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :return: DashboardInstanceSkillsConfigurationsListOutput
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

        request = MetorialRequest(
            path=['instances', instance_id, 'skills', 'configurations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSkillsConfigurationsListOutput.from_dict)

    def get(self, instance_id: str, skill_configuration_id: str) -> DashboardInstanceSkillsConfigurationsGetOutput:
        """
    Get skill configuration
    Retrieves a specific skill configuration by ID, or the default.

    :param instance_id: str
    :param skill_configuration_id: str
    :return: DashboardInstanceSkillsConfigurationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', 'configurations', skill_configuration_id]
        )
        return self._get(request).transform(mapDashboardInstanceSkillsConfigurationsGetOutput.from_dict)

    def update(self, instance_id: str, skill_configuration_id: str, *, allow_scripts: Optional[bool] = None, allowed_file_extensions: Optional[List[str]] = None, allow_non_standard_directories: Optional[bool] = None) -> DashboardInstanceSkillsConfigurationsUpdateOutput:
        """
    Update skill configuration
    Updates a specific skill configuration. Updating default creates it first if needed.

    :param instance_id: str
    :param skill_configuration_id: str
    :param allow_scripts: Optional[bool] (optional)
    :param allowed_file_extensions: Optional[List[str]] (optional)
    :param allow_non_standard_directories: Optional[bool] (optional)
    :return: DashboardInstanceSkillsConfigurationsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if allow_scripts is not None:
            body_dict["allow_scripts"] = allow_scripts
        if allowed_file_extensions is not None:
            body_dict["allowed_file_extensions"] = allowed_file_extensions
        if allow_non_standard_directories is not None:
            body_dict["allow_non_standard_directories"] = allow_non_standard_directories

        request = MetorialRequest(
            path=['instances', instance_id, 'skills', 'configurations', skill_configuration_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSkillsConfigurationsUpdateOutput.from_dict)

    def delete(self, instance_id: str, skill_configuration_id: str) -> DashboardInstanceSkillsConfigurationsDeleteOutput:
        """
    Delete skill configuration
    Soft deletes a specific non-internal skill configuration.

    :param instance_id: str
    :param skill_configuration_id: str
    :return: DashboardInstanceSkillsConfigurationsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'skills', 'configurations', skill_configuration_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSkillsConfigurationsDeleteOutput.from_dict)