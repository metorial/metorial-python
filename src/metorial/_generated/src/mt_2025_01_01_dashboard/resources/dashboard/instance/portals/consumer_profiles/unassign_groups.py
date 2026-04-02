from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputGroupsGroup:
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
class DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputGroups:
    object: str
    group: DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputGroupsGroup
    assigned_via: str
@dataclass
class DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputSurfaceAuth:
    object: str
    session_expiry_time_in_seconds: float
@dataclass
class DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputSurface:
    object: str
    id: str
    status: str
    name: str
    auth: DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputSurfaceAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    surface: DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputSurface
    groups: Optional[List[DashboardInstancePortalsConsumerProfilesUnassignGroupsOutputGroups]] = None


class mapDashboardInstancePortalsConsumerProfilesUnassignGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput:
        return DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapDashboardInstancePortalsConsumerProfilesUnassignGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        surface=mapDashboardInstancePortalsConsumerProfilesUnassignGroupsOutputSurface.from_dict(data.get('surface')) if data.get('surface') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesUnassignGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerProfilesUnassignGroupsBody:
    group_ids: List[str]


class mapDashboardInstancePortalsConsumerProfilesUnassignGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesUnassignGroupsBody:
        return DashboardInstancePortalsConsumerProfilesUnassignGroupsBody(
        group_ids=data.get('group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesUnassignGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

