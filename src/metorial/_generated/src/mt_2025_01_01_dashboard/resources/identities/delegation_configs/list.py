from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationConfigsListOutputItems:
    object: str
    id: str
    status: str
    is_default: bool
    sub_delegation_behavior: str
    sub_delegation_depth: float
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class IdentitiesDelegationConfigsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IdentitiesDelegationConfigsListOutput:
    items: List[IdentitiesDelegationConfigsListOutputItems]
    pagination: IdentitiesDelegationConfigsListOutputPagination


class mapIdentitiesDelegationConfigsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationConfigsListOutputItems:
        return IdentitiesDelegationConfigsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        sub_delegation_behavior=data.get('sub_delegation_behavior'),
        sub_delegation_depth=data.get('sub_delegation_depth'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationConfigsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationConfigsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationConfigsListOutputPagination:
        return IdentitiesDelegationConfigsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationConfigsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIdentitiesDelegationConfigsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationConfigsListOutput:
        return IdentitiesDelegationConfigsListOutput(
        items=[mapIdentitiesDelegationConfigsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIdentitiesDelegationConfigsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationConfigsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IdentitiesDelegationConfigsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IdentitiesDelegationConfigsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IdentitiesDelegationConfigsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[IdentitiesDelegationConfigsListQueryCreatedAt] = None
    updated_at: Optional[IdentitiesDelegationConfigsListQueryUpdatedAt] = None


class mapIdentitiesDelegationConfigsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationConfigsListQuery:
        return IdentitiesDelegationConfigsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        created_at=mapIdentitiesDelegationConfigsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapIdentitiesDelegationConfigsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationConfigsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

