from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ToolCallsCreateOutputSenderParticipantData:
    identifier: str
    name: str
@dataclass
class ToolCallsCreateOutputSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ToolCallsCreateOutputSenderParticipantData
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
class ToolCallsCreateOutputResponderParticipantData:
    identifier: str
    name: str
@dataclass
class ToolCallsCreateOutputResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ToolCallsCreateOutputResponderParticipantData
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
class ToolCallsCreateOutputToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsCreateOutputToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsCreateOutputToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ToolCallsCreateOutputTool:
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
    input_schema: Optional[ToolCallsCreateOutputToolInputSchema] = None
    output_schema: Optional[ToolCallsCreateOutputToolOutputSchema] = None
    tags: Optional[ToolCallsCreateOutputToolTags] = None
@dataclass
class ToolCallsCreateOutputError:
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
class ToolCallsCreateOutput:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ToolCallsCreateOutputTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[ToolCallsCreateOutputSenderParticipant] = None
    responder_participant: Optional[ToolCallsCreateOutputResponderParticipant] = None
    error: Optional[ToolCallsCreateOutputError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None


class mapToolCallsCreateOutputSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputSenderParticipantData:
        return ToolCallsCreateOutputSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputSenderParticipant:
        return ToolCallsCreateOutputSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapToolCallsCreateOutputSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ToolCallsCreateOutputSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputResponderParticipantData:
        return ToolCallsCreateOutputResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputResponderParticipant:
        return ToolCallsCreateOutputResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapToolCallsCreateOutputResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ToolCallsCreateOutputResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputToolInputSchema:
        return ToolCallsCreateOutputToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputToolOutputSchema:
        return ToolCallsCreateOutputToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputToolTags:
        return ToolCallsCreateOutputToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputTool:
        return ToolCallsCreateOutputTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapToolCallsCreateOutputToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapToolCallsCreateOutputToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapToolCallsCreateOutputToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutputTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutputError:
        return ToolCallsCreateOutputError(
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
    def to_dict(value: Union[ToolCallsCreateOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateOutput:
        return ToolCallsCreateOutput(
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
        sender_participant=mapToolCallsCreateOutputSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapToolCallsCreateOutputResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapToolCallsCreateOutputTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapToolCallsCreateOutputError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ToolCallsCreateBody:
    tool_id: str
    input: Dict[str, Any]
    session_id: str
    metadata: Optional[Dict[str, Any]] = None


class mapToolCallsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsCreateBody:
        return ToolCallsCreateBody(
        tool_id=data.get('tool_id'),
        input=data.get('input'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

