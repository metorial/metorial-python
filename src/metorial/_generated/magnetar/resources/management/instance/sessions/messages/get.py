from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsMessagesGetOutputHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsMessagesGetOutputTransportToolCall:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionsMessagesGetOutputTransport:
    object: str
    type: str
    mcp: Optional[ManagementInstanceSessionsMessagesGetOutputTransportMcp] = None
    tool_call: Optional[ManagementInstanceSessionsMessagesGetOutputTransportToolCall] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsMessagesGetOutputToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputToolCallTool:
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
    input_schema: Optional[ManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema] = None
    output_schema: Optional[ManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema] = None
    tags: Optional[ManagementInstanceSessionsMessagesGetOutputToolCallToolTags] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputToolCallError:
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
class ManagementInstanceSessionsMessagesGetOutputToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ManagementInstanceSessionsMessagesGetOutputToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[ManagementInstanceSessionsMessagesGetOutputToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesGetOutputError:
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
class ManagementInstanceSessionsMessagesGetOutput:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: ManagementInstanceSessionsMessagesGetOutputHierarchy
    transport: ManagementInstanceSessionsMessagesGetOutputTransport
    sender_participant: ManagementInstanceSessionsMessagesGetOutputSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[ManagementInstanceSessionsMessagesGetOutputToolCall] = None
    responder_participant: Optional[ManagementInstanceSessionsMessagesGetOutputResponderParticipant] = None
    error: Optional[ManagementInstanceSessionsMessagesGetOutputError] = None


class mapManagementInstanceSessionsMessagesGetOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputHierarchy:
        return ManagementInstanceSessionsMessagesGetOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputTransportMcp:
        return ManagementInstanceSessionsMessagesGetOutputTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputTransportToolCall:
        return ManagementInstanceSessionsMessagesGetOutputTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputTransport:
        return ManagementInstanceSessionsMessagesGetOutputTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapManagementInstanceSessionsMessagesGetOutputTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapManagementInstanceSessionsMessagesGetOutputTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema:
        return ManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema:
        return ManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputToolCallToolTags:
        return ManagementInstanceSessionsMessagesGetOutputToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputToolCallTool:
        return ManagementInstanceSessionsMessagesGetOutputToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceSessionsMessagesGetOutputToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceSessionsMessagesGetOutputToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceSessionsMessagesGetOutputToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputToolCallError:
        return ManagementInstanceSessionsMessagesGetOutputToolCallError(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputToolCall:
        return ManagementInstanceSessionsMessagesGetOutputToolCall(
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
        tool=mapManagementInstanceSessionsMessagesGetOutputToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapManagementInstanceSessionsMessagesGetOutputToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputSenderParticipant:
        return ManagementInstanceSessionsMessagesGetOutputSenderParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputResponderParticipant:
        return ManagementInstanceSessionsMessagesGetOutputResponderParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutputError:
        return ManagementInstanceSessionsMessagesGetOutputError(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesGetOutput:
        return ManagementInstanceSessionsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapManagementInstanceSessionsMessagesGetOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapManagementInstanceSessionsMessagesGetOutputTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapManagementInstanceSessionsMessagesGetOutputToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapManagementInstanceSessionsMessagesGetOutputSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapManagementInstanceSessionsMessagesGetOutputResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapManagementInstanceSessionsMessagesGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

