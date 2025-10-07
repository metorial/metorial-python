from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomServersEventsGetOutput:
    object: str
    id: str
    type: str
    message: str
    payload: Dict[str, Any]
    custom_server_id: str
    created_at: datetime
    custom_server_version_id: Optional[str] = None


class mapManagementInstanceCustomServersEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersEventsGetOutput:
        return ManagementInstanceCustomServersEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        payload=data.get('payload'),
        custom_server_id=data.get('custom_server_id'),
        custom_server_version_id=data.get('custom_server_version_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

