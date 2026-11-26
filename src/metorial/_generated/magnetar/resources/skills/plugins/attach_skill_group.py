from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsPluginsAttachSkillGroupOutputSkillsSkillImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class SkillsPluginsAttachSkillGroupOutputSkillsSkill:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: SkillsPluginsAttachSkillGroupOutputSkillsSkillImage
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
class SkillsPluginsAttachSkillGroupOutputSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    skill: SkillsPluginsAttachSkillGroupOutputSkillsSkill
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsPluginsAttachSkillGroupOutput:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    source: Dict[str, Any]
    skills: List[SkillsPluginsAttachSkillGroupOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None


class mapSkillsPluginsAttachSkillGroupOutputSkillsSkillImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsAttachSkillGroupOutputSkillsSkillImage:
        return SkillsPluginsAttachSkillGroupOutputSkillsSkillImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsAttachSkillGroupOutputSkillsSkillImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsAttachSkillGroupOutputSkillsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsAttachSkillGroupOutputSkillsSkill:
        return SkillsPluginsAttachSkillGroupOutputSkillsSkill(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapSkillsPluginsAttachSkillGroupOutputSkillsSkillImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[SkillsPluginsAttachSkillGroupOutputSkillsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsAttachSkillGroupOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsAttachSkillGroupOutputSkills:
        return SkillsPluginsAttachSkillGroupOutputSkills(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        status=data.get('status'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        client_metadata=data.get('client_metadata'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_id=data.get('skill_id'),
        skill=mapSkillsPluginsAttachSkillGroupOutputSkillsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsAttachSkillGroupOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsAttachSkillGroupOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsAttachSkillGroupOutput:
        return SkillsPluginsAttachSkillGroupOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sync_status=data.get('sync_status'),
        image_url=data.get('image_url'),
        name=data.get('name'),
        description=data.get('description'),
        long_description=data.get('long_description'),
        category=data.get('category'),
        slug=data.get('slug'),
        skill_configuration_id=data.get('skill_configuration_id'),
        source=data.get('source'),
        skills=[mapSkillsPluginsAttachSkillGroupOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsAttachSkillGroupOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsPluginsAttachSkillGroupBody:
    skill_group_id: str


class mapSkillsPluginsAttachSkillGroupBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsAttachSkillGroupBody:
        return SkillsPluginsAttachSkillGroupBody(
        skill_group_id=data.get('skill_group_id')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsAttachSkillGroupBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

