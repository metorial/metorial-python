from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsEventsGetOutputConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class DashboardInstanceSessionsEventsGetOutputConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsEventsGetOutputConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: DashboardInstanceSessionsEventsGetOutputConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    last_active_at: datetime
    mcp: Optional[DashboardInstanceSessionsEventsGetOutputConnectionMcp] = None
    participant: Optional[DashboardInstanceSessionsEventsGetOutputConnectionParticipant] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputProviderRun:
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
class DashboardInstanceSessionsEventsGetOutputMessageHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageTransportToolCall:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageTransport:
    object: str
    type: str
    mcp: Optional[DashboardInstanceSessionsEventsGetOutputMessageTransportMcp] = None
    tool_call: Optional[DashboardInstanceSessionsEventsGetOutputMessageTransportToolCall] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageToolCallTool:
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
    input_schema: Optional[DashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema] = None
    output_schema: Optional[DashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema] = None
    tags: Optional[DashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageToolCallError:
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
class DashboardInstanceSessionsEventsGetOutputMessageToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: DashboardInstanceSessionsEventsGetOutputMessageToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[DashboardInstanceSessionsEventsGetOutputMessageToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputMessageError:
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
class DashboardInstanceSessionsEventsGetOutputMessage:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: DashboardInstanceSessionsEventsGetOutputMessageHierarchy
    transport: DashboardInstanceSessionsEventsGetOutputMessageTransport
    sender_participant: DashboardInstanceSessionsEventsGetOutputMessageSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[DashboardInstanceSessionsEventsGetOutputMessageToolCall] = None
    responder_participant: Optional[DashboardInstanceSessionsEventsGetOutputMessageResponderParticipant] = None
    error: Optional[DashboardInstanceSessionsEventsGetOutputMessageError] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutputError:
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
class DashboardInstanceSessionsEventsGetOutputWarning:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    created_at: datetime
    connection_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsGetOutput:
    object: str
    id: str
    type: str
    session_id: str
    created_at: datetime
    connection: Optional[DashboardInstanceSessionsEventsGetOutputConnection] = None
    provider_run: Optional[DashboardInstanceSessionsEventsGetOutputProviderRun] = None
    message: Optional[DashboardInstanceSessionsEventsGetOutputMessage] = None
    error: Optional[DashboardInstanceSessionsEventsGetOutputError] = None
    warning: Optional[DashboardInstanceSessionsEventsGetOutputWarning] = None


class mapDashboardInstanceSessionsEventsGetOutputConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputConnectionUsage:
        return DashboardInstanceSessionsEventsGetOutputConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputConnectionMcp:
        return DashboardInstanceSessionsEventsGetOutputConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputConnectionParticipant:
        return DashboardInstanceSessionsEventsGetOutputConnectionParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputConnection:
        return DashboardInstanceSessionsEventsGetOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapDashboardInstanceSessionsEventsGetOutputConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapDashboardInstanceSessionsEventsGetOutputConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapDashboardInstanceSessionsEventsGetOutputConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputProviderRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputProviderRun:
        return DashboardInstanceSessionsEventsGetOutputProviderRun(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputProviderRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageHierarchy:
        return DashboardInstanceSessionsEventsGetOutputMessageHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageTransportMcp:
        return DashboardInstanceSessionsEventsGetOutputMessageTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageTransportToolCall:
        return DashboardInstanceSessionsEventsGetOutputMessageTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageTransport:
        return DashboardInstanceSessionsEventsGetOutputMessageTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapDashboardInstanceSessionsEventsGetOutputMessageTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapDashboardInstanceSessionsEventsGetOutputMessageTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema:
        return DashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema:
        return DashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags:
        return DashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageToolCallTool:
        return DashboardInstanceSessionsEventsGetOutputMessageToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceSessionsEventsGetOutputMessageToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageToolCallError:
        return DashboardInstanceSessionsEventsGetOutputMessageToolCallError(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageToolCall:
        return DashboardInstanceSessionsEventsGetOutputMessageToolCall(
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
        tool=mapDashboardInstanceSessionsEventsGetOutputMessageToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapDashboardInstanceSessionsEventsGetOutputMessageToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageSenderParticipant:
        return DashboardInstanceSessionsEventsGetOutputMessageSenderParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageResponderParticipant:
        return DashboardInstanceSessionsEventsGetOutputMessageResponderParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessageError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessageError:
        return DashboardInstanceSessionsEventsGetOutputMessageError(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessageError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputMessage:
        return DashboardInstanceSessionsEventsGetOutputMessage(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapDashboardInstanceSessionsEventsGetOutputMessageHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapDashboardInstanceSessionsEventsGetOutputMessageTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapDashboardInstanceSessionsEventsGetOutputMessageToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapDashboardInstanceSessionsEventsGetOutputMessageSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapDashboardInstanceSessionsEventsGetOutputMessageResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapDashboardInstanceSessionsEventsGetOutputMessageError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputError:
        return DashboardInstanceSessionsEventsGetOutputError(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutputWarning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutputWarning:
        return DashboardInstanceSessionsEventsGetOutputWarning(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutputWarning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsGetOutput:
        return DashboardInstanceSessionsEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        connection=mapDashboardInstanceSessionsEventsGetOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        provider_run=mapDashboardInstanceSessionsEventsGetOutputProviderRun.from_dict(data.get('provider_run')) if data.get('provider_run') else None,
        message=mapDashboardInstanceSessionsEventsGetOutputMessage.from_dict(data.get('message')) if data.get('message') else None,
        error=mapDashboardInstanceSessionsEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        warning=mapDashboardInstanceSessionsEventsGetOutputWarning.from_dict(data.get('warning')) if data.get('warning') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

