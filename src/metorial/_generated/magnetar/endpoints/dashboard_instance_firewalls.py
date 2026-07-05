from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceFirewallsListOutput, DashboardInstanceFirewallsListOutput, mapDashboardInstanceFirewallsListQuery, DashboardInstanceFirewallsListQuery, mapDashboardInstanceFirewallsGetOutput, DashboardInstanceFirewallsGetOutput, mapDashboardInstanceFirewallsCreateOutput, DashboardInstanceFirewallsCreateOutput, mapDashboardInstanceFirewallsCreateBody, DashboardInstanceFirewallsCreateBody, mapDashboardInstanceFirewallsUpdateOutput, DashboardInstanceFirewallsUpdateOutput, mapDashboardInstanceFirewallsUpdateBody, DashboardInstanceFirewallsUpdateBody, mapDashboardInstanceFirewallsDeleteOutput, DashboardInstanceFirewallsDeleteOutput

class MetorialDashboardInstanceFirewallsEndpoint(BaseMetorialEndpoint):
    """Manage firewalls and their attached network policies."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, slug: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, network_id: Optional[Union[str, List[str]]] = None, enclave_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, network_policy_id: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None, updated_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceFirewallsListOutput:
        """
    List firewalls
    Returns a paginated list of firewalls.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param slug: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param network_id: Optional[Union[str, List[str]]] (optional)
    :param enclave_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param network_policy_id: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :param updated_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceFirewallsListOutput
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
        if slug is not None:
            query_dict["slug"] = slug
        if status is not None:
            query_dict["status"] = status
        if network_id is not None:
            query_dict["network_id"] = network_id
        if enclave_id is not None:
            query_dict["enclave_id"] = enclave_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if network_policy_id is not None:
            query_dict["network_policy_id"] = network_policy_id
        if created_at is not None:
            query_dict["created_at"] = created_at
        if updated_at is not None:
            query_dict["updated_at"] = updated_at

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'firewalls'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceFirewallsListOutput.from_dict)

    def get(self, instance_id: str, firewall_id: str) -> DashboardInstanceFirewallsGetOutput:
        """
    Get firewall
    Retrieves a specific firewall by ID.

    :param instance_id: str
    :param firewall_id: str
    :return: DashboardInstanceFirewallsGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'firewalls', firewall_id]
        )
        return self._get(request).transform(mapDashboardInstanceFirewallsGetOutput.from_dict)

    def create(self, instance_id: str, *, name: str, network_id: str, description: Optional[str] = None, slug: Optional[str] = None, bindings: Optional[List[Dict[str, Any]]] = None, network_policy_ids: Optional[List[str]] = None) -> DashboardInstanceFirewallsCreateOutput:
        """
    Create firewall
    Creates a new firewall.

    :param instance_id: str
    :param name: str
    :param description: Optional[str] (optional)
    :param slug: Optional[str] (optional)
    :param network_id: str
    :param bindings: Optional[List[Dict[str, Any]]] (optional)
    :param network_policy_ids: Optional[List[str]] (optional)
    :return: DashboardInstanceFirewallsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if slug is not None:
            body_dict["slug"] = slug
        body_dict["network_id"] = network_id
        if bindings is not None:
            body_dict["bindings"] = bindings
        if network_policy_ids is not None:
            body_dict["network_policy_ids"] = network_policy_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'firewalls'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceFirewallsCreateOutput.from_dict)

    def update(self, instance_id: str, firewall_id: str, *, name: Optional[str] = None, description: Optional[str] = None, slug: Optional[str] = None, network_policy_ids: Optional[List[str]] = None) -> DashboardInstanceFirewallsUpdateOutput:
        """
    Update firewall
    Updates a firewall definition.

    :param instance_id: str
    :param firewall_id: str
    :param name: Optional[str] (optional)
    :param description: Optional[str] (optional)
    :param slug: Optional[str] (optional)
    :param network_policy_ids: Optional[List[str]] (optional)
    :return: DashboardInstanceFirewallsUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if description is not None:
            body_dict["description"] = description
        if slug is not None:
            body_dict["slug"] = slug
        if network_policy_ids is not None:
            body_dict["network_policy_ids"] = network_policy_ids

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'firewalls', firewall_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceFirewallsUpdateOutput.from_dict)

    def delete(self, instance_id: str, firewall_id: str) -> DashboardInstanceFirewallsDeleteOutput:
        """
    Delete firewall
    Archives a firewall.

    :param instance_id: str
    :param firewall_id: str
    :return: DashboardInstanceFirewallsDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'firewalls', firewall_id]
        )
        return self._delete(request).transform(mapDashboardInstanceFirewallsDeleteOutput.from_dict)