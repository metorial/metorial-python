from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsGroupsCreateOutputImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGroupsCreateOutputSkillsImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGroupsCreateOutputSkills:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsGroupsCreateOutputSkillsImage
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
class DashboardInstanceSkillsGroupsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsGroupsCreateOutputImage
    allow_consumer_skill_assignment: bool
    skills: List[DashboardInstanceSkillsGroupsCreateOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSkillsGroupsCreateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsCreateOutputImage:
        return DashboardInstanceSkillsGroupsCreateOutputImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsCreateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsCreateOutputSkillsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsCreateOutputSkillsImage:
        return DashboardInstanceSkillsGroupsCreateOutputSkillsImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsCreateOutputSkillsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsCreateOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsCreateOutputSkills:
        return DashboardInstanceSkillsGroupsCreateOutputSkills(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsGroupsCreateOutputSkillsImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsGroupsCreateOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsCreateOutput:
        return DashboardInstanceSkillsGroupsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsGroupsCreateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment'),
        skills=[mapDashboardInstanceSkillsGroupsCreateOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsGroupsCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    skill_ids: Optional[List[str]] = None
    allow_consumer_skill_assignment: Optional[bool] = None


class mapDashboardInstanceSkillsGroupsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsCreateBody:
        return DashboardInstanceSkillsGroupsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        skill_ids=data.get('skill_ids', []),
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

