from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class DashboardInstanceFirewallsUpdateOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules]
@dataclass
class DashboardInstanceFirewallsUpdateOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[DashboardInstanceFirewallsUpdateOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapDashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts:
        return DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules:
        return DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsUpdateOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsUpdateOutputNetworkPolicies:
        return DashboardInstanceFirewallsUpdateOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapDashboardInstanceFirewallsUpdateOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsUpdateOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsUpdateOutput:
        return DashboardInstanceFirewallsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapDashboardInstanceFirewallsUpdateOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceFirewallsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    network_policy_ids: Optional[List[str]] = None


class mapDashboardInstanceFirewallsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallsUpdateBody:
        return DashboardInstanceFirewallsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        network_policy_ids=data.get('network_policy_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

