from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceFirewallBindingsListOutput, DashboardInstanceFirewallBindingsListOutput, mapDashboardInstanceFirewallBindingsListQuery, DashboardInstanceFirewallBindingsListQuery, mapDashboardInstanceFirewallBindingsGetOutput, DashboardInstanceFirewallBindingsGetOutput, mapDashboardInstanceFirewallBindingsCreateOutput, DashboardInstanceFirewallBindingsCreateOutput, mapDashboardInstanceFirewallBindingsCreateBody, DashboardInstanceFirewallBindingsCreateBody, mapDashboardInstanceFirewallBindingsDeleteOutput, DashboardInstanceFirewallBindingsDeleteOutput

class MetorialFirewallBindingsEndpoint(BaseMetorialEndpoint):
    """Manage bindings that apply firewalls to enclaves, providers, or networks."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, firewall_id: Optional[Union[str, List[str]]] = None, enclave_id: Optional[Union[str, List[str]]] = None, provider_id: Optional[Union[str, List[str]]] = None, network_id: Optional[Union[str, List[str]]] = None, target_type: Optional[Union[str, List[str]]] = None, created_at: Optional[Dict[str, Any]] = None) -> DashboardInstanceFirewallBindingsListOutput:
        """
    List firewall bindings
    Returns a paginated list of firewall bindings.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param firewall_id: Optional[Union[str, List[str]]] (optional)
    :param enclave_id: Optional[Union[str, List[str]]] (optional)
    :param provider_id: Optional[Union[str, List[str]]] (optional)
    :param network_id: Optional[Union[str, List[str]]] (optional)
    :param target_type: Optional[Union[str, List[str]]] (optional)
    :param created_at: Optional[Dict[str, Any]] (optional)
    :return: DashboardInstanceFirewallBindingsListOutput
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
        if firewall_id is not None:
            query_dict["firewall_id"] = firewall_id
        if enclave_id is not None:
            query_dict["enclave_id"] = enclave_id
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if network_id is not None:
            query_dict["network_id"] = network_id
        if target_type is not None:
            query_dict["target_type"] = target_type
        if created_at is not None:
            query_dict["created_at"] = created_at

        request = MetorialRequest(
            path=['firewall-bindings'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceFirewallBindingsListOutput.from_dict)

    def get(self, firewall_binding_id: str) -> DashboardInstanceFirewallBindingsGetOutput:
        """
    Get firewall binding
    Retrieves a specific firewall binding by ID.

    :param firewall_binding_id: str
    :return: DashboardInstanceFirewallBindingsGetOutput
    """
        request = MetorialRequest(
            path=['firewall-bindings', firewall_binding_id]
        )
        return self._get(request).transform(mapDashboardInstanceFirewallBindingsGetOutput.from_dict)

    def create(self, *, firewall_id: str, target_type: str, enclave_id: Optional[str] = None, provider_id: Optional[str] = None, network_id: Optional[str] = None) -> DashboardInstanceFirewallBindingsCreateOutput:
        """
    Create firewall binding
    Creates a binding that applies a firewall to a target.

    :param firewall_id: str
    :param target_type: str
    :param enclave_id: Optional[str] (optional)
    :param provider_id: Optional[str] (optional)
    :param network_id: Optional[str] (optional)
    :return: DashboardInstanceFirewallBindingsCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["firewall_id"] = firewall_id
        body_dict["target_type"] = target_type
        if enclave_id is not None:
            body_dict["enclave_id"] = enclave_id
        if provider_id is not None:
            body_dict["provider_id"] = provider_id
        if network_id is not None:
            body_dict["network_id"] = network_id

        request = MetorialRequest(
            path=['firewall-bindings'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceFirewallBindingsCreateOutput.from_dict)

    def delete(self, firewall_binding_id: str) -> DashboardInstanceFirewallBindingsDeleteOutput:
        """
    Delete firewall binding
    Deletes a firewall binding.

    :param firewall_binding_id: str
    :return: DashboardInstanceFirewallBindingsDeleteOutput
    """
        request = MetorialRequest(
            path=['firewall-bindings', firewall_binding_id]
        )
        return self._delete(request).transform(mapDashboardInstanceFirewallBindingsDeleteOutput.from_dict)