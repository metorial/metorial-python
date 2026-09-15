from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsThreadsListOutputItemsContextAuthor:
    id: str
    name: str
@dataclass
class DashboardInstanceChatsThreadsListOutputItemsContextAssignee:
    id: str
    name: str
@dataclass
class DashboardInstanceChatsThreadsListOutputItemsContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[DashboardInstanceChatsThreadsListOutputItemsContextAuthor] = None
    assignee: Optional[DashboardInstanceChatsThreadsListOutputItemsContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class DashboardInstanceChatsThreadsListOutputItems:
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
    context: Optional[DashboardInstanceChatsThreadsListOutputItemsContext] = None
    reply_count: Optional[float] = None
    last_reply_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None
@dataclass
class DashboardInstanceChatsThreadsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceChatsThreadsListOutput:
    items: List[DashboardInstanceChatsThreadsListOutputItems]
    pagination: DashboardInstanceChatsThreadsListOutputPagination


class mapDashboardInstanceChatsThreadsListOutputItemsContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListOutputItemsContextAuthor:
        return DashboardInstanceChatsThreadsListOutputItemsContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListOutputItemsContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsListOutputItemsContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListOutputItemsContextAssignee:
        return DashboardInstanceChatsThreadsListOutputItemsContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListOutputItemsContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsListOutputItemsContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListOutputItemsContext:
        return DashboardInstanceChatsThreadsListOutputItemsContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapDashboardInstanceChatsThreadsListOutputItemsContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapDashboardInstanceChatsThreadsListOutputItemsContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListOutputItemsContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListOutputItems:
        return DashboardInstanceChatsThreadsListOutputItems(
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
        context=mapDashboardInstanceChatsThreadsListOutputItemsContext.from_dict(data.get('context')) if data.get('context') else None,
        reply_count=data.get('reply_count'),
        last_reply_at=datetime.fromisoformat(data.get('last_reply_at').replace('Z', '+00:00')) if data.get('last_reply_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListOutputPagination:
        return DashboardInstanceChatsThreadsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListOutput:
        return DashboardInstanceChatsThreadsListOutput(
        items=[mapDashboardInstanceChatsThreadsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceChatsThreadsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsThreadsListQuery:
    channel_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None


class mapDashboardInstanceChatsThreadsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsListQuery:
        return DashboardInstanceChatsThreadsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        channel_id=data.get('channel_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

