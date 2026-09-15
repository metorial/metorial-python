from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors:
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
class DashboardInstanceChatsMessagesReactionsDeleteOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[DashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors]] = None
@dataclass
class DashboardInstanceChatsMessagesReactionsDeleteOutput:
    object: str
    reactions: List[DashboardInstanceChatsMessagesReactionsDeleteOutputReactions]


class mapDashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors:
        return DashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors(
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
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsMessagesReactionsDeleteOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsDeleteOutputReactions:
        return DashboardInstanceChatsMessagesReactionsDeleteOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapDashboardInstanceChatsMessagesReactionsDeleteOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsDeleteOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsMessagesReactionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsDeleteOutput:
        return DashboardInstanceChatsMessagesReactionsDeleteOutput(
        object=data.get('object'),
        reactions=[mapDashboardInstanceChatsMessagesReactionsDeleteOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsMessagesReactionsDeleteQuery:
    channel_id: str
    emoji: str


class mapDashboardInstanceChatsMessagesReactionsDeleteQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsDeleteQuery:
        return DashboardInstanceChatsMessagesReactionsDeleteQuery(
        channel_id=data.get('channel_id'),
        emoji=data.get('emoji')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsDeleteQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

