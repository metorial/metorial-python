from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatInstancesListOutputItemsIdentity:
    id: str
    user_id: str
    name: str
    username: str
    provider_type: str
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ChatInstancesListOutputItems:
    object: str
    id: str
    status: str
    chat_connection_id: str
    name: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    identity: Optional[ChatInstancesListOutputItemsIdentity] = None
@dataclass
class ChatInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ChatInstancesListOutput:
    items: List[ChatInstancesListOutputItems]
    pagination: ChatInstancesListOutputPagination


class mapChatInstancesListOutputItemsIdentity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesListOutputItemsIdentity:
        return ChatInstancesListOutputItemsIdentity(
        id=data.get('id'),
        user_id=data.get('user_id'),
        name=data.get('name'),
        username=data.get('username'),
        provider_type=data.get('provider_type'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesListOutputItemsIdentity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesListOutputItems:
        return ChatInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        chat_connection_id=data.get('chat_connection_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        identity=mapChatInstancesListOutputItemsIdentity.from_dict(data.get('identity')) if data.get('identity') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesListOutputPagination:
        return ChatInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesListOutput:
        return ChatInstancesListOutput(
        items=[mapChatInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapChatInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatInstancesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ChatInstancesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ChatInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    chat_connection_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ChatInstancesListQueryCreatedAt] = None
    updated_at: Optional[ChatInstancesListQueryUpdatedAt] = None


class mapChatInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatInstancesListQuery:
        return ChatInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        chat_connection_id=data.get('chat_connection_id'),
        created_at=mapChatInstancesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapChatInstancesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

