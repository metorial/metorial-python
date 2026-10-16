from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationFirewallAssignmentsDeleteOutputFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsDeleteOutputTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsDeleteOutput:
    object: str
    id: str
    target_type: str
    firewall: IntegrationFirewallAssignmentsDeleteOutputFirewall
    created_at: datetime
    target: Optional[IntegrationFirewallAssignmentsDeleteOutputTarget] = None


class mapIntegrationFirewallAssignmentsDeleteOutputFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsDeleteOutputFirewall:
        return IntegrationFirewallAssignmentsDeleteOutputFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsDeleteOutputFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsDeleteOutputTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsDeleteOutputTarget:
        return IntegrationFirewallAssignmentsDeleteOutputTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsDeleteOutputTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsDeleteOutput:
        return IntegrationFirewallAssignmentsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapIntegrationFirewallAssignmentsDeleteOutputFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapIntegrationFirewallAssignmentsDeleteOutputTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

