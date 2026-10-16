from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsGetOutput:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall
    created_at: datetime
    target: Optional[DashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget] = None


class mapDashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall:
        return DashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget:
        return DashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsGetOutput:
        return DashboardInstanceIntegrationFirewallAssignmentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceIntegrationFirewallAssignmentsGetOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceIntegrationFirewallAssignmentsGetOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

