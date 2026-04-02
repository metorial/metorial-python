from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputGroupsGroup:
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
class ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputGroups:
    object: str
    group: ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputGroupsGroup
    assigned_via: str
@dataclass
class ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputSurfaceAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputSurface:
    object: str
    id: str
    status: str
    name: str
    auth: ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputSurfaceAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstancePortalsConsumerProfilesUnassignGroupsOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    surface: ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputSurface
    groups: Optional[List[ManagementInstancePortalsConsumerProfilesUnassignGroupsOutputGroups]] = None


class mapManagementInstancePortalsConsumerProfilesUnassignGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerProfilesUnassignGroupsOutput:
        return ManagementInstancePortalsConsumerProfilesUnassignGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapManagementInstancePortalsConsumerProfilesUnassignGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        surface=mapManagementInstancePortalsConsumerProfilesUnassignGroupsOutputSurface.from_dict(data.get('surface')) if data.get('surface') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerProfilesUnassignGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsConsumerProfilesUnassignGroupsBody:
    group_ids: List[str]


class mapManagementInstancePortalsConsumerProfilesUnassignGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerProfilesUnassignGroupsBody:
        return ManagementInstancePortalsConsumerProfilesUnassignGroupsBody(
        group_ids=data.get('group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerProfilesUnassignGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

