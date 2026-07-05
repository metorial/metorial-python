from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIdentitiesDelegationRequestsListOutput, DashboardInstanceIdentitiesDelegationRequestsListOutput, mapDashboardInstanceIdentitiesDelegationRequestsListQuery, DashboardInstanceIdentitiesDelegationRequestsListQuery, mapDashboardInstanceIdentitiesDelegationRequestsGetOutput, DashboardInstanceIdentitiesDelegationRequestsGetOutput, mapDashboardInstanceIdentitiesDelegationRequestsGetQuery, DashboardInstanceIdentitiesDelegationRequestsGetQuery, mapDashboardInstanceIdentitiesDelegationRequestsCreateOutput, DashboardInstanceIdentitiesDelegationRequestsCreateOutput, mapDashboardInstanceIdentitiesDelegationRequestsCreateBody, DashboardInstanceIdentitiesDelegationRequestsCreateBody, mapDashboardInstanceIdentitiesDelegationRequestsApproveOutput, DashboardInstanceIdentitiesDelegationRequestsApproveOutput, mapDashboardInstanceIdentitiesDelegationRequestsApproveQuery, DashboardInstanceIdentitiesDelegationRequestsApproveQuery, mapDashboardInstanceIdentitiesDelegationRequestsDenyOutput, DashboardInstanceIdentitiesDelegationRequestsDenyOutput, mapDashboardInstanceIdentitiesDelegationRequestsDenyQuery, DashboardInstanceIdentitiesDelegationRequestsDenyQuery

class MetorialDashboardInstanceIdentitiesDelegationRequestsEndpoint(BaseMetorialEndpoint):
    """Identity delegation requests represent approval workflows for creating delegations that require consent."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, actor_id: Optional[Union[str, List[str]]] = None, identity_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentitiesDelegationRequestsListOutput:
        """
    List identity delegation requests
    Returns a paginated list of identity delegation requests.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param actor_id: Optional[Union[str, List[str]]] (optional)
    :param identity_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentitiesDelegationRequestsListOutput
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
        if actor_id is not None:
            query_dict["actor_id"] = actor_id
        if identity_id is not None:
            query_dict["identity_id"] = identity_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'identity-delegation-requests'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesDelegationRequestsListOutput.from_dict)

    def get(self, instance_id: str, identity_delegation_request_id: str, *, allow_deleted: Optional[bool] = None) -> DashboardInstanceIdentitiesDelegationRequestsGetOutput:
        """
    Get identity delegation request
    Retrieves a specific identity delegation request by ID.

    :param instance_id: str
    :param identity_delegation_request_id: str
    :param allow_deleted: Optional[bool] (optional)
    :return: DashboardInstanceIdentitiesDelegationRequestsGetOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if allow_deleted is not None:
            query_dict["allow_deleted"] = allow_deleted

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'identity-delegation-requests', identity_delegation_request_id],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesDelegationRequestsGetOutput.from_dict)

    def create(self, instance_id: str, *, identity_id: str, requester_actor_id: str, expires_at: datetime, delegator_actor_id: Optional[str] = None, permissions: Optional[List[str]] = None, delegation_config_id: Optional[str] = None, credential_overrides: Optional[List[Dict[str, Any]]] = None, note: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentitiesDelegationRequestsCreateOutput:
        """
    Create identity delegation request
    Creates a new identity delegation request.

    :param instance_id: str
    :param identity_id: str
    :param requester_actor_id: str
    :param delegator_actor_id: Optional[str] (optional)
    :param permissions: Optional[List[str]] (optional)
    :param expires_at: datetime
    :param delegation_config_id: Optional[str] (optional)
    :param credential_overrides: Optional[List[Dict[str, Any]]] (optional)
    :param note: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentitiesDelegationRequestsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["identity_id"] = identity_id
        body_dict["requester_actor_id"] = requester_actor_id
        if delegator_actor_id is not None:
            body_dict["delegator_actor_id"] = delegator_actor_id
        if permissions is not None:
            body_dict["permissions"] = permissions
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
            path=['dashboard', 'instances', instance_id, 'identity-delegation-requests'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesDelegationRequestsCreateOutput.from_dict)

    def approve(self, instance_id: str, identity_delegation_request_id: str, *, allow_deleted: Optional[bool] = None) -> DashboardInstanceIdentitiesDelegationRequestsApproveOutput:
        """
    Approve identity delegation request
    Approves an existing identity delegation request.

    :param instance_id: str
    :param identity_delegation_request_id: str
    :param allow_deleted: Optional[bool] (optional)
    :return: DashboardInstanceIdentitiesDelegationRequestsApproveOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if allow_deleted is not None:
            query_dict["allow_deleted"] = allow_deleted

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'identity-delegation-requests', identity_delegation_request_id, 'approve'],
            query=query_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesDelegationRequestsApproveOutput.from_dict)

    def deny(self, instance_id: str, identity_delegation_request_id: str, *, allow_deleted: Optional[bool] = None) -> DashboardInstanceIdentitiesDelegationRequestsDenyOutput:
        """
    Deny identity delegation request
    Denies an existing identity delegation request.

    :param instance_id: str
    :param identity_delegation_request_id: str
    :param allow_deleted: Optional[bool] (optional)
    :return: DashboardInstanceIdentitiesDelegationRequestsDenyOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if allow_deleted is not None:
            query_dict["allow_deleted"] = allow_deleted

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'identity-delegation-requests', identity_delegation_request_id, 'deny'],
            query=query_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesDelegationRequestsDenyOutput.from_dict)