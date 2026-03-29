from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceIdentitiesDelegationConfigsListOutput, DashboardInstanceIdentitiesDelegationConfigsListOutput, mapDashboardInstanceIdentitiesDelegationConfigsListQuery, DashboardInstanceIdentitiesDelegationConfigsListQuery, mapDashboardInstanceIdentitiesDelegationConfigsGetOutput, DashboardInstanceIdentitiesDelegationConfigsGetOutput, mapDashboardInstanceIdentitiesDelegationConfigsCreateOutput, DashboardInstanceIdentitiesDelegationConfigsCreateOutput, mapDashboardInstanceIdentitiesDelegationConfigsCreateBody, DashboardInstanceIdentitiesDelegationConfigsCreateBody, mapDashboardInstanceIdentitiesDelegationConfigsUpdateOutput, DashboardInstanceIdentitiesDelegationConfigsUpdateOutput, mapDashboardInstanceIdentitiesDelegationConfigsUpdateBody, DashboardInstanceIdentitiesDelegationConfigsUpdateBody, mapDashboardInstanceIdentitiesDelegationConfigsDeleteOutput, DashboardInstanceIdentitiesDelegationConfigsDeleteOutput

class MetorialIdentitiesDelegationConfigsEndpoint(BaseMetorialEndpoint):
    """Delegation configs define the default policy for sub-delegation behavior and delegation depth."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, search: Optional[str] = None, status: Optional[Union[str, List[str]]] = None, id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceIdentitiesDelegationConfigsListOutput:
        """
    List identity delegation configs
    Returns a paginated list of identity delegation configs.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param search: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceIdentitiesDelegationConfigsListOutput
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

        request = MetorialRequest(
            path=['identity-delegation-configs'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesDelegationConfigsListOutput.from_dict)

    def get(self, identity_delegation_config_id: str) -> DashboardInstanceIdentitiesDelegationConfigsGetOutput:
        """
    Get identity delegation config
    Retrieves a specific identity delegation config by ID.

    :param identity_delegation_config_id: str
    :return: DashboardInstanceIdentitiesDelegationConfigsGetOutput
    """
        request = MetorialRequest(
            path=['identity-delegation-configs', identity_delegation_config_id]
        )
        return self._get(request).transform(mapDashboardInstanceIdentitiesDelegationConfigsGetOutput.from_dict)

    def create(self, *, sub_delegation_behavior: str, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, sub_delegation_depth: Optional[float] = None) -> DashboardInstanceIdentitiesDelegationConfigsCreateOutput:
        """
    Create identity delegation config
    Creates a new identity delegation config.

    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param sub_delegation_behavior: str
    :param sub_delegation_depth: Optional[float] (optional)
    :return: DashboardInstanceIdentitiesDelegationConfigsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        body_dict["sub_delegation_behavior"] = sub_delegation_behavior
        if sub_delegation_depth is not None:
            body_dict["sub_delegation_depth"] = sub_delegation_depth

        request = MetorialRequest(
            path=['identity-delegation-configs'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceIdentitiesDelegationConfigsCreateOutput.from_dict)

    def update(self, identity_delegation_config_id: str, *, name: Optional[str] = None, description: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None, sub_delegation_behavior: Optional[str] = None, sub_delegation_depth: Optional[float] = None) -> DashboardInstanceIdentitiesDelegationConfigsUpdateOutput:
        """
    Update identity delegation config
    Updates mutable fields on an existing identity delegation config.

    :param identity_delegation_config_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param sub_delegation_behavior: Optional[str] (optional)
    :param sub_delegation_depth: Optional[float] (optional)
    :return: DashboardInstanceIdentitiesDelegationConfigsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if metadata is not None:
            body_dict["metadata"] = metadata
        if sub_delegation_behavior is not None:
            body_dict["sub_delegation_behavior"] = sub_delegation_behavior
        if sub_delegation_depth is not None:
            body_dict["sub_delegation_depth"] = sub_delegation_depth

        request = MetorialRequest(
            path=['identity-delegation-configs', identity_delegation_config_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceIdentitiesDelegationConfigsUpdateOutput.from_dict)

    def delete(self, identity_delegation_config_id: str) -> DashboardInstanceIdentitiesDelegationConfigsDeleteOutput:
        """
    Delete identity delegation config
    Archives an identity delegation config.

    :param identity_delegation_config_id: str
    :return: DashboardInstanceIdentitiesDelegationConfigsDeleteOutput
    """
        request = MetorialRequest(
            path=['identity-delegation-configs', identity_delegation_config_id]
        )
        return self._delete(request).transform(mapDashboardInstanceIdentitiesDelegationConfigsDeleteOutput.from_dict)