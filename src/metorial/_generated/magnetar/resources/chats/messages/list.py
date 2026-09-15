from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsMessagesListOutputItemsAuthor:
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
class ChatsMessagesListOutputItemsReactionsAuthors:
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
class ChatsMessagesListOutputItemsReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ChatsMessagesListOutputItemsReactionsAuthors]] = None
@dataclass
class ChatsMessagesListOutputItemsUnfurls:
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    site_name: Optional[str] = None
    message_id: Optional[str] = None
@dataclass
class ChatsMessagesListOutputItemsAttachments:
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
class ChatsMessagesListOutputItems:
    object: str
    id: str
    chat_id: str
    channel_id: str
    provider_type: str
    provider_message_id: str
    attachments: List[ChatsMessagesListOutputItemsAttachments]
    sent_at: datetime
    edited: bool
    created_at: datetime
    updated_at: datetime
    thread_id: Optional[str] = None
    provider_reply_to_message_id: Optional[str] = None
    author: Optional[ChatsMessagesListOutputItemsAuthor] = None
    body: Optional[Dict[str, Any]] = None
    reactions: Optional[List[ChatsMessagesListOutputItemsReactions]] = None
    unfurls: Optional[List[ChatsMessagesListOutputItemsUnfurls]] = None
    edited_at: Optional[datetime] = None
    last_interaction_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ChatsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ChatsMessagesListOutput:
    items: List[ChatsMessagesListOutputItems]
    pagination: ChatsMessagesListOutputPagination


class mapChatsMessagesListOutputItemsAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputItemsAuthor:
        return ChatsMessagesListOutputItemsAuthor(
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
    def to_dict(value: Union[ChatsMessagesListOutputItemsAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutputItemsReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputItemsReactionsAuthors:
        return ChatsMessagesListOutputItemsReactionsAuthors(
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
    def to_dict(value: Union[ChatsMessagesListOutputItemsReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutputItemsReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputItemsReactions:
        return ChatsMessagesListOutputItemsReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapChatsMessagesListOutputItemsReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesListOutputItemsReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutputItemsUnfurls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputItemsUnfurls:
        return ChatsMessagesListOutputItemsUnfurls(
        url=data.get('url'),
        title=data.get('title'),
        description=data.get('description'),
        image_url=data.get('imageUrl'),
        site_name=data.get('siteName'),
        message_id=data.get('messageId')
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesListOutputItemsUnfurls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutputItemsAttachments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputItemsAttachments:
        return ChatsMessagesListOutputItemsAttachments(
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
    def to_dict(value: Union[ChatsMessagesListOutputItemsAttachments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputItems:
        return ChatsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        channel_id=data.get('channel_id'),
        thread_id=data.get('thread_id'),
        provider_type=data.get('provider_type'),
        provider_message_id=data.get('provider_message_id'),
        provider_reply_to_message_id=data.get('provider_reply_to_message_id'),
        author=mapChatsMessagesListOutputItemsAuthor.from_dict(data.get('author')) if data.get('author') else None,
        body=data.get('body'),
        reactions=[mapChatsMessagesListOutputItemsReactions.from_dict(item) for item in data.get('reactions', []) if item],
        unfurls=[mapChatsMessagesListOutputItemsUnfurls.from_dict(item) for item in data.get('unfurls', []) if item],
        attachments=[mapChatsMessagesListOutputItemsAttachments.from_dict(item) for item in data.get('attachments', []) if item],
        sent_at=datetime.fromisoformat(data.get('sent_at').replace('Z', '+00:00')) if data.get('sent_at') else None,
        edited=data.get('edited'),
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_interaction_at=datetime.fromisoformat(data.get('last_interaction_at').replace('Z', '+00:00')) if data.get('last_interaction_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutputPagination:
        return ChatsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListOutput:
        return ChatsMessagesListOutput(
        items=[mapChatsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapChatsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsMessagesListQuery:
    channel_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    thread_id: Optional[str] = None
    search: Optional[str] = None


class mapChatsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesListQuery:
        return ChatsMessagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        channel_id=data.get('channel_id'),
        thread_id=data.get('thread_id'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

