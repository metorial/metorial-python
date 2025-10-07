from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsSender:
    object: str
    type: str
    id: str
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsMcpMessage:
    object: str
    id: str
    method: str
    payload: Dict[str, Any]
    original_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItems:
    object: str
    id: str
    type: str
    sender: ManagementInstanceSessionsMessagesListOutputItemsSender
    mcp_message: ManagementInstanceSessionsMessagesListOutputItemsMcpMessage
    session_id: str
    server_session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceSessionsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsMessagesListOutput:
    items: List[ManagementInstanceSessionsMessagesListOutputItems]
    pagination: ManagementInstanceSessionsMessagesListOutputPagination


class mapManagementInstanceSessionsMessagesListOutputItemsSender:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsSender:
        return ManagementInstanceSessionsMessagesListOutputItemsSender(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsSender, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsMcpMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsMcpMessage:
        return ManagementInstanceSessionsMessagesListOutputItemsMcpMessage(
        object=data.get('object'),
        id=data.get('id'),
        original_id=data.get('original_id'),
        method=data.get('method'),
        payload=data.get('payload')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsMcpMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItems:
        return ManagementInstanceSessionsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        sender=mapManagementInstanceSessionsMessagesListOutputItemsSender.from_dict(data.get('sender')) if data.get('sender') else None,
        mcp_message=mapManagementInstanceSessionsMessagesListOutputItemsMcpMessage.from_dict(data.get('mcp_message')) if data.get('mcp_message') else None,
        session_id=data.get('session_id'),
        server_session_id=data.get('server_session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputPagination:
        return ManagementInstanceSessionsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutput:
        return ManagementInstanceSessionsMessagesListOutput(
        items=[mapManagementInstanceSessionsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsMessagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_run_id: Optional[Union[str, List[str]]] = None
    server_session_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSessionsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListQuery:
        return ManagementInstanceSessionsMessagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_run_id=data.get('server_run_id'),
        server_session_id=data.get('server_session_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

