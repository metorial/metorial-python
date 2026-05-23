from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsHierarchy:
    object: str
    type: str
    child_message_ids: List[str]
    parent_message_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsTransportMcp:
    object: str
    id: Union[str, float]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsTransportToolCall:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsTransport:
    object: str
    type: str
    mcp: Optional[DashboardInstanceSessionsMessagesListOutputItemsTransportMcp] = None
    tool_call: Optional[DashboardInstanceSessionsMessagesListOutputItemsTransportToolCall] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData
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
class DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData
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
class DashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallTool:
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
    input_schema: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema] = None
    output_schema: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema] = None
    tags: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsToolCallError:
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
class DashboardInstanceSessionsMessagesListOutputItemsToolCall:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: DashboardInstanceSessionsMessagesListOutputItemsToolCallTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant] = None
    responder_participant: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant] = None
    error: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCallError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData
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
class DashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceSessionsMessagesListOutputItemsResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData
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
class DashboardInstanceSessionsMessagesListOutputItemsError:
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
class DashboardInstanceSessionsMessagesListOutputItems:
    object: str
    id: str
    type: str
    status: str
    source: str
    session_id: str
    hierarchy: DashboardInstanceSessionsMessagesListOutputItemsHierarchy
    transport: DashboardInstanceSessionsMessagesListOutputItemsTransport
    sender_participant: DashboardInstanceSessionsMessagesListOutputItemsSenderParticipant
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    tool_call: Optional[DashboardInstanceSessionsMessagesListOutputItemsToolCall] = None
    responder_participant: Optional[DashboardInstanceSessionsMessagesListOutputItemsResponderParticipant] = None
    error: Optional[DashboardInstanceSessionsMessagesListOutputItemsError] = None
@dataclass
class DashboardInstanceSessionsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsMessagesListOutput:
    items: List[DashboardInstanceSessionsMessagesListOutputItems]
    pagination: DashboardInstanceSessionsMessagesListOutputPagination


class mapDashboardInstanceSessionsMessagesListOutputItemsHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsHierarchy:
        return DashboardInstanceSessionsMessagesListOutputItemsHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_message_id=data.get('parent_message_id'),
        child_message_ids=data.get('child_message_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsTransportMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsTransportMcp:
        return DashboardInstanceSessionsMessagesListOutputItemsTransportMcp(
        object=data.get('object'),
        id=data.get('id'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsTransportMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsTransportToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsTransportToolCall:
        return DashboardInstanceSessionsMessagesListOutputItemsTransportToolCall(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsTransportToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsTransport:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsTransport:
        return DashboardInstanceSessionsMessagesListOutputItemsTransport(
        object=data.get('object'),
        type=data.get('type'),
        mcp=mapDashboardInstanceSessionsMessagesListOutputItemsTransportMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        tool_call=mapDashboardInstanceSessionsMessagesListOutputItemsTransportToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsTransport, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallTool:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCallError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCallError:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCallError(
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCallError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsToolCall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsToolCall:
        return DashboardInstanceSessionsMessagesListOutputItemsToolCall(
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
        sender_participant=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapDashboardInstanceSessionsMessagesListOutputItemsToolCallError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsToolCall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData:
        return DashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsSenderParticipant:
        return DashboardInstanceSessionsMessagesListOutputItemsSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceSessionsMessagesListOutputItemsSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData:
        return DashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsResponderParticipant:
        return DashboardInstanceSessionsMessagesListOutputItemsResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceSessionsMessagesListOutputItemsResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItemsError:
        return DashboardInstanceSessionsMessagesListOutputItemsError(
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
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputItems:
        return DashboardInstanceSessionsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=data.get('source'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        connection_id=data.get('connection_id'),
        provider_run_id=data.get('provider_run_id'),
        hierarchy=mapDashboardInstanceSessionsMessagesListOutputItemsHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        transport=mapDashboardInstanceSessionsMessagesListOutputItemsTransport.from_dict(data.get('transport')) if data.get('transport') else None,
        input=data.get('input'),
        output=data.get('output'),
        tool_call=mapDashboardInstanceSessionsMessagesListOutputItemsToolCall.from_dict(data.get('tool_call')) if data.get('tool_call') else None,
        sender_participant=mapDashboardInstanceSessionsMessagesListOutputItemsSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapDashboardInstanceSessionsMessagesListOutputItemsResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        error=mapDashboardInstanceSessionsMessagesListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutputPagination:
        return DashboardInstanceSessionsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListOutput:
        return DashboardInstanceSessionsMessagesListOutput(
        items=[mapDashboardInstanceSessionsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsMessagesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsMessagesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsMessagesListQuery:
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
    created_at: Optional[DashboardInstanceSessionsMessagesListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceSessionsMessagesListQueryUpdatedAt] = None


class mapDashboardInstanceSessionsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsMessagesListQuery:
        return DashboardInstanceSessionsMessagesListQuery(
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
        created_at=mapDashboardInstanceSessionsMessagesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceSessionsMessagesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

