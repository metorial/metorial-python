from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceToolCallsGetOutputSenderParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceToolCallsGetOutputSenderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceToolCallsGetOutputSenderParticipantData
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
class DashboardInstanceToolCallsGetOutputResponderParticipantData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceToolCallsGetOutputResponderParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceToolCallsGetOutputResponderParticipantData
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
class DashboardInstanceToolCallsGetOutputToolInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceToolCallsGetOutputToolOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceToolCallsGetOutputToolTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceToolCallsGetOutputTool:
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
    input_schema: Optional[DashboardInstanceToolCallsGetOutputToolInputSchema] = None
    output_schema: Optional[DashboardInstanceToolCallsGetOutputToolOutputSchema] = None
    tags: Optional[DashboardInstanceToolCallsGetOutputToolTags] = None
@dataclass
class DashboardInstanceToolCallsGetOutputError:
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
class DashboardInstanceToolCallsGetOutput:
    object: str
    id: str
    tool_key: str
    type: str
    status: str
    source: str
    transport: str
    session_id: str
    message_id: str
    tool: DashboardInstanceToolCallsGetOutputTool
    created_at: datetime
    session_provider_id: Optional[str] = None
    connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
    sender_participant: Optional[DashboardInstanceToolCallsGetOutputSenderParticipant] = None
    responder_participant: Optional[DashboardInstanceToolCallsGetOutputResponderParticipant] = None
    error: Optional[DashboardInstanceToolCallsGetOutputError] = None
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None


class mapDashboardInstanceToolCallsGetOutputSenderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputSenderParticipantData:
        return DashboardInstanceToolCallsGetOutputSenderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputSenderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputSenderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputSenderParticipant:
        return DashboardInstanceToolCallsGetOutputSenderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceToolCallsGetOutputSenderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputSenderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputResponderParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputResponderParticipantData:
        return DashboardInstanceToolCallsGetOutputResponderParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputResponderParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputResponderParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputResponderParticipant:
        return DashboardInstanceToolCallsGetOutputResponderParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceToolCallsGetOutputResponderParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputResponderParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputToolInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputToolInputSchema:
        return DashboardInstanceToolCallsGetOutputToolInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputToolInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputToolOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputToolOutputSchema:
        return DashboardInstanceToolCallsGetOutputToolOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputToolOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputToolTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputToolTags:
        return DashboardInstanceToolCallsGetOutputToolTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputToolTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputTool:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputTool:
        return DashboardInstanceToolCallsGetOutputTool(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceToolCallsGetOutputToolInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceToolCallsGetOutputToolOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceToolCallsGetOutputToolTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputTool, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutputError:
        return DashboardInstanceToolCallsGetOutputError(
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
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceToolCallsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceToolCallsGetOutput:
        return DashboardInstanceToolCallsGetOutput(
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
        sender_participant=mapDashboardInstanceToolCallsGetOutputSenderParticipant.from_dict(data.get('sender_participant')) if data.get('sender_participant') else None,
        responder_participant=mapDashboardInstanceToolCallsGetOutputResponderParticipant.from_dict(data.get('responder_participant')) if data.get('responder_participant') else None,
        tool=mapDashboardInstanceToolCallsGetOutputTool.from_dict(data.get('tool')) if data.get('tool') else None,
        error=mapDashboardInstanceToolCallsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        input=data.get('input'),
        output=data.get('output'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceToolCallsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

