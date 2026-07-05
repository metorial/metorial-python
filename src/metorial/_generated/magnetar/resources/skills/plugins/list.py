from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsPluginsListOutputItemsSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsPluginsListOutputItems:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    skills: List[SkillsPluginsListOutputItemsSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsPluginsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsPluginsListOutput:
    items: List[SkillsPluginsListOutputItems]
    pagination: SkillsPluginsListOutputPagination


class mapSkillsPluginsListOutputItemsSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsListOutputItemsSkills:
        return SkillsPluginsListOutputItemsSkills(
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
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsListOutputItemsSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsListOutputItems:
        return SkillsPluginsListOutputItems(
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
        skills=[mapSkillsPluginsListOutputItemsSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsListOutputPagination:
        return SkillsPluginsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsListOutput:
        return SkillsPluginsListOutput(
        items=[mapSkillsPluginsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsPluginsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsPluginsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsPluginsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsPluginsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    skill_marketplace_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    category: Optional[str] = None
    search: Optional[str] = None
    skill_configuration_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SkillsPluginsListQueryCreatedAt] = None
    updated_at: Optional[SkillsPluginsListQueryUpdatedAt] = None


class mapSkillsPluginsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsListQuery:
        return SkillsPluginsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        skill_marketplace_id=data.get('skill_marketplace_id'),
        status=data.get('status'),
        category=data.get('category'),
        search=data.get('search'),
        skill_configuration_id=data.get('skill_configuration_id'),
        created_at=mapSkillsPluginsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSkillsPluginsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

