from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFirewallBindingsDeleteOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsDeleteOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsDeleteOutput:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceFirewallBindingsDeleteOutputFirewall
    created_at: datetime
    target: Optional[DashboardInstanceFirewallBindingsDeleteOutputTarget] = None


class mapDashboardInstanceFirewallBindingsDeleteOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsDeleteOutputFirewall:
        return DashboardInstanceFirewallBindingsDeleteOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsDeleteOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsDeleteOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsDeleteOutputTarget:
        return DashboardInstanceFirewallBindingsDeleteOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsDeleteOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsDeleteOutput:
        return DashboardInstanceFirewallBindingsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceFirewallBindingsDeleteOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceFirewallBindingsDeleteOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

