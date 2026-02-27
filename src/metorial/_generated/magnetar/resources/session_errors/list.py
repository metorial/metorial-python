from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionErrorsListOutputItems:
    object: str
    id: str
    session_id: str
    created_at: datetime
    type: Optional[str] = None
    name: Optional[str] = None
    message: Optional[str] = None
    stack: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_error_group_id: Optional[str] = None
    provider_run_id: Optional[str] = None
@dataclass
class SessionErrorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionErrorsListOutput:
    items: List[SessionErrorsListOutputItems]
    pagination: SessionErrorsListOutputPagination


class mapSessionErrorsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorsListOutputItems:
        return SessionErrorsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        message=data.get('message'),
        stack=data.get('stack'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_error_group_id=data.get('session_error_group_id'),
        provider_run_id=data.get('provider_run_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionErrorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorsListOutputPagination:
        return SessionErrorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionErrorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorsListOutput:
        return SessionErrorsListOutput(
        items=[mapSessionErrorsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionErrorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionErrorsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_error_group_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None


class mapSessionErrorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionErrorsListQuery:
        return SessionErrorsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        session_error_group_id=data.get('session_error_group_id'),
        provider_run_id=data.get('provider_run_id')
        )

    @staticmethod
    def to_dict(value: Union[SessionErrorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
