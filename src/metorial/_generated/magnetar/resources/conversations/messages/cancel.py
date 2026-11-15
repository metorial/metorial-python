from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsMessagesCancelOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsMessagesCancelOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsMessagesCancelOutputModelProvider
@dataclass
class ConversationsMessagesCancelOutputRequestActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ConversationsMessagesCancelOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesCancelOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsMessagesCancelOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ConversationsMessagesCancelOutputRequestActorOrganizationActorMember] = None
@dataclass
class ConversationsMessagesCancelOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ConversationsMessagesCancelOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsMessagesCancelOutputRequestActorOrganizationActor] = None
    consumer: Optional[ConversationsMessagesCancelOutputRequestActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ConversationsMessagesCancelOutputRequestContext:
    mode: str
    requested_mode: str
    can_write: bool
@dataclass
class ConversationsMessagesCancelOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ConversationsMessagesCancelOutputRequestActor] = None
    context: Optional[ConversationsMessagesCancelOutputRequestContext] = None
@dataclass
class ConversationsMessagesCancelOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: ConversationsMessagesCancelOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ConversationsMessagesCancelOutputModel] = None


class mapConversationsMessagesCancelOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputModelProvider:
        return ConversationsMessagesCancelOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputModel:
        return ConversationsMessagesCancelOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsMessagesCancelOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequestActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequestActorOrganizationActorMember:
        return ConversationsMessagesCancelOutputRequestActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequestActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequestActorOrganizationActorTeams:
        return ConversationsMessagesCancelOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequestActorOrganizationActor:
        return ConversationsMessagesCancelOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapConversationsMessagesCancelOutputRequestActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapConversationsMessagesCancelOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequestActorConsumer:
        return ConversationsMessagesCancelOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequestActor:
        return ConversationsMessagesCancelOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsMessagesCancelOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsMessagesCancelOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequestContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequestContext:
        return ConversationsMessagesCancelOutputRequestContext(
        mode=data.get('mode'),
        requested_mode=data.get('requested_mode'),
        can_write=data.get('can_write')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequestContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutputRequest:
        return ConversationsMessagesCancelOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapConversationsMessagesCancelOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        context=mapConversationsMessagesCancelOutputRequestContext.from_dict(data.get('context')) if data.get('context') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesCancelOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesCancelOutput:
        return ConversationsMessagesCancelOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapConversationsMessagesCancelOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapConversationsMessagesCancelOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesCancelOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

