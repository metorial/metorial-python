from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationFirewallAssignmentsGetOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsGetOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsGetOutput:
    object: str
    id: str
    target_type: str
    firewall: IntegrationFirewallAssignmentsGetOutputFirewall
    created_at: datetime
    target: Optional[IntegrationFirewallAssignmentsGetOutputTarget] = None


class mapIntegrationFirewallAssignmentsGetOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsGetOutputFirewall:
        return IntegrationFirewallAssignmentsGetOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsGetOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsGetOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsGetOutputTarget:
        return IntegrationFirewallAssignmentsGetOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsGetOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsGetOutput:
        return IntegrationFirewallAssignmentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapIntegrationFirewallAssignmentsGetOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapIntegrationFirewallAssignmentsGetOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

