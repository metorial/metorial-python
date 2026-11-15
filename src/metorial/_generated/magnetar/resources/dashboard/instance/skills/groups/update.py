from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsGroupsUpdateOutputImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGroupsUpdateOutputSkillsImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGroupsUpdateOutputSkills:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsGroupsUpdateOutputSkillsImage
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
class DashboardInstanceSkillsGroupsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsGroupsUpdateOutputImage
    allow_consumer_skill_assignment: bool
    skills: List[DashboardInstanceSkillsGroupsUpdateOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSkillsGroupsUpdateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsUpdateOutputImage:
        return DashboardInstanceSkillsGroupsUpdateOutputImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsUpdateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsUpdateOutputSkillsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsUpdateOutputSkillsImage:
        return DashboardInstanceSkillsGroupsUpdateOutputSkillsImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsUpdateOutputSkillsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsUpdateOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsUpdateOutputSkills:
        return DashboardInstanceSkillsGroupsUpdateOutputSkills(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsGroupsUpdateOutputSkillsImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsGroupsUpdateOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsUpdateOutput:
        return DashboardInstanceSkillsGroupsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsGroupsUpdateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment'),
        skills=[mapDashboardInstanceSkillsGroupsUpdateOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsGroupsUpdateBodyImageIcon:
    icon: str
    color: str
@dataclass
class DashboardInstanceSkillsGroupsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    skill_ids: Optional[List[str]] = None
    allow_consumer_skill_assignment: Optional[bool] = None
    image_file_id: Optional[str] = None
    image_icon: Optional[DashboardInstanceSkillsGroupsUpdateBodyImageIcon] = None


class mapDashboardInstanceSkillsGroupsUpdateBodyImageIcon:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsUpdateBodyImageIcon:
        return DashboardInstanceSkillsGroupsUpdateBodyImageIcon(
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsUpdateBodyImageIcon, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsUpdateBody:
        return DashboardInstanceSkillsGroupsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        skill_ids=data.get('skill_ids', []),
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment'),
        image_file_id=data.get('image_file_id'),
        image_icon=mapDashboardInstanceSkillsGroupsUpdateBodyImageIcon.from_dict(data.get('image_icon')) if data.get('image_icon') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

