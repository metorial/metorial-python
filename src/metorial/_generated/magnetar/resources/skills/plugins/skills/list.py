from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsPluginsSkillsListOutputItems:
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
class SkillsPluginsSkillsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsPluginsSkillsListOutput:
    items: List[SkillsPluginsSkillsListOutputItems]
    pagination: SkillsPluginsSkillsListOutputPagination


class mapSkillsPluginsSkillsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillsListOutputItems:
        return SkillsPluginsSkillsListOutputItems(
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
    def to_dict(value: Union[SkillsPluginsSkillsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsSkillsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillsListOutputPagination:
        return SkillsPluginsSkillsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsPluginsSkillsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillsListOutput:
        return SkillsPluginsSkillsListOutput(
        items=[mapSkillsPluginsSkillsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsPluginsSkillsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsPluginsSkillsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsPluginsSkillsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsPluginsSkillsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    skill_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    skill_configuration_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SkillsPluginsSkillsListQueryCreatedAt] = None
    updated_at: Optional[SkillsPluginsSkillsListQueryUpdatedAt] = None


class mapSkillsPluginsSkillsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsPluginsSkillsListQuery:
        return SkillsPluginsSkillsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        status=data.get('status'),
        skill_configuration_id=data.get('skill_configuration_id'),
        created_at=mapSkillsPluginsSkillsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSkillsPluginsSkillsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsPluginsSkillsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

