from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsTransportToolCall:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsTransport:
    object: str
    type: str
    mcp: Optional[ManagementInstanceSessionsMessagesListOutputItemsTransportMcp] = None
    tool_call: Optional[ManagementInstanceSessionsMessagesListOutputItemsTransportToolCall] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsToolCallTool:
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
    input_schema: Optional[ManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema] = None
    output_schema: Optional[ManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema] = None
    tags: Optional[ManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsToolCallError:
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
class ManagementInstanceSessionsMessagesListOutputItemsToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ManagementInstanceSessionsMessagesListOutputItemsToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    error: Optional[ManagementInstanceSessionsMessagesListOutputItemsToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputItemsError:
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
class ManagementInstanceSessionsMessagesListOutputItems:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: ManagementInstanceSessionsMessagesListOutputItemsHierarchy
    transport: ManagementInstanceSessionsMessagesListOutputItemsTransport
    sender_participant: ManagementInstanceSessionsMessagesListOutputItemsSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[ManagementInstanceSessionsMessagesListOutputItemsToolCall] = None
    responder_participant: Optional[ManagementInstanceSessionsMessagesListOutputItemsResponderParticipant] = None
    error: Optional[ManagementInstanceSessionsMessagesListOutputItemsError] = None
@dataclass
class ManagementInstanceSessionsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsMessagesListOutput:
    items: List[ManagementInstanceSessionsMessagesListOutputItems]
    pagination: ManagementInstanceSessionsMessagesListOutputPagination


class mapManagementInstanceSessionsMessagesListOutputItemsHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsHierarchy:
        return ManagementInstanceSessionsMessagesListOutputItemsHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsTransportMcp:
        return ManagementInstanceSessionsMessagesListOutputItemsTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsTransportToolCall:
        return ManagementInstanceSessionsMessagesListOutputItemsTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsTransport:
        return ManagementInstanceSessionsMessagesListOutputItemsTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapManagementInstanceSessionsMessagesListOutputItemsTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapManagementInstanceSessionsMessagesListOutputItemsTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema:
        return ManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema:
        return ManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags:
        return ManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsToolCallTool:
        return ManagementInstanceSessionsMessagesListOutputItemsToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceSessionsMessagesListOutputItemsToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsToolCallError:
        return ManagementInstanceSessionsMessagesListOutputItemsToolCallError(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsToolCall:
        return ManagementInstanceSessionsMessagesListOutputItemsToolCall(
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
        tool=mapManagementInstanceSessionsMessagesListOutputItemsToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapManagementInstanceSessionsMessagesListOutputItemsToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsSenderParticipant:
        return ManagementInstanceSessionsMessagesListOutputItemsSenderParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsResponderParticipant:
        return ManagementInstanceSessionsMessagesListOutputItemsResponderParticipant(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItemsError:
        return ManagementInstanceSessionsMessagesListOutputItemsError(
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
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputItems:
        return ManagementInstanceSessionsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapManagementInstanceSessionsMessagesListOutputItemsHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapManagementInstanceSessionsMessagesListOutputItemsTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapManagementInstanceSessionsMessagesListOutputItemsToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapManagementInstanceSessionsMessagesListOutputItemsSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapManagementInstanceSessionsMessagesListOutputItemsResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapManagementInstanceSessionsMessagesListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutputPagination:
        return ManagementInstanceSessionsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListOutput:
        return ManagementInstanceSessionsMessagesListOutput(
        items=[mapManagementInstanceSessionsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsMessagesListQuery:
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


class mapManagementInstanceSessionsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsMessagesListQuery:
        return ManagementInstanceSessionsMessagesListQuery(
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
        parent_message_id=data.get('parent_message_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

