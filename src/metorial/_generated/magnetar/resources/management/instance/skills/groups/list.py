from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsGroupsListOutputItemsImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class ManagementInstanceSkillsGroupsListOutputItemsSkillsImage:
    object: str
    type: str
    icon: Optional[str] = None
    color: Optional[str] = None
@dataclass
class ManagementInstanceSkillsGroupsListOutputItemsSkills:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    image: ManagementInstanceSkillsGroupsListOutputItemsSkillsImage
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
class ManagementInstanceSkillsGroupsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    image_url: str
    image: ManagementInstanceSkillsGroupsListOutputItemsImage
    allow_consumer_skill_assignment: bool
    skills: List[ManagementInstanceSkillsGroupsListOutputItemsSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceSkillsGroupsListOutput:
    object: str
    items: List[ManagementInstanceSkillsGroupsListOutputItems]
    pagination: ManagementInstanceSkillsGroupsListOutputPagination


class mapManagementInstanceSkillsGroupsListOutputItemsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListOutputItemsImage:
        return ManagementInstanceSkillsGroupsListOutputItemsImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListOutputItemsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsGroupsListOutputItemsSkillsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListOutputItemsSkillsImage:
        return ManagementInstanceSkillsGroupsListOutputItemsSkillsImage(
        object=data.get('object'),
        type=data.get('type'),
        icon=data.get('icon'),
        color=data.get('color')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListOutputItemsSkillsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsGroupsListOutputItemsSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListOutputItemsSkills:
        return ManagementInstanceSkillsGroupsListOutputItemsSkills(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        image=mapManagementInstanceSkillsGroupsListOutputItemsSkillsImage.from_dict(data.get('image')) if data.get('image') else None,
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
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListOutputItemsSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListOutputItems:
        return ManagementInstanceSkillsGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        image_url=data.get('image_url'),
        image=mapManagementInstanceSkillsGroupsListOutputItemsImage.from_dict(data.get('image')) if data.get('image') else None,
        allow_consumer_skill_assignment=data.get('allow_consumer_skill_assignment'),
        skills=[mapManagementInstanceSkillsGroupsListOutputItemsSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListOutputPagination:
        return ManagementInstanceSkillsGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListOutput:
        return ManagementInstanceSkillsGroupsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceSkillsGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsGroupsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsGroupsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    skill_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceSkillsGroupsListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceSkillsGroupsListQueryUpdatedAt] = None


class mapManagementInstanceSkillsGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsGroupsListQuery:
        return ManagementInstanceSkillsGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        created_at=mapManagementInstanceSkillsGroupsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceSkillsGroupsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

