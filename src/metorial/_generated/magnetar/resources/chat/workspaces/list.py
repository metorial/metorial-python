from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatWorkspacesListOutputItems:
    object: str
    id: str
    chat_id: str
    provider_workspace_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    domain: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ChatWorkspacesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ChatWorkspacesListOutput:
    items: List[ChatWorkspacesListOutputItems]
    pagination: ChatWorkspacesListOutputPagination


class mapChatWorkspacesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatWorkspacesListOutputItems:
        return ChatWorkspacesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        chat_id=data.get('chat_id'),
        provider_workspace_id=data.get('provider_workspace_id'),
        name=data.get('name'),
        domain=data.get('domain'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatWorkspacesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatWorkspacesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatWorkspacesListOutputPagination:
        return ChatWorkspacesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ChatWorkspacesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapChatWorkspacesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatWorkspacesListOutput:
        return ChatWorkspacesListOutput(
        items=[mapChatWorkspacesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapChatWorkspacesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatWorkspacesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatWorkspacesListQuery:
    chat_instance_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None


class mapChatWorkspacesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatWorkspacesListQuery:
        return ChatWorkspacesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        chat_instance_id=data.get('chat_instance_id'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ChatWorkspacesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

