from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIntegrationsSetupSessionsListOutput, DashboardInstanceIntegrationsSetupSessionsListOutput, mapDashboardInstanceIntegrationsSetupSessionsListQuery, DashboardInstanceIntegrationsSetupSessionsListQuery, mapDashboardInstanceIntegrationsSetupSessionsGetOutput, DashboardInstanceIntegrationsSetupSessionsGetOutput, mapDashboardInstanceIntegrationsSetupSessionsCreateOutput, DashboardInstanceIntegrationsSetupSessionsCreateOutput, mapDashboardInstanceIntegrationsSetupSessionsCreateBody, DashboardInstanceIntegrationsSetupSessionsCreateBody

class MetorialDashboardInstanceIntegrationsSetupSessionsEndpoint(BaseMetorialEndpoint):
    """Integration setup sessions orchestrate configuring every provider required by an integration instance."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, integration_id: Optional[Union[str, List[str]]] = None, integration_instance_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsSetupSessionsListOutput:
        """
    List integration setup sessions
    Returns a paginated list of integration setup sessions.

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
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsSetupSessionsListOutput
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
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-setup-sessions'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsSetupSessionsListOutput.from_dict)

    def get(self, instance_id: str, integration_setup_session_id: str) -> DashboardInstanceIntegrationsSetupSessionsGetOutput:
        """
    Get integration setup session
    Retrieves a specific integration setup session.

    :param instance_id: str
    :param integration_setup_session_id: str
    :return: DashboardInstanceIntegrationsSetupSessionsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-setup-sessions', integration_setup_session_id]
        )
        return self._get(request).transform(mapDashboardInstanceIntegrationsSetupSessionsGetOutput.from_dict)

    def create(self, instance_id: str, *, integration_id: str, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, identity_actor_id: Optional[str] = None, identity_id: Optional[str] = None, expires_at: Optional[datetime] = None, redirect_url: Optional[str] = None, configuration: Optional[Dict[str, Any]] = None) -> DashboardInstanceIntegrationsSetupSessionsCreateOutput:
        """
    Create integration setup session
    Creates a new integration setup session and draft integration instance.

    :param instance_id: str
    :param integration_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param identity_actor_id: Optional[str] (optional)
    :param identity_id: Optional[str] (optional)
    :param expires_at: Optional[datetime] (optional)
    :param redirect_url: Optional[str] (optional)
    :param configuration: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIntegrationsSetupSessionsCreateOutput
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
        if expires_at is not None:
            body_dict["expires_at"] = expires_at
        if redirect_url is not None:
            body_dict["redirect_url"] = redirect_url
        if configuration is not None:
            body_dict["configuration"] = configuration

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'integration-setup-sessions'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIntegrationsSetupSessionsCreateOutput.from_dict)