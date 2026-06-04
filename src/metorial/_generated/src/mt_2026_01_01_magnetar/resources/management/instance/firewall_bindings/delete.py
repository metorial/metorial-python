from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallBindingsDeleteOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsDeleteOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsDeleteOutput:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceFirewallBindingsDeleteOutputFirewall
    created_at: datetime
    target: Optional[ManagementInstanceFirewallBindingsDeleteOutputTarget] = None


class mapManagementInstanceFirewallBindingsDeleteOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsDeleteOutputFirewall:
        return ManagementInstanceFirewallBindingsDeleteOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsDeleteOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsDeleteOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsDeleteOutputTarget:
        return ManagementInstanceFirewallBindingsDeleteOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsDeleteOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsDeleteOutput:
        return ManagementInstanceFirewallBindingsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceFirewallBindingsDeleteOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceFirewallBindingsDeleteOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

