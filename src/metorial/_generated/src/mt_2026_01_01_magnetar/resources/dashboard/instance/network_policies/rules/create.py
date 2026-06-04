from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceNetworkPoliciesRulesCreateOutputPorts:
    object: str
    from_: float
    to: float
@dataclass
class DashboardInstanceNetworkPoliciesRulesCreateOutput:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceNetworkPoliciesRulesCreateOutputPorts]] = None


class mapDashboardInstanceNetworkPoliciesRulesCreateOutputPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesCreateOutputPorts:
        return DashboardInstanceNetworkPoliciesRulesCreateOutputPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesCreateOutputPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesRulesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesCreateOutput:
        return DashboardInstanceNetworkPoliciesRulesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceNetworkPoliciesRulesCreateOutputPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceNetworkPoliciesRulesCreateBodyPorts:
    from_: float
    to: float
@dataclass
class DashboardInstanceNetworkPoliciesRulesCreateBody:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceNetworkPoliciesRulesCreateBodyPorts]] = None


class mapDashboardInstanceNetworkPoliciesRulesCreateBodyPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesCreateBodyPorts:
        return DashboardInstanceNetworkPoliciesRulesCreateBodyPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesCreateBodyPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesRulesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesRulesCreateBody:
        return DashboardInstanceNetworkPoliciesRulesCreateBody(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceNetworkPoliciesRulesCreateBodyPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesRulesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

