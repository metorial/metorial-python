from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksEventsGetOutput:
    object: str
    id: str
    type: str
    source_id: str
    trigger_key: str
    input: Dict[str, Any]
    output: Dict[str, Any]
    delivery_status: str
    callback_id: str
    created_at: datetime
    callback_instance_id: Optional[str] = None


class mapManagementInstanceCallbacksEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksEventsGetOutput:
        return ManagementInstanceCallbacksEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source_id=data.get('source_id'),
        trigger_key=data.get('trigger_key'),
        input=data.get('input'),
        output=data.get('output'),
        delivery_status=data.get('delivery_status'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

