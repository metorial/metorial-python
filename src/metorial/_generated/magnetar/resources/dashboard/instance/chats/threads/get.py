from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsThreadsGetOutputContextAuthor:
    id: str
    name: str
@dataclass
class DashboardInstanceChatsThreadsGetOutputContextAssignee:
    id: str
    name: str
@dataclass
class DashboardInstanceChatsThreadsGetOutputContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[DashboardInstanceChatsThreadsGetOutputContextAuthor] = None
    assignee: Optional[DashboardInstanceChatsThreadsGetOutputContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class DashboardInstanceChatsThreadsGetOutput:
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
    context: Optional[DashboardInstanceChatsThreadsGetOutputContext] = None
    reply_count: Optional[float] = None
    last_reply_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None


class mapDashboardInstanceChatsThreadsGetOutputContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsGetOutputContextAuthor:
        return DashboardInstanceChatsThreadsGetOutputContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsGetOutputContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsGetOutputContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsGetOutputContextAssignee:
        return DashboardInstanceChatsThreadsGetOutputContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsGetOutputContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsGetOutputContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsGetOutputContext:
        return DashboardInstanceChatsThreadsGetOutputContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapDashboardInstanceChatsThreadsGetOutputContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapDashboardInstanceChatsThreadsGetOutputContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsGetOutputContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsThreadsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsGetOutput:
        return DashboardInstanceChatsThreadsGetOutput(
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
        context=mapDashboardInstanceChatsThreadsGetOutputContext.from_dict(data.get('context')) if data.get('context') else None,
        reply_count=data.get('reply_count'),
        last_reply_at=datetime.fromisoformat(data.get('last_reply_at').replace('Z', '+00:00')) if data.get('last_reply_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsThreadsGetQuery:
    channel_id: str


class mapDashboardInstanceChatsThreadsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsThreadsGetQuery:
        return DashboardInstanceChatsThreadsGetQuery(
        channel_id=data.get('channel_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsThreadsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

