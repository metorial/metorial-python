from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsMessagesHandoffResponsesOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsMessagesHandoffResponsesOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsMessagesHandoffResponsesOutputModelProvider
@dataclass
class ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesHandoffResponsesOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor] = None
    consumer: Optional[ConversationsMessagesHandoffResponsesOutputRequestActorConsumer] = None
@dataclass
class ConversationsMessagesHandoffResponsesOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ConversationsMessagesHandoffResponsesOutputRequestActor] = None
@dataclass
class ConversationsMessagesHandoffResponsesOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: ConversationsMessagesHandoffResponsesOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ConversationsMessagesHandoffResponsesOutputModel] = None


class mapConversationsMessagesHandoffResponsesOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputModelProvider:
        return ConversationsMessagesHandoffResponsesOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputModel:
        return ConversationsMessagesHandoffResponsesOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsMessagesHandoffResponsesOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
        return ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
        return ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
        return ConversationsMessagesHandoffResponsesOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputRequestActor:
        return ConversationsMessagesHandoffResponsesOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsMessagesHandoffResponsesOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutputRequest:
        return ConversationsMessagesHandoffResponsesOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapConversationsMessagesHandoffResponsesOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesOutput:
        return ConversationsMessagesHandoffResponsesOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapConversationsMessagesHandoffResponsesOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapConversationsMessagesHandoffResponsesOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConversationsMessagesHandoffResponsesBodyResponses:
    tool_call_id: str
    output: Any
@dataclass
class ConversationsMessagesHandoffResponsesBody:
    responses: List[ConversationsMessagesHandoffResponsesBodyResponses]


class mapConversationsMessagesHandoffResponsesBodyResponses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesBodyResponses:
        return ConversationsMessagesHandoffResponsesBodyResponses(
        tool_call_id=data.get('tool_call_id'),
        output=data.get('output')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesBodyResponses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesHandoffResponsesBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesHandoffResponsesBody:
        return ConversationsMessagesHandoffResponsesBody(
        responses=[mapConversationsMessagesHandoffResponsesBodyResponses.from_dict(item) for item in data.get('responses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesHandoffResponsesBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

