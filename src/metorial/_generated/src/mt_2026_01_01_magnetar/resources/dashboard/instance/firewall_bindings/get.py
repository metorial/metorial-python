from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFirewallBindingsGetOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsGetOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsGetOutput:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceFirewallBindingsGetOutputFirewall
    created_at: datetime
    target: Optional[DashboardInstanceFirewallBindingsGetOutputTarget] = None


class mapDashboardInstanceFirewallBindingsGetOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsGetOutputFirewall:
        return DashboardInstanceFirewallBindingsGetOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsGetOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsGetOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsGetOutputTarget:
        return DashboardInstanceFirewallBindingsGetOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsGetOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsGetOutput:
        return DashboardInstanceFirewallBindingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceFirewallBindingsGetOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceFirewallBindingsGetOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

