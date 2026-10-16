from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallsCreateOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class FirewallsCreateOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[FirewallsCreateOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class FirewallsCreateOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[FirewallsCreateOutputNetworkPoliciesRules]
@dataclass
class FirewallsCreateOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_policies: List[FirewallsCreateOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapFirewallsCreateOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsCreateOutputNetworkPoliciesRulesPorts:
        return FirewallsCreateOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[FirewallsCreateOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsCreateOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsCreateOutputNetworkPoliciesRules:
        return FirewallsCreateOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapFirewallsCreateOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[FirewallsCreateOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsCreateOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsCreateOutputNetworkPolicies:
        return FirewallsCreateOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapFirewallsCreateOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[FirewallsCreateOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsCreateOutput:
        return FirewallsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_policies=[mapFirewallsCreateOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class FirewallsCreateBody:
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None
    network_policy_ids: Optional[List[str]] = None


class mapFirewallsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsCreateBody:
        return FirewallsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        network_policy_ids=data.get('network_policy_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[FirewallsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

