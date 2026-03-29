from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIdentityActorsListOutput, DashboardInstanceIdentityActorsListOutput, mapDashboardInstanceIdentityActorsListQuery, DashboardInstanceIdentityActorsListQuery, mapDashboardInstanceIdentityActorsGetOutput, DashboardInstanceIdentityActorsGetOutput, mapDashboardInstanceIdentityActorsCreateOutput, DashboardInstanceIdentityActorsCreateOutput, mapDashboardInstanceIdentityActorsCreateBody, DashboardInstanceIdentityActorsCreateBody, mapDashboardInstanceIdentityActorsUpdateOutput, DashboardInstanceIdentityActorsUpdateOutput, mapDashboardInstanceIdentityActorsUpdateBody, DashboardInstanceIdentityActorsUpdateBody, mapDashboardInstanceIdentityActorsDeleteOutput, DashboardInstanceIdentityActorsDeleteOutput

class MetorialManagementInstanceIdentityActorsEndpoint(BaseMetorialEndpoint):
    """Identity actors represent people or agents that can own identities and participate in delegations."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, agent_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceIdentityActorsListOutput:
        """
    List identity actors
    Returns a paginated list of identity actors for the instance.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param agent_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceIdentityActorsListOutput
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
        if agent_id is not None:
            query_dict["agent_id"] = agent_id

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-actors'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentityActorsListOutput.from_dict)

    def get(self, instance_id: str, identity_actor_id: str) -> DashboardInstanceIdentityActorsGetOutput:
        """
    Get identity actor
    Retrieves a specific identity actor by ID.

    :param instance_id: str
    :param identity_actor_id: str
    :return: DashboardInstanceIdentityActorsGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identity-actors', identity_actor_id]
        )
        return self._get(request).transform(mapDashboardInstanceIdentityActorsGetOutput.from_dict)

    def create(self, instance_id: str, *, type: str, name: str, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentityActorsCreateOutput:
        """
    Create identity actor
    Creates a new identity actor.

    :param instance_id: str
    :param type: str
    :param name: str
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentityActorsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["type"] = type
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata

        request = MetorialRequest(
            path=['instances', instance_id, 'identity-actors'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentityActorsCreateOutput.from_dict)

    def update(self, instance_id: str, identity_actor_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentityActorsUpdateOutput:
        """
    Update identity actor
    Updates mutable fields on an existing identity actor.

    :param instance_id: str
    :param identity_actor_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentityActorsUpdateOutput
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
            path=['instances', instance_id, 'identity-actors', identity_actor_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIdentityActorsUpdateOutput.from_dict)

    def delete(self, instance_id: str, identity_actor_id: str) -> DashboardInstanceIdentityActorsDeleteOutput:
        """
    Delete identity actor
    Archives an identity actor.

    :param instance_id: str
    :param identity_actor_id: str
    :return: DashboardInstanceIdentityActorsDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identity-actors', identity_actor_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIdentityActorsDeleteOutput.from_dict)