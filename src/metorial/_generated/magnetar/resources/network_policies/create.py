from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class NetworkPoliciesCreateOutputRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class NetworkPoliciesCreateOutputRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesCreateOutputRulesPorts]] = None
@dataclass
class NetworkPoliciesCreateOutput:
    object: str
    id: str
    name: str
    status: str
    version: float
    rules: List[NetworkPoliciesCreateOutputRules]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    firewall_ids: Optional[List[str]] = None
    archived_at: Optional[datetime] = None


class mapNetworkPoliciesCreateOutputRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesCreateOutputRulesPorts:
        return NetworkPoliciesCreateOutputRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesCreateOutputRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesCreateOutputRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesCreateOutputRules:
        return NetworkPoliciesCreateOutputRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesCreateOutputRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesCreateOutputRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesCreateOutput:
        return NetworkPoliciesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        version=data.get('version'),
        rules=[mapNetworkPoliciesCreateOutputRules.from_dict(item) for item in data.get('rules', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class NetworkPoliciesCreateBodyRulesPorts:
    from_: float
    to: float
@dataclass
class NetworkPoliciesCreateBodyRules:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesCreateBodyRulesPorts]] = None
@dataclass
class NetworkPoliciesCreateBody:
    name: str
    description: Optional[str] = None
    rules: Optional[List[NetworkPoliciesCreateBodyRules]] = None


class mapNetworkPoliciesCreateBodyRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesCreateBodyRulesPorts:
        return NetworkPoliciesCreateBodyRulesPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesCreateBodyRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesCreateBodyRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesCreateBodyRules:
        return NetworkPoliciesCreateBodyRules(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesCreateBodyRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesCreateBodyRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesCreateBody:
        return NetworkPoliciesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        rules=[mapNetworkPoliciesCreateBodyRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

