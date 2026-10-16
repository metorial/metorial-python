from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsCreateOutput:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall
    created_at: datetime
    target: Optional[DashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget] = None


class mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall:
        return DashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget:
        return DashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsCreateOutput:
        return DashboardInstanceIntegrationFirewallAssignmentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceIntegrationFirewallAssignmentsCreateOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsCreateBody:
    firewall_id: str
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None


class mapDashboardInstanceIntegrationFirewallAssignmentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsCreateBody:
        return DashboardInstanceIntegrationFirewallAssignmentsCreateBody(
        firewall_id=data.get('firewall_id'),
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

