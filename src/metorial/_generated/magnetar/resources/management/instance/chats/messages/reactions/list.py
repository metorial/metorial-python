from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors:
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
class ManagementInstanceChatsMessagesReactionsListOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[ManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors]] = None
@dataclass
class ManagementInstanceChatsMessagesReactionsListOutput:
    object: str
    reactions: List[ManagementInstanceChatsMessagesReactionsListOutputReactions]


class mapManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors:
        return ManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors(
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
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsMessagesReactionsListOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsListOutputReactions:
        return ManagementInstanceChatsMessagesReactionsListOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapManagementInstanceChatsMessagesReactionsListOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsListOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceChatsMessagesReactionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsListOutput:
        return ManagementInstanceChatsMessagesReactionsListOutput(
        object=data.get('object'),
        reactions=[mapManagementInstanceChatsMessagesReactionsListOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatsMessagesReactionsListQuery:
    channel_id: str


class mapManagementInstanceChatsMessagesReactionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsMessagesReactionsListQuery:
        return ManagementInstanceChatsMessagesReactionsListQuery(
        channel_id=data.get('channel_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsMessagesReactionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

