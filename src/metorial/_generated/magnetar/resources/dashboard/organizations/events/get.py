from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventsGetOutput:
    object: str
    id: str
    organization_id: str
    source: str
    event_type: str
    created_at: datetime
    instance_id: Optional[str] = None
    callback_id: Optional[str] = None
    callback_event_id: Optional[str] = None
    callback_trigger_key: Optional[str] = None
    chat_event_id: Optional[str] = None
    chat_connection_id: Optional[str] = None
    provider_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None


class mapDashboardOrganizationsEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventsGetOutput:
        return DashboardOrganizationsEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        source=data.get('source'),
        event_type=data.get('event_type'),
        callback_id=data.get('callback_id'),
        callback_event_id=data.get('callback_event_id'),
        callback_trigger_key=data.get('callback_trigger_key'),
        chat_event_id=data.get('chat_event_id'),
        chat_connection_id=data.get('chat_connection_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        payload=data.get('payload')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

