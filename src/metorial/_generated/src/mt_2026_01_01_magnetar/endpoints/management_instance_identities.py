from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIdentitiesListOutput, DashboardInstanceIdentitiesListOutput, mapDashboardInstanceIdentitiesListQuery, DashboardInstanceIdentitiesListQuery, mapDashboardInstanceIdentitiesGetOutput, DashboardInstanceIdentitiesGetOutput, mapDashboardInstanceIdentitiesCreateOutput, DashboardInstanceIdentitiesCreateOutput, mapDashboardInstanceIdentitiesCreateBody, DashboardInstanceIdentitiesCreateBody, mapDashboardInstanceIdentitiesUpdateOutput, DashboardInstanceIdentitiesUpdateOutput, mapDashboardInstanceIdentitiesUpdateBody, DashboardInstanceIdentitiesUpdateBody, mapDashboardInstanceIdentitiesDeleteOutput, DashboardInstanceIdentitiesDeleteOutput

class MetorialManagementInstanceIdentitiesEndpoint(BaseMetorialEndpoint):
    """Identities bundle credentials under a single owner actor so provider access can be managed and delegated consistently."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None, agent_id: Optional[Union[str, List[str]]] = None, actor_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceIdentitiesListOutput:
        """
    List identities
    Returns a paginated list of identities for the instance.

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
    :param actor_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceIdentitiesListOutput
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
        if actor_id is not None:
            query_dict["actor_id"] = actor_id

        request = MetorialRequest(
            path=['instances', instance_id, 'identities'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesListOutput.from_dict)

    def get(self, instance_id: str, identity_id: str) -> DashboardInstanceIdentitiesGetOutput:
        """
    Get identity
    Retrieves a specific identity by ID.

    :param instance_id: str
    :param identity_id: str
    :return: DashboardInstanceIdentitiesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identities', identity_id]
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesGetOutput.from_dict)

    def create(self, instance_id: str, *, actor_id: str, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, credentials: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceIdentitiesCreateOutput:
        """
    Create identity
    Creates a new identity owned by an existing identity actor.

    :param instance_id: str
    :param actor_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param credentials: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceIdentitiesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["actor_id"] = actor_id
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if credentials is not None:
            body_dict["credentials"] = credentials

        request = MetorialRequest(
            path=['instances', instance_id, 'identities'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesCreateOutput.from_dict)

    def update(self, instance_id: str, identity_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> DashboardInstanceIdentitiesUpdateOutput:
        """
    Update identity
    Updates mutable fields on an existing identity.

    :param instance_id: str
    :param identity_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceIdentitiesUpdateOutput
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
            path=['instances', instance_id, 'identities', identity_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIdentitiesUpdateOutput.from_dict)

    def delete(self, instance_id: str, identity_id: str) -> DashboardInstanceIdentitiesDeleteOutput:
        """
    Delete identity
    Archives an identity.

    :param instance_id: str
    :param identity_id: str
    :return: DashboardInstanceIdentitiesDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'identities', identity_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIdentitiesDeleteOutput.from_dict)