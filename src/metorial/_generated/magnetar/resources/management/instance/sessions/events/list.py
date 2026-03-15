from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsEventsListOutputItemsConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: ManagementInstanceSessionsEventsListOutputItemsConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    last_active_at: datetime
    mcp: Optional[ManagementInstanceSessionsEventsListOutputItemsConnectionMcp] = None
    participant: Optional[ManagementInstanceSessionsEventsListOutputItemsConnectionParticipant] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsProviderRun:
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
class ManagementInstanceSessionsEventsListOutputItemsMessageHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageTransport:
    object: str
    type: str
    mcp: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp] = None
    tool_call: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool:
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
    input_schema: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema] = None
    output_schema: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema] = None
    tags: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageToolCallError:
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
class ManagementInstanceSessionsEventsListOutputItemsMessageToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsMessageError:
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
class ManagementInstanceSessionsEventsListOutputItemsMessage:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: ManagementInstanceSessionsEventsListOutputItemsMessageHierarchy
    transport: ManagementInstanceSessionsEventsListOutputItemsMessageTransport
    sender_participant: ManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageToolCall] = None
    responder_participant: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant] = None
    error: Optional[ManagementInstanceSessionsEventsListOutputItemsMessageError] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsError:
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
class ManagementInstanceSessionsEventsListOutputItemsWarning:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    created_at: datetime
    connection_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItems:
    object: str
    id: str
    type: str
    session_id: str
    created_at: datetime
    connection: Optional[ManagementInstanceSessionsEventsListOutputItemsConnection] = None
    provider_run: Optional[ManagementInstanceSessionsEventsListOutputItemsProviderRun] = None
    message: Optional[ManagementInstanceSessionsEventsListOutputItemsMessage] = None
    error: Optional[ManagementInstanceSessionsEventsListOutputItemsError] = None
    warning: Optional[ManagementInstanceSessionsEventsListOutputItemsWarning] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsEventsListOutput:
    items: List[ManagementInstanceSessionsEventsListOutputItems]
    pagination: ManagementInstanceSessionsEventsListOutputPagination


class mapManagementInstanceSessionsEventsListOutputItemsConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsConnectionUsage:
        return ManagementInstanceSessionsEventsListOutputItemsConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsConnectionMcp:
        return ManagementInstanceSessionsEventsListOutputItemsConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsConnectionParticipant:
        return ManagementInstanceSessionsEventsListOutputItemsConnectionParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsConnection:
        return ManagementInstanceSessionsEventsListOutputItemsConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapManagementInstanceSessionsEventsListOutputItemsConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapManagementInstanceSessionsEventsListOutputItemsConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapManagementInstanceSessionsEventsListOutputItemsConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsProviderRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsProviderRun:
        return ManagementInstanceSessionsEventsListOutputItemsProviderRun(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsProviderRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageHierarchy:
        return ManagementInstanceSessionsEventsListOutputItemsMessageHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp:
        return ManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall:
        return ManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageTransport:
        return ManagementInstanceSessionsEventsListOutputItemsMessageTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapManagementInstanceSessionsEventsListOutputItemsMessageTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapManagementInstanceSessionsEventsListOutputItemsMessageTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema:
        return ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema:
        return ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags:
        return ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool:
        return ManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageToolCallError:
        return ManagementInstanceSessionsEventsListOutputItemsMessageToolCallError(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageToolCall:
        return ManagementInstanceSessionsEventsListOutputItemsMessageToolCall(
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
        tool=mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapManagementInstanceSessionsEventsListOutputItemsMessageToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant:
        return ManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant:
        return ManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessageError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessageError:
        return ManagementInstanceSessionsEventsListOutputItemsMessageError(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessageError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsMessage:
        return ManagementInstanceSessionsEventsListOutputItemsMessage(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapManagementInstanceSessionsEventsListOutputItemsMessageHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapManagementInstanceSessionsEventsListOutputItemsMessageTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapManagementInstanceSessionsEventsListOutputItemsMessageToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapManagementInstanceSessionsEventsListOutputItemsMessageSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapManagementInstanceSessionsEventsListOutputItemsMessageResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapManagementInstanceSessionsEventsListOutputItemsMessageError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsError:
        return ManagementInstanceSessionsEventsListOutputItemsError(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsWarning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsWarning:
        return ManagementInstanceSessionsEventsListOutputItemsWarning(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsWarning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItems:
        return ManagementInstanceSessionsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        connection=mapManagementInstanceSessionsEventsListOutputItemsConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        provider_run=mapManagementInstanceSessionsEventsListOutputItemsProviderRun.from_dict(data.get('provider_run')) if data.get('provider_run') else None,
        message=mapManagementInstanceSessionsEventsListOutputItemsMessage.from_dict(data.get('message')) if data.get('message') else None,
        error=mapManagementInstanceSessionsEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        warning=mapManagementInstanceSessionsEventsListOutputItemsWarning.from_dict(data.get('warning')) if data.get('warning') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputPagination:
        return ManagementInstanceSessionsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutput:
        return ManagementInstanceSessionsEventsListOutput(
        items=[mapManagementInstanceSessionsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsEventsListQuery:
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


class mapManagementInstanceSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListQuery:
        return ManagementInstanceSessionsEventsListQuery(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

