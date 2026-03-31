from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumersProfilesGetOutputGroupsGroup:
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
class ManagementInstanceConsumersProfilesGetOutputGroups:
    object: str
    group: ManagementInstanceConsumersProfilesGetOutputGroupsGroup
    assigned_via: str
@dataclass
class ManagementInstanceConsumersProfilesGetOutput:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[ManagementInstanceConsumersProfilesGetOutputGroups]] = None


class mapManagementInstanceConsumersProfilesGetOutputGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesGetOutputGroupsGroup:
        return ManagementInstanceConsumersProfilesGetOutputGroupsGroup(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        is_default=data.get('is_default'),
        sso_group_ids=data.get('sso_group_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesGetOutputGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesGetOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesGetOutputGroups:
        return ManagementInstanceConsumersProfilesGetOutputGroups(
        object=data.get('object'),
        group=mapManagementInstanceConsumersProfilesGetOutputGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        assigned_via=data.get('assigned_via')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesGetOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesGetOutput:
        return ManagementInstanceConsumersProfilesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapManagementInstanceConsumersProfilesGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

