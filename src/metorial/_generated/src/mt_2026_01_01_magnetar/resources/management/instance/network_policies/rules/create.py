from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceNetworkPoliciesRulesCreateOutputPorts:
    object: str
    from_: float
    to: float
@dataclass
class ManagementInstanceNetworkPoliciesRulesCreateOutput:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceNetworkPoliciesRulesCreateOutputPorts]] = None


class mapManagementInstanceNetworkPoliciesRulesCreateOutputPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesCreateOutputPorts:
        return ManagementInstanceNetworkPoliciesRulesCreateOutputPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesCreateOutputPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworkPoliciesRulesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesCreateOutput:
        return ManagementInstanceNetworkPoliciesRulesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceNetworkPoliciesRulesCreateOutputPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceNetworkPoliciesRulesCreateBodyPorts:
    from_: float
    to: float
@dataclass
class ManagementInstanceNetworkPoliciesRulesCreateBody:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceNetworkPoliciesRulesCreateBodyPorts]] = None


class mapManagementInstanceNetworkPoliciesRulesCreateBodyPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesCreateBodyPorts:
        return ManagementInstanceNetworkPoliciesRulesCreateBodyPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesCreateBodyPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworkPoliciesRulesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesCreateBody:
        return ManagementInstanceNetworkPoliciesRulesCreateBody(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceNetworkPoliciesRulesCreateBodyPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

