from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceFirewallsNetworkPoliciesAttachOutput, DashboardInstanceFirewallsNetworkPoliciesAttachOutput, mapDashboardInstanceFirewallsNetworkPoliciesAttachBody, DashboardInstanceFirewallsNetworkPoliciesAttachBody, mapDashboardInstanceFirewallsNetworkPoliciesDetachOutput, DashboardInstanceFirewallsNetworkPoliciesDetachOutput

class MetorialFirewallsNetworkPoliciesEndpoint(BaseMetorialEndpoint):
    """Manage firewalls and their attached network policies."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def attach(self, firewall_id: str, *, network_policy_id: str, position: Optional[float] = None) -> DashboardInstanceFirewallsNetworkPoliciesAttachOutput:
        """
    Attach network policy
    Attaches a network policy to a firewall.

    :param firewall_id: str
    :param network_policy_id: str
    :param position: Optional[float] (optional)
    :return: DashboardInstanceFirewallsNetworkPoliciesAttachOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["network_policy_id"] = network_policy_id
        if position is not None:
            body_dict["position"] = position

        request = MetorialRequest(
            path=['firewalls', firewall_id, 'network-policies'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceFirewallsNetworkPoliciesAttachOutput.from_dict)

    def detach(self, firewall_id: str, network_policy_id: str) -> DashboardInstanceFirewallsNetworkPoliciesDetachOutput:
        """
    Detach network policy
    Detaches a network policy from a firewall.

    :param firewall_id: str
    :param network_policy_id: str
    :return: DashboardInstanceFirewallsNetworkPoliciesDetachOutput
    """
        request = MetorialRequest(
            path=['firewalls', firewall_id, 'network-policies', network_policy_id]
        )
        return self._delete(request).transform(mapDashboardInstanceFirewallsNetworkPoliciesDetachOutput.from_dict)