from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage
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
class DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    skill: DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsPluginsAttachSkillGroupOutput:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    source: Dict[str, Any]
    skills: List[DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None


class mapDashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage:
        return DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill:
        return DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkillImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills:
        return DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills(
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
        skill=mapDashboardInstanceSkillsPluginsAttachSkillGroupOutputSkillsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsPluginsAttachSkillGroupOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsAttachSkillGroupOutput:
        return DashboardInstanceSkillsPluginsAttachSkillGroupOutput(
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
        skills=[mapDashboardInstanceSkillsPluginsAttachSkillGroupOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsAttachSkillGroupOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsPluginsAttachSkillGroupBody:
    skill_group_id: str


class mapDashboardInstanceSkillsPluginsAttachSkillGroupBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsPluginsAttachSkillGroupBody:
        return DashboardInstanceSkillsPluginsAttachSkillGroupBody(
        skill_group_id=data.get('skill_group_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsPluginsAttachSkillGroupBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

