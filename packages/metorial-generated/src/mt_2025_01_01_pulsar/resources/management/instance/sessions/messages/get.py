from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsMessagesGetOutputSender:
    object: str
    type: str
    id: str
@dataclass
class ManagementInstanceSessionsMessagesGetOutputMcpMessage:
    object: str
    id: str
    method: str
    payload: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsMessagesGetOutput:
    object: str
    id: str
    type: str
    sender: ManagementInstanceSessionsMessagesGetOutputSender
    mcp_message: ManagementInstanceSessionsMessagesGetOutputMcpMessage
    session_id: str
    server_session_id: str
    created_at: datetime


class mapManagementInstanceSessionsMessagesGetOutputSender:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputSender:
        return ManagementInstanceSessionsMessagesGetOutputSender(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputSender, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputMcpMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputMcpMessage:
        return ManagementInstanceSessionsMessagesGetOutputMcpMessage(
        object=data.get('object'),
        id=data.get('id'),
        method=data.get('method'),
        payload=data.get('payload')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputMcpMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutput:
        return ManagementInstanceSessionsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        sender=mapManagementInstanceSessionsMessagesGetOutputSender.from_dict(data.get('sender')) if data.get('sender') else None,
        mcp_message=mapManagementInstanceSessionsMessagesGetOutputMcpMessage.from_dict(data.get('mcp_message')) if data.get('mcp_message') else None,
        session_id=data.get('session_id'),
        server_session_id=data.get('server_session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

