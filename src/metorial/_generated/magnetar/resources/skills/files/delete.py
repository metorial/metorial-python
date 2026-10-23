from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsFilesDeleteOutputFile:
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
class SkillsFilesDeleteOutput:
    object: str
    type: str
    path: str
    previous_path: Optional[str] = None
    file: Optional[SkillsFilesDeleteOutputFile] = None


class mapSkillsFilesDeleteOutputFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesDeleteOutputFile:
        return SkillsFilesDeleteOutputFile(
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
    def to_dict(value: Union[SkillsFilesDeleteOutputFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesDeleteOutput:
        return SkillsFilesDeleteOutput(
        object=data.get('object'),
        type=data.get('type'),
        path=data.get('path'),
        previous_path=data.get('previous_path'),
        file=mapSkillsFilesDeleteOutputFile.from_dict(data.get('file')) if data.get('file') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsFilesDeleteQuery:
    path: str
    if_match: Optional[str] = None


class mapSkillsFilesDeleteQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesDeleteQuery:
        return SkillsFilesDeleteQuery(
        path=data.get('path'),
        if_match=data.get('if_match')
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesDeleteQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

