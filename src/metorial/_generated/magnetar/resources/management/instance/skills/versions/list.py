from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsVersionsListOutputItems:
    object: str
    id: str
    skill_id: str
    store_id: str
    store_version_id: str
    version_number: float
    created_at: datetime
@dataclass
class ManagementInstanceSkillsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsVersionsListOutput:
    items: List[ManagementInstanceSkillsVersionsListOutputItems]
    pagination: ManagementInstanceSkillsVersionsListOutputPagination


class mapManagementInstanceSkillsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsVersionsListOutputItems:
        return ManagementInstanceSkillsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        store_id=data.get('store_id'),
        store_version_id=data.get('store_version_id'),
        version_number=data.get('version_number'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsVersionsListOutputPagination:
        return ManagementInstanceSkillsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsVersionsListOutput:
        return ManagementInstanceSkillsVersionsListOutput(
        items=[mapManagementInstanceSkillsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceSkillsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsVersionsListQuery:
        return ManagementInstanceSkillsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

