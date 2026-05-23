from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsMessagesCreateOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsMessagesCreateOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsMessagesCreateOutputModelProvider
@dataclass
class ConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesCreateOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsMessagesCreateOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ConversationsMessagesCreateOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesCreateOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsMessagesCreateOutputRequestActorOrganizationActor] = None
    consumer: Optional[ConversationsMessagesCreateOutputRequestActorConsumer] = None
@dataclass
class ConversationsMessagesCreateOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ConversationsMessagesCreateOutputRequestActor] = None
@dataclass
class ConversationsMessagesCreateOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    request: ConversationsMessagesCreateOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ConversationsMessagesCreateOutputModel] = None


class mapConversationsMessagesCreateOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputModelProvider:
        return ConversationsMessagesCreateOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputModel:
        return ConversationsMessagesCreateOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsMessagesCreateOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
        return ConversationsMessagesCreateOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputRequestActorOrganizationActor:
        return ConversationsMessagesCreateOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapConversationsMessagesCreateOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputRequestActorConsumer:
        return ConversationsMessagesCreateOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputRequestActor:
        return ConversationsMessagesCreateOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsMessagesCreateOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsMessagesCreateOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutputRequest:
        return ConversationsMessagesCreateOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapConversationsMessagesCreateOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateOutput:
        return ConversationsMessagesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapConversationsMessagesCreateOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapConversationsMessagesCreateOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConversationsMessagesCreateBodyMessage:
    parts: List[Dict[str, Any]]
@dataclass
class ConversationsMessagesCreateBody:
    message: ConversationsMessagesCreateBodyMessage
    parent_message_id: Optional[str] = None
    model_id: Optional[str] = None


class mapConversationsMessagesCreateBodyMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateBodyMessage:
        return ConversationsMessagesCreateBodyMessage(
        parts=data.get('parts', [])
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateBodyMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCreateBody:
        return ConversationsMessagesCreateBody(
        message=mapConversationsMessagesCreateBodyMessage.from_dict(data.get('message')) if data.get('message') else None,
        parent_message_id=data.get('parent_message_id'),
        model_id=data.get('model_id')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

