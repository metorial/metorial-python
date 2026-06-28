from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class NetworkPoliciesRulesCreateOutputPorts:
    object: str
    from_: float
    to: float
@dataclass
class NetworkPoliciesRulesCreateOutput:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesRulesCreateOutputPorts]] = None


class mapNetworkPoliciesRulesCreateOutputPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesCreateOutputPorts:
        return NetworkPoliciesRulesCreateOutputPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesCreateOutputPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesRulesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesCreateOutput:
        return NetworkPoliciesRulesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesRulesCreateOutputPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class NetworkPoliciesRulesCreateBodyPorts:
    from_: float
    to: float
@dataclass
class NetworkPoliciesRulesCreateBody:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesRulesCreateBodyPorts]] = None


class mapNetworkPoliciesRulesCreateBodyPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesCreateBodyPorts:
        return NetworkPoliciesRulesCreateBodyPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesCreateBodyPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesRulesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesCreateBody:
        return NetworkPoliciesRulesCreateBody(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesRulesCreateBodyPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

