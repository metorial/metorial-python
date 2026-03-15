from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsEventsListOutputItemsConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: DashboardInstanceSessionsEventsListOutputItemsConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    last_active_at: datetime
    mcp: Optional[DashboardInstanceSessionsEventsListOutputItemsConnectionMcp] = None
    participant: Optional[DashboardInstanceSessionsEventsListOutputItemsConnectionParticipant] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsProviderRun:
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
class DashboardInstanceSessionsEventsListOutputItemsMessageHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageTransport:
    object: str
    type: str
    mcp: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp] = None
    tool_call: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool:
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
    input_schema: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema] = None
    output_schema: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema] = None
    tags: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageToolCallError:
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
class DashboardInstanceSessionsEventsListOutputItemsMessageToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: DashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsMessageError:
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
class DashboardInstanceSessionsEventsListOutputItemsMessage:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: DashboardInstanceSessionsEventsListOutputItemsMessageHierarchy
    transport: DashboardInstanceSessionsEventsListOutputItemsMessageTransport
    sender_participant: DashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageToolCall] = None
    responder_participant: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant] = None
    error: Optional[DashboardInstanceSessionsEventsListOutputItemsMessageError] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsError:
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
class DashboardInstanceSessionsEventsListOutputItemsWarning:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    created_at: datetime
    connection_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItems:
    object: str
    id: str
    type: str
    session_id: str
    created_at: datetime
    connection: Optional[DashboardInstanceSessionsEventsListOutputItemsConnection] = None
    provider_run: Optional[DashboardInstanceSessionsEventsListOutputItemsProviderRun] = None
    message: Optional[DashboardInstanceSessionsEventsListOutputItemsMessage] = None
    error: Optional[DashboardInstanceSessionsEventsListOutputItemsError] = None
    warning: Optional[DashboardInstanceSessionsEventsListOutputItemsWarning] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsEventsListOutput:
    items: List[DashboardInstanceSessionsEventsListOutputItems]
    pagination: DashboardInstanceSessionsEventsListOutputPagination


class mapDashboardInstanceSessionsEventsListOutputItemsConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsConnectionUsage:
        return DashboardInstanceSessionsEventsListOutputItemsConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsConnectionMcp:
        return DashboardInstanceSessionsEventsListOutputItemsConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsConnectionParticipant:
        return DashboardInstanceSessionsEventsListOutputItemsConnectionParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsConnection:
        return DashboardInstanceSessionsEventsListOutputItemsConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapDashboardInstanceSessionsEventsListOutputItemsConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapDashboardInstanceSessionsEventsListOutputItemsConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapDashboardInstanceSessionsEventsListOutputItemsConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsProviderRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsProviderRun:
        return DashboardInstanceSessionsEventsListOutputItemsProviderRun(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsProviderRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageHierarchy:
        return DashboardInstanceSessionsEventsListOutputItemsMessageHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp:
        return DashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall:
        return DashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageTransport:
        return DashboardInstanceSessionsEventsListOutputItemsMessageTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapDashboardInstanceSessionsEventsListOutputItemsMessageTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapDashboardInstanceSessionsEventsListOutputItemsMessageTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
        return DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
        return DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags:
        return DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool:
        return DashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageToolCallError:
        return DashboardInstanceSessionsEventsListOutputItemsMessageToolCallError(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageToolCall:
        return DashboardInstanceSessionsEventsListOutputItemsMessageToolCall(
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
        tool=mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant:
        return DashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant:
        return DashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessageError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessageError:
        return DashboardInstanceSessionsEventsListOutputItemsMessageError(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessageError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsMessage:
        return DashboardInstanceSessionsEventsListOutputItemsMessage(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapDashboardInstanceSessionsEventsListOutputItemsMessageHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapDashboardInstanceSessionsEventsListOutputItemsMessageTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapDashboardInstanceSessionsEventsListOutputItemsMessageToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapDashboardInstanceSessionsEventsListOutputItemsMessageSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapDashboardInstanceSessionsEventsListOutputItemsMessageResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapDashboardInstanceSessionsEventsListOutputItemsMessageError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsError:
        return DashboardInstanceSessionsEventsListOutputItemsError(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsWarning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsWarning:
        return DashboardInstanceSessionsEventsListOutputItemsWarning(
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
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsWarning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItems:
        return DashboardInstanceSessionsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        connection=mapDashboardInstanceSessionsEventsListOutputItemsConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        provider_run=mapDashboardInstanceSessionsEventsListOutputItemsProviderRun.from_dict(data.get('provider_run')) if data.get('provider_run') else None,
        message=mapDashboardInstanceSessionsEventsListOutputItemsMessage.from_dict(data.get('message')) if data.get('message') else None,
        error=mapDashboardInstanceSessionsEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        warning=mapDashboardInstanceSessionsEventsListOutputItemsWarning.from_dict(data.get('warning')) if data.get('warning') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputPagination:
        return DashboardInstanceSessionsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutput:
        return DashboardInstanceSessionsEventsListOutput(
        items=[mapDashboardInstanceSessionsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsEventsListQuery:
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


class mapDashboardInstanceSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListQuery:
        return DashboardInstanceSessionsEventsListQuery(
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
        session_error_id=data.get('session_error_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

