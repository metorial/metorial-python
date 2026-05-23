from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsEventsGetOutputConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsEventsGetOutputConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class SessionsEventsGetOutputConnectionParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsGetOutputConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsGetOutputConnectionParticipantData
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
class SessionsEventsGetOutputConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: SessionsEventsGetOutputConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    mcp: Optional[SessionsEventsGetOutputConnectionMcp] = None
    participant: Optional[SessionsEventsGetOutputConnectionParticipant] = None
    last_active_at: Optional[datetime] = None
@dataclass
class SessionsEventsGetOutputProviderRun:
    object: str
    id: str
    status: str
    session_id: str
    session_provider_id: str
    provider_id: str
    connection_id: str
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
@dataclass
class SessionsEventsGetOutputMessageHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class SessionsEventsGetOutputMessageTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class SessionsEventsGetOutputMessageTransportToolCall:
    object: str
    id: str
@dataclass
class SessionsEventsGetOutputMessageTransport:
    object: str
    type: str
    mcp: Optional[SessionsEventsGetOutputMessageTransportMcp] = None
    tool_call: Optional[SessionsEventsGetOutputMessageTransportToolCall] = None
@dataclass
class SessionsEventsGetOutputMessageToolCallSenderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsGetOutputMessageToolCallSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsGetOutputMessageToolCallSenderParticipantData
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
class SessionsEventsGetOutputMessageToolCallResponderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsGetOutputMessageToolCallResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsGetOutputMessageToolCallResponderParticipantData
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
class SessionsEventsGetOutputMessageToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsEventsGetOutputMessageToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsEventsGetOutputMessageToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class SessionsEventsGetOutputMessageToolCallTool:
    object: str
    id: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    constraints: List[str]
    instructions: List[str]
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[SessionsEventsGetOutputMessageToolCallToolInputSchema] = None
    output_schema: Optional[SessionsEventsGetOutputMessageToolCallToolOutputSchema] = None
    tags: Optional[SessionsEventsGetOutputMessageToolCallToolTags] = None
@dataclass
class SessionsEventsGetOutputMessageToolCallError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    status: str
    session_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
    group_id: Optional[str] = None
