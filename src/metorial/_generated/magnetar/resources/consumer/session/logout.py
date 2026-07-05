from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerSessionLogoutOutput:
    object: str
    id: str
    created_at: datetime
    expires_at: datetime
    last_used_at: datetime


class mapConsumerSessionLogoutOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionLogoutOutput:
        return ConsumerSessionLogoutOutput(
        object=data.get('object'),
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionLogoutOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

