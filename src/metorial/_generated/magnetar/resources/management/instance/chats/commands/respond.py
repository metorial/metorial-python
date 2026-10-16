from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatsCommandsRespondOutputMessageAuthor:
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
class ManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors:
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
class ManagementInstanceChatsCommandsRespondOutputMessageReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors]] = None
@dataclass
class ManagementInstanceChatsCommandsRespondOutputMessageUnfurls:
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    site_name: Optional[str] = None
    message_id: Optional[str] = None
@dataclass
class ManagementInstanceChatsCommandsRespondOutputMessageAttachments:
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
class ManagementInstanceChatsCommandsRespondOutputMessage:
    object: str
    id: str
    chat_id: str
    channel_id: str
    provider_type: str
    provider_message_id: str
    attachments: List[ManagementInstanceChatsCommandsRespondOutputMessageAttachments]
    sent_at: datetime
    edited: bool
    created_at: datetime
    updated_at: datetime
    thread_id: Optional[str] = None
    provider_reply_to_message_id: Optional[str] = None
    author: Optional[ManagementInstanceChatsCommandsRespondOutputMessageAuthor] = None
    body: Optional[Dict[str, Any]] = None
    reactions: Optional[List[ManagementInstanceChatsCommandsRespondOutputMessageReactions]] = None
    unfurls: Optional[List[ManagementInstanceChatsCommandsRespondOutputMessageUnfurls]] = None
    edited_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementInstanceChatsCommandsRespondOutput:
    object: str
    message: Optional[ManagementInstanceChatsCommandsRespondOutputMessage] = None


class mapManagementInstanceChatsCommandsRespondOutputMessageAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutputMessageAuthor:
        return ManagementInstanceChatsCommandsRespondOutputMessageAuthor(
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
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutputMessageAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors:
        return ManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors(
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
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsCommandsRespondOutputMessageReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutputMessageReactions:
        return ManagementInstanceChatsCommandsRespondOutputMessageReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapManagementInstanceChatsCommandsRespondOutputMessageReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutputMessageReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsCommandsRespondOutputMessageUnfurls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutputMessageUnfurls:
        return ManagementInstanceChatsCommandsRespondOutputMessageUnfurls(
        url=data.get('url'),
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('imageUrl'),
        site_name=data.get('siteName'),
        message_id=data.get('messageId')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutputMessageUnfurls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsCommandsRespondOutputMessageAttachments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutputMessageAttachments:
        return ManagementInstanceChatsCommandsRespondOutputMessageAttachments(
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
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutputMessageAttachments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsCommandsRespondOutputMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutputMessage:
        return ManagementInstanceChatsCommandsRespondOutputMessage(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        channel_id=data.get('channel_id'),
        thread_id=data.get('thread_id'),
        provider_type=data.get('provider_type'),
        provider_message_id=data.get('provider_message_id'),
        provider_reply_to_message_id=data.get('provider_reply_to_message_id'),
        author=mapManagementInstanceChatsCommandsRespondOutputMessageAuthor.from_dict(data.get('author')) if data.get('author') else None,
        body=data.get('body'),
        reactions=[mapManagementInstanceChatsCommandsRespondOutputMessageReactions.from_dict(item) for item in data.get('reactions', []) if item],
        unfurls=[mapManagementInstanceChatsCommandsRespondOutputMessageUnfurls.from_dict(item) for item in data.get('unfurls', []) if item],
        attachments=[mapManagementInstanceChatsCommandsRespondOutputMessageAttachments.from_dict(item) for item in data.get('attachments', []) if item],
        sent_at=datetime.fromisoformat(data.get('sent_at').replace('Z', '+00:00')) if data.get('sent_at') else None,
        edited=data.get('edited'),
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutputMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsCommandsRespondOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondOutput:
        return ManagementInstanceChatsCommandsRespondOutput(
        object=data.get('object'),
        message=mapManagementInstanceChatsCommandsRespondOutputMessage.from_dict(data.get('message')) if data.get('message') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatsCommandsRespondBody:
    chat_event_id: str
    parts: List[Dict[str, Any]]
    alt_text: Optional[str] = None
    ephemeral: Optional[bool] = None


class mapManagementInstanceChatsCommandsRespondBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsCommandsRespondBody:
        return ManagementInstanceChatsCommandsRespondBody(
        chat_event_id=data.get('chat_event_id'),
        parts=data.get('parts', []),
        alt_text=data.get('alt_text'),
        ephemeral=data.get('ephemeral')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsCommandsRespondBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

