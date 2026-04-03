from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersGetMemberConsumerOutputProfileGroupsGroup:
    object: str
    id: str
    status: str
    name: str
    is_default: bool
    sso_group_ids: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ConsumersGetMemberConsumerOutputProfileGroups:
    object: str
    group: ConsumersGetMemberConsumerOutputProfileGroupsGroup
    assigned_via: str
@dataclass
class ConsumersGetMemberConsumerOutputProfile:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[ConsumersGetMemberConsumerOutputProfileGroups]] = None
@dataclass
class ConsumersGetMemberConsumerOutput:
    object: str
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
    profile: ConsumersGetMemberConsumerOutputProfile


class mapConsumersGetMemberConsumerOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersGetMemberConsumerOutput:
        return ConsumersGetMemberConsumerOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        profile=mapConsumersGetMemberConsumerOutputProfile.from_dict(data.get('profile')) if data.get('profile') else None
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

