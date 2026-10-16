from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsCreateOutput:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall
    created_at: datetime
    target: Optional[ManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget] = None


class mapManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall:
        return ManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget:
        return ManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsCreateOutput:
        return ManagementInstanceIntegrationFirewallAssignmentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceIntegrationFirewallAssignmentsCreateOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceIntegrationFirewallAssignmentsCreateOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsCreateBody:
    firewall_id: str
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None


class mapManagementInstanceIntegrationFirewallAssignmentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsCreateBody:
        return ManagementInstanceIntegrationFirewallAssignmentsCreateBody(
        firewall_id=data.get('firewall_id'),
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

