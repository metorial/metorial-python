from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts]] = None
@dataclass
class ManagementInstanceFirewallsUpdateOutputNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules]
@dataclass
class ManagementInstanceFirewallsUpdateOutput:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[ManagementInstanceFirewallsUpdateOutputNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts:
        return ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules:
        return ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceFirewallsUpdateOutputNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsUpdateOutputNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsUpdateOutputNetworkPolicies:
        return ManagementInstanceFirewallsUpdateOutputNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapManagementInstanceFirewallsUpdateOutputNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsUpdateOutputNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsUpdateOutput:
        return ManagementInstanceFirewallsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapManagementInstanceFirewallsUpdateOutputNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFirewallsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    network_policy_ids: Optional[List[str]] = None


class mapManagementInstanceFirewallsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallsUpdateBody:
        return ManagementInstanceFirewallsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        network_policy_ids=data.get('network_policy_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

