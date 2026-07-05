from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsConnectionsGetOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsConnectionsGetOutputMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class SessionsConnectionsGetOutputParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsConnectionsGetOutputParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsConnectionsGetOutputParticipantData
    created_at: datetime
    provider_id: Optional[str] = None
    connection_type: Optional[str] = None
    agent_id: Optional[str] = None
    agent_instance_id: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    agent_actor_id: Optional[str] = None
    agent_client_id: Optional[str] = None
    consumer_id: Optional[str] = None
@dataclass
class SessionsConnectionsGetOutput:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: SessionsConnectionsGetOutputUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    mcp: Optional[SessionsConnectionsGetOutputMcp] = None
    participant: Optional[SessionsConnectionsGetOutputParticipant] = None
    last_active_at: Optional[datetime] = None


class mapSessionsConnectionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputUsage:
        return SessionsConnectionsGetOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcp:
        return SessionsConnectionsGetOutputMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutputParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputParticipantData:
        return SessionsConnectionsGetOutputParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutputParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputParticipant:
        return SessionsConnectionsGetOutputParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsConnectionsGetOutputParticipantData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        connection_type=data.get('connection_type'),
        agent_id=data.get('agent_id'),
        agent_instance_id=data.get('agent_instance_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        agent_actor_id=data.get('agent_actor_id'),
        agent_client_id=data.get('agent_client_id'),
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutput:
        return SessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapSessionsConnectionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapSessionsConnectionsGetOutputParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

