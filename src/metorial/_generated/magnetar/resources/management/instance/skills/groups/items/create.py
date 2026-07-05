from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsGroupsItemsCreateOutputSkill:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsGroupsItemsCreateOutput:
    object: str
    id: str
    status: str
    skill_group_id: str
    skill: ManagementInstanceSkillsGroupsItemsCreateOutputSkill
    created_at: datetime


class mapManagementInstanceSkillsGroupsItemsCreateOutputSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsItemsCreateOutputSkill:
        return ManagementInstanceSkillsGroupsItemsCreateOutputSkill(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        client_metadata=data.get('client_metadata'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsItemsCreateOutputSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsGroupsItemsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsItemsCreateOutput:
        return ManagementInstanceSkillsGroupsItemsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        skill_group_id=data.get('skill_group_id'),
        skill=mapManagementInstanceSkillsGroupsItemsCreateOutputSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsItemsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsGroupsItemsCreateBody:
    skill_id: str


class mapManagementInstanceSkillsGroupsItemsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsItemsCreateBody:
        return ManagementInstanceSkillsGroupsItemsCreateBody(
        skill_id=data.get('skill_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsItemsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

