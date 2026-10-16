from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationFirewallAssignmentsCreateOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsCreateOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsCreateOutput:
    object: str
    id: str
    target_type: str
    firewall: IntegrationFirewallAssignmentsCreateOutputFirewall
    created_at: datetime
    target: Optional[IntegrationFirewallAssignmentsCreateOutputTarget] = None


class mapIntegrationFirewallAssignmentsCreateOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsCreateOutputFirewall:
        return IntegrationFirewallAssignmentsCreateOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsCreateOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsCreateOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsCreateOutputTarget:
        return IntegrationFirewallAssignmentsCreateOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsCreateOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsCreateOutput:
        return IntegrationFirewallAssignmentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapIntegrationFirewallAssignmentsCreateOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapIntegrationFirewallAssignmentsCreateOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationFirewallAssignmentsCreateBody:
    firewall_id: str
    target_type: str
    enclave_id: Optional[str] = None
    provider_id: Optional[str] = None


class mapIntegrationFirewallAssignmentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsCreateBody:
        return IntegrationFirewallAssignmentsCreateBody(
        firewall_id=data.get('firewall_id'),
        target_type=data.get('target_type'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

