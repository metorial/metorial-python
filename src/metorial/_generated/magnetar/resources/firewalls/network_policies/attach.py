from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class FirewallsNetworkPoliciesAttachOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules]
@dataclass
class FirewallsNetworkPoliciesAttachOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[FirewallsNetworkPoliciesAttachOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts:
        return FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules:
        return FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[FirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsNetworkPoliciesAttachOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsNetworkPoliciesAttachOutputNetworkPolicies:
        return FirewallsNetworkPoliciesAttachOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[FirewallsNetworkPoliciesAttachOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsNetworkPoliciesAttachOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsNetworkPoliciesAttachOutput:
        return FirewallsNetworkPoliciesAttachOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapFirewallsNetworkPoliciesAttachOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallsNetworkPoliciesAttachOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class FirewallsNetworkPoliciesAttachBody:
    network_policy_id: str
    position: Optional[float] = None


class mapFirewallsNetworkPoliciesAttachBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsNetworkPoliciesAttachBody:
        return FirewallsNetworkPoliciesAttachBody(
        network_policy_id=data.get('network_policy_id'),
        position=data.get('position')
        )

    @staticmethod
    def to_dict(value: Union[FirewallsNetworkPoliciesAttachBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

