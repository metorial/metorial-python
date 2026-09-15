from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerToolCallsListOutputItemsSenderParticipantData:
    identifier: str
    name: str
@dataclass
class ConsumerToolCallsListOutputItemsSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ConsumerToolCallsListOutputItemsSenderParticipantData
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
class ConsumerToolCallsListOutputItemsResponderParticipantData:
    identifier: str
    name: str
@dataclass
class ConsumerToolCallsListOutputItemsResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ConsumerToolCallsListOutputItemsResponderParticipantData
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
class ConsumerToolCallsListOutputItemsToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerToolCallsListOutputItemsToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerToolCallsListOutputItemsToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ConsumerToolCallsListOutputItemsTool:
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
    input_schema: Optional[ConsumerToolCallsListOutputItemsToolInputSchema] = None
    output_schema: Optional[ConsumerToolCallsListOutputItemsToolOutputSchema] = None
    tags: Optional[ConsumerToolCallsListOutputItemsToolTags] = None
@dataclass
class ConsumerToolCallsListOutputItemsError:
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
class ConsumerToolCallsListOutputItems:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ConsumerToolCallsListOutputItemsTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[ConsumerToolCallsListOutputItemsSenderParticipant] = None
    responder_participant: Optional[ConsumerToolCallsListOutputItemsResponderParticipant] = None
    error: Optional[ConsumerToolCallsListOutputItemsError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class ConsumerToolCallsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerToolCallsListOutput:
    items: List[ConsumerToolCallsListOutputItems]
    pagination: ConsumerToolCallsListOutputPagination


class mapConsumerToolCallsListOutputItemsSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsSenderParticipantData:
        return ConsumerToolCallsListOutputItemsSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsSenderParticipant:
        return ConsumerToolCallsListOutputItemsSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapConsumerToolCallsListOutputItemsSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsResponderParticipantData:
        return ConsumerToolCallsListOutputItemsResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsResponderParticipant:
        return ConsumerToolCallsListOutputItemsResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapConsumerToolCallsListOutputItemsResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsToolInputSchema:
        return ConsumerToolCallsListOutputItemsToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsToolOutputSchema:
        return ConsumerToolCallsListOutputItemsToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsToolTags:
        return ConsumerToolCallsListOutputItemsToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsTool:
        return ConsumerToolCallsListOutputItemsTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapConsumerToolCallsListOutputItemsToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapConsumerToolCallsListOutputItemsToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapConsumerToolCallsListOutputItemsToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItemsError:
        return ConsumerToolCallsListOutputItemsError(
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
    def to_dict(value: Union[ConsumerToolCallsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputItems:
        return ConsumerToolCallsListOutputItems(
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
        sender_participant=mapConsumerToolCallsListOutputItemsSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapConsumerToolCallsListOutputItemsResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapConsumerToolCallsListOutputItemsTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapConsumerToolCallsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutputPagination:
        return ConsumerToolCallsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerToolCallsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListOutput:
        return ConsumerToolCallsListOutput(
        items=[mapConsumerToolCallsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerToolCallsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerToolCallsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ConsumerToolCallsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    agent_id: Optional[str] = None
    tool_id: Optional[str] = None
    provider_ids: Optional[Union[str, List[str]]] = None
    connection_id: Optional[str] = None
    created_at: Optional[ConsumerToolCallsListQueryCreatedAt] = None


class mapConsumerToolCallsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerToolCallsListQuery:
        return ConsumerToolCallsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        agent_id=data.get('agent_id'),
        tool_id=data.get('tool_id'),
        provider_ids=data.get('provider_ids'),
        connection_id=data.get('connection_id'),
        created_at=mapConsumerToolCallsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerToolCallsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

