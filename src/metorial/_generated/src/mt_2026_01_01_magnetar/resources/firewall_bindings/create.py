from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallBindingsCreateOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class FirewallBindingsCreateOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class FirewallBindingsCreateOutput:
    object: str
    id: str
    target_type: str
    firewall: FirewallBindingsCreateOutputFirewall
    created_at: datetime
    target: Optional[FirewallBindingsCreateOutputTarget] = None


class mapFirewallBindingsCreateOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsCreateOutputFirewall:
        return FirewallBindingsCreateOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsCreateOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsCreateOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsCreateOutputTarget:
        return FirewallBindingsCreateOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsCreateOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsCreateOutput:
        return FirewallBindingsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapFirewallBindingsCreateOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapFirewallBindingsCreateOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class FirewallBindingsCreateBody:
    firewall_id: str
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None
    network_id: Optional[str] = None


class mapFirewallBindingsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsCreateBody:
        return FirewallBindingsCreateBody(
        firewall_id=data.get('firewall_id'),
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_id=data.get('network_id')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

