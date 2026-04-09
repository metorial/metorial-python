from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerSurfacesListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class ConsumerSurfacesListOutputItems:
    object: str
    id: str
    status: str
    name: str
    auth: ConsumerSurfacesListOutputItemsAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ConsumerSurfacesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerSurfacesListOutput:
    items: List[ConsumerSurfacesListOutputItems]
    pagination: ConsumerSurfacesListOutputPagination


class mapConsumerSurfacesListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesListOutputItemsAuth:
        return ConsumerSurfacesListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        email_whitelist=data.get('email_whitelist', [])
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSurfacesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesListOutputItems:
        return ConsumerSurfacesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        auth=mapConsumerSurfacesListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSurfacesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesListOutputPagination:
        return ConsumerSurfacesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSurfacesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesListOutput:
        return ConsumerSurfacesListOutput(
        items=[mapConsumerSurfacesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerSurfacesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerSurfacesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapConsumerSurfacesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSurfacesListQuery:
        return ConsumerSurfacesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSurfacesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

