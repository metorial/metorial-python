from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceNetworkPoliciesListOutput, DashboardInstanceNetworkPoliciesListOutput, mapDashboardInstanceNetworkPoliciesListQuery, DashboardInstanceNetworkPoliciesListQuery, mapDashboardInstanceNetworkPoliciesGetOutput, DashboardInstanceNetworkPoliciesGetOutput, mapDashboardInstanceNetworkPoliciesCreateOutput, DashboardInstanceNetworkPoliciesCreateOutput, mapDashboardInstanceNetworkPoliciesCreateBody, DashboardInstanceNetworkPoliciesCreateBody, mapDashboardInstanceNetworkPoliciesUpdateOutput, DashboardInstanceNetworkPoliciesUpdateOutput, mapDashboardInstanceNetworkPoliciesUpdateBody, DashboardInstanceNetworkPoliciesUpdateBody, mapDashboardInstanceNetworkPoliciesDeleteOutput, DashboardInstanceNetworkPoliciesDeleteOutput

class MetorialManagementInstanceNetworkPoliciesEndpoint(BaseMetorialEndpoint):
    """Manage reusable network policy definitions and their rules."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, firewall_id: Optional[Union[str, List[str]]] = None, search: Optional[str] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceNetworkPoliciesListOutput:
        """
    List network policies
    Returns a paginated list of network policies.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param firewall_id: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceNetworkPoliciesListOutput
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
        if id is not None:
            query_dict["id"] = id
        if status is not None:
            query_dict["status"] = status
        if firewall_id is not None:
            query_dict["firewall_id"] = firewall_id
        if search is not None:
            query_dict["search"] = search
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['instances', instance_id, 'network-policies'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceNetworkPoliciesListOutput.from_dict)

    def get(self, instance_id: str, network_policy_id: str) -> DashboardInstanceNetworkPoliciesGetOutput:
        """
    Get network policy
    Retrieves a specific network policy by ID.

    :param instance_id: str
    :param network_policy_id: str
    :return: DashboardInstanceNetworkPoliciesGetOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'network-policies', network_policy_id]
        )
        return self._get(request).transform(mapDashboardInstanceNetworkPoliciesGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, description: Optional[str] = None, rules: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceNetworkPoliciesCreateOutput:
        """
    Create network policy
    Creates a new network policy.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param rules: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceNetworkPoliciesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if rules is not None:
            body_dict["rules"] = rules

        request = MetorialRequest(
            path=['instances', instance_id, 'network-policies'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceNetworkPoliciesCreateOutput.from_dict)

    def update(self, instance_id: str, network_policy_id: str, *, name: Optional[str] = None, description: Optional[str] = None, rules: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceNetworkPoliciesUpdateOutput:
        """
    Update network policy
    Updates a network policy definition.

    :param instance_id: str
    :param network_policy_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param rules: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceNetworkPoliciesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if rules is not None:
            body_dict["rules"] = rules

        request = MetorialRequest(
            path=['instances', instance_id, 'network-policies', network_policy_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceNetworkPoliciesUpdateOutput.from_dict)

    def delete(self, instance_id: str, network_policy_id: str) -> DashboardInstanceNetworkPoliciesDeleteOutput:
        """
    Delete network policy
    Archives a network policy.

    :param instance_id: str
    :param network_policy_id: str
    :return: DashboardInstanceNetworkPoliciesDeleteOutput
    """
        request = MetorialRequest(
            path=['instances', instance_id, 'network-policies', network_policy_id]
        )
        return self._delete(request).transform(mapDashboardInstanceNetworkPoliciesDeleteOutput.from_dict)