from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsEventsGetOutputConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class ManagementInstanceSessionsEventsGetOutputConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsEventsGetOutputConnectionParticipantData:
    identifier: str
    name: str
@dataclass
class ManagementInstanceSessionsEventsGetOutputConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ManagementInstanceSessionsEventsGetOutputConnectionParticipantData
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: ManagementInstanceSessionsEventsGetOutputConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    mcp: Optional[ManagementInstanceSessionsEventsGetOutputConnectionMcp] = None
    participant: Optional[ManagementInstanceSessionsEventsGetOutputConnectionParticipant] = None
    last_active_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputProviderRun:
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
class ManagementInstanceSessionsEventsGetOutputMessageHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageTransportToolCall:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageTransport:
    object: str
    type: str
    mcp: Optional[ManagementInstanceSessionsEventsGetOutputMessageTransportMcp] = None
    tool_call: Optional[ManagementInstanceSessionsEventsGetOutputMessageTransportToolCall] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageToolCallTool:
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
    input_schema: Optional[ManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema] = None
    output_schema: Optional[ManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema] = None
    tags: Optional[ManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageToolCallError:
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
class ManagementInstanceSessionsEventsGetOutputMessageToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ManagementInstanceSessionsEventsGetOutputMessageToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[ManagementInstanceSessionsEventsGetOutputMessageToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData:
    identifier: str
    name: str
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData:
    identifier: str
    name: str
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputMessageError:
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
class ManagementInstanceSessionsEventsGetOutputMessage:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: ManagementInstanceSessionsEventsGetOutputMessageHierarchy
    transport: ManagementInstanceSessionsEventsGetOutputMessageTransport
    sender_participant: ManagementInstanceSessionsEventsGetOutputMessageSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[ManagementInstanceSessionsEventsGetOutputMessageToolCall] = None
    responder_participant: Optional[ManagementInstanceSessionsEventsGetOutputMessageResponderParticipant] = None
    error: Optional[ManagementInstanceSessionsEventsGetOutputMessageError] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutputError:
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
class ManagementInstanceSessionsEventsGetOutputWarning:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    session_id: str
    created_at: datetime
    connection_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsGetOutput:
    object: str
    id: str
    type: str
    session_id: str
    created_at: datetime
    connection: Optional[ManagementInstanceSessionsEventsGetOutputConnection] = None
    provider_run: Optional[ManagementInstanceSessionsEventsGetOutputProviderRun] = None
    message: Optional[ManagementInstanceSessionsEventsGetOutputMessage] = None
    error: Optional[ManagementInstanceSessionsEventsGetOutputError] = None
    warning: Optional[ManagementInstanceSessionsEventsGetOutputWarning] = None


class mapManagementInstanceSessionsEventsGetOutputConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputConnectionUsage:
        return ManagementInstanceSessionsEventsGetOutputConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputConnectionMcp:
        return ManagementInstanceSessionsEventsGetOutputConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputConnectionParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputConnectionParticipantData:
        return ManagementInstanceSessionsEventsGetOutputConnectionParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputConnectionParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputConnectionParticipant:
        return ManagementInstanceSessionsEventsGetOutputConnectionParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapManagementInstanceSessionsEventsGetOutputConnectionParticipantData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputConnection:
        return ManagementInstanceSessionsEventsGetOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapManagementInstanceSessionsEventsGetOutputConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapManagementInstanceSessionsEventsGetOutputConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapManagementInstanceSessionsEventsGetOutputConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputProviderRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputProviderRun:
        return ManagementInstanceSessionsEventsGetOutputProviderRun(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputProviderRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageHierarchy:
        return ManagementInstanceSessionsEventsGetOutputMessageHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageTransportMcp:
        return ManagementInstanceSessionsEventsGetOutputMessageTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageTransportToolCall:
        return ManagementInstanceSessionsEventsGetOutputMessageTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageTransport:
        return ManagementInstanceSessionsEventsGetOutputMessageTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapManagementInstanceSessionsEventsGetOutputMessageTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapManagementInstanceSessionsEventsGetOutputMessageTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema:
        return ManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema:
        return ManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags:
        return ManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageToolCallTool:
        return ManagementInstanceSessionsEventsGetOutputMessageToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceSessionsEventsGetOutputMessageToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceSessionsEventsGetOutputMessageToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceSessionsEventsGetOutputMessageToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageToolCallError:
        return ManagementInstanceSessionsEventsGetOutputMessageToolCallError(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageToolCall:
        return ManagementInstanceSessionsEventsGetOutputMessageToolCall(
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
        tool=mapManagementInstanceSessionsEventsGetOutputMessageToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapManagementInstanceSessionsEventsGetOutputMessageToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData:
        return ManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageSenderParticipant:
        return ManagementInstanceSessionsEventsGetOutputMessageSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapManagementInstanceSessionsEventsGetOutputMessageSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData:
        return ManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageResponderParticipant:
        return ManagementInstanceSessionsEventsGetOutputMessageResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapManagementInstanceSessionsEventsGetOutputMessageResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessageError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessageError:
        return ManagementInstanceSessionsEventsGetOutputMessageError(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessageError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputMessage:
        return ManagementInstanceSessionsEventsGetOutputMessage(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapManagementInstanceSessionsEventsGetOutputMessageHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapManagementInstanceSessionsEventsGetOutputMessageTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapManagementInstanceSessionsEventsGetOutputMessageToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapManagementInstanceSessionsEventsGetOutputMessageSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapManagementInstanceSessionsEventsGetOutputMessageResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapManagementInstanceSessionsEventsGetOutputMessageError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputError:
        return ManagementInstanceSessionsEventsGetOutputError(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutputWarning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutputWarning:
        return ManagementInstanceSessionsEventsGetOutputWarning(
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
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutputWarning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsGetOutput:
        return ManagementInstanceSessionsEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        connection=mapManagementInstanceSessionsEventsGetOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        provider_run=mapManagementInstanceSessionsEventsGetOutputProviderRun.from_dict(data.get('provider_run')) if data.get('provider_run') else None,
        message=mapManagementInstanceSessionsEventsGetOutputMessage.from_dict(data.get('message')) if data.get('message') else None,
        error=mapManagementInstanceSessionsEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        warning=mapManagementInstanceSessionsEventsGetOutputWarning.from_dict(data.get('warning')) if data.get('warning') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

