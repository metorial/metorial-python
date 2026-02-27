from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsMessagesGetOutputHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class SessionsMessagesGetOutputTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class SessionsMessagesGetOutputTransportToolCall:
    object: str
    id: Optional[str] = None
@dataclass
class SessionsMessagesGetOutputTransport:
    object: str
    type: str
    mcp: Optional[SessionsMessagesGetOutputTransportMcp] = None
    tool_call: Optional[SessionsMessagesGetOutputTransportToolCall] = None
@dataclass
class SessionsMessagesGetOutputToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsMessagesGetOutputToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionsMessagesGetOutputToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class SessionsMessagesGetOutputToolCallTool:
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
    input_schema: Optional[SessionsMessagesGetOutputToolCallToolInputSchema] = None
    output_schema: Optional[SessionsMessagesGetOutputToolCallToolOutputSchema] = None
    tags: Optional[SessionsMessagesGetOutputToolCallToolTags] = None
@dataclass
class SessionsMessagesGetOutputToolCallError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    group_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
@dataclass
class SessionsMessagesGetOutputToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: SessionsMessagesGetOutputToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[SessionsMessagesGetOutputToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class SessionsMessagesGetOutputSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class SessionsMessagesGetOutputResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class SessionsMessagesGetOutputError:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    group_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
@dataclass
class SessionsMessagesGetOutput:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: SessionsMessagesGetOutputHierarchy
    transport: SessionsMessagesGetOutputTransport
    sender_participant: SessionsMessagesGetOutputSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[SessionsMessagesGetOutputToolCall] = None
    responder_participant: Optional[SessionsMessagesGetOutputResponderParticipant] = None
    error: Optional[SessionsMessagesGetOutputError] = None


class mapSessionsMessagesGetOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputHierarchy:
        return SessionsMessagesGetOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputTransportMcp:
        return SessionsMessagesGetOutputTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputTransportToolCall:
        return SessionsMessagesGetOutputTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputTransport:
        return SessionsMessagesGetOutputTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapSessionsMessagesGetOutputTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapSessionsMessagesGetOutputTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputToolCallToolInputSchema:
        return SessionsMessagesGetOutputToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputToolCallToolOutputSchema:
        return SessionsMessagesGetOutputToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputToolCallToolTags:
        return SessionsMessagesGetOutputToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputToolCallTool:
        return SessionsMessagesGetOutputToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapSessionsMessagesGetOutputToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapSessionsMessagesGetOutputToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapSessionsMessagesGetOutputToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputToolCallError:
        return SessionsMessagesGetOutputToolCallError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputToolCall:
        return SessionsMessagesGetOutputToolCall(
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
        tool=mapSessionsMessagesGetOutputToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapSessionsMessagesGetOutputToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputSenderParticipant:
        return SessionsMessagesGetOutputSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputResponderParticipant:
        return SessionsMessagesGetOutputResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutputError:
        return SessionsMessagesGetOutputError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutput:
        return SessionsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapSessionsMessagesGetOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapSessionsMessagesGetOutputTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapSessionsMessagesGetOutputToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapSessionsMessagesGetOutputSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapSessionsMessagesGetOutputResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapSessionsMessagesGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
