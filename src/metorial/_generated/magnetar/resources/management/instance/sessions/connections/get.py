from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsConnectionsGetOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutput:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: ManagementInstanceSessionsConnectionsGetOutputUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    last_active_at: datetime
    mcp: Optional[ManagementInstanceSessionsConnectionsGetOutputMcp] = None
    participant: Optional[ManagementInstanceSessionsConnectionsGetOutputParticipant] = None


class mapManagementInstanceSessionsConnectionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputUsage:
        return ManagementInstanceSessionsConnectionsGetOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputMcp:
        return ManagementInstanceSessionsConnectionsGetOutputMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputParticipant:
        return ManagementInstanceSessionsConnectionsGetOutputParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutput:
        return ManagementInstanceSessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapManagementInstanceSessionsConnectionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapManagementInstanceSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapManagementInstanceSessionsConnectionsGetOutputParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

