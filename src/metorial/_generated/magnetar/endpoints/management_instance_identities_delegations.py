from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIdentitiesDelegationsListOutput, DashboardInstanceIdentitiesDelegationsListOutput, mapDashboardInstanceIdentitiesDelegationsListQuery, DashboardInstanceIdentitiesDelegationsListQuery, mapDashboardInstanceIdentitiesDelegationsGetOutput, DashboardInstanceIdentitiesDelegationsGetOutput, mapDashboardInstanceIdentitiesDelegationsCreateOutput, DashboardInstanceIdentitiesDelegationsCreateOutput, mapDashboardInstanceIdentitiesDelegationsCreateBody, DashboardInstanceIdentitiesDelegationsCreateBody, mapDashboardInstanceIdentitiesDelegationsRevokeOutput, DashboardInstanceIdentitiesDelegationsRevokeOutput

class MetorialManagementInstanceIdentitiesDelegationsEndpoint(BaseMetorialEndpoint):
    """Identity delegations grant provider permissions from one identity owner to another actor, with optional per-credential overrides."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, permissions: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, owner_actor_id: Optional[Union[str, List[str]]] = None, delegator_actor_id: Optional[Union[str, List[str]]] = None, delegatee_actor_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentitiesDelegationsListOutput:
        """
    List identity delegations
    Returns a paginated list of identity delegations for the instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param permissions: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param owner_actor_id: Optional[Union[str, List[str]]] (optional)
    :param delegator_actor_id: Optional[Union[str, List[str]]] (optional)
    :param delegatee_actor_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentitiesDelegationsListOutput
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
        if permissions is not None:
            query_dict["permissions"] = permissions
        if id is not None:
            query_dict["id"] = id
        if owner_actor_id is not None:
            query_dict["owner_actor_id"] = owner_actor_id
        if delegator_actor_id is not None:
            query_dict["delegator_actor_id"] = delegator_actor_id
        if delegatee_actor_id is not None:
            query_dict["delegatee_actor_id"] = delegatee_actor_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-delegations'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesDelegationsListOutput.from_dict)

    def get(self, instance_id: str, identity_delegation_id: str) -> DashboardInstanceIdentitiesDelegationsGetOutput:
        """
    Get identity delegation
    Retrieves a specific identity delegation by ID.

    :param instance_id: str
    :param identity_delegation_id: str
    :return: DashboardInstanceIdentitiesDelegationsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identity-delegations', identity_delegation_id]
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesDelegationsGetOutput.from_dict)

    def create(self, instance_id: str, *, identity_id: str, delegatee_actor_id: str, delegator_actor_id: Optional[str] = None, permissions: Optional[List[str]] = None, expires_at: Optional[datetime] = None, delegation_config_id: Optional[str] = None, credential_overrides: Optional[List[Dict[str, Any]]] = None, note: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentitiesDelegationsCreateOutput:
        """
    Create identity delegation
    Creates a new identity delegation.

    :param instance_id: str
    :param identity_id: str
    :param delegator_actor_id: Optional[str] (optional)
    :param delegatee_actor_id: str
    :param permissions: Optional[List[str]] (optional)
    :param expires_at: Optional[datetime] (optional)
    :param delegation_config_id: Optional[str] (optional)
    :param credential_overrides: Optional[List[Dict[str, Any]]] (optional)
    :param note: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentitiesDelegationsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["identity_id"] = identity_id
        if delegator_actor_id is not None:
            body_dict["delegator_actor_id"] = delegator_actor_id
        body_dict["delegatee_actor_id"] = delegatee_actor_id
        if permissions is not None:
            body_dict["permissions"] = permissions
        if expires_at is not None:
            body_dict["expires_at"] = expires_at
        if delegation_config_id is not None:
            body_dict["delegation_config_id"] = delegation_config_id
        if credential_overrides is not None:
            body_dict["credential_overrides"] = credential_overrides
        if note is not None:
            body_dict["note"] = note
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-delegations'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesDelegationsCreateOutput.from_dict)

    def revoke(self, instance_id: str, identity_delegation_id: str) -> DashboardInstanceIdentitiesDelegationsRevokeOutput:
        """
    Revoke identity delegation
    Revokes an existing identity delegation.

    :param instance_id: str
    :param identity_delegation_id: str
    :return: DashboardInstanceIdentitiesDelegationsRevokeOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identity-delegations', identity_delegation_id, 'revoke']
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesDelegationsRevokeOutput.from_dict)