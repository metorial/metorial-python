from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventsGetOutput:
    object: str
    id: str
    organization_id: str
    source: str
    event_type: str
    created_at: datetime
    instance_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
    callback_id: Optional[str] = None
    callback_trigger_key: Optional[str] = None
    chat_event_id: Optional[str] = None
    chat_integration_id: Optional[str] = None


class mapManagementOrganizationEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventsGetOutput:
        return ManagementOrganizationEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        source=data.get('source'),
        event_type=data.get('event_type'),
        payload=data.get('payload'),
        callback_id=data.get('callback_id'),
        callback_trigger_key=data.get('callback_trigger_key'),
        chat_event_id=data.get('chat_event_id'),
        chat_integration_id=data.get('chat_integration_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

