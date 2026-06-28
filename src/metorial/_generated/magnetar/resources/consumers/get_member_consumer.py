from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersGetMemberConsumerOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    profile: Dict[str, Any]


class mapConsumersGetMemberConsumerOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersGetMemberConsumerOutput:
        return ConsumersGetMemberConsumerOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        profile=data.get('profile')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersGetMemberConsumerOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumersGetMemberConsumerBody:
    surface_identifier: Optional[str] = None


class mapConsumersGetMemberConsumerBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersGetMemberConsumerBody:
        return ConsumersGetMemberConsumerBody(
        surface_identifier=data.get('surface_identifier')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersGetMemberConsumerBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

