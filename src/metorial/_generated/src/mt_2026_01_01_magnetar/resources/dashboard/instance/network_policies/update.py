from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceNetworkPoliciesUpdateOutputRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class DashboardInstanceNetworkPoliciesUpdateOutputRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceNetworkPoliciesUpdateOutputRulesPorts]] = None
@dataclass
class DashboardInstanceNetworkPoliciesUpdateOutput:
    object: str
    id: str
    name: str
    status: str
    version: float
    rules: List[DashboardInstanceNetworkPoliciesUpdateOutputRules]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    firewall_ids: Optional[List[str]] = None
    archived_at: Optional[datetime] = None


class mapDashboardInstanceNetworkPoliciesUpdateOutputRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesUpdateOutputRulesPorts:
        return DashboardInstanceNetworkPoliciesUpdateOutputRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesUpdateOutputRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesUpdateOutputRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesUpdateOutputRules:
        return DashboardInstanceNetworkPoliciesUpdateOutputRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceNetworkPoliciesUpdateOutputRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesUpdateOutputRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesUpdateOutput:
        return DashboardInstanceNetworkPoliciesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        version=data.get('version'),
        rules=[mapDashboardInstanceNetworkPoliciesUpdateOutputRules.from_dict(item) for item in data.get('rules', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceNetworkPoliciesUpdateBodyRulesPorts:
    from_: float
    to: float
@dataclass
class DashboardInstanceNetworkPoliciesUpdateBodyRules:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceNetworkPoliciesUpdateBodyRulesPorts]] = None
@dataclass
class DashboardInstanceNetworkPoliciesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    rules: Optional[List[DashboardInstanceNetworkPoliciesUpdateBodyRules]] = None


class mapDashboardInstanceNetworkPoliciesUpdateBodyRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesUpdateBodyRulesPorts:
        return DashboardInstanceNetworkPoliciesUpdateBodyRulesPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesUpdateBodyRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesUpdateBodyRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesUpdateBodyRules:
        return DashboardInstanceNetworkPoliciesUpdateBodyRules(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceNetworkPoliciesUpdateBodyRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesUpdateBodyRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesUpdateBody:
        return DashboardInstanceNetworkPoliciesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        rules=[mapDashboardInstanceNetworkPoliciesUpdateBodyRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

