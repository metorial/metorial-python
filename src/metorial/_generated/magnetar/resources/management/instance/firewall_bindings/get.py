from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallBindingsGetOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsGetOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsGetOutput:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceFirewallBindingsGetOutputFirewall
    created_at: datetime
    target: Optional[ManagementInstanceFirewallBindingsGetOutputTarget] = None


class mapManagementInstanceFirewallBindingsGetOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsGetOutputFirewall:
        return ManagementInstanceFirewallBindingsGetOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsGetOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsGetOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsGetOutputTarget:
        return ManagementInstanceFirewallBindingsGetOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsGetOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsGetOutput:
        return ManagementInstanceFirewallBindingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceFirewallBindingsGetOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceFirewallBindingsGetOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

