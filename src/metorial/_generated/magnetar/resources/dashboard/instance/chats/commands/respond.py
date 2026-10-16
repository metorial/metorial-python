from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsCommandsRespondOutputMessageAuthor:
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
class DashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors:
    user_id: str
    user_name: str
    full_name: str
    type: str
    is_me: bool
    role: Optional[str] = None
    provider_type: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
    raw: Optional[Any] = None
@dataclass
class DashboardInstanceChatsCommandsRespondOutputMessageReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[DashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors]] = None
@dataclass
class DashboardInstanceChatsCommandsRespondOutputMessageUnfurls:
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    site_name: Optional[str] = None
    message_id: Optional[str] = None
@dataclass
class DashboardInstanceChatsCommandsRespondOutputMessageAttachments:
    object: str
    id: str
    type: str
    position: float
    file_id: str
    created_at: datetime
    provider_attachment_id: Optional[str] = None
    name: Optional[str] = None
    mime_type: Optional[str] = None
    size: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None
    download_url: Optional[str] = None
@dataclass
class DashboardInstanceChatsCommandsRespondOutputMessage:
    object: str
    id: str
    chat_id: str
    channel_id: str
    provider_type: str
    provider_message_id: str
    attachments: List[DashboardInstanceChatsCommandsRespondOutputMessageAttachments]
    sent_at: datetime
    edited: bool
    created_at: datetime
    updated_at: datetime
    thread_id: Optional[str] = None
    provider_reply_to_message_id: Optional[str] = None
    author: Optional[DashboardInstanceChatsCommandsRespondOutputMessageAuthor] = None
    body: Optional[Dict[str, Any]] = None
    reactions: Optional[List[DashboardInstanceChatsCommandsRespondOutputMessageReactions]] = None
    unfurls: Optional[List[DashboardInstanceChatsCommandsRespondOutputMessageUnfurls]] = None
    edited_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardInstanceChatsCommandsRespondOutput:
    object: str
    message: Optional[DashboardInstanceChatsCommandsRespondOutputMessage] = None


class mapDashboardInstanceChatsCommandsRespondOutputMessageAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutputMessageAuthor:
        return DashboardInstanceChatsCommandsRespondOutputMessageAuthor(
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
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutputMessageAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors:
        return DashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors(
        user_id=data.get('userId'),
        user_name=data.get('userName'),
        full_name=data.get('fullName'),
        type=data.get('type'),
        role=data.get('role'),
        provider_type=data.get('providerType'),
        is_me=data.get('isMe'),
        email=data.get('email'),
        image_url=data.get('imageUrl'),
        raw=data.get('raw')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsCommandsRespondOutputMessageReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutputMessageReactions:
        return DashboardInstanceChatsCommandsRespondOutputMessageReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapDashboardInstanceChatsCommandsRespondOutputMessageReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutputMessageReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsCommandsRespondOutputMessageUnfurls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutputMessageUnfurls:
        return DashboardInstanceChatsCommandsRespondOutputMessageUnfurls(
        url=data.get('url'),
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('imageUrl'),
        site_name=data.get('siteName'),
        message_id=data.get('messageId')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutputMessageUnfurls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsCommandsRespondOutputMessageAttachments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutputMessageAttachments:
        return DashboardInstanceChatsCommandsRespondOutputMessageAttachments(
        object=data.get('object'),
        id=data.get('id'),
        provider_attachment_id=data.get('provider_attachment_id'),
        type=data.get('type'),
        name=data.get('name'),
        mime_type=data.get('mime_type'),
        size=data.get('size'),
        width=data.get('width'),
        height=data.get('height'),
        position=data.get('position'),
        file_id=data.get('file_id'),
        download_url=data.get('download_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutputMessageAttachments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsCommandsRespondOutputMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutputMessage:
        return DashboardInstanceChatsCommandsRespondOutputMessage(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        channel_id=data.get('channel_id'),
        thread_id=data.get('thread_id'),
        provider_type=data.get('provider_type'),
        provider_message_id=data.get('provider_message_id'),
        provider_reply_to_message_id=data.get('provider_reply_to_message_id'),
        author=mapDashboardInstanceChatsCommandsRespondOutputMessageAuthor.from_dict(data.get('author')) if data.get('author') else None,
        body=data.get('body'),
        reactions=[mapDashboardInstanceChatsCommandsRespondOutputMessageReactions.from_dict(item) for item in data.get('reactions', []) if item],
        unfurls=[mapDashboardInstanceChatsCommandsRespondOutputMessageUnfurls.from_dict(item) for item in data.get('unfurls', []) if item],
        attachments=[mapDashboardInstanceChatsCommandsRespondOutputMessageAttachments.from_dict(item) for item in data.get('attachments', []) if item],
        sent_at=datetime.fromisoformat(data.get('sent_at').replace('Z', '+00:00')) if data.get('sent_at') else None,
        edited=data.get('edited'),
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutputMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsCommandsRespondOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondOutput:
        return DashboardInstanceChatsCommandsRespondOutput(
        object=data.get('object'),
        message=mapDashboardInstanceChatsCommandsRespondOutputMessage.from_dict(data.get('message')) if data.get('message') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsCommandsRespondBody:
    chat_event_id: str
    parts: List[Dict[str, Any]]
    alt_text: Optional[str] = None
    ephemeral: Optional[bool] = None


class mapDashboardInstanceChatsCommandsRespondBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsCommandsRespondBody:
        return DashboardInstanceChatsCommandsRespondBody(
        chat_event_id=data.get('chat_event_id'),
        parts=data.get('parts', []),
        alt_text=data.get('alt_text'),
        ephemeral=data.get('ephemeral')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsCommandsRespondBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

