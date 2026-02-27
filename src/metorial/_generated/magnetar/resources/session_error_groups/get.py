from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionErrorGroupsGetOutput:
    object: str
    id: str
    count: float
    session_id: str
    created_at: datetime
    updated_at: datetime
    type: Optional[str] = None
    name: Optional[str] = None
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSessionErrorGroupsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorGroupsGetOutput:
        return SessionErrorGroupsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        message=data.get('message'),
        count=data.get('count'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorGroupsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
