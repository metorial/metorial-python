from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionErrorGroupsListOutputItems:
    object: str
    id: str
    count: float
    session_id: str
    created_at: datetime
    updated_at: datetime
    type: Optional[str] = None
    name: Optional[str] = None
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class SessionErrorGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionErrorGroupsListOutput:
    items: List[SessionErrorGroupsListOutputItems]
    pagination: SessionErrorGroupsListOutputPagination


class mapSessionErrorGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorGroupsListOutputItems:
        return SessionErrorGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        message=data.get('message'),
        count=data.get('count'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionErrorGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorGroupsListOutputPagination:
        return SessionErrorGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionErrorGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorGroupsListOutput:
        return SessionErrorGroupsListOutput(
        items=[mapSessionErrorGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionErrorGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionErrorGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None
    session_id: Optional[Union[str, List[str]]] = None


class mapSessionErrorGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorGroupsListQuery:
        return SessionErrorGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        session_id=data.get('session_id')
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
