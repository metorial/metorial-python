from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationsInstanceGroupsListOutput, DashboardInstanceIntegrationsInstanceGroupsListOutput, mapDashboardInstanceIntegrationsInstanceGroupsListQuery, DashboardInstanceIntegrationsInstanceGroupsListQuery, mapDashboardInstanceIntegrationsInstanceGroupsGetOutput, DashboardInstanceIntegrationsInstanceGroupsGetOutput, mapDashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateOutput, DashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateOutput, mapDashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateBody, DashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateBody, mapDashboardInstanceIntegrationsInstanceGroupsCreateSessionOutput, DashboardInstanceIntegrationsInstanceGroupsCreateSessionOutput, mapDashboardInstanceIntegrationsInstanceGroupsCreateSessionBody, DashboardInstanceIntegrationsInstanceGroupsCreateSessionBody, mapDashboardInstanceIntegrationsInstanceGroupsCreateOutput, DashboardInstanceIntegrationsInstanceGroupsCreateOutput, mapDashboardInstanceIntegrationsInstanceGroupsCreateBody, DashboardInstanceIntegrationsInstanceGroupsCreateBody, mapDashboardInstanceIntegrationsInstanceGroupsUpdateOutput, DashboardInstanceIntegrationsInstanceGroupsUpdateOutput, mapDashboardInstanceIntegrationsInstanceGroupsUpdateBody, DashboardInstanceIntegrationsInstanceGroupsUpdateBody, mapDashboardInstanceIntegrationsInstanceGroupsDeleteOutput, DashboardInstanceIntegrationsInstanceGroupsDeleteOutput

class MetorialDashboardInstanceIntegrationsInstanceGroupsEndpoint(BaseMetorialEndpoint):
    """Integration instance groups combine instance providers into a grouped routed configuration."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, integration_instance_id: Optional[Union[str, List[str]]] = None, integration_instance_provider_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, integration_provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, session_template_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstanceGroupsListOutput:
        """
    List integration instance groups
    Returns a paginated list of integration instance groups.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param integration_instance_id: Optional[Union[str, List[str]]] (optional)
    :param integration_instance_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param integration_provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstanceGroupsListOutput
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
        if status is not None:
            query_dict["status"] = status
        if id is not None:
            query_dict["id"] = id
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if integration_instance_id is not None:
            query_dict["integration_instance_id"] = integration_instance_id
        if integration_instance_provider_id is not None:
            query_dict["integration_instance_provider_id"] = integration_instance_provider_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if integration_provider_id is not None:
            query_dict["integration_provider_id"] = integration_provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if session_template_id is not None:
            query_dict["session_template_id"] = session_template_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsListOutput.from_dict)

    def get(self, instance_id: str, integration_instance_group_id: str) -> DashboardInstanceIntegrationsInstanceGroupsGetOutput:
        """
    Get integration instance group
    Retrieves a specific integration instance group.

    :param instance_id: str
    :param integration_instance_group_id: str
    :return: DashboardInstanceIntegrationsInstanceGroupsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups', integration_instance_group_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsGetOutput.from_dict)

    def create_session_template(self, instance_id: str, integration_instance_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateOutput:
        """
    Create integration instance group session template
    Creates or updates the shared session template for a specific integration instance group.

    :param instance_id: str
    :param integration_instance_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateOutput
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
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups', integration_instance_group_id, 'session-template'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsCreateSessionTemplateOutput.from_dict)

    def create_session(self, instance_id: str, integration_instance_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstanceGroupsCreateSessionOutput:
        """
    Create integration instance group session
    Creates a session from the shared session template of a specific integration instance group.

    :param instance_id: str
    :param integration_instance_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstanceGroupsCreateSessionOutput
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
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups', integration_instance_group_id, 'session'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsCreateSessionOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, providers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceIntegrationsInstanceGroupsCreateOutput:
        """
    Create integration instance group
    Creates a new integration instance group.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param providers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceIntegrationsInstanceGroupsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if providers is not None:
            body_dict["providers"] = providers

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsCreateOutput.from_dict)

    def update(self, instance_id: str, integration_instance_group_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, providers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceIntegrationsInstanceGroupsUpdateOutput:
        """
    Update integration instance group
    Updates a specific integration instance group.

    :param instance_id: str
    :param integration_instance_group_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param providers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceIntegrationsInstanceGroupsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if providers is not None:
            body_dict["providers"] = providers

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups', integration_instance_group_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsUpdateOutput.from_dict)

    def delete(self, instance_id: str, integration_instance_group_id: str) -> DashboardInstanceIntegrationsInstanceGroupsDeleteOutput:
        """
    Delete integration instance group
    Archives a specific integration instance group.

    :param instance_id: str
    :param integration_instance_group_id: str
    :return: DashboardInstanceIntegrationsInstanceGroupsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-instance-groups', integration_instance_group_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIntegrationsInstanceGroupsDeleteOutput.from_dict)