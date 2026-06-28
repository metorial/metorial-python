from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksDestinationsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    url: str
    method: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    signing_secret: Optional[str] = None
@dataclass
class CallbacksDestinationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbacksDestinationsListOutput:
    items: List[CallbacksDestinationsListOutputItems]
    pagination: CallbacksDestinationsListOutputPagination


class mapCallbacksDestinationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListOutputItems:
        return CallbacksDestinationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksDestinationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksDestinationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListOutputPagination:
        return CallbacksDestinationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksDestinationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksDestinationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListOutput:
        return CallbacksDestinationsListOutput(
        items=[mapCallbacksDestinationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbacksDestinationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksDestinationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksDestinationsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksDestinationsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksDestinationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    callback_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[CallbacksDestinationsListQueryCreatedAt] = None
    updated_at: Optional[CallbacksDestinationsListQueryUpdatedAt] = None


class mapCallbacksDestinationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsListQuery:
        return CallbacksDestinationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        callback_id=data.get('callback_id'),
        created_at=mapCallbacksDestinationsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCallbacksDestinationsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksDestinationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

