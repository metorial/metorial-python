from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors:
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
class DashboardInstanceChatsMessagesReactionsCreateOutputReactions:
    emoji: Dict[str, Any]
    count: float
    authors: Optional[List[DashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors]] = None
@dataclass
class DashboardInstanceChatsMessagesReactionsCreateOutput:
    object: str
    reactions: List[DashboardInstanceChatsMessagesReactionsCreateOutputReactions]


class mapDashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors:
        return DashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors(
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
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsMessagesReactionsCreateOutputReactions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsCreateOutputReactions:
        return DashboardInstanceChatsMessagesReactionsCreateOutputReactions(
        emoji=data.get('emoji'),
        count=data.get('count'),
        authors=[mapDashboardInstanceChatsMessagesReactionsCreateOutputReactionsAuthors.from_dict(item) for item in data.get('authors', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsCreateOutputReactions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceChatsMessagesReactionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsCreateOutput:
        return DashboardInstanceChatsMessagesReactionsCreateOutput(
        object=data.get('object'),
        reactions=[mapDashboardInstanceChatsMessagesReactionsCreateOutputReactions.from_dict(item) for item in data.get('reactions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsMessagesReactionsCreateBody:
    channel_id: str
    emoji: Union[str, Dict[str, Any]]


class mapDashboardInstanceChatsMessagesReactionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsMessagesReactionsCreateBody:
        return DashboardInstanceChatsMessagesReactionsCreateBody(
        channel_id=data.get('channel_id'),
        emoji=data.get('emoji')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsMessagesReactionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

