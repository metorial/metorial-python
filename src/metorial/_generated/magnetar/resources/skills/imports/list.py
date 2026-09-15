from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsImportsListOutputItemsItemsSkill:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class SkillsImportsListOutputItemsItems:
    object: str
    id: str
    status: str
    path: str
    created_at: datetime
    error: Optional[str] = None
    skill: Optional[SkillsImportsListOutputItemsItemsSkill] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsImportsListOutputItems:
    object: str
    id: str
    status: str
    source: Dict[str, Any]
    items: List[SkillsImportsListOutputItemsItems]
    created_at: datetime
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsImportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsImportsListOutput:
    items: List[SkillsImportsListOutputItems]
    pagination: SkillsImportsListOutputPagination


class mapSkillsImportsListOutputItemsItemsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsListOutputItemsItemsSkill:
        return SkillsImportsListOutputItemsItemsSkill(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsListOutputItemsItemsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsImportsListOutputItemsItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsListOutputItemsItems:
        return SkillsImportsListOutputItemsItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        path=data.get('path'),
        error=data.get('error'),
        skill=mapSkillsImportsListOutputItemsItemsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsListOutputItemsItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsImportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsListOutputItems:
        return SkillsImportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        error=data.get('error'),
        items=[mapSkillsImportsListOutputItemsItems.from_dict(item) for item in data.get('items', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsImportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsListOutputPagination:
        return SkillsImportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsImportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsListOutput:
        return SkillsImportsListOutput(
        items=[mapSkillsImportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsImportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsImportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapSkillsImportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsListQuery:
        return SkillsImportsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

