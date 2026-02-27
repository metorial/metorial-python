from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsErrorGroupsListOutputItems:
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
class SessionsErrorGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsErrorGroupsListOutput:
    items: List[SessionsErrorGroupsListOutputItems]
    pagination: SessionsErrorGroupsListOutputPagination


class mapSessionsErrorGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsErrorGroupsListOutputItems:
        return SessionsErrorGroupsListOutputItems(
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
    def to_dict(value: Union[SessionsErrorGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsErrorGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsErrorGroupsListOutputPagination:
        return SessionsErrorGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsErrorGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsErrorGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsErrorGroupsListOutput:
        return SessionsErrorGroupsListOutput(
        items=[mapSessionsErrorGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsErrorGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsErrorGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsErrorGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None


class mapSessionsErrorGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsErrorGroupsListQuery:
        return SessionsErrorGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[SessionsErrorGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
