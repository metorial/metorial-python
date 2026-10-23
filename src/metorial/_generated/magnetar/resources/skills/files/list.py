from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsFilesListOutputItems:
    object: str
    path: str
    kind: str
    size: float
    etag: str
    skill_id: str
    store_item_id: str
    updated_at: datetime
    document_id: Optional[str] = None
    file_id: Optional[str] = None
@dataclass
class SkillsFilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsFilesListOutput:
    items: List[SkillsFilesListOutputItems]
    pagination: SkillsFilesListOutputPagination


class mapSkillsFilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesListOutputItems:
        return SkillsFilesListOutputItems(
        object=data.get('object'),
        path=data.get('path'),
        kind=data.get('kind'),
        size=data.get('size'),
        etag=data.get('etag'),
        skill_id=data.get('skill_id'),
        store_item_id=data.get('store_item_id'),
        document_id=data.get('document_id'),
        file_id=data.get('file_id'),
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesListOutputPagination:
        return SkillsFilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesListOutput:
        return SkillsFilesListOutput(
        items=[mapSkillsFilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsFilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

