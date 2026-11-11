from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAuditLogsGetOutputActor:
    type: str
    id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    record: Optional[Any] = None
@dataclass
class DashboardOrganizationsAuditLogsGetOutputContext:
    ip: Optional[str] = None
    ua: Optional[str] = None
@dataclass
class DashboardOrganizationsAuditLogsGetOutput:
    object: str
    id: str
    event_id: str
    resource: str
    action: str
    organization_id: str
    context: DashboardOrganizationsAuditLogsGetOutputContext
    recorded_at: datetime
    instance_id: Optional[str] = None
    organization_actor_id: Optional[str] = None
    actor: Optional[DashboardOrganizationsAuditLogsGetOutputActor] = None
    payload: Optional[Dict[str, Any]] = None
    previous_attributes: Optional[Dict[str, Any]] = None


class mapDashboardOrganizationsAuditLogsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAuditLogsGetOutputActor:
        return DashboardOrganizationsAuditLogsGetOutputActor(
        type=data.get('type'),
        id=data.get('id'),
        metadata=data.get('metadata'),
        record=data.get('record')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAuditLogsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAuditLogsGetOutputContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAuditLogsGetOutputContext:
        return DashboardOrganizationsAuditLogsGetOutputContext(
        ip=data.get('ip'),
        ua=data.get('ua')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAuditLogsGetOutputContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAuditLogsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAuditLogsGetOutput:
        return DashboardOrganizationsAuditLogsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        event_id=data.get('event_id'),
        resource=data.get('resource'),
        action=data.get('action'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        organization_actor_id=data.get('organization_actor_id'),
        actor=mapDashboardOrganizationsAuditLogsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        context=mapDashboardOrganizationsAuditLogsGetOutputContext.from_dict(data.get('context')) if data.get('context') else None,
        payload=data.get('payload'),
        previous_attributes=data.get('previous_attributes'),
        recorded_at=datetime.fromisoformat(data.get('recorded_at').replace('Z', '+00:00')) if data.get('recorded_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAuditLogsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

