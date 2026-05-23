from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsGroupsItemsListOutputItemsSkill:
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
class SkillsGroupsItemsListOutputItems:
    object: str
    id: str
    status: str
    skill_group_id: str
    skill: SkillsGroupsItemsListOutputItemsSkill
    created_at: datetime
@dataclass
class SkillsGroupsItemsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsGroupsItemsListOutput:
    items: List[SkillsGroupsItemsListOutputItems]
    pagination: SkillsGroupsItemsListOutputPagination


class mapSkillsGroupsItemsListOutputItemsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsListOutputItemsSkill:
        return SkillsGroupsItemsListOutputItemsSkill(
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
    def to_dict(value: Union[SkillsGroupsItemsListOutputItemsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsItemsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsListOutputItems:
        return SkillsGroupsItemsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        skill_group_id=data.get('skill_group_id'),
        skill=mapSkillsGroupsItemsListOutputItemsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsItemsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsItemsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsListOutputPagination:
        return SkillsGroupsItemsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsItemsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsGroupsItemsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsListOutput:
        return SkillsGroupsItemsListOutput(
        items=[mapSkillsGroupsItemsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsGroupsItemsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsItemsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsGroupsItemsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsGroupsItemsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    skill_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SkillsGroupsItemsListQueryCreatedAt] = None


class mapSkillsGroupsItemsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsGroupsItemsListQuery:
        return SkillsGroupsItemsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        created_at=mapSkillsGroupsItemsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsGroupsItemsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

