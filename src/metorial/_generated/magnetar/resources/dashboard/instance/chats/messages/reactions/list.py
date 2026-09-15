from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors:
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
class DashboardInstanceChatsMessagesReactionsListOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[DashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors]] = None
@dataclass
class DashboardInstanceChatsMessagesReactionsListOutput:
    object: str
    reactions: List[DashboardInstanceChatsMessagesReactionsListOutputReactions]


class mapDashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors:
        return DashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors(
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
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsMessagesReactionsListOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsListOutputReactions:
        return DashboardInstanceChatsMessagesReactionsListOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapDashboardInstanceChatsMessagesReactionsListOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsListOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsMessagesReactionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsListOutput:
        return DashboardInstanceChatsMessagesReactionsListOutput(
        object=data.get('object'),
        reactions=[mapDashboardInstanceChatsMessagesReactionsListOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsMessagesReactionsListQuery:
    channel_id: str


class mapDashboardInstanceChatsMessagesReactionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsListQuery:
        return DashboardInstanceChatsMessagesReactionsListQuery(
        channel_id=data.get('channel_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

