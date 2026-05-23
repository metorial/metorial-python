from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsConfigurationsListOutputItems:
    object: str
    id: str
    is_default: bool
    allow_scripts: bool
    allowed_file_extensions: List[str]
    allow_non_standard_directories: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
@dataclass
class SkillsConfigurationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsConfigurationsListOutput:
    items: List[SkillsConfigurationsListOutputItems]
    pagination: SkillsConfigurationsListOutputPagination


class mapSkillsConfigurationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsConfigurationsListOutputItems:
        return SkillsConfigurationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        allow_scripts=data.get('allow_scripts'),
        allowed_file_extensions=data.get('allowed_file_extensions', []),
        allow_non_standard_directories=data.get('allow_non_standard_directories'),
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsConfigurationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsConfigurationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsConfigurationsListOutputPagination:
        return SkillsConfigurationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsConfigurationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsConfigurationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsConfigurationsListOutput:
        return SkillsConfigurationsListOutput(
        items=[mapSkillsConfigurationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsConfigurationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsConfigurationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsConfigurationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSkillsConfigurationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsConfigurationsListQuery:
        return SkillsConfigurationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SkillsConfigurationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

