from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class NetworkPoliciesDeleteOutputRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class NetworkPoliciesDeleteOutputRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesDeleteOutputRulesPorts]] = None
@dataclass
class NetworkPoliciesDeleteOutput:
    object: str
    id: str
    name: str
    status: str
    version: float
    rules: List[NetworkPoliciesDeleteOutputRules]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    firewall_ids: Optional[List[str]] = None
    archived_at: Optional[datetime] = None


class mapNetworkPoliciesDeleteOutputRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesDeleteOutputRulesPorts:
        return NetworkPoliciesDeleteOutputRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesDeleteOutputRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesDeleteOutputRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesDeleteOutputRules:
        return NetworkPoliciesDeleteOutputRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesDeleteOutputRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesDeleteOutputRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesDeleteOutput:
        return NetworkPoliciesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        version=data.get('version'),
        rules=[mapNetworkPoliciesDeleteOutputRules.from_dict(item) for item in data.get('rules', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

