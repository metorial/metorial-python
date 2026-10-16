from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsGetOutput:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall
    created_at: datetime
    target: Optional[ManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget] = None


class mapManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall:
        return ManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget:
        return ManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsGetOutput:
        return ManagementInstanceIntegrationFirewallAssignmentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceIntegrationFirewallAssignmentsGetOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceIntegrationFirewallAssignmentsGetOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

