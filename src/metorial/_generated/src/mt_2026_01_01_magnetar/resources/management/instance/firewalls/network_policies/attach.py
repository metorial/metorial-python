from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules]
@dataclass
class ManagementInstanceFirewallsNetworkPoliciesAttachOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts:
        return ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules:
        return ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies:
        return ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsNetworkPoliciesAttachOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesAttachOutput:
        return ManagementInstanceFirewallsNetworkPoliciesAttachOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapManagementInstanceFirewallsNetworkPoliciesAttachOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesAttachOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFirewallsNetworkPoliciesAttachBody:
    network_policy_id: str
    position: Optional[float] = None


class mapManagementInstanceFirewallsNetworkPoliciesAttachBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesAttachBody:
        return ManagementInstanceFirewallsNetworkPoliciesAttachBody(
        network_policy_id=data.get('network_policy_id'),
        position=data.get('position')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesAttachBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

