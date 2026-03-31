from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsConsumerProfilesAssignGroupsOutputGroupsGroup:
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
class ManagementInstancePortalsConsumerProfilesAssignGroupsOutputGroups:
    object: str
    group: ManagementInstancePortalsConsumerProfilesAssignGroupsOutputGroupsGroup
    assigned_via: str
@dataclass
class ManagementInstancePortalsConsumerProfilesAssignGroupsOutputSurfaceAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class ManagementInstancePortalsConsumerProfilesAssignGroupsOutputSurface:
    object: str
    id: str
    status: str
    name: str
    auth: ManagementInstancePortalsConsumerProfilesAssignGroupsOutputSurfaceAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstancePortalsConsumerProfilesAssignGroupsOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    surface: ManagementInstancePortalsConsumerProfilesAssignGroupsOutputSurface
    groups: Optional[List[ManagementInstancePortalsConsumerProfilesAssignGroupsOutputGroups]] = None


class mapManagementInstancePortalsConsumerProfilesAssignGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerProfilesAssignGroupsOutput:
        return ManagementInstancePortalsConsumerProfilesAssignGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapManagementInstancePortalsConsumerProfilesAssignGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        surface=mapManagementInstancePortalsConsumerProfilesAssignGroupsOutputSurface.from_dict(data.get('surface')) if data.get('surface') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerProfilesAssignGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsConsumerProfilesAssignGroupsBody:
    group_ids: List[str]


class mapManagementInstancePortalsConsumerProfilesAssignGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerProfilesAssignGroupsBody:
        return ManagementInstancePortalsConsumerProfilesAssignGroupsBody(
        group_ids=data.get('group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerProfilesAssignGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

