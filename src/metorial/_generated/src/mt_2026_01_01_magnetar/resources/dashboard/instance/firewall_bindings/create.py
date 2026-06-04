from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFirewallBindingsCreateOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsCreateOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsCreateOutput:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceFirewallBindingsCreateOutputFirewall
    created_at: datetime
    target: Optional[DashboardInstanceFirewallBindingsCreateOutputTarget] = None


class mapDashboardInstanceFirewallBindingsCreateOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsCreateOutputFirewall:
        return DashboardInstanceFirewallBindingsCreateOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsCreateOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsCreateOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsCreateOutputTarget:
        return DashboardInstanceFirewallBindingsCreateOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsCreateOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsCreateOutput:
        return DashboardInstanceFirewallBindingsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceFirewallBindingsCreateOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceFirewallBindingsCreateOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceFirewallBindingsCreateBody:
    firewall_id: str
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None
    network_id: Optional[str] = None


class mapDashboardInstanceFirewallBindingsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsCreateBody:
        return DashboardInstanceFirewallBindingsCreateBody(
        firewall_id=data.get('firewall_id'),
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_id=data.get('network_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

