from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsDeleteOutput:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall
    created_at: datetime
    target: Optional[ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget] = None


class mapManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall:
        return ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget:
        return ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsDeleteOutput:
        return ManagementInstanceIntegrationFirewallAssignmentsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceIntegrationFirewallAssignmentsDeleteOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceIntegrationFirewallAssignmentsDeleteOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

