from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProtoGuardAlertsGetOutputFilters:
    object: str
    id: str
    filter_id: str
    key: str
    name: str
    issue_type: str
    severity: str
    created_at: datetime
    description: Optional[str] = None
    confidence: Optional[float] = None
@dataclass
class ManagementInstanceProtoGuardAlertsGetOutput:
    object: str
    id: str
    run_id: str
    filters: List[ManagementInstanceProtoGuardAlertsGetOutputFilters]
    created_at: datetime
    session_id: Optional[str] = None
    session_message_id: Optional[str] = None
    session_connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None


class mapManagementInstanceProtoGuardAlertsGetOutputFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsGetOutputFilters:
        return ManagementInstanceProtoGuardAlertsGetOutputFilters(
        object=data.get('object'),
        id=data.get('id'),
        filter_id=data.get('filter_id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        issue_type=data.get('issue_type'),
        severity=data.get('severity'),
        confidence=data.get('confidence'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsGetOutputFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardAlertsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsGetOutput:
        return ManagementInstanceProtoGuardAlertsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        run_id=data.get('run_id'),
        session_id=data.get('session_id'),
        session_message_id=data.get('session_message_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        filters=[mapManagementInstanceProtoGuardAlertsGetOutputFilters.from_dict(item) for item in data.get('filters', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

