from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsSender:
    object: str
    type: str
    id: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsMcpMessage:
    object: str
    id: str
    method: str
    payload: Dict[str, Any]
    original_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputItems:
    object: str
    id: str
    type: str
    sender: DashboardInstanceSessionsMessagesListOutputItemsSender
    mcp_message: DashboardInstanceSessionsMessagesListOutputItemsMcpMessage
    session_id: str
    server_session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceSessionsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsMessagesListOutput:
    items: List[DashboardInstanceSessionsMessagesListOutputItems]
    pagination: DashboardInstanceSessionsMessagesListOutputPagination


class mapDashboardInstanceSessionsMessagesListOutputItemsSender:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsSender:
        return DashboardInstanceSessionsMessagesListOutputItemsSender(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsSender, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsMcpMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsMcpMessage:
        return DashboardInstanceSessionsMessagesListOutputItemsMcpMessage(
        object=data.get('object'),
        id=data.get('id'),
        original_id=data.get('original_id'),
        method=data.get('method'),
        payload=data.get('payload')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsMcpMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItems:
        return DashboardInstanceSessionsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        sender=mapDashboardInstanceSessionsMessagesListOutputItemsSender.from_dict(data.get('sender')) if data.get('sender') else None,
        mcp_message=mapDashboardInstanceSessionsMessagesListOutputItemsMcpMessage.from_dict(data.get('mcp_message')) if data.get('mcp_message') else None,
        session_id=data.get('session_id'),
        server_session_id=data.get('server_session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputPagination:
        return DashboardInstanceSessionsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutput:
        return DashboardInstanceSessionsMessagesListOutput(
        items=[mapDashboardInstanceSessionsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsMessagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_run_id: Optional[Union[str, List[str]]] = None
    server_session_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSessionsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListQuery:
        return DashboardInstanceSessionsMessagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_run_id=data.get('server_run_id'),
        server_session_id=data.get('server_session_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

