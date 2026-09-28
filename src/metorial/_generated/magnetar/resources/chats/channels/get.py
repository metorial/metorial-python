from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsChannelsGetOutputRecipient:
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
class ChatsChannelsGetOutputContextAuthor:
    id: str
    name: str
@dataclass
class ChatsChannelsGetOutputContextAssignee:
    id: str
    name: str
@dataclass
class ChatsChannelsGetOutputContext:
    type: str
    id: str
    description: Optional[str] = None
    status: Optional[str] = None
    url: Optional[str] = None
    author: Optional[ChatsChannelsGetOutputContextAuthor] = None
    assignee: Optional[ChatsChannelsGetOutputContextAssignee] = None
    labels: Optional[List[str]] = None
@dataclass
class ChatsChannelsGetOutput:
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
    recipient: Optional[ChatsChannelsGetOutputRecipient] = None
    member_count: Optional[float] = None
    permalink: Optional[str] = None
    context: Optional[ChatsChannelsGetOutputContext] = None
    last_interaction_at: Optional[datetime] = None


class mapChatsChannelsGetOutputRecipient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsGetOutputRecipient:
        return ChatsChannelsGetOutputRecipient(
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
    def to_dict(value: Union[ChatsChannelsGetOutputRecipient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsGetOutputContextAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsGetOutputContextAuthor:
        return ChatsChannelsGetOutputContextAuthor(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsGetOutputContextAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsGetOutputContextAssignee:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsGetOutputContextAssignee:
        return ChatsChannelsGetOutputContextAssignee(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsGetOutputContextAssignee, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsGetOutputContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsGetOutputContext:
        return ChatsChannelsGetOutputContext(
        type=data.get('type'),
        id=data.get('id'),
        description=data.get('description'),
        status=data.get('status'),
        url=data.get('url'),
        author=mapChatsChannelsGetOutputContextAuthor.from_dict(data.get('author')) if data.get('author') else None,
        assignee=mapChatsChannelsGetOutputContextAssignee.from_dict(data.get('assignee')) if data.get('assignee') else None,
        labels=data.get('labels', [])
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsGetOutputContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsChannelsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsGetOutput:
        return ChatsChannelsGetOutput(
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
        recipient=mapChatsChannelsGetOutputRecipient.from_dict(data.get('recipient')) if data.get('recipient') else None,
        member_count=data.get('member_count'),
        permalink=data.get('permalink'),
        context=mapChatsChannelsGetOutputContext.from_dict(data.get('context')) if data.get('context') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

