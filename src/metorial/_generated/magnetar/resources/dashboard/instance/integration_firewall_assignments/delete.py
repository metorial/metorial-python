from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall
    created_at: datetime
    target: Optional[DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget] = None


class mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall:
        return DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget:
        return DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput:
        return DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceIntegrationFirewallAssignmentsDeleteOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

