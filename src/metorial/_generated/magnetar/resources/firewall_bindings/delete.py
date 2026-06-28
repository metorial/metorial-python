from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallBindingsDeleteOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class FirewallBindingsDeleteOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class FirewallBindingsDeleteOutput:
    object: str
    id: str
    target_type: str
    firewall: FirewallBindingsDeleteOutputFirewall
    created_at: datetime
    target: Optional[FirewallBindingsDeleteOutputTarget] = None


class mapFirewallBindingsDeleteOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsDeleteOutputFirewall:
        return FirewallBindingsDeleteOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsDeleteOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsDeleteOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsDeleteOutputTarget:
        return FirewallBindingsDeleteOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsDeleteOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsDeleteOutput:
        return FirewallBindingsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapFirewallBindingsDeleteOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapFirewallBindingsDeleteOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

