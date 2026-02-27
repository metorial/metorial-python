from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesListOutputItems:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class SessionTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionTemplatesListOutput:
    items: List[SessionTemplatesListOutputItems]
    pagination: SessionTemplatesListOutputPagination


class mapSessionTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListOutputItems:
        return SessionTemplatesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListOutputPagination:
        return SessionTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListOutput:
        return SessionTemplatesListOutput(
        items=[mapSessionTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionTemplatesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapSessionTemplatesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListQuery:
        return SessionTemplatesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
