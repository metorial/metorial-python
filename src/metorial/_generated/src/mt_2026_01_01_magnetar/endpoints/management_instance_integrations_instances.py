from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationsInstancesListOutput, DashboardInstanceIntegrationsInstancesListOutput, mapDashboardInstanceIntegrationsInstancesListQuery, DashboardInstanceIntegrationsInstancesListQuery, mapDashboardInstanceIntegrationsInstancesGetOutput, DashboardInstanceIntegrationsInstancesGetOutput, mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput, DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput, mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateBody, DashboardInstanceIntegrationsInstancesCreateSessionTemplateBody, mapDashboardInstanceIntegrationsInstancesCreateSessionOutput, DashboardInstanceIntegrationsInstancesCreateSessionOutput, mapDashboardInstanceIntegrationsInstancesCreateSessionBody, DashboardInstanceIntegrationsInstancesCreateSessionBody, mapDashboardInstanceIntegrationsInstancesCreateOutput, DashboardInstanceIntegrationsInstancesCreateOutput, mapDashboardInstanceIntegrationsInstancesCreateBody, DashboardInstanceIntegrationsInstancesCreateBody, mapDashboardInstanceIntegrationsInstancesUpdateOutput, DashboardInstanceIntegrationsInstancesUpdateOutput, mapDashboardInstanceIntegrationsInstancesUpdateBody, DashboardInstanceIntegrationsInstancesUpdateBody, mapDashboardInstanceIntegrationsInstancesDeleteOutput, DashboardInstanceIntegrationsInstancesDeleteOutput

class MetorialManagementInstanceIntegrationsInstancesEndpoint(BaseMetorialEndpoint):
    """Integration instances materialize an integration for a specific actor, identity, or runtime configuration."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, integration_provider_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, identity_credential_id: Optional[Union[str, List[str]]] = None, identity_actor_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, session_template_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstancesListOutput:
        """
    List integration instances
    Returns a paginated list of integration instances.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param integration_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param integration_provider_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param identity_credential_id: Optional[Union[str, List[str]]] (optional)
    :param identity_actor_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param session_template_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstancesListOutput
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
        if integration_id is not None:
            query_dict["integration_id"] = integration_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if integration_provider_id is not None:
            query_dict["integration_provider_id"] = integration_provider_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if identity_credential_id is not None:
            query_dict["identity_credential_id"] = identity_credential_id
        if identity_actor_id is not None:
            query_dict["identity_actor_id"] = identity_actor_id
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
            path=['instances', instance_id, 'integration-instances'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsInstancesListOutput.from_dict)

    def get(self, instance_id: str, integration_instance_id: str) -> DashboardInstanceIntegrationsInstancesGetOutput:
        """
    Get integration instance
    Retrieves a specific integration instance.

    :param instance_id: str
    :param integration_instance_id: str
    :return: DashboardInstanceIntegrationsInstancesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instances', integration_instance_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsInstancesGetOutput.from_dict)

    def create_session_template(self, instance_id: str, integration_instance_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput:
        """
    Create integration instance session template
    Creates or updates the shared session template for a specific integration instance.

    :param instance_id: str
    :param integration_instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput
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
            path=['instances', instance_id, 'integration-instances', integration_instance_id, 'session-template'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput.from_dict)

    def create_session(self, instance_id: str, integration_instance_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsInstancesCreateSessionOutput:
        """
    Create integration instance session
    Creates a session from the shared session template of a specific integration instance.

    :param instance_id: str
    :param integration_instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsInstancesCreateSessionOutput
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
            path=['instances', instance_id, 'integration-instances', integration_instance_id, 'session'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsInstancesCreateSessionOutput.from_dict)

    def create(self, instance_id: str, *, integration_id: str, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, identity_actor_id: Optional[str] = None, identity_id: Optional[str] = None, providers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceIntegrationsInstancesCreateOutput:
        """
    Create integration instance
    Creates a new integration instance.

    :param instance_id: str
    :param integration_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param identity_actor_id: Optional[str] (optional)
    :param identity_id: Optional[str] (optional)
    :param providers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceIntegrationsInstancesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["integration_id"] = integration_id
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if identity_actor_id is not None:
            body_dict["identity_actor_id"] = identity_actor_id
        if identity_id is not None:
            body_dict["identity_id"] = identity_id
        if providers is not None:
            body_dict["providers"] = providers

        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instances'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsInstancesCreateOutput.from_dict)

    def update(self, instance_id: str, integration_instance_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, identity_actor_id: Optional[str] = None, identity_id: Optional[str] = None, providers: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceIntegrationsInstancesUpdateOutput:
        """
    Update integration instance
    Updates a specific integration instance.

    :param instance_id: str
    :param integration_instance_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param identity_actor_id: Optional[str] (optional)
    :param identity_id: Optional[str] (optional)
    :param providers: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceIntegrationsInstancesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if identity_actor_id is not None:
            body_dict["identity_actor_id"] = identity_actor_id
        if identity_id is not None:
            body_dict["identity_id"] = identity_id
        if providers is not None:
            body_dict["providers"] = providers

        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instances', integration_instance_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIntegrationsInstancesUpdateOutput.from_dict)

    def delete(self, instance_id: str, integration_instance_id: str) -> DashboardInstanceIntegrationsInstancesDeleteOutput:
        """
    Delete integration instance
    Archives a specific integration instance.

    :param instance_id: str
    :param integration_instance_id: str
    :return: DashboardInstanceIntegrationsInstancesDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'integration-instances', integration_instance_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIntegrationsInstancesDeleteOutput.from_dict)