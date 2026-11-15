from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsGroupsItemsGetOutputSkillImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class SkillsGroupsItemsGetOutputSkill:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: SkillsGroupsItemsGetOutputSkillImage
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
class SkillsGroupsItemsGetOutput:
    object: str
    id: str
    status: str
    skill_group_id: str
    skill: SkillsGroupsItemsGetOutputSkill
    created_at: datetime


class mapSkillsGroupsItemsGetOutputSkillImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsGetOutputSkillImage:
        return SkillsGroupsItemsGetOutputSkillImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsItemsGetOutputSkillImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsItemsGetOutputSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsGetOutputSkill:
        return SkillsGroupsItemsGetOutputSkill(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapSkillsGroupsItemsGetOutputSkillImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[SkillsGroupsItemsGetOutputSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsItemsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsGetOutput:
        return SkillsGroupsItemsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        skill_group_id=data.get('skill_group_id'),
        skill=mapSkillsGroupsItemsGetOutputSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsItemsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

