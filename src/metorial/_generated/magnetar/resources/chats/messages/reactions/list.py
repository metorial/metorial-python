from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsMessagesReactionsListOutputReactionsAuthors:
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
class ChatsMessagesReactionsListOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ChatsMessagesReactionsListOutputReactionsAuthors]] = None
@dataclass
class ChatsMessagesReactionsListOutput:
    object: str
    reactions: List[ChatsMessagesReactionsListOutputReactions]


class mapChatsMessagesReactionsListOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsListOutputReactionsAuthors:
        return ChatsMessagesReactionsListOutputReactionsAuthors(
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
    def to_dict(value: Union[ChatsMessagesReactionsListOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesReactionsListOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsListOutputReactions:
        return ChatsMessagesReactionsListOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapChatsMessagesReactionsListOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsListOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesReactionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsListOutput:
        return ChatsMessagesReactionsListOutput(
        object=data.get('object'),
        reactions=[mapChatsMessagesReactionsListOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsMessagesReactionsListQuery:
    channel_id: str


class mapChatsMessagesReactionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsListQuery:
        return ChatsMessagesReactionsListQuery(
        channel_id=data.get('channel_id')
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

