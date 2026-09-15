from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsChannelsListOutputItemsContextAuthor:
    id: str
    name: str
@dataclass
class ChatsChannelsListOutputItemsContextAssignee:
    id: str
    name: str
@dataclass
class ChatsChannelsListOutputItemsContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[ChatsChannelsListOutputItemsContextAuthor] = None
    assignee: Optional[ChatsChannelsListOutputItemsContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class ChatsChannelsListOutputItems:
    object: str
    id: str
    chat_id: str
    type: str
    provider_type: str
    provider_channel_id: str
    created_at: datetime
    updated_at: datetime
    workspace_id: Optional[str] = None
    name: Optional[str] = None
    topic: Optional[str] = None
    subject: Optional[str] = None
    member_count: Optional[float] = None
    permalink: Optional[str] = None
    context: Optional[ChatsChannelsListOutputItemsContext] = None
    last_interaction_at: Optional[datetime] = None
@dataclass
class ChatsChannelsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ChatsChannelsListOutput:
    items: List[ChatsChannelsListOutputItems]
    pagination: ChatsChannelsListOutputPagination


class mapChatsChannelsListOutputItemsContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListOutputItemsContextAuthor:
        return ChatsChannelsListOutputItemsContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListOutputItemsContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsListOutputItemsContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListOutputItemsContextAssignee:
        return ChatsChannelsListOutputItemsContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListOutputItemsContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsListOutputItemsContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListOutputItemsContext:
        return ChatsChannelsListOutputItemsContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapChatsChannelsListOutputItemsContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapChatsChannelsListOutputItemsContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListOutputItemsContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListOutputItems:
        return ChatsChannelsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        workspace_id=data.get('workspace_id'),
        type=data.get('type'),
        provider_type=data.get('provider_type'),
        provider_channel_id=data.get('provider_channel_id'),
        name=data.get('name'),
        topic=data.get('topic'),
        subject=data.get('subject'),
        member_count=data.get('member_count'),
        permalink=data.get('permalink'),
        context=mapChatsChannelsListOutputItemsContext.from_dict(data.get('context')) if data.get('context') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListOutputPagination:
        return ChatsChannelsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListOutput:
        return ChatsChannelsListOutput(
        items=[mapChatsChannelsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapChatsChannelsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsChannelsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    workspace_id: Optional[str] = None
    type: Optional[str] = None
    search: Optional[str] = None


class mapChatsChannelsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsListQuery:
        return ChatsChannelsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        workspace_id=data.get('workspace_id'),
        type=data.get('type'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

