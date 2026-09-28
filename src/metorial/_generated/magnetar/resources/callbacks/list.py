from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CallbacksListOutputItems:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_provider_id: str
    provider: CallbacksListOutputItemsProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CallbacksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbacksListOutput:
    items: List[CallbacksListOutputItems]
    pagination: CallbacksListOutputPagination


class mapCallbacksListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItemsProvider:
        return CallbacksListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputItems:
        return CallbacksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider=mapCallbacksListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutputPagination:
        return CallbacksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListOutput:
        return CallbacksListOutput(
        items=[mapCallbacksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbacksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CallbacksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    created_at: Optional[CallbacksListQueryCreatedAt] = None
    updated_at: Optional[CallbacksListQueryUpdatedAt] = None


class mapCallbacksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksListQuery:
        return CallbacksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider_id=data.get('provider_id'),
        search=data.get('search'),
        status=data.get('status'),
        created_at=mapCallbacksListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCallbacksListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

