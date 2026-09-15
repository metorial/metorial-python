from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsMessagesReactionsDeleteOutputReactionsAuthors:
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
class ChatsMessagesReactionsDeleteOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ChatsMessagesReactionsDeleteOutputReactionsAuthors]] = None
@dataclass
class ChatsMessagesReactionsDeleteOutput:
    object: str
    reactions: List[ChatsMessagesReactionsDeleteOutputReactions]


class mapChatsMessagesReactionsDeleteOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsDeleteOutputReactionsAuthors:
        return ChatsMessagesReactionsDeleteOutputReactionsAuthors(
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
    def to_dict(value: Union[ChatsMessagesReactionsDeleteOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesReactionsDeleteOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsDeleteOutputReactions:
        return ChatsMessagesReactionsDeleteOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapChatsMessagesReactionsDeleteOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsDeleteOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatsMessagesReactionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsDeleteOutput:
        return ChatsMessagesReactionsDeleteOutput(
        object=data.get('object'),
        reactions=[mapChatsMessagesReactionsDeleteOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsMessagesReactionsDeleteQuery:
    channel_id: str
    emoji: str


class mapChatsMessagesReactionsDeleteQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsMessagesReactionsDeleteQuery:
        return ChatsMessagesReactionsDeleteQuery(
        channel_id=data.get('channel_id'),
        emoji=data.get('emoji')
        )

    @staticmethod
    def to_dict(value: Union[ChatsMessagesReactionsDeleteQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

