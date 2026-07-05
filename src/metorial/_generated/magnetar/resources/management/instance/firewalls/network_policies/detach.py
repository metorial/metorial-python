from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules]
@dataclass
class ManagementInstanceFirewallsNetworkPoliciesDetachOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts:
        return ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules:
        return ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies:
        return ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsNetworkPoliciesDetachOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsNetworkPoliciesDetachOutput:
        return ManagementInstanceFirewallsNetworkPoliciesDetachOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapManagementInstanceFirewallsNetworkPoliciesDetachOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsNetworkPoliciesDetachOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

