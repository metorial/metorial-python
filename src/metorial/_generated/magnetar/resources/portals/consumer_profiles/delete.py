from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerProfilesDeleteOutputGroupsGroup:
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
class PortalsConsumerProfilesDeleteOutputGroups:
    object: str
    group: PortalsConsumerProfilesDeleteOutputGroupsGroup
    assigned_via: str
@dataclass
class PortalsConsumerProfilesDeleteOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[PortalsConsumerProfilesDeleteOutputGroups]] = None


class mapPortalsConsumerProfilesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesDeleteOutput:
        return PortalsConsumerProfilesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        consumer_id=data.get('consumer_id'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        groups=[mapPortalsConsumerProfilesDeleteOutputGroups.from_dict(item) for item in data.get('groups', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

