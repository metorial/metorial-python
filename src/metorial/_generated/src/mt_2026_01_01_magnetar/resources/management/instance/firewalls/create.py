from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class ManagementInstanceFirewallsCreateOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class ManagementInstanceFirewallsCreateOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[ManagementInstanceFirewallsCreateOutputNetworkPoliciesRules]
@dataclass
class ManagementInstanceFirewallsCreateOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[ManagementInstanceFirewallsCreateOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts:
        return ManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsCreateOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsCreateOutputNetworkPoliciesRules:
        return ManagementInstanceFirewallsCreateOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceFirewallsCreateOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsCreateOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsCreateOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsCreateOutputNetworkPolicies:
        return ManagementInstanceFirewallsCreateOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapManagementInstanceFirewallsCreateOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsCreateOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsCreateOutput:
        return ManagementInstanceFirewallsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapManagementInstanceFirewallsCreateOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFirewallsCreateBodyBindings:
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None
    network_id: Optional[str] = None
@dataclass
class ManagementInstanceFirewallsCreateBody:
    name: str
    network_id: str
    description: Optional[str] = None
    slug: Optional[str] = None
    bindings: Optional[List[ManagementInstanceFirewallsCreateBodyBindings]] = None
    network_policy_ids: Optional[List[str]] = None


class mapManagementInstanceFirewallsCreateBodyBindings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsCreateBodyBindings:
        return ManagementInstanceFirewallsCreateBodyBindings(
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_id=data.get('network_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsCreateBodyBindings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsCreateBody:
        return ManagementInstanceFirewallsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        network_id=data.get('network_id'),
        bindings=[mapManagementInstanceFirewallsCreateBodyBindings.from_dict(item) for item in data.get('bindings', []) if item],
        network_policy_ids=data.get('network_policy_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

