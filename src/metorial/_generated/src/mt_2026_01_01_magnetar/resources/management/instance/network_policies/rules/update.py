from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceNetworkPoliciesRulesUpdateOutputPorts:
    object: str
    from_: float
    to: float
@dataclass
class ManagementInstanceNetworkPoliciesRulesUpdateOutput:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceNetworkPoliciesRulesUpdateOutputPorts]] = None


class mapManagementInstanceNetworkPoliciesRulesUpdateOutputPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesUpdateOutputPorts:
        return ManagementInstanceNetworkPoliciesRulesUpdateOutputPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesUpdateOutputPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworkPoliciesRulesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesUpdateOutput:
        return ManagementInstanceNetworkPoliciesRulesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceNetworkPoliciesRulesUpdateOutputPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceNetworkPoliciesRulesUpdateBodyPorts:
    from_: float
    to: float
@dataclass
class ManagementInstanceNetworkPoliciesRulesUpdateBody:
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[ManagementInstanceNetworkPoliciesRulesUpdateBodyPorts]] = None


class mapManagementInstanceNetworkPoliciesRulesUpdateBodyPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesUpdateBodyPorts:
        return ManagementInstanceNetworkPoliciesRulesUpdateBodyPorts(
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesUpdateBodyPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworkPoliciesRulesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworkPoliciesRulesUpdateBody:
        return ManagementInstanceNetworkPoliciesRulesUpdateBody(
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapManagementInstanceNetworkPoliciesRulesUpdateBodyPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworkPoliciesRulesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

