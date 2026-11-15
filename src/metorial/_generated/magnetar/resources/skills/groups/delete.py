from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsGroupsDeleteOutputImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class SkillsGroupsDeleteOutputSkillsImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class SkillsGroupsDeleteOutputSkills:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: SkillsGroupsDeleteOutputSkillsImage
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
class SkillsGroupsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    image_url: str
    image: SkillsGroupsDeleteOutputImage
    allow_consumer_skill_assignment: bool
    skills: List[SkillsGroupsDeleteOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSkillsGroupsDeleteOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsDeleteOutputImage:
        return SkillsGroupsDeleteOutputImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsDeleteOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsDeleteOutputSkillsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsDeleteOutputSkillsImage:
        return SkillsGroupsDeleteOutputSkillsImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsDeleteOutputSkillsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsDeleteOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsDeleteOutputSkills:
        return SkillsGroupsDeleteOutputSkills(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapSkillsGroupsDeleteOutputSkillsImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[SkillsGroupsDeleteOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsDeleteOutput:
        return SkillsGroupsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        image_url=data.get('image_url'),
        image=mapSkillsGroupsDeleteOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment'),
        skills=[mapSkillsGroupsDeleteOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

