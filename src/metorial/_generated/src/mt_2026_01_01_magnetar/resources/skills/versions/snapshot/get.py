from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsVersionsSnapshotGetOutputItems:
    object: str
    id: str
    kind: str
    path: str
    created_at: datetime
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class SkillsVersionsSnapshotGetOutput:
    object: str
    id: str
    skill_id: str
    store_id: str
    store_version_id: str
    version_number: float
    items: List[SkillsVersionsSnapshotGetOutputItems]
    created_at: datetime


class mapSkillsVersionsSnapshotGetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsVersionsSnapshotGetOutputItems:
        return SkillsVersionsSnapshotGetOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsVersionsSnapshotGetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsVersionsSnapshotGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsVersionsSnapshotGetOutput:
        return SkillsVersionsSnapshotGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        store_id=data.get('store_id'),
        store_version_id=data.get('store_version_id'),
        version_number=data.get('version_number'),
        items=[mapSkillsVersionsSnapshotGetOutputItems.from_dict(item) for item in data.get('items', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsVersionsSnapshotGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

