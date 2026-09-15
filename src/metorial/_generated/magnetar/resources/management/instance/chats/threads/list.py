from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatsThreadsListOutputItemsContextAuthor:
    id: str
    name: str
@dataclass
class ManagementInstanceChatsThreadsListOutputItemsContextAssignee:
    id: str
    name: str
@dataclass
class ManagementInstanceChatsThreadsListOutputItemsContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[ManagementInstanceChatsThreadsListOutputItemsContextAuthor] = None
    assignee: Optional[ManagementInstanceChatsThreadsListOutputItemsContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class ManagementInstanceChatsThreadsListOutputItems:
    object: str
    id: str
    chat_id: str
    channel_id: str
    type: str
    provider_type: str
    provider_thread_id: str
    created_at: datetime
    updated_at: datetime
    provider_root_message_id: Optional[str] = None
    subject: Optional[str] = None
    permalink: Optional[str] = None
    context: Optional[ManagementInstanceChatsThreadsListOutputItemsContext] = None
    reply_count: Optional[float] = None
    last_reply_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None
@dataclass
class ManagementInstanceChatsThreadsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceChatsThreadsListOutput:
    items: List[ManagementInstanceChatsThreadsListOutputItems]
    pagination: ManagementInstanceChatsThreadsListOutputPagination


class mapManagementInstanceChatsThreadsListOutputItemsContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListOutputItemsContextAuthor:
        return ManagementInstanceChatsThreadsListOutputItemsContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListOutputItemsContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsThreadsListOutputItemsContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListOutputItemsContextAssignee:
        return ManagementInstanceChatsThreadsListOutputItemsContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListOutputItemsContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsThreadsListOutputItemsContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListOutputItemsContext:
        return ManagementInstanceChatsThreadsListOutputItemsContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapManagementInstanceChatsThreadsListOutputItemsContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapManagementInstanceChatsThreadsListOutputItemsContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListOutputItemsContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsThreadsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListOutputItems:
        return ManagementInstanceChatsThreadsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        channel_id=data.get('channel_id'),
        type=data.get('type'),
        provider_type=data.get('provider_type'),
        provider_thread_id=data.get('provider_thread_id'),
        provider_root_message_id=data.get('provider_root_message_id'),
        subject=data.get('subject'),
        permalink=data.get('permalink'),
        context=mapManagementInstanceChatsThreadsListOutputItemsContext.from_dict(data.get('context')) if data.get('context') else None,
        reply_count=data.get('reply_count'),
        last_reply_at=datetime.fromisoformat(data.get('last_reply_at').replace('Z', '+00:00')) if data.get('last_reply_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsThreadsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListOutputPagination:
        return ManagementInstanceChatsThreadsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsThreadsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListOutput:
        return ManagementInstanceChatsThreadsListOutput(
        items=[mapManagementInstanceChatsThreadsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceChatsThreadsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatsThreadsListQuery:
    channel_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None


class mapManagementInstanceChatsThreadsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsThreadsListQuery:
        return ManagementInstanceChatsThreadsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        channel_id=data.get('channel_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsThreadsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

