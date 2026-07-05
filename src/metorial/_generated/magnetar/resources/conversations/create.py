from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsCreateOutputCreatedByActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsCreateOutputCreatedByActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsCreateOutputCreatedByActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ConversationsCreateOutputCreatedByActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsCreateOutputCreatedByActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsCreateOutputCreatedByActorOrganizationActor] = None
    consumer: Optional[ConversationsCreateOutputCreatedByActorConsumer] = None
@dataclass
class ConversationsCreateOutputAssistantDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsCreateOutputAssistantDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsCreateOutputAssistantDefaultModelProvider
@dataclass
class ConversationsCreateOutputAssistantAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsCreateOutputAssistantAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsCreateOutputAssistantAvailableModelsProvider
@dataclass
class ConversationsCreateOutputAssistant:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ConversationsCreateOutputAssistantAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ConversationsCreateOutputAssistantDefaultModel] = None
@dataclass
class ConversationsCreateOutput:
    object: str
    id: str
    assistant_id: str
    instance_id: str
    organization_id: str
    created_by_actor: ConversationsCreateOutputCreatedByActor
    root_message_id: str
    assistant: ConversationsCreateOutputAssistant
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None


class mapConversationsCreateOutputCreatedByActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputCreatedByActorOrganizationActorTeams:
        return ConversationsCreateOutputCreatedByActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputCreatedByActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputCreatedByActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputCreatedByActorOrganizationActor:
        return ConversationsCreateOutputCreatedByActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapConversationsCreateOutputCreatedByActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputCreatedByActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputCreatedByActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputCreatedByActorConsumer:
        return ConversationsCreateOutputCreatedByActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputCreatedByActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputCreatedByActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputCreatedByActor:
        return ConversationsCreateOutputCreatedByActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsCreateOutputCreatedByActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsCreateOutputCreatedByActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputCreatedByActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputAssistantDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputAssistantDefaultModelProvider:
        return ConversationsCreateOutputAssistantDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputAssistantDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputAssistantDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputAssistantDefaultModel:
        return ConversationsCreateOutputAssistantDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsCreateOutputAssistantDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputAssistantDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputAssistantAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputAssistantAvailableModelsProvider:
        return ConversationsCreateOutputAssistantAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputAssistantAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputAssistantAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputAssistantAvailableModels:
        return ConversationsCreateOutputAssistantAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsCreateOutputAssistantAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputAssistantAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutputAssistant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutputAssistant:
        return ConversationsCreateOutputAssistant(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapConversationsCreateOutputAssistantDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapConversationsCreateOutputAssistantAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutputAssistant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateOutput:
        return ConversationsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        title=data.get('title'),
        assistant_id=data.get('assistant_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        created_by_actor=mapConversationsCreateOutputCreatedByActor.from_dict(data.get('created_by_actor')) if data.get('created_by_actor') else None,
        root_message_id=data.get('root_message_id'),
        assistant=mapConversationsCreateOutputAssistant.from_dict(data.get('assistant')) if data.get('assistant') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConversationsCreateBody:
    assistant_id: str
    title: Optional[str] = None
    input: Optional[Dict[str, Any]] = None


class mapConversationsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsCreateBody:
        return ConversationsCreateBody(
        assistant_id=data.get('assistant_id'),
        title=data.get('title'),
        input=data.get('input')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

