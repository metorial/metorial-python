from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallBindingsGetOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class FirewallBindingsGetOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class FirewallBindingsGetOutput:
    object: str
    id: str
    target_type: str
    firewall: FirewallBindingsGetOutputFirewall
    created_at: datetime
    target: Optional[FirewallBindingsGetOutputTarget] = None


class mapFirewallBindingsGetOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsGetOutputFirewall:
        return FirewallBindingsGetOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsGetOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsGetOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsGetOutputTarget:
        return FirewallBindingsGetOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsGetOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsGetOutput:
        return FirewallBindingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapFirewallBindingsGetOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapFirewallBindingsGetOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

