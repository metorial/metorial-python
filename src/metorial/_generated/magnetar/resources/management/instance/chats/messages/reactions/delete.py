from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors:
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
class ManagementInstanceChatsMessagesReactionsDeleteOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors]] = None
@dataclass
class ManagementInstanceChatsMessagesReactionsDeleteOutput:
    object: str
    reactions: List[ManagementInstanceChatsMessagesReactionsDeleteOutputReactions]


class mapManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors:
        return ManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors(
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
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsMessagesReactionsDeleteOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsDeleteOutputReactions:
        return ManagementInstanceChatsMessagesReactionsDeleteOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapManagementInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsDeleteOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsMessagesReactionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsDeleteOutput:
        return ManagementInstanceChatsMessagesReactionsDeleteOutput(
        object=data.get('object'),
        reactions=[mapManagementInstanceChatsMessagesReactionsDeleteOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatsMessagesReactionsDeleteQuery:
    channel_id: str
    emoji: str


class mapManagementInstanceChatsMessagesReactionsDeleteQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsDeleteQuery:
        return ManagementInstanceChatsMessagesReactionsDeleteQuery(
        channel_id=data.get('channel_id'),
        emoji=data.get('emoji')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsDeleteQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

