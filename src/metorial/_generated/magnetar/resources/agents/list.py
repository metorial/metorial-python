from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AgentsListOutputItems:
    object: str
    id: str
    type: str
    status: str
    name: str
    slug: str
    actor_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class AgentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class AgentsListOutput:
    items: List[AgentsListOutputItems]
    pagination: AgentsListOutputPagination


class mapAgentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AgentsListOutputItems:
        return AgentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AgentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAgentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AgentsListOutputPagination:
        return AgentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[AgentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAgentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AgentsListOutput:
        return AgentsListOutput(
        items=[mapAgentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAgentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AgentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AgentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class AgentsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class AgentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[AgentsListQueryCreatedAt] = None
    updated_at: Optional[AgentsListQueryUpdatedAt] = None


class mapAgentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AgentsListQuery:
        return AgentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        type=data.get('type'),
        id=data.get('id'),
        created_at=mapAgentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapAgentsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AgentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

