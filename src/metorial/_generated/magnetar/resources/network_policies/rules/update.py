from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class NetworkPoliciesRulesUpdateOutputPorts:
    object: str
    from_: float
    to: float
@dataclass
class NetworkPoliciesRulesUpdateOutput:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesRulesUpdateOutputPorts]] = None


class mapNetworkPoliciesRulesUpdateOutputPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesUpdateOutputPorts:
        return NetworkPoliciesRulesUpdateOutputPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesUpdateOutputPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesRulesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesUpdateOutput:
        return NetworkPoliciesRulesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesRulesUpdateOutputPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class NetworkPoliciesRulesUpdateBodyPorts:
    from_: float
    to: float
@dataclass
class NetworkPoliciesRulesUpdateBody:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesRulesUpdateBodyPorts]] = None


class mapNetworkPoliciesRulesUpdateBodyPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesUpdateBodyPorts:
        return NetworkPoliciesRulesUpdateBodyPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesUpdateBodyPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesRulesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesRulesUpdateBody:
        return NetworkPoliciesRulesUpdateBody(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesRulesUpdateBodyPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesRulesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

