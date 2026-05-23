from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsEventsListOutputItemsConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsEventsListOutputItemsConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class SessionsEventsListOutputItemsConnectionParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsListOutputItemsConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsListOutputItemsConnectionParticipantData
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
class SessionsEventsListOutputItemsConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: SessionsEventsListOutputItemsConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    mcp: Optional[SessionsEventsListOutputItemsConnectionMcp] = None
    participant: Optional[SessionsEventsListOutputItemsConnectionParticipant] = None
    last_active_at: Optional[datetime] = None
@dataclass
class SessionsEventsListOutputItemsProviderRun:
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
class SessionsEventsListOutputItemsMessageHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class SessionsEventsListOutputItemsMessageTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class SessionsEventsListOutputItemsMessageTransportToolCall:
    object: str
    id: str
@dataclass
class SessionsEventsListOutputItemsMessageTransport:
    object: str
    type: str
    mcp: Optional[SessionsEventsListOutputItemsMessageTransportMcp] = None
    tool_call: Optional[SessionsEventsListOutputItemsMessageTransportToolCall] = None
@dataclass
class SessionsEventsListOutputItemsMessageToolCallSenderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsListOutputItemsMessageToolCallSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsListOutputItemsMessageToolCallSenderParticipantData
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
class SessionsEventsListOutputItemsMessageToolCallResponderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsListOutputItemsMessageToolCallResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsListOutputItemsMessageToolCallResponderParticipantData
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
class SessionsEventsListOutputItemsMessageToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsEventsListOutputItemsMessageToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class SessionsEventsListOutputItemsMessageToolCallTool:
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
    input_schema: Optional[SessionsEventsListOutputItemsMessageToolCallToolInputSchema] = None
    output_schema: Optional[SessionsEventsListOutputItemsMessageToolCallToolOutputSchema] = None
    tags: Optional[SessionsEventsListOutputItemsMessageToolCallToolTags] = None
