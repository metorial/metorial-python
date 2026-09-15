from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsThreadsGetOutputContextAuthor:
    id: str
    name: str
@dataclass
class ChatsThreadsGetOutputContextAssignee:
    id: str
    name: str
@dataclass
class ChatsThreadsGetOutputContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[ChatsThreadsGetOutputContextAuthor] = None
    assignee: Optional[ChatsThreadsGetOutputContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class ChatsThreadsGetOutput:
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
    context: Optional[ChatsThreadsGetOutputContext] = None
    reply_count: Optional[float] = None
    last_reply_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None


class mapChatsThreadsGetOutputContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsThreadsGetOutputContextAuthor:
        return ChatsThreadsGetOutputContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ChatsThreadsGetOutputContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsThreadsGetOutputContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsThreadsGetOutputContextAssignee:
        return ChatsThreadsGetOutputContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ChatsThreadsGetOutputContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsThreadsGetOutputContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsThreadsGetOutputContext:
        return ChatsThreadsGetOutputContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapChatsThreadsGetOutputContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapChatsThreadsGetOutputContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[ChatsThreadsGetOutputContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsThreadsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsThreadsGetOutput:
        return ChatsThreadsGetOutput(
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
        context=mapChatsThreadsGetOutputContext.from_dict(data.get('context')) if data.get('context') else None,
        reply_count=data.get('reply_count'),
        last_reply_at=datetime.fromisoformat(data.get('last_reply_at').replace('Z', '+00:00')) if data.get('last_reply_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsThreadsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsThreadsGetQuery:
    channel_id: str


class mapChatsThreadsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsThreadsGetQuery:
        return ChatsThreadsGetQuery(
        channel_id=data.get('channel_id')
        )

    @staticmethod
    def to_dict(value: Union[ChatsThreadsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

