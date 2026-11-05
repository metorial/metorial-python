from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsFilesBatchOutputItemsFile:
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
class SkillsFilesBatchOutputItems:
    object: str
    type: str
    path: str
    previous_path: Optional[str] = None
    file: Optional[SkillsFilesBatchOutputItemsFile] = None
@dataclass
class SkillsFilesBatchOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsFilesBatchOutput:
    items: List[SkillsFilesBatchOutputItems]
    pagination: SkillsFilesBatchOutputPagination


class mapSkillsFilesBatchOutputItemsFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesBatchOutputItemsFile:
        return SkillsFilesBatchOutputItemsFile(
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
    def to_dict(value: Union[SkillsFilesBatchOutputItemsFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesBatchOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesBatchOutputItems:
        return SkillsFilesBatchOutputItems(
        object=data.get('object'),
        type=data.get('type'),
        path=data.get('path'),
        previous_path=data.get('previous_path'),
        file=mapSkillsFilesBatchOutputItemsFile.from_dict(data.get('file')) if data.get('file') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesBatchOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesBatchOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesBatchOutputPagination:
        return SkillsFilesBatchOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesBatchOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesBatchOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesBatchOutput:
        return SkillsFilesBatchOutput(
        items=[mapSkillsFilesBatchOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsFilesBatchOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesBatchOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsFilesBatchBody:
    changes: List[Dict[str, Any]]


class mapSkillsFilesBatchBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesBatchBody:
        return SkillsFilesBatchBody(
        changes=data.get('changes', [])
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesBatchBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