@dataclass
class SessionsEventsGetOutputMessageToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: SessionsEventsGetOutputMessageToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[SessionsEventsGetOutputMessageToolCallSenderParticipant] = None
    responder_participant: Optional[SessionsEventsGetOutputMessageToolCallResponderParticipant] = None
    error: Optional[SessionsEventsGetOutputMessageToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class SessionsEventsGetOutputMessageSenderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsGetOutputMessageSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsGetOutputMessageSenderParticipantData
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
class SessionsEventsGetOutputMessageResponderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsGetOutputMessageResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsGetOutputMessageResponderParticipantData
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
class SessionsEventsGetOutputMessageError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    status: str
    session_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
    group_id: Optional[str] = None
@dataclass
class SessionsEventsGetOutputMessage:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: SessionsEventsGetOutputMessageHierarchy
    transport: SessionsEventsGetOutputMessageTransport
    sender_participant: SessionsEventsGetOutputMessageSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[SessionsEventsGetOutputMessageToolCall] = None
    responder_participant: Optional[SessionsEventsGetOutputMessageResponderParticipant] = None
    error: Optional[SessionsEventsGetOutputMessageError] = None
@dataclass
class SessionsEventsGetOutputError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    status: str
    session_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
    group_id: Optional[str] = None
@dataclass
class SessionsEventsGetOutputWarning:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    created_at: datetime
    connection_id: Optional[str] = None
@dataclass
class SessionsEventsGetOutput:
    object: str
    id: str
    type: str
    session_id: str
    created_at: datetime
    connection: Optional[SessionsEventsGetOutputConnection] = None
    provider_run: Optional[SessionsEventsGetOutputProviderRun] = None
    message: Optional[SessionsEventsGetOutputMessage] = None
    error: Optional[SessionsEventsGetOutputError] = None
    warning: Optional[SessionsEventsGetOutputWarning] = None


class mapSessionsEventsGetOutputConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputConnectionUsage:
        return SessionsEventsGetOutputConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputConnectionMcp:
        return SessionsEventsGetOutputConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputConnectionParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputConnectionParticipantData:
        return SessionsEventsGetOutputConnectionParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputConnectionParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputConnectionParticipant:
        return SessionsEventsGetOutputConnectionParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsGetOutputConnectionParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsGetOutputConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputConnection:
        return SessionsEventsGetOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapSessionsEventsGetOutputConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapSessionsEventsGetOutputConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapSessionsEventsGetOutputConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputProviderRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputProviderRun:
        return SessionsEventsGetOutputProviderRun(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_id=data.get('provider_id'),
        connection_id=data.get('connection_id'),
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputProviderRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageHierarchy:
        return SessionsEventsGetOutputMessageHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageTransportMcp:
        return SessionsEventsGetOutputMessageTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageTransportToolCall:
        return SessionsEventsGetOutputMessageTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageTransport:
        return SessionsEventsGetOutputMessageTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapSessionsEventsGetOutputMessageTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapSessionsEventsGetOutputMessageTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallSenderParticipantData:
        return SessionsEventsGetOutputMessageToolCallSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallSenderParticipant:
        return SessionsEventsGetOutputMessageToolCallSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsGetOutputMessageToolCallSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallResponderParticipantData:
        return SessionsEventsGetOutputMessageToolCallResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallResponderParticipant:
        return SessionsEventsGetOutputMessageToolCallResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsGetOutputMessageToolCallResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallToolInputSchema:
        return SessionsEventsGetOutputMessageToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallToolOutputSchema:
        return SessionsEventsGetOutputMessageToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallToolTags:
        return SessionsEventsGetOutputMessageToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallTool:
        return SessionsEventsGetOutputMessageToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapSessionsEventsGetOutputMessageToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapSessionsEventsGetOutputMessageToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapSessionsEventsGetOutputMessageToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCallError:
        return SessionsEventsGetOutputMessageToolCallError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageToolCall:
        return SessionsEventsGetOutputMessageToolCall(
        object=data.get('object'),
        id=data.get('id'),
        tool_key=data.get('tool_key'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        transport=data.get('transport'),
        session_id=data.get('session_id'),
        message_id=data.get('message_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        sender_participant=mapSessionsEventsGetOutputMessageToolCallSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsEventsGetOutputMessageToolCallResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapSessionsEventsGetOutputMessageToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapSessionsEventsGetOutputMessageToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageSenderParticipantData:
        return SessionsEventsGetOutputMessageSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageSenderParticipant:
        return SessionsEventsGetOutputMessageSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsGetOutputMessageSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsGetOutputMessageSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageResponderParticipantData:
        return SessionsEventsGetOutputMessageResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageResponderParticipant:
        return SessionsEventsGetOutputMessageResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsGetOutputMessageResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsGetOutputMessageResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessageError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessageError:
        return SessionsEventsGetOutputMessageError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessageError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputMessage:
        return SessionsEventsGetOutputMessage(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapSessionsEventsGetOutputMessageHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapSessionsEventsGetOutputMessageTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapSessionsEventsGetOutputMessageToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapSessionsEventsGetOutputMessageSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsEventsGetOutputMessageResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapSessionsEventsGetOutputMessageError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputError:
        return SessionsEventsGetOutputError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutputWarning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutputWarning:
        return SessionsEventsGetOutputWarning(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        session_id=data.get('session_id'),
        connection_id=data.get('connection_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutputWarning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsGetOutput:
        return SessionsEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        connection=mapSessionsEventsGetOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        provider_run=mapSessionsEventsGetOutputProviderRun.from_dict(data.get('provider_run')) if data.get('provider_run') else None,
        message=mapSessionsEventsGetOutputMessage.from_dict(data.get('message')) if data.get('message') else None,
        error=mapSessionsEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        warning=mapSessionsEventsGetOutputWarning.from_dict(data.get('warning')) if data.get('warning') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

