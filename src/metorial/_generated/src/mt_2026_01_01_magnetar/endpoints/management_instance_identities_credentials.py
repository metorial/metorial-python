from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIdentitiesCredentialsListOutput, DashboardInstanceIdentitiesCredentialsListOutput, mapDashboardInstanceIdentitiesCredentialsListQuery, DashboardInstanceIdentitiesCredentialsListQuery, mapDashboardInstanceIdentitiesCredentialsGetOutput, DashboardInstanceIdentitiesCredentialsGetOutput, mapDashboardInstanceIdentitiesCredentialsCreateOutput, DashboardInstanceIdentitiesCredentialsCreateOutput, mapDashboardInstanceIdentitiesCredentialsCreateBody, DashboardInstanceIdentitiesCredentialsCreateBody, mapDashboardInstanceIdentitiesCredentialsUpdateOutput, DashboardInstanceIdentitiesCredentialsUpdateOutput, mapDashboardInstanceIdentitiesCredentialsUpdateBody, DashboardInstanceIdentitiesCredentialsUpdateBody, mapDashboardInstanceIdentitiesCredentialsDeleteOutput, DashboardInstanceIdentitiesCredentialsDeleteOutput

class MetorialManagementInstanceIdentitiesCredentialsEndpoint(BaseMetorialEndpoint):
    """Identity credentials bind an identity to concrete provider deployment, config, and auth resources."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, agent_id: Optional[Union[str, List[str]]] = None, actor_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, provider_deployment_id: Optional[Union[str, List[str]]] = None, provider_config_id: Optional[Union[str, List[str]]] = None, provider_auth_config_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentitiesCredentialsListOutput:
        """
    List identity credentials
    Returns a paginated list of identity credentials for the instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param agent_id: Optional[Union[str, List[str]]] (optional)
    :param actor_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param provider_deployment_id: Optional[Union[str, List[str]]] (optional)
    :param provider_config_id: Optional[Union[str, List[str]]] (optional)
    :param provider_auth_config_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentitiesCredentialsListOutput
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
        if agent_id is not None:
            query_dict["agent_id"] = agent_id
        if actor_id is not None:
            query_dict["actor_id"] = actor_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if provider_deployment_id is not None:
            query_dict["provider_deployment_id"] = provider_deployment_id
        if provider_config_id is not None:
            query_dict["provider_config_id"] = provider_config_id
        if provider_auth_config_id is not None:
            query_dict["provider_auth_config_id"] = provider_auth_config_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-credentials'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesCredentialsListOutput.from_dict)

    def get(self, instance_id: str, identity_credential_id: str) -> DashboardInstanceIdentitiesCredentialsGetOutput:
        """
    Get identity credential
    Retrieves a specific identity credential by ID.

    :param instance_id: str
    :param identity_credential_id: str
    :return: DashboardInstanceIdentitiesCredentialsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identity-credentials', identity_credential_id]
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesCredentialsGetOutput.from_dict)

    def create(self, instance_id: str, *, identity_id: str, deployment_id: Optional[str] = None, config_id: Optional[str] = None, auth_config_id: Optional[str] = None, delegation_config_id: Optional[str] = None) -> DashboardInstanceIdentitiesCredentialsCreateOutput:
        """
    Create identity credential
    Creates a new credential and attaches it to an identity.

    :param instance_id: str
    :param identity_id: str
    :param deployment_id: Optional[str] (optional)
    :param config_id: Optional[str] (optional)
    :param auth_config_id: Optional[str] (optional)
    :param delegation_config_id: Optional[str] (optional)
    :return: DashboardInstanceIdentitiesCredentialsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["identity_id"] = identity_id
        if deployment_id is not None:
            body_dict["deployment_id"] = deployment_id
        if config_id is not None:
            body_dict["config_id"] = config_id
        if auth_config_id is not None:
            body_dict["auth_config_id"] = auth_config_id
        if delegation_config_id is not None:
            body_dict["delegation_config_id"] = delegation_config_id

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-credentials'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesCredentialsCreateOutput.from_dict)

    def update(self, instance_id: str, identity_credential_id: str, *, delegation_config_id: str) -> DashboardInstanceIdentitiesCredentialsUpdateOutput:
        """
    Update identity credential
    Updates the delegation config attached to an identity credential.

    :param instance_id: str
    :param identity_credential_id: str
    :param delegation_config_id: str
    :return: DashboardInstanceIdentitiesCredentialsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["delegation_config_id"] = delegation_config_id

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-credentials', identity_credential_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIdentitiesCredentialsUpdateOutput.from_dict)

    def delete(self, instance_id: str, identity_credential_id: str) -> DashboardInstanceIdentitiesCredentialsDeleteOutput:
        """
    Delete identity credential
    Archives an identity credential.

    :param instance_id: str
    :param identity_credential_id: str
    :return: DashboardInstanceIdentitiesCredentialsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identity-credentials', identity_credential_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIdentitiesCredentialsDeleteOutput.from_dict)