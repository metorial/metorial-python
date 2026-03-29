from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsConnectionsGetOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceSessionsConnectionsGetOutputParticipantData
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutput:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: DashboardInstanceSessionsConnectionsGetOutputUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    mcp: Optional[DashboardInstanceSessionsConnectionsGetOutputMcp] = None
    participant: Optional[DashboardInstanceSessionsConnectionsGetOutputParticipant] = None
    last_active_at: Optional[datetime] = None


class mapDashboardInstanceSessionsConnectionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputUsage:
        return DashboardInstanceSessionsConnectionsGetOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputMcp:
        return DashboardInstanceSessionsConnectionsGetOutputMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputParticipantData:
        return DashboardInstanceSessionsConnectionsGetOutputParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputParticipant:
        return DashboardInstanceSessionsConnectionsGetOutputParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceSessionsConnectionsGetOutputParticipantData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutput:
        return DashboardInstanceSessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapDashboardInstanceSessionsConnectionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapDashboardInstanceSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapDashboardInstanceSessionsConnectionsGetOutputParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

