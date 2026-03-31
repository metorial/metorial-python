from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentityActorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IdentityActorsListOutput:
    items: List[Dict[str, Any]]
    pagination: IdentityActorsListOutputPagination


class mapIdentityActorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentityActorsListOutputPagination:
        return IdentityActorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IdentityActorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentityActorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentityActorsListOutput:
        return IdentityActorsListOutput(
        items=data.get('items', []),
        pagination=mapIdentityActorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentityActorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentityActorsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IdentityActorsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IdentityActorsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    agent_id: Optional[Union[str, List[str]]] = None
    consumer_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[IdentityActorsListQueryCreatedAt] = None
    updated_at: Optional[IdentityActorsListQueryUpdatedAt] = None


class mapIdentityActorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentityActorsListQuery:
        return IdentityActorsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        agent_id=data.get('agent_id'),
        consumer_id=data.get('consumer_id'),
        created_at=mapIdentityActorsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapIdentityActorsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentityActorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

