from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsVersionsListOutputItems:
    object: str
    id: str
    skill_id: str
    store_id: str
    store_version_id: str
    version_number: float
    created_at: datetime
@dataclass
class SkillsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsVersionsListOutput:
    items: List[SkillsVersionsListOutputItems]
    pagination: SkillsVersionsListOutputPagination


class mapSkillsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsVersionsListOutputItems:
        return SkillsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        store_id=data.get('store_id'),
        store_version_id=data.get('store_version_id'),
        version_number=data.get('version_number'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsVersionsListOutputPagination:
        return SkillsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsVersionsListOutput:
        return SkillsVersionsListOutput(
        items=[mapSkillsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSkillsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsVersionsListQuery:
        return SkillsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SkillsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

