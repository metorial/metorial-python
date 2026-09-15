from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsImportsGetOutputItemsSkill:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsImportsGetOutputItems:
    object: str
    id: str
    status: str
    path: str
    created_at: datetime
    error: Optional[str] = None
    skill: Optional[ManagementInstanceSkillsImportsGetOutputItemsSkill] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsImportsGetOutput:
    object: str
    id: str
    status: str
    source: Dict[str, Any]
    items: List[ManagementInstanceSkillsImportsGetOutputItems]
    created_at: datetime
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapManagementInstanceSkillsImportsGetOutputItemsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsGetOutputItemsSkill:
        return ManagementInstanceSkillsImportsGetOutputItemsSkill(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsGetOutputItemsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsImportsGetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsGetOutputItems:
        return ManagementInstanceSkillsImportsGetOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        path=data.get('path'),
        error=data.get('error'),
        skill=mapManagementInstanceSkillsImportsGetOutputItemsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsGetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsImportsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsGetOutput:
        return ManagementInstanceSkillsImportsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        error=data.get('error'),
        items=[mapManagementInstanceSkillsImportsGetOutputItems.from_dict(item) for item in data.get('items', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