@dataclass
class SessionsEventsListOutputItemsMessageToolCallError:
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
class SessionsEventsListOutputItemsMessageToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: SessionsEventsListOutputItemsMessageToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[SessionsEventsListOutputItemsMessageToolCallSenderParticipant] = None
    responder_participant: Optional[SessionsEventsListOutputItemsMessageToolCallResponderParticipant] = None
    error: Optional[SessionsEventsListOutputItemsMessageToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class SessionsEventsListOutputItemsMessageSenderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsListOutputItemsMessageSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsListOutputItemsMessageSenderParticipantData
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
class SessionsEventsListOutputItemsMessageResponderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsEventsListOutputItemsMessageResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsEventsListOutputItemsMessageResponderParticipantData
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
class SessionsEventsListOutputItemsMessageError:
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
class SessionsEventsListOutputItemsMessage:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: SessionsEventsListOutputItemsMessageHierarchy
    transport: SessionsEventsListOutputItemsMessageTransport
    sender_participant: SessionsEventsListOutputItemsMessageSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[SessionsEventsListOutputItemsMessageToolCall] = None
    responder_participant: Optional[SessionsEventsListOutputItemsMessageResponderParticipant] = None
    error: Optional[SessionsEventsListOutputItemsMessageError] = None
@dataclass
class SessionsEventsListOutputItemsError:
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
class SessionsEventsListOutputItemsWarning:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    created_at: datetime
    connection_id: Optional[str] = None
@dataclass
class SessionsEventsListOutputItems:
    object: str
    id: str
    type: str
    session_id: str
    created_at: datetime
    connection: Optional[SessionsEventsListOutputItemsConnection] = None
    provider_run: Optional[SessionsEventsListOutputItemsProviderRun] = None
    message: Optional[SessionsEventsListOutputItemsMessage] = None
    error: Optional[SessionsEventsListOutputItemsError] = None
    warning: Optional[SessionsEventsListOutputItemsWarning] = None
@dataclass
class SessionsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsEventsListOutput:
    items: List[SessionsEventsListOutputItems]
    pagination: SessionsEventsListOutputPagination


class mapSessionsEventsListOutputItemsConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsConnectionUsage:
        return SessionsEventsListOutputItemsConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsConnectionMcp:
        return SessionsEventsListOutputItemsConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsConnectionParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsConnectionParticipantData:
        return SessionsEventsListOutputItemsConnectionParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsConnectionParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsConnectionParticipant:
        return SessionsEventsListOutputItemsConnectionParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsListOutputItemsConnectionParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsListOutputItemsConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsConnection:
        return SessionsEventsListOutputItemsConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapSessionsEventsListOutputItemsConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapSessionsEventsListOutputItemsConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapSessionsEventsListOutputItemsConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsProviderRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsProviderRun:
        return SessionsEventsListOutputItemsProviderRun(
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
    def to_dict(value: Union[SessionsEventsListOutputItemsProviderRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageHierarchy:
        return SessionsEventsListOutputItemsMessageHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageTransportMcp:
        return SessionsEventsListOutputItemsMessageTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageTransportToolCall:
        return SessionsEventsListOutputItemsMessageTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageTransport:
        return SessionsEventsListOutputItemsMessageTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapSessionsEventsListOutputItemsMessageTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapSessionsEventsListOutputItemsMessageTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallSenderParticipantData:
        return SessionsEventsListOutputItemsMessageToolCallSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallSenderParticipant:
        return SessionsEventsListOutputItemsMessageToolCallSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsListOutputItemsMessageToolCallSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallResponderParticipantData:
        return SessionsEventsListOutputItemsMessageToolCallResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallResponderParticipant:
        return SessionsEventsListOutputItemsMessageToolCallResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsListOutputItemsMessageToolCallResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallToolInputSchema:
        return SessionsEventsListOutputItemsMessageToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
        return SessionsEventsListOutputItemsMessageToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallToolTags:
        return SessionsEventsListOutputItemsMessageToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallTool:
        return SessionsEventsListOutputItemsMessageToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapSessionsEventsListOutputItemsMessageToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapSessionsEventsListOutputItemsMessageToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapSessionsEventsListOutputItemsMessageToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCallError:
        return SessionsEventsListOutputItemsMessageToolCallError(
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
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageToolCall:
        return SessionsEventsListOutputItemsMessageToolCall(
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
        sender_participant=mapSessionsEventsListOutputItemsMessageToolCallSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsEventsListOutputItemsMessageToolCallResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapSessionsEventsListOutputItemsMessageToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapSessionsEventsListOutputItemsMessageToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageSenderParticipantData:
        return SessionsEventsListOutputItemsMessageSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageSenderParticipant:
        return SessionsEventsListOutputItemsMessageSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsListOutputItemsMessageSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageResponderParticipantData:
        return SessionsEventsListOutputItemsMessageResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageResponderParticipant:
        return SessionsEventsListOutputItemsMessageResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsEventsListOutputItemsMessageResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessageError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessageError:
        return SessionsEventsListOutputItemsMessageError(
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
    def to_dict(value: Union[SessionsEventsListOutputItemsMessageError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsMessage:
        return SessionsEventsListOutputItemsMessage(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapSessionsEventsListOutputItemsMessageHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapSessionsEventsListOutputItemsMessageTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapSessionsEventsListOutputItemsMessageToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapSessionsEventsListOutputItemsMessageSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsEventsListOutputItemsMessageResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapSessionsEventsListOutputItemsMessageError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItemsMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsError:
        return SessionsEventsListOutputItemsError(
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
    def to_dict(value: Union[SessionsEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItemsWarning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItemsWarning:
        return SessionsEventsListOutputItemsWarning(
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
    def to_dict(value: Union[SessionsEventsListOutputItemsWarning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputItems:
        return SessionsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        connection=mapSessionsEventsListOutputItemsConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        provider_run=mapSessionsEventsListOutputItemsProviderRun.from_dict(data.get('provider_run')) if data.get('provider_run') else None,
        message=mapSessionsEventsListOutputItemsMessage.from_dict(data.get('message')) if data.get('message') else None,
        error=mapSessionsEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        warning=mapSessionsEventsListOutputItemsWarning.from_dict(data.get('warning')) if data.get('warning') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutputPagination:
        return SessionsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutput:
        return SessionsEventsListOutput(
        items=[mapSessionsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsEventsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionsEventsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionsEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None
    session_message_id: Optional[Union[str, List[str]]] = None
    session_error_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SessionsEventsListQueryCreatedAt] = None
    updated_at: Optional[SessionsEventsListQueryUpdatedAt] = None


class mapSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListQuery:
        return SessionsEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        id=data.get('id'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        session_message_id=data.get('session_message_id'),
        session_error_id=data.get('session_error_id'),
        created_at=mapSessionsEventsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSessionsEventsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

