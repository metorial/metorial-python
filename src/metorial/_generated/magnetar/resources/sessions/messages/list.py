from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsMessagesListOutputItemsHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class SessionsMessagesListOutputItemsTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class SessionsMessagesListOutputItemsTransportToolCall:
    object: str
    id: str
@dataclass
class SessionsMessagesListOutputItemsTransport:
    object: str
    type: str
    mcp: Optional[SessionsMessagesListOutputItemsTransportMcp] = None
    tool_call: Optional[SessionsMessagesListOutputItemsTransportToolCall] = None
@dataclass
class SessionsMessagesListOutputItemsToolCallSenderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsMessagesListOutputItemsToolCallSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsMessagesListOutputItemsToolCallSenderParticipantData
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
class SessionsMessagesListOutputItemsToolCallResponderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsMessagesListOutputItemsToolCallResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsMessagesListOutputItemsToolCallResponderParticipantData
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
class SessionsMessagesListOutputItemsToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsMessagesListOutputItemsToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsMessagesListOutputItemsToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class SessionsMessagesListOutputItemsToolCallTool:
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
    input_schema: Optional[SessionsMessagesListOutputItemsToolCallToolInputSchema] = None
    output_schema: Optional[SessionsMessagesListOutputItemsToolCallToolOutputSchema] = None
    tags: Optional[SessionsMessagesListOutputItemsToolCallToolTags] = None
@dataclass
class SessionsMessagesListOutputItemsToolCallError:
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
class SessionsMessagesListOutputItemsToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: SessionsMessagesListOutputItemsToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[SessionsMessagesListOutputItemsToolCallSenderParticipant] = None
    responder_participant: Optional[SessionsMessagesListOutputItemsToolCallResponderParticipant] = None
    error: Optional[SessionsMessagesListOutputItemsToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class SessionsMessagesListOutputItemsSenderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsMessagesListOutputItemsSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsMessagesListOutputItemsSenderParticipantData
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
class SessionsMessagesListOutputItemsResponderParticipantData:
    identifier: str
    name: str
@dataclass
class SessionsMessagesListOutputItemsResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsMessagesListOutputItemsResponderParticipantData
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
class SessionsMessagesListOutputItemsError:
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
class SessionsMessagesListOutputItems:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: SessionsMessagesListOutputItemsHierarchy
    transport: SessionsMessagesListOutputItemsTransport
    sender_participant: SessionsMessagesListOutputItemsSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[SessionsMessagesListOutputItemsToolCall] = None
    responder_participant: Optional[SessionsMessagesListOutputItemsResponderParticipant] = None
    error: Optional[SessionsMessagesListOutputItemsError] = None
@dataclass
class SessionsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsMessagesListOutput:
    items: List[SessionsMessagesListOutputItems]
    pagination: SessionsMessagesListOutputPagination


class mapSessionsMessagesListOutputItemsHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsHierarchy:
        return SessionsMessagesListOutputItemsHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsTransportMcp:
        return SessionsMessagesListOutputItemsTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsTransportToolCall:
        return SessionsMessagesListOutputItemsTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsTransport:
        return SessionsMessagesListOutputItemsTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapSessionsMessagesListOutputItemsTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapSessionsMessagesListOutputItemsTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallSenderParticipantData:
        return SessionsMessagesListOutputItemsToolCallSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallSenderParticipant:
        return SessionsMessagesListOutputItemsToolCallSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsMessagesListOutputItemsToolCallSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallResponderParticipantData:
        return SessionsMessagesListOutputItemsToolCallResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallResponderParticipant:
        return SessionsMessagesListOutputItemsToolCallResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsMessagesListOutputItemsToolCallResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallToolInputSchema:
        return SessionsMessagesListOutputItemsToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallToolOutputSchema:
        return SessionsMessagesListOutputItemsToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallToolTags:
        return SessionsMessagesListOutputItemsToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallTool:
        return SessionsMessagesListOutputItemsToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapSessionsMessagesListOutputItemsToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapSessionsMessagesListOutputItemsToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapSessionsMessagesListOutputItemsToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCallError:
        return SessionsMessagesListOutputItemsToolCallError(
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
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsToolCall:
        return SessionsMessagesListOutputItemsToolCall(
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
        sender_participant=mapSessionsMessagesListOutputItemsToolCallSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsMessagesListOutputItemsToolCallResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapSessionsMessagesListOutputItemsToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapSessionsMessagesListOutputItemsToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsSenderParticipantData:
        return SessionsMessagesListOutputItemsSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsSenderParticipant:
        return SessionsMessagesListOutputItemsSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsMessagesListOutputItemsSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsMessagesListOutputItemsSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsResponderParticipantData:
        return SessionsMessagesListOutputItemsResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItemsResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsResponderParticipant:
        return SessionsMessagesListOutputItemsResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsMessagesListOutputItemsResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[SessionsMessagesListOutputItemsResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsError:
        return SessionsMessagesListOutputItemsError(
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
    def to_dict(value: Union[SessionsMessagesListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItems:
        return SessionsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapSessionsMessagesListOutputItemsHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapSessionsMessagesListOutputItemsTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapSessionsMessagesListOutputItemsToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapSessionsMessagesListOutputItemsSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsMessagesListOutputItemsResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapSessionsMessagesListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputPagination:
        return SessionsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutput:
        return SessionsMessagesListOutput(
        items=[mapSessionsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsMessagesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionsMessagesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionsMessagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    source: Optional[Union[str, List[str]]] = None
    hierarchy: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None
    error_id: Optional[Union[str, List[str]]] = None
    participant_id: Optional[Union[str, List[str]]] = None
    parent_message_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SessionsMessagesListQueryCreatedAt] = None
    updated_at: Optional[SessionsMessagesListQueryUpdatedAt] = None


class mapSessionsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesListQuery:
        return SessionsMessagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        source=data.get('source'),
        hierarchy=data.get('hierarchy'),
        id=data.get('id'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        error_id=data.get('error_id'),
        participant_id=data.get('participant_id'),
        parent_message_id=data.get('parent_message_id'),
        created_at=mapSessionsMessagesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSessionsMessagesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

