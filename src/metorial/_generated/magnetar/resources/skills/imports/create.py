from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsImportsCreateOutputItemsSkill:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class SkillsImportsCreateOutputItems:
    object: str
    id: str
    status: str
    path: str
    created_at: datetime
    error: Optional[str] = None
    skill: Optional[SkillsImportsCreateOutputItemsSkill] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsImportsCreateOutput:
    object: str
    id: str
    status: str
    source: Dict[str, Any]
    items: List[SkillsImportsCreateOutputItems]
    created_at: datetime
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapSkillsImportsCreateOutputItemsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsCreateOutputItemsSkill:
        return SkillsImportsCreateOutputItemsSkill(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsCreateOutputItemsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsImportsCreateOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsCreateOutputItems:
        return SkillsImportsCreateOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        path=data.get('path'),
        error=data.get('error'),
        skill=mapSkillsImportsCreateOutputItemsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsCreateOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsImportsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsCreateOutput:
        return SkillsImportsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        error=data.get('error'),
        items=[mapSkillsImportsCreateOutputItems.from_dict(item) for item in data.get('items', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsImportsCreateBody:
    source: Dict[str, Any]


class mapSkillsImportsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsImportsCreateBody:
        return SkillsImportsCreateBody(
        source=data.get('source')
        )

    @staticmethod
    def to_dict(value: Union[SkillsImportsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

