from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class DashboardInstanceNetworkPoliciesRulesDeleteOutputRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts]] = None
@dataclass
class DashboardInstanceNetworkPoliciesRulesDeleteOutput:
    object: str
    id: str
    name: str
    status: str
    version: float
    rules: List[DashboardInstanceNetworkPoliciesRulesDeleteOutputRules]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    firewall_ids: Optional[List[str]] = None
    archived_at: Optional[datetime] = None


class mapDashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts:
        return DashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesRulesDeleteOutputRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesDeleteOutputRules:
        return DashboardInstanceNetworkPoliciesRulesDeleteOutputRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceNetworkPoliciesRulesDeleteOutputRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesDeleteOutputRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesRulesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesDeleteOutput:
        return DashboardInstanceNetworkPoliciesRulesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        version=data.get('version'),
        rules=[mapDashboardInstanceNetworkPoliciesRulesDeleteOutputRules.from_dict(item) for item in data.get('rules', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

