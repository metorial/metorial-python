from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class DashboardInstanceFirewallsCreateOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class DashboardInstanceFirewallsCreateOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[DashboardInstanceFirewallsCreateOutputNetworkPoliciesRules]
@dataclass
class DashboardInstanceFirewallsCreateOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[DashboardInstanceFirewallsCreateOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapDashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts:
        return DashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsCreateOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsCreateOutputNetworkPoliciesRules:
        return DashboardInstanceFirewallsCreateOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsCreateOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsCreateOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsCreateOutputNetworkPolicies:
        return DashboardInstanceFirewallsCreateOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapDashboardInstanceFirewallsCreateOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsCreateOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsCreateOutput:
        return DashboardInstanceFirewallsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapDashboardInstanceFirewallsCreateOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceFirewallsCreateBodyBindings:
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None
    network_id: Optional[str] = None
@dataclass
class DashboardInstanceFirewallsCreateBody:
    name: str
    network_id: str
    description: Optional[str] = None
    slug: Optional[str] = None
    bindings: Optional[List[DashboardInstanceFirewallsCreateBodyBindings]] = None
    network_policy_ids: Optional[List[str]] = None


class mapDashboardInstanceFirewallsCreateBodyBindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsCreateBodyBindings:
        return DashboardInstanceFirewallsCreateBodyBindings(
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_id=data.get('network_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsCreateBodyBindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsCreateBody:
        return DashboardInstanceFirewallsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        network_id=data.get('network_id'),
        bindings=[mapDashboardInstanceFirewallsCreateBodyBindings.from_dict(item) for item in data.get('bindings', []) if item],
        network_policy_ids=data.get('network_policy_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

