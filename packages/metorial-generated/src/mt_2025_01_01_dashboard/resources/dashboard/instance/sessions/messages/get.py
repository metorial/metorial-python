from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsMessagesGetOutputSender:
    object: str
    type: str
    id: str
@dataclass
class DashboardInstanceSessionsMessagesGetOutputMcpMessage:
    object: str
    id: str
    method: str
    payload: Dict[str, Any]
    original_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutput:
    object: str
    id: str
    type: str
    sender: DashboardInstanceSessionsMessagesGetOutputSender
    mcp_message: DashboardInstanceSessionsMessagesGetOutputMcpMessage
    session_id: str
    server_session_id: str
    created_at: datetime


class mapDashboardInstanceSessionsMessagesGetOutputSender:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputSender:
        return DashboardInstanceSessionsMessagesGetOutputSender(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputSender, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputMcpMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputMcpMessage:
        return DashboardInstanceSessionsMessagesGetOutputMcpMessage(
        object=data.get('object'),
        id=data.get('id'),
        original_id=data.get('original_id'),
        method=data.get('method'),
        payload=data.get('payload')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputMcpMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutput:
        return DashboardInstanceSessionsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        sender=mapDashboardInstanceSessionsMessagesGetOutputSender.from_dict(data.get('sender')) if data.get('sender') else None,
        mcp_message=mapDashboardInstanceSessionsMessagesGetOutputMcpMessage.from_dict(data.get('mcp_message')) if data.get('mcp_message') else None,
        session_id=data.get('session_id'),
        server_session_id=data.get('server_session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

