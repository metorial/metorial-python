from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumersGetMemberConsumerOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    profile: Dict[str, Any]


class mapManagementInstanceConsumersGetMemberConsumerOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersGetMemberConsumerOutput:
        return ManagementInstanceConsumersGetMemberConsumerOutput(
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
    def to_dict(value: Union[ManagementInstanceConsumersGetMemberConsumerOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConsumersGetMemberConsumerBody:
    surface_identifier: Optional[str] = None


class mapManagementInstanceConsumersGetMemberConsumerBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersGetMemberConsumerBody:
        return ManagementInstanceConsumersGetMemberConsumerBody(
        surface_identifier=data.get('surface_identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersGetMemberConsumerBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

