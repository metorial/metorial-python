from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallBindingsCreateOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsCreateOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsCreateOutput:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceFirewallBindingsCreateOutputFirewall
    created_at: datetime
    target: Optional[ManagementInstanceFirewallBindingsCreateOutputTarget] = None


class mapManagementInstanceFirewallBindingsCreateOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsCreateOutputFirewall:
        return ManagementInstanceFirewallBindingsCreateOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsCreateOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsCreateOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsCreateOutputTarget:
        return ManagementInstanceFirewallBindingsCreateOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsCreateOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsCreateOutput:
        return ManagementInstanceFirewallBindingsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceFirewallBindingsCreateOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceFirewallBindingsCreateOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFirewallBindingsCreateBody:
    firewall_id: str
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None
    network_id: Optional[str] = None


class mapManagementInstanceFirewallBindingsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsCreateBody:
        return ManagementInstanceFirewallBindingsCreateBody(
        firewall_id=data.get('firewall_id'),
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_id=data.get('network_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

