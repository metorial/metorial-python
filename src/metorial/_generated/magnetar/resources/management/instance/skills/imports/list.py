from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsImportsListOutputItemsItemsSkill:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsImportsListOutputItemsItems:
    object: str
    id: str
    status: str
    path: str
    created_at: datetime
    error: Optional[str] = None
    skill: Optional[ManagementInstanceSkillsImportsListOutputItemsItemsSkill] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsImportsListOutputItems:
    object: str
    id: str
    status: str
    source: Dict[str, Any]
    items: List[ManagementInstanceSkillsImportsListOutputItemsItems]
    created_at: datetime
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsImportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsImportsListOutput:
    items: List[ManagementInstanceSkillsImportsListOutputItems]
    pagination: ManagementInstanceSkillsImportsListOutputPagination


class mapManagementInstanceSkillsImportsListOutputItemsItemsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsListOutputItemsItemsSkill:
        return ManagementInstanceSkillsImportsListOutputItemsItemsSkill(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsListOutputItemsItemsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsImportsListOutputItemsItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsListOutputItemsItems:
        return ManagementInstanceSkillsImportsListOutputItemsItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        path=data.get('path'),
        error=data.get('error'),
        skill=mapManagementInstanceSkillsImportsListOutputItemsItemsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsListOutputItemsItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsImportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsListOutputItems:
        return ManagementInstanceSkillsImportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        error=data.get('error'),
        items=[mapManagementInstanceSkillsImportsListOutputItemsItems.from_dict(item) for item in data.get('items', []) if item],
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsImportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsListOutputPagination:
        return ManagementInstanceSkillsImportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsImportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsListOutput:
        return ManagementInstanceSkillsImportsListOutput(
        items=[mapManagementInstanceSkillsImportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsImportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsImportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSkillsImportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsImportsListQuery:
        return ManagementInstanceSkillsImportsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsImportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

