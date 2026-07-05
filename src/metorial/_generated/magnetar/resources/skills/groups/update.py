from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsGroupsUpdateOutputSkills:
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
class SkillsGroupsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    skills: List[SkillsGroupsUpdateOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSkillsGroupsUpdateOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsUpdateOutputSkills:
        return SkillsGroupsUpdateOutputSkills(
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
    def to_dict(value: Union[SkillsGroupsUpdateOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsUpdateOutput:
        return SkillsGroupsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        skills=[mapSkillsGroupsUpdateOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsGroupsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    skill_ids: Optional[List[str]] = None


class mapSkillsGroupsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsUpdateBody:
        return SkillsGroupsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        skill_ids=data.get('skill_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

