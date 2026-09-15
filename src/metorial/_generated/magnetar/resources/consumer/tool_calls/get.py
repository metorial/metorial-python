from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerToolCallsGetOutputSenderParticipantData:
    identifier: str
    name: str
@dataclass
class ConsumerToolCallsGetOutputSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ConsumerToolCallsGetOutputSenderParticipantData
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
class ConsumerToolCallsGetOutputResponderParticipantData:
    identifier: str
    name: str
@dataclass
class ConsumerToolCallsGetOutputResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ConsumerToolCallsGetOutputResponderParticipantData
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
class ConsumerToolCallsGetOutputToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerToolCallsGetOutputToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerToolCallsGetOutputToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ConsumerToolCallsGetOutputTool:
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
    input_schema: Optional[ConsumerToolCallsGetOutputToolInputSchema] = None
    output_schema: Optional[ConsumerToolCallsGetOutputToolOutputSchema] = None
    tags: Optional[ConsumerToolCallsGetOutputToolTags] = None
@dataclass
class ConsumerToolCallsGetOutputError:
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
class ConsumerToolCallsGetOutput:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ConsumerToolCallsGetOutputTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[ConsumerToolCallsGetOutputSenderParticipant] = None
    responder_participant: Optional[ConsumerToolCallsGetOutputResponderParticipant] = None
    error: Optional[ConsumerToolCallsGetOutputError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None


class mapConsumerToolCallsGetOutputSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputSenderParticipantData:
        return ConsumerToolCallsGetOutputSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutputSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputSenderParticipant:
        return ConsumerToolCallsGetOutputSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapConsumerToolCallsGetOutputSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ConsumerToolCallsGetOutputSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputResponderParticipantData:
        return ConsumerToolCallsGetOutputResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutputResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputResponderParticipant:
        return ConsumerToolCallsGetOutputResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapConsumerToolCallsGetOutputResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ConsumerToolCallsGetOutputResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputToolInputSchema:
        return ConsumerToolCallsGetOutputToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutputToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputToolOutputSchema:
        return ConsumerToolCallsGetOutputToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutputToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputToolTags:
        return ConsumerToolCallsGetOutputToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutputToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputTool:
        return ConsumerToolCallsGetOutputTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapConsumerToolCallsGetOutputToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapConsumerToolCallsGetOutputToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapConsumerToolCallsGetOutputToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutputTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutputError:
        return ConsumerToolCallsGetOutputError(
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
    def to_dict(value: Union[ConsumerToolCallsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsGetOutput:
        return ConsumerToolCallsGetOutput(
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
        sender_participant=mapConsumerToolCallsGetOutputSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapConsumerToolCallsGetOutputResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapConsumerToolCallsGetOutputTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapConsumerToolCallsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

