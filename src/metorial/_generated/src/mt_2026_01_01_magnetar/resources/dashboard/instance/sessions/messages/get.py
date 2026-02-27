from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsMessagesGetOutputHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsMessagesGetOutputTransportToolCall:
    object: str
    id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputTransport:
    object: str
    type: str
    mcp: Optional[DashboardInstanceSessionsMessagesGetOutputTransportMcp] = None
    tool_call: Optional[DashboardInstanceSessionsMessagesGetOutputTransportToolCall] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsMessagesGetOutputToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputToolCallTool:
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
    input_schema: Optional[DashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema] = None
    output_schema: Optional[DashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema] = None
    tags: Optional[DashboardInstanceSessionsMessagesGetOutputToolCallToolTags] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputToolCallError:
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
class DashboardInstanceSessionsMessagesGetOutputToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: DashboardInstanceSessionsMessagesGetOutputToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[DashboardInstanceSessionsMessagesGetOutputToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesGetOutputError:
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
class DashboardInstanceSessionsMessagesGetOutput:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: DashboardInstanceSessionsMessagesGetOutputHierarchy
    transport: DashboardInstanceSessionsMessagesGetOutputTransport
    sender_participant: DashboardInstanceSessionsMessagesGetOutputSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[DashboardInstanceSessionsMessagesGetOutputToolCall] = None
    responder_participant: Optional[DashboardInstanceSessionsMessagesGetOutputResponderParticipant] = None
    error: Optional[DashboardInstanceSessionsMessagesGetOutputError] = None


class mapDashboardInstanceSessionsMessagesGetOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputHierarchy:
        return DashboardInstanceSessionsMessagesGetOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputTransportMcp:
        return DashboardInstanceSessionsMessagesGetOutputTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputTransportToolCall:
        return DashboardInstanceSessionsMessagesGetOutputTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputTransport:
        return DashboardInstanceSessionsMessagesGetOutputTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapDashboardInstanceSessionsMessagesGetOutputTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapDashboardInstanceSessionsMessagesGetOutputTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema:
        return DashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema:
        return DashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputToolCallToolTags:
        return DashboardInstanceSessionsMessagesGetOutputToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputToolCallTool:
        return DashboardInstanceSessionsMessagesGetOutputToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceSessionsMessagesGetOutputToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceSessionsMessagesGetOutputToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceSessionsMessagesGetOutputToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputToolCallError:
        return DashboardInstanceSessionsMessagesGetOutputToolCallError(
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputToolCall:
        return DashboardInstanceSessionsMessagesGetOutputToolCall(
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
        tool=mapDashboardInstanceSessionsMessagesGetOutputToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapDashboardInstanceSessionsMessagesGetOutputToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputSenderParticipant:
        return DashboardInstanceSessionsMessagesGetOutputSenderParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputResponderParticipant:
        return DashboardInstanceSessionsMessagesGetOutputResponderParticipant(
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutputError:
        return DashboardInstanceSessionsMessagesGetOutputError(
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesGetOutput:
        return DashboardInstanceSessionsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapDashboardInstanceSessionsMessagesGetOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapDashboardInstanceSessionsMessagesGetOutputTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapDashboardInstanceSessionsMessagesGetOutputToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapDashboardInstanceSessionsMessagesGetOutputSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapDashboardInstanceSessionsMessagesGetOutputResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapDashboardInstanceSessionsMessagesGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
