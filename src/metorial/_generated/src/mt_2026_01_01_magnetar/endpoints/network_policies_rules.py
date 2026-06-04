from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceNetworkPoliciesRulesCreateOutput, DashboardInstanceNetworkPoliciesRulesCreateOutput, mapDashboardInstanceNetworkPoliciesRulesCreateBody, DashboardInstanceNetworkPoliciesRulesCreateBody, mapDashboardInstanceNetworkPoliciesRulesUpdateOutput, DashboardInstanceNetworkPoliciesRulesUpdateOutput, mapDashboardInstanceNetworkPoliciesRulesUpdateBody, DashboardInstanceNetworkPoliciesRulesUpdateBody, mapDashboardInstanceNetworkPoliciesRulesDeleteOutput, DashboardInstanceNetworkPoliciesRulesDeleteOutput

class MetorialNetworkPoliciesRulesEndpoint(BaseMetorialEndpoint):
    """Manage reusable network policy definitions and their rules."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def create(self, network_policy_id: str, *, effect: str, direction: str, cidrs: List[str], enabled: bool, priority: float, description: Optional[str] = None, ports: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceNetworkPoliciesRulesCreateOutput:
        """
    Create network policy rule
    Adds a rule to a network policy.

    :param network_policy_id: str
    :param effect: str
    :param direction: str
    :param cidrs: List[str]
    :param description: Optional[str] (optional)
    :param enabled: bool
    :param priority: float
    :param ports: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceNetworkPoliciesRulesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["effect"] = effect
        body_dict["direction"] = direction
        body_dict["cidrs"] = cidrs
        if description is not None:
            body_dict["description"] = description
        body_dict["enabled"] = enabled
        body_dict["priority"] = priority
        if ports is not None:
            body_dict["ports"] = ports

        request = MetorialRequest(
            path=['network-policies', network_policy_id, 'rules'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceNetworkPoliciesRulesCreateOutput.from_dict)

    def update(self, network_policy_id: str, rule_id: str, *, effect: str, direction: str, cidrs: List[str], enabled: bool, priority: float, description: Optional[str] = None, ports: Optional[List[Dict[str, Any]]] = None) -> DashboardInstanceNetworkPoliciesRulesUpdateOutput:
        """
    Update network policy rule
    Updates a rule on a network policy.

    :param network_policy_id: str
    :param rule_id: str
    :param effect: str
    :param direction: str
    :param cidrs: List[str]
    :param description: Optional[str] (optional)
    :param enabled: bool
    :param priority: float
    :param ports: Optional[List[Dict[str, Any]]] (optional)
    :return: DashboardInstanceNetworkPoliciesRulesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["effect"] = effect
        body_dict["direction"] = direction
        body_dict["cidrs"] = cidrs
        if description is not None:
            body_dict["description"] = description
        body_dict["enabled"] = enabled
        body_dict["priority"] = priority
        if ports is not None:
            body_dict["ports"] = ports

        request = MetorialRequest(
            path=['network-policies', network_policy_id, 'rules', rule_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceNetworkPoliciesRulesUpdateOutput.from_dict)

    def delete(self, network_policy_id: str, rule_id: str) -> DashboardInstanceNetworkPoliciesRulesDeleteOutput:
        """
    Delete network policy rule
    Removes a rule from a network policy.

    :param network_policy_id: str
    :param rule_id: str
    :return: DashboardInstanceNetworkPoliciesRulesDeleteOutput
    """
        request = MetorialRequest(
            path=['network-policies', network_policy_id, 'rules', rule_id]
        )
        return self._delete(request).transform(mapDashboardInstanceNetworkPoliciesRulesDeleteOutput.from_dict)