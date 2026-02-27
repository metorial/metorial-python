from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionErrorGroupsListOutputItems:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    occurrence_count: float
    created_at: datetime
    provider_id: Optional[str] = None
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
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        occurrence_count=data.get('occurrence_count'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
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
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None


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
        id=data.get('id'),
        session_id=data.get('session_id'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
