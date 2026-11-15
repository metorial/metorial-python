from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsGroupsGetOutputImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGroupsGetOutputSkillsImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGroupsGetOutputSkills:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsGroupsGetOutputSkillsImage
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
class DashboardInstanceSkillsGroupsGetOutput:
    object: str
    id: str
    status: str
    name: str
    image_url: str
    image: DashboardInstanceSkillsGroupsGetOutputImage
    allow_consumer_skill_assignment: bool
    skills: List[DashboardInstanceSkillsGroupsGetOutputSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSkillsGroupsGetOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsGetOutputImage:
        return DashboardInstanceSkillsGroupsGetOutputImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsGetOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsGetOutputSkillsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsGetOutputSkillsImage:
        return DashboardInstanceSkillsGroupsGetOutputSkillsImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsGetOutputSkillsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsGetOutputSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsGetOutputSkills:
        return DashboardInstanceSkillsGroupsGetOutputSkills(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsGroupsGetOutputSkillsImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsGroupsGetOutputSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGroupsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGroupsGetOutput:
        return DashboardInstanceSkillsGroupsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        image_url=data.get('image_url'),
        image=mapDashboardInstanceSkillsGroupsGetOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment'),
        skills=[mapDashboardInstanceSkillsGroupsGetOutputSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGroupsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

