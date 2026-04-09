from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerProfilesGetOutputGroupsGroup:
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
class PortalsConsumerProfilesGetOutputGroups:
    object: str
    group: PortalsConsumerProfilesGetOutputGroupsGroup
    assigned_via: str
@dataclass
class PortalsConsumerProfilesGetOutputSurfaceAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class PortalsConsumerProfilesGetOutputSurface:
    object: str
    id: str
    status: str
    name: str
    auth: PortalsConsumerProfilesGetOutputSurfaceAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsConsumerProfilesGetOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    surface: PortalsConsumerProfilesGetOutputSurface
    groups: Optional[List[PortalsConsumerProfilesGetOutputGroups]] = None


class mapPortalsConsumerProfilesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesGetOutput:
        return PortalsConsumerProfilesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapPortalsConsumerProfilesGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        surface=mapPortalsConsumerProfilesGetOutputSurface.from_dict(data.get('surface')) if data.get('surface') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

