from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsMessagesReactionsCreateOutputReactionsAuthors:
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
class ChatsMessagesReactionsCreateOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ChatsMessagesReactionsCreateOutputReactionsAuthors]] = None
@dataclass
class ChatsMessagesReactionsCreateOutput:
    object: str
    reactions: List[ChatsMessagesReactionsCreateOutputReactions]


class mapChatsMessagesReactionsCreateOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsCreateOutputReactionsAuthors:
        return ChatsMessagesReactionsCreateOutputReactionsAuthors(
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
    def to_dict(value: Union[ChatsMessagesReactionsCreateOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesReactionsCreateOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsCreateOutputReactions:
        return ChatsMessagesReactionsCreateOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapChatsMessagesReactionsCreateOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsCreateOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesReactionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsCreateOutput:
        return ChatsMessagesReactionsCreateOutput(
        object=data.get('object'),
        reactions=[mapChatsMessagesReactionsCreateOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsMessagesReactionsCreateBody:
    channel_id: str
    emoji: Union[str, Dict[str, Any]]


class mapChatsMessagesReactionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsCreateBody:
        return ChatsMessagesReactionsCreateBody(
        channel_id=data.get('channel_id'),
        emoji=data.get('emoji')
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

