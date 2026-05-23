from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsAgentsListOutputItems:
    object: str
    id: str
    skill_id: str
    name: str
    slug: str
    status: str
    store_id: str
    document_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    store_item_id: Optional[str] = None
    path: Optional[str] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsAgentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsAgentsListOutput:
    items: List[ManagementInstanceSkillsAgentsListOutputItems]
    pagination: ManagementInstanceSkillsAgentsListOutputPagination


class mapManagementInstanceSkillsAgentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAgentsListOutputItems:
        return ManagementInstanceSkillsAgentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        status=data.get('status'),
        store_id=data.get('store_id'),
        store_item_id=data.get('store_item_id'),
        path=data.get('path'),
        document_id=data.get('document_id'),
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAgentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsAgentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAgentsListOutputPagination:
        return ManagementInstanceSkillsAgentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAgentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsAgentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAgentsListOutput:
        return ManagementInstanceSkillsAgentsListOutput(
        items=[mapManagementInstanceSkillsAgentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsAgentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAgentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsAgentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    include_archived: Optional[bool] = None


class mapManagementInstanceSkillsAgentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsAgentsListQuery:
        return ManagementInstanceSkillsAgentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        include_archived=data.get('include_archived')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsAgentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

