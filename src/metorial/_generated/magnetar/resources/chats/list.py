from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    chat_connection_id: str
    chat_instance_id: str
    chat_instance_provider_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    workspace_id: Optional[str] = None
@dataclass
class ChatsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ChatsListOutput:
    items: List[ChatsListOutputItems]
    pagination: ChatsListOutputPagination


class mapChatsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsListOutputItems:
        return ChatsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        chat_connection_id=data.get('chat_connection_id'),
        chat_instance_id=data.get('chat_instance_id'),
        chat_instance_provider_id=data.get('chat_instance_provider_id'),
        provider_id=data.get('provider_id'),
        workspace_id=data.get('workspace_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsListOutputPagination:
        return ChatsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ChatsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsListOutput:
        return ChatsListOutput(
        items=[mapChatsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapChatsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ChatsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ChatsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    chat_connection_id: Optional[Union[str, List[str]]] = None
    chat_instance_id: Optional[Union[str, List[str]]] = None
    chat_instance_provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ChatsListQueryCreatedAt] = None
    updated_at: Optional[ChatsListQueryUpdatedAt] = None


class mapChatsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsListQuery:
        return ChatsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        chat_connection_id=data.get('chat_connection_id'),
        chat_instance_id=data.get('chat_instance_id'),
        chat_instance_provider_id=data.get('chat_instance_provider_id'),
        created_at=mapChatsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapChatsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

