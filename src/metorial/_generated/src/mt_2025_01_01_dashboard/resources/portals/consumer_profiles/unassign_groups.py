from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerProfilesUnassignGroupsOutputGroupsGroup:
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
class PortalsConsumerProfilesUnassignGroupsOutputGroups:
    object: str
    group: PortalsConsumerProfilesUnassignGroupsOutputGroupsGroup
    assigned_via: str
@dataclass
class PortalsConsumerProfilesUnassignGroupsOutputSurfaceAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class PortalsConsumerProfilesUnassignGroupsOutputSurface:
    object: str
    id: str
    status: str
    name: str
    auth: PortalsConsumerProfilesUnassignGroupsOutputSurfaceAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsConsumerProfilesUnassignGroupsOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    surface: PortalsConsumerProfilesUnassignGroupsOutputSurface
    groups: Optional[List[PortalsConsumerProfilesUnassignGroupsOutputGroups]] = None


class mapPortalsConsumerProfilesUnassignGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesUnassignGroupsOutput:
        return PortalsConsumerProfilesUnassignGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapPortalsConsumerProfilesUnassignGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        surface=mapPortalsConsumerProfilesUnassignGroupsOutputSurface.from_dict(data.get('surface')) if data.get('surface') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesUnassignGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsConsumerProfilesUnassignGroupsBody:
    group_ids: List[str]


class mapPortalsConsumerProfilesUnassignGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerProfilesUnassignGroupsBody:
        return PortalsConsumerProfilesUnassignGroupsBody(
        group_ids=data.get('group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerProfilesUnassignGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

