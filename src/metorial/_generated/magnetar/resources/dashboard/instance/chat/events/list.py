from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatEventsListOutputItems:
    object: str
    id: str
    type: str
    source: str
    chat_id: str
    occurred_at: datetime
    created_at: datetime
    channel_id: Optional[str] = None
    thread_id: Optional[str] = None
    message_id: Optional[str] = None
    author_id: Optional[str] = None
    provider_event_id: Optional[str] = None
    provider_channel_id: Optional[str] = None
    provider_thread_id: Optional[str] = None
    provider_message_id: Optional[str] = None
    provider_author_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceChatEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceChatEventsListOutput:
    items: List[DashboardInstanceChatEventsListOutputItems]
    pagination: DashboardInstanceChatEventsListOutputPagination


class mapDashboardInstanceChatEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatEventsListOutputItems:
        return DashboardInstanceChatEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source=data.get('source'),
        chat_id=data.get('chat_id'),
        channel_id=data.get('channel_id'),
        thread_id=data.get('thread_id'),
        message_id=data.get('message_id'),
        author_id=data.get('author_id'),
        provider_event_id=data.get('provider_event_id'),
        provider_channel_id=data.get('provider_channel_id'),
        provider_thread_id=data.get('provider_thread_id'),
        provider_message_id=data.get('provider_message_id'),
        provider_author_id=data.get('provider_author_id'),
        payload=data.get('payload'),
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatEventsListOutputPagination:
        return DashboardInstanceChatEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatEventsListOutput:
        return DashboardInstanceChatEventsListOutput(
        items=[mapDashboardInstanceChatEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceChatEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatEventsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceChatEventsListQueryOccurredAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceChatEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    chat_id: Optional[Union[str, List[str]]] = None
    chat_connection_id: Optional[Union[str, List[str]]] = None
    chat_instance_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceChatEventsListQueryCreatedAt] = None
    occurred_at: Optional[DashboardInstanceChatEventsListQueryOccurredAt] = None


class mapDashboardInstanceChatEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatEventsListQuery:
        return DashboardInstanceChatEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        chat_id=data.get('chat_id'),
        chat_connection_id=data.get('chat_connection_id'),
        chat_instance_id=data.get('chat_instance_id'),
        type=data.get('type'),
        created_at=mapDashboardInstanceChatEventsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        occurred_at=mapDashboardInstanceChatEventsListQueryOccurredAt.from_dict(data.get('occurred_at')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

