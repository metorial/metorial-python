from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsUpdateOutputCreatedByActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsUpdateOutputCreatedByActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsUpdateOutputCreatedByActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ConversationsUpdateOutputCreatedByActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsUpdateOutputCreatedByActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsUpdateOutputCreatedByActorOrganizationActor] = None
    consumer: Optional[ConversationsUpdateOutputCreatedByActorConsumer] = None
@dataclass
class ConversationsUpdateOutputAssistantDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsUpdateOutputAssistantDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsUpdateOutputAssistantDefaultModelProvider
@dataclass
class ConversationsUpdateOutputAssistantAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsUpdateOutputAssistantAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsUpdateOutputAssistantAvailableModelsProvider
@dataclass
class ConversationsUpdateOutputAssistant:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ConversationsUpdateOutputAssistantAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ConversationsUpdateOutputAssistantDefaultModel] = None
@dataclass
class ConversationsUpdateOutput:
    object: str
    id: str
    assistant_id: str
    instance_id: str
    organization_id: str
    created_by_actor: ConversationsUpdateOutputCreatedByActor
    root_message_id: str
    assistant: ConversationsUpdateOutputAssistant
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None


class mapConversationsUpdateOutputCreatedByActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputCreatedByActorOrganizationActorTeams:
        return ConversationsUpdateOutputCreatedByActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputCreatedByActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputCreatedByActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputCreatedByActorOrganizationActor:
        return ConversationsUpdateOutputCreatedByActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapConversationsUpdateOutputCreatedByActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputCreatedByActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputCreatedByActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputCreatedByActorConsumer:
        return ConversationsUpdateOutputCreatedByActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputCreatedByActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputCreatedByActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputCreatedByActor:
        return ConversationsUpdateOutputCreatedByActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsUpdateOutputCreatedByActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsUpdateOutputCreatedByActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputCreatedByActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputAssistantDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputAssistantDefaultModelProvider:
        return ConversationsUpdateOutputAssistantDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputAssistantDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputAssistantDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputAssistantDefaultModel:
        return ConversationsUpdateOutputAssistantDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsUpdateOutputAssistantDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputAssistantDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputAssistantAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputAssistantAvailableModelsProvider:
        return ConversationsUpdateOutputAssistantAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputAssistantAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputAssistantAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputAssistantAvailableModels:
        return ConversationsUpdateOutputAssistantAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsUpdateOutputAssistantAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputAssistantAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutputAssistant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutputAssistant:
        return ConversationsUpdateOutputAssistant(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapConversationsUpdateOutputAssistantDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapConversationsUpdateOutputAssistantAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutputAssistant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateOutput:
        return ConversationsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        title=data.get('title'),
        assistant_id=data.get('assistant_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        created_by_actor=mapConversationsUpdateOutputCreatedByActor.from_dict(data.get('created_by_actor')) if data.get('created_by_actor') else None,
        root_message_id=data.get('root_message_id'),
        assistant=mapConversationsUpdateOutputAssistant.from_dict(data.get('assistant')) if data.get('assistant') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConversationsUpdateBody:
    title: Optional[str] = None


class mapConversationsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsUpdateBody:
        return ConversationsUpdateBody(
        title=data.get('title')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

