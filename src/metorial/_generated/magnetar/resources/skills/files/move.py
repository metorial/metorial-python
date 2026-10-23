from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsFilesMoveOutputFile:
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
class SkillsFilesMoveOutput:
    object: str
    type: str
    path: str
    previous_path: Optional[str] = None
    file: Optional[SkillsFilesMoveOutputFile] = None


class mapSkillsFilesMoveOutputFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesMoveOutputFile:
        return SkillsFilesMoveOutputFile(
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
    def to_dict(value: Union[SkillsFilesMoveOutputFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsFilesMoveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesMoveOutput:
        return SkillsFilesMoveOutput(
        object=data.get('object'),
        type=data.get('type'),
        path=data.get('path'),
        previous_path=data.get('previous_path'),
        file=mapSkillsFilesMoveOutputFile.from_dict(data.get('file')) if data.get('file') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesMoveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsFilesMoveBody:
    path: str
    to_path: str
    if_match: Optional[str] = None


class mapSkillsFilesMoveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsFilesMoveBody:
        return SkillsFilesMoveBody(
        path=data.get('path'),
        to_path=data.get('to_path'),
        if_match=data.get('if_match')
        )

    @staticmethod
    def to_dict(value: Union[SkillsFilesMoveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

