from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerProfilesAssignGroupsOutputGroupsGroup:
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
class DashboardInstancePortalsConsumerProfilesAssignGroupsOutputGroups:
    object: str
    group: DashboardInstancePortalsConsumerProfilesAssignGroupsOutputGroupsGroup
    assigned_via: str
@dataclass
class DashboardInstancePortalsConsumerProfilesAssignGroupsOutputSurfaceAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class DashboardInstancePortalsConsumerProfilesAssignGroupsOutputSurface:
    object: str
    id: str
    status: str
    name: str
    auth: DashboardInstancePortalsConsumerProfilesAssignGroupsOutputSurfaceAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsConsumerProfilesAssignGroupsOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    status: str
    created_at: datetime
    updated_at: datetime
    surface: DashboardInstancePortalsConsumerProfilesAssignGroupsOutputSurface
    groups: Optional[List[DashboardInstancePortalsConsumerProfilesAssignGroupsOutputGroups]] = None


class mapDashboardInstancePortalsConsumerProfilesAssignGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesAssignGroupsOutput:
        return DashboardInstancePortalsConsumerProfilesAssignGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapDashboardInstancePortalsConsumerProfilesAssignGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        surface=mapDashboardInstancePortalsConsumerProfilesAssignGroupsOutputSurface.from_dict(data.get('surface')) if data.get('surface') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesAssignGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerProfilesAssignGroupsBody:
    group_ids: List[str]


class mapDashboardInstancePortalsConsumerProfilesAssignGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesAssignGroupsBody:
        return DashboardInstancePortalsConsumerProfilesAssignGroupsBody(
        group_ids=data.get('group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesAssignGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

