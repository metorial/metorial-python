from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ToolCallsListOutputItemsSenderParticipantData:
    identifier: str
    name: str
@dataclass
class ToolCallsListOutputItemsSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ToolCallsListOutputItemsSenderParticipantData
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
class ToolCallsListOutputItemsResponderParticipantData:
    identifier: str
    name: str
@dataclass
class ToolCallsListOutputItemsResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ToolCallsListOutputItemsResponderParticipantData
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
class ToolCallsListOutputItemsToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsListOutputItemsToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ToolCallsListOutputItemsToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ToolCallsListOutputItemsTool:
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
    input_schema: Optional[ToolCallsListOutputItemsToolInputSchema] = None
    output_schema: Optional[ToolCallsListOutputItemsToolOutputSchema] = None
    tags: Optional[ToolCallsListOutputItemsToolTags] = None
@dataclass
class ToolCallsListOutputItemsError:
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
class ToolCallsListOutputItems:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: ToolCallsListOutputItemsTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[ToolCallsListOutputItemsSenderParticipant] = None
    responder_participant: Optional[ToolCallsListOutputItemsResponderParticipant] = None
    error: Optional[ToolCallsListOutputItemsError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
@dataclass
class ToolCallsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ToolCallsListOutput:
    items: List[ToolCallsListOutputItems]
    pagination: ToolCallsListOutputPagination


class mapToolCallsListOutputItemsSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsSenderParticipantData:
        return ToolCallsListOutputItemsSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItemsSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsSenderParticipant:
        return ToolCallsListOutputItemsSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapToolCallsListOutputItemsSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ToolCallsListOutputItemsSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsResponderParticipantData:
        return ToolCallsListOutputItemsResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItemsResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsResponderParticipant:
        return ToolCallsListOutputItemsResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapToolCallsListOutputItemsResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ToolCallsListOutputItemsResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsToolInputSchema:
        return ToolCallsListOutputItemsToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItemsToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsToolOutputSchema:
        return ToolCallsListOutputItemsToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItemsToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsToolTags:
        return ToolCallsListOutputItemsToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItemsToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsTool:
        return ToolCallsListOutputItemsTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapToolCallsListOutputItemsToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapToolCallsListOutputItemsToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapToolCallsListOutputItemsToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItemsTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItemsError:
        return ToolCallsListOutputItemsError(
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
    def to_dict(value: Union[ToolCallsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputItems:
        return ToolCallsListOutputItems(
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
        sender_participant=mapToolCallsListOutputItemsSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapToolCallsListOutputItemsResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapToolCallsListOutputItemsTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapToolCallsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutputPagination:
        return ToolCallsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapToolCallsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListOutput:
        return ToolCallsListOutput(
        items=[mapToolCallsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapToolCallsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ToolCallsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ToolCallsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ToolCallsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    session_template_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    agent_id: Optional[Union[str, List[str]]] = None
    actor_id: Optional[Union[str, List[str]]] = None
    consumer_id: Optional[Union[str, List[str]]] = None
    identity_id: Optional[Union[str, List[str]]] = None
    agent_instance_id: Optional[Union[str, List[str]]] = None
    tool_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ToolCallsListQueryCreatedAt] = None
    updated_at: Optional[ToolCallsListQueryUpdatedAt] = None


class mapToolCallsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ToolCallsListQuery:
        return ToolCallsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        session_template_id=data.get('session_template_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        agent_id=data.get('agent_id'),
        actor_id=data.get('actor_id'),
        consumer_id=data.get('consumer_id'),
        identity_id=data.get('identity_id'),
        agent_instance_id=data.get('agent_instance_id'),
        tool_id=data.get('tool_id'),
        created_at=mapToolCallsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapToolCallsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ToolCallsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

