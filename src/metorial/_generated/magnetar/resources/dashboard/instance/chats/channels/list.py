from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsChannelsListOutputItemsRecipient:
    object: str
    id: str
    chat_id: str
    type: str
    role: str
    provider_type: str
    provider_author_id: str
    user_name: str
    full_name: str
    is_self: bool
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    image_url: Optional[str] = None
    last_interaction_at: Optional[datetime] = None
@dataclass
class DashboardInstanceChatsChannelsListOutputItemsContextAuthor:
    id: str
    name: str
@dataclass
class DashboardInstanceChatsChannelsListOutputItemsContextAssignee:
    id: str
    name: str
@dataclass
class DashboardInstanceChatsChannelsListOutputItemsContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[DashboardInstanceChatsChannelsListOutputItemsContextAuthor] = None
    assignee: Optional[DashboardInstanceChatsChannelsListOutputItemsContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class DashboardInstanceChatsChannelsListOutputItems:
    object: str
    id: str
    chat_id: str
    type: str
    provider_type: str
    provider_channel_id: str
    has_access: bool
    created_at: datetime
    updated_at: datetime
    workspace_id: Optional[str] = None
    name: Optional[str] = None
    topic: Optional[str] = None
    subject: Optional[str] = None
    recipient: Optional[DashboardInstanceChatsChannelsListOutputItemsRecipient] = None
    member_count: Optional[float] = None
    permalink: Optional[str] = None
    context: Optional[DashboardInstanceChatsChannelsListOutputItemsContext] = None
    last_interaction_at: Optional[datetime] = None
@dataclass
class DashboardInstanceChatsChannelsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceChatsChannelsListOutput:
    items: List[DashboardInstanceChatsChannelsListOutputItems]
    pagination: DashboardInstanceChatsChannelsListOutputPagination


class mapDashboardInstanceChatsChannelsListOutputItemsRecipient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutputItemsRecipient:
        return DashboardInstanceChatsChannelsListOutputItemsRecipient(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        type=data.get('type'),
        role=data.get('role'),
        provider_type=data.get('provider_type'),
        provider_author_id=data.get('provider_author_id'),
        user_name=data.get('user_name'),
        full_name=data.get('full_name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        is_self=data.get('is_self'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutputItemsRecipient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsChannelsListOutputItemsContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutputItemsContextAuthor:
        return DashboardInstanceChatsChannelsListOutputItemsContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutputItemsContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsChannelsListOutputItemsContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutputItemsContextAssignee:
        return DashboardInstanceChatsChannelsListOutputItemsContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutputItemsContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsChannelsListOutputItemsContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutputItemsContext:
        return DashboardInstanceChatsChannelsListOutputItemsContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapDashboardInstanceChatsChannelsListOutputItemsContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapDashboardInstanceChatsChannelsListOutputItemsContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutputItemsContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsChannelsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutputItems:
        return DashboardInstanceChatsChannelsListOutputItems(
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
        has_access=data.get('has_access'),
        recipient=mapDashboardInstanceChatsChannelsListOutputItemsRecipient.from_dict(data.get('recipient')) if data.get('recipient') else None,
        member_count=data.get('member_count'),
        permalink=data.get('permalink'),
        context=mapDashboardInstanceChatsChannelsListOutputItemsContext.from_dict(data.get('context')) if data.get('context') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsChannelsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutputPagination:
        return DashboardInstanceChatsChannelsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsChannelsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListOutput:
        return DashboardInstanceChatsChannelsListOutput(
        items=[mapDashboardInstanceChatsChannelsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceChatsChannelsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsChannelsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    workspace_id: Optional[str] = None
    type: Optional[str] = None
    search: Optional[str] = None
    has_access: Optional[bool] = None


class mapDashboardInstanceChatsChannelsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsListQuery:
        return DashboardInstanceChatsChannelsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        workspace_id=data.get('workspace_id'),
        type=data.get('type'),
        search=data.get('search'),
        has_access=data.get('has_access')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

