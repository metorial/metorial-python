from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersGetOutput:
    object: str
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
    is_portal_consumer: bool
    is_organization_member: bool


class mapConsumersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersGetOutput:
        return ConsumersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        is_portal_consumer=data.get('is_portal_consumer'),
        is_organization_member=data.get('is_organization_member')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

